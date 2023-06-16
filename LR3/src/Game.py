import json
import random
import pygame.mouse
import pygame.mixer
from model.Chicken import Chicken
pygame.mixer.init()
background_music = pygame.mixer.music.load('background.mp3')
pygame.mixer.pre_init(44100, -16, 2, 2048)
shoot_sound = pygame.mixer.Sound('shoot.wav')
class Game:
    shoot_sound = pygame.mixer.Sound('shoot.wav')
    __CREATION_TIME = 500
    __speed = 5
    __JSON_FILE = "config/cfg.json"
    __DISPLAY_WIDTH = 1920
    __CLOCK = pygame.time.Clock()
    __DISPLAY_HEIGHT = 500
    __CHICKEN_TIMER = pygame.USEREVENT + 1
    __IS_RUNNING = True
    __CHICKENS_RECT = []
    __DEFAULT_SIZE = [77, 70]
    __CHICKENS = []
    __IMAGE_HEIGHT = 422

    def read_json(self):
        with open(self.__JSON_FILE) as json_file:
            cfg = json.load(json_file)
        return cfg

    def write_json(self):
        with open(self.__JSON_FILE, 'w') as outfile:
            json.dump(self.cfg, outfile)

    def is_pressed(self, elem):
        mouse = pygame.mouse.get_pos()
        if elem.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            return True
        return False

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.__DISPLAY_WIDTH, self.__DISPLAY_HEIGHT))
        self.cfg = self.read_json()
        pygame.display.set_caption("Moorhuhn")
        pygame.display.set_icon(pygame.image.load('images/logo/logo.png').convert_alpha())
        self.bg = pygame.image.load(self.cfg['background_image']).convert_alpha()
        self.sky = pygame.image.load(self.cfg['sky_image']).convert_alpha()
        pygame.time.set_timer(self.__CHICKEN_TIMER, (4 - self.cfg['difficulty_level']) * self.__CREATION_TIME)
        pygame.mouse.set_visible(False)
        self.cursor_img = pygame.image.load('images/cursor/cursor.png')
        self.cursor_img_rect = self.cursor_img.get_rect()
        pygame.font.init()
        self.my_font = pygame.font.Font('config/fonts/AA_Magnum.ttf', 40)
        self.score = 0

    def get_chicken_image(self, chicken: Chicken):
        image = pygame.transform.scale(pygame.image.load(chicken.get_image()),
                                       (self.__DEFAULT_SIZE[0] / chicken.mode,
                                        self.__DEFAULT_SIZE[1] / chicken.mode))
        chicken.x -= self.__speed * self.read_json()['difficulty_level']
        return image

    def print_all_targets(self):
        if self.__CHICKENS_RECT:
            i = 0
            while i < len(self.__CHICKENS_RECT):
                if self.is_pressed(self.__CHICKENS_RECT[i]):
                    self.__CHICKENS[i].is_dying = True
                    self.shoot_sound.play()
                    self.__CHICKENS[i].counter = 0
                if self.__CHICKENS[i].is_dying and self.__CHICKENS[i].counter == 7:
                    self.score += 10 * self.read_json()['difficulty_level'] ** 2
                    del self.__CHICKENS[i]
                    del self.__CHICKENS_RECT[i]
                    if i != 0:
                        i -= 1
                else:
                    if self.__CHICKENS[i].is_dying:
                        self.__CHICKENS_RECT[i].y += 5
                    self.screen.blit(self.get_chicken_image(self.__CHICKENS[i]), self.__CHICKENS_RECT[i])
                    self.__CHICKENS_RECT[i].x -= self.__speed * self.read_json()['difficulty_level']
                    i += 1

    def create_chicken(self):
        chicken = Chicken()
        chicken.x = self.__DISPLAY_WIDTH + 50
        chicken.y = random.randrange(10, 200)
        chicken.mode = random.randrange(1, 3)
        chicken_image = pygame.transform.scale(pygame.image.load(chicken.flight_images[0]),
                                               (self.__DEFAULT_SIZE[0] / chicken.mode,
                                                self.__DEFAULT_SIZE[1] / chicken.mode))
        self.__CHICKENS.append(chicken)
        self.__CHICKENS_RECT.append(chicken_image.get_rect(topleft=(chicken.x, chicken.y)))

    def run(self):
        pygame.mixer.music.play(-1)
        timer = 0
        while self.__IS_RUNNING:
            self.screen.blit(self.sky, (0, 0))
            self.screen.blit(self.bg, (0, self.__DISPLAY_HEIGHT - self.__IMAGE_HEIGHT))
            self.print_all_targets()

            self.cursor_img_rect.center = pygame.mouse.get_pos()  # update position
            self.screen.blit(self.cursor_img, self.cursor_img_rect)
            text_surface = self.my_font.render(str(self.score), False, (255, 255, 255))
            self.screen.blit(text_surface, (self.__DISPLAY_WIDTH / 2, 20))
            if timer / 50 < 25:
                timer += 1
            else:
                self.__CHICKENS_RECT.clear()
                self.__CHICKENS.clear()
                self.print_result()
            text = self.my_font.render(f"Time: {timer / 50}", True, (255, 255, 255))
            self.screen.blit(text, (10, 10))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.write_json()
                    self.__IS_RUNNING = False
                    pygame.quit()
                if event.type == self.__CHICKEN_TIMER:
                    self.create_chicken()

            self.__CLOCK.tick(50)
            pygame.time.delay(1)

    def print_menu(self):
        while self.__IS_RUNNING:
            self.screen.blit(self.sky, (0, 0))
            self.screen.blit(self.bg, (0, self.__DISPLAY_HEIGHT - self.__IMAGE_HEIGHT))
            start_text = self.my_font.render('start', False, (255, 255, 255))
            settings_text = self.my_font.render('settings', False, (255, 255, 255))
            score_text = self.my_font.render('high score', False, (255, 255, 255))
            start_text_rect = start_text.get_rect(topleft=(self.__DISPLAY_WIDTH / 3 - 300, 20))
            settings_text_rect = settings_text.get_rect(topleft=(self.__DISPLAY_WIDTH / 3 * 2 - 350, 20))
            score_text_rect = score_text.get_rect(topleft=(self.__DISPLAY_WIDTH - 300, 20))
            self.screen.blit(start_text, start_text_rect)
            self.screen.blit(settings_text, settings_text_rect)
            self.screen.blit(score_text, score_text_rect)
            if self.is_pressed(start_text_rect):
                self.run()
            elif self.is_pressed(settings_text_rect):
                self.print_settings()
            elif self.is_pressed(score_text_rect):
                self.print_high_score()
            self.cursor_img_rect.center = pygame.mouse.get_pos()
            self.screen.blit(self.cursor_img, self.cursor_img_rect)

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.write_json()
                    self.__IS_RUNNING = False
                    pygame.quit()

    def print_settings(self):
        while self.__IS_RUNNING:
            self.screen.blit(self.sky, (0, 0))
            self.screen.blit(self.bg, (0, self.__DISPLAY_HEIGHT - self.__IMAGE_HEIGHT))
            colors = []
            for i in range(3):
                if i == self.cfg['difficulty_level'] - 1:
                    colors.append((255, 10, 10))
                else:
                    colors.append((255, 255, 255))
            difficulty_level_text = self.my_font.render('difficulty level: ', False, (255, 255, 255))
            easy_text = self.my_font.render('easy', False, colors[0])
            med_text = self.my_font.render('med', False, colors[1])
            hard_text = self.my_font.render('hard', False, colors[2])
            back_text = self.my_font.render('back', False, (255, 255, 255))

            back_text_rect = back_text.get_rect(topleft=(self.__DISPLAY_WIDTH / 6 - 20, self.__DISPLAY_HEIGHT - 100))
            difficulty_level_text_rect = difficulty_level_text.get_rect(topleft=(self.__DISPLAY_WIDTH / 6 - 20, 20))
            easy_text_rect = easy_text.get_rect(topleft=(self.__DISPLAY_WIDTH / 6 + 300, 20))
            med_text_rect = med_text.get_rect(topleft=(self.__DISPLAY_WIDTH / 6 + 600, 20))
            hard_text_rect = hard_text.get_rect(topleft=(self.__DISPLAY_WIDTH / 6 + 900, 20))
            self.screen.blit(difficulty_level_text, difficulty_level_text_rect)
            self.screen.blit(easy_text, easy_text_rect)
            self.screen.blit(med_text, med_text_rect)
            self.screen.blit(hard_text, hard_text_rect)
            self.screen.blit(back_text, back_text_rect)
            if self.is_pressed(easy_text_rect):
                self.cfg['difficulty_level'] = 1
            elif self.is_pressed(med_text_rect):
                self.cfg['difficulty_level'] = 2
            elif self.is_pressed(hard_text_rect):
                self.cfg['difficulty_level'] = 3
            elif self.is_pressed(back_text_rect):
                self.write_json()
                self.print_menu()
            self.cursor_img_rect.center = pygame.mouse.get_pos()
            self.screen.blit(self.cursor_img, self.cursor_img_rect)

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.write_json()
                    self.__IS_RUNNING = False
                    pygame.quit()

    def print_result(self):
        while self.__IS_RUNNING:
            self.screen.blit(self.sky, (0, 0))
            self.screen.blit(self.bg, (0, self.__DISPLAY_HEIGHT - self.__IMAGE_HEIGHT))
            res_text = self.my_font.render(str(self.score), False, (255, 0, 0))
            ok_text = self.my_font.render('ok', False, (255, 0, 0))
            res_text_rect = res_text.get_rect(topleft=(self.__DISPLAY_WIDTH / 2, 20))
            ok_text_rect = ok_text.get_rect(topleft=(self.__DISPLAY_WIDTH / 2, self.__DISPLAY_HEIGHT - 50))
            self.screen.blit(res_text, res_text_rect)
            self.screen.blit(ok_text, ok_text_rect)-
            if self.is_pressed(ok_text_rect):
                self.update_high_score(self.score)
                self.score = 0
                self.print_menu()
            self.cursor_img_rect.center = pygame.mouse.get_pos()
            self.screen.blit(self.cursor_img, self.cursor_img_rect)

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.write_json()
                    self.__IS_RUNNING = False
                    pygame.quit()

    def update_high_score(self, score):
        high_score = sorted(self.cfg['high_score'])
        for el in reversed(high_score):
            if el < score:
                high_score.insert(high_score.index(el) + 1, score)
                break

        for i in range(3):
            j = -1 - i
            self.cfg['high_score'][j] = high_score[j]
        self.write_json()

    def print_high_score(self):
        while self.__IS_RUNNING:
            self.screen.blit(self.sky, (0, 0))
            self.screen.blit(self.bg, (0, self.__DISPLAY_HEIGHT - self.__IMAGE_HEIGHT))
            first_place_text = self.my_font.render(str(self.cfg['high_score'][2]), False, (255, 0, 0))
            second_place_text = self.my_font.render(str(self.cfg['high_score'][1]), False, (255, 0, 0))
            third_place_text = self.my_font.render(str(self.cfg['high_score'][0]), False, (255, 0, 0))
            high_score_text = self.my_font.render('HIGH SCORE', False, (255, 0, 0))
            back_text = self.my_font.render('back', False, (255, 0, 0))
            high_score_text_rect = high_score_text.get_rect(topleft=(self.__DISPLAY_WIDTH / 20 - 50, 20))
            first_place_text_rect = first_place_text.get_rect(topleft=(self.__DISPLAY_WIDTH / 20 - 50, 50))
            second_place_text_rect = second_place_text.get_rect(topleft=(self.__DISPLAY_WIDTH / 20 - 50, 80))
            third_place_text_rect = third_place_text.get_rect(topleft=(self.__DISPLAY_WIDTH / 20 - 50, 110))
            back_text_rect = back_text.get_rect(topleft=(self.__DISPLAY_WIDTH / 6 - 20, self.__DISPLAY_HEIGHT - 100))

            self.screen.blit(high_score_text, high_score_text_rect)
            self.screen.blit(first_place_text, first_place_text_rect)
            self.screen.blit(second_place_text, second_place_text_rect)
            self.screen.blit(third_place_text, third_place_text_rect)
            self.screen.blit(back_text, back_text_rect)

            if self.is_pressed(back_text_rect):
                self.write_json()
                self.print_menu()
            self.cursor_img_rect.center = pygame.mouse.get_pos()
            self.screen.blit(self.cursor_img, self.cursor_img_rect)

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.write_json()
                    self.__IS_RUNNING = False
                    pygame.quit()
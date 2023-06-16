from src.Game import Game
import pygame

pygame.mixer.init()
game = Game()

if __name__ == '__main__':
    game.print_menu()
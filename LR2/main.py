from kivy import Config
from kivy.core.window import Window
from kivymd.app import MDApp

from controllers.controller import Controller

Config.set('graphics', 'resizable', False)
Config.write()


class App(MDApp):

    def build(self):
        Window.size = (800, 500)
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.material_style = "M2"
        self.title = "ppois_lab_2"
        sm = Controller()
        return sm



if __name__ == "__main__":
    App().run()
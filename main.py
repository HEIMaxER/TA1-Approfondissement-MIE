from kivy. app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import NumericProperty, ReferenceListProperty, \
    ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
import random as rd

class Tir(Widget):

    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(7)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class Eleve(Widget):
    score = NumericProperty(0)
    pass

class Cours(Widget):
    type = ['TD', 'TA', 'CM']
    pass

class ControleContinu(Widget):
    pass

class ValidationGame(Widget):

    tir = ObjectProperty(None)
    eleve = ObjectProperty(None)


    def test_tir(self):
        self.tir.center = - self.top

    def __init__(self, **kwargs):
        super(PongGame, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'd':
            self.eleve.center_x += 10
        elif keycode[1] == 'q':
            self.eleve.center_x -= 10
        elif keycode[1] == 'right':
            self.eleve.center_x += 10
        elif keycode[1] == 'left':
            self.eleve.center_x -= 10
        elif keycode[1] == 'left':
            self.eleve.center_x -= 10
        return True

    def update(self, dt):
        self.tir.move()


class ValidationApp(App):
    def build(self):
        game = ValidationGame()
        game.test_tir()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game

if __name__ == '__main__':
    ValidationApp().run()
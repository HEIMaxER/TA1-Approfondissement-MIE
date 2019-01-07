from kivy. app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import NumericProperty, ReferenceListProperty, \
    ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
import numpy as np
import random as rd

class Tir(Widget):

    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(7)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

    def Presence_cours(self, target):
        if self.collide_widget(cours):
            target.touch

class Eleve(Widget):
    score = NumericProperty(0)

class TD(Widget):
    t = 0

    def touch(self):
        self.center_y: -self.parent.height*2

    def move(self):
        self.t +=1/60
        self.pos[0] = self.pos[0] + int(5*(0.5-np.sin(self.t)))


class TA(Widget):
    pass

class CM(Widget):
    pass

class ControleContinu(Widget):
    pass

class TopDownShooterGame(Widget):

    tir = ObjectProperty(None)
    eleve = ObjectProperty(None)
    td = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(TopDownShooterGame, self).__init__(**kwargs)
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
        elif keycode[1] == 'spacebar':
            self.tir.center_x = self.eleve.center_x
            self.tir.center_y = self.eleve.center_y
        return True

    def update(self, dt):
        self.tir.move()
        self.td.move()



class TopDownShooterApp(App):
    def build(self):
        game = TopDownShooterGame()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game

if __name__ == '__main__':
    TopDownShooterApp().run()
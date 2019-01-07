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

    def kill(self, target, player):
        if self.collide_widget(target):
            target.velocity_y *= 1.05
            player.score += target.value
            target.pos[1]+= 300

class Joueur(Widget):
    score = NumericProperty(0)

class EnemieA(Widget):
    t = 0
    velocity_y = NumericProperty(0.1)
    value =  100
    real_y = 0


    def move(self):
        self.t+=1
        self.real_y = self.pos[1]-self.velocity_y
        self.pos[1] = int(self.real_y)
        self.pos[0] = self.pos[0]+int(10*(np.cos(((self.t%180)/180)*2*np.pi)))
        pass



class TA(Widget):
    pass

class CM(Widget):
    pass

class ControleContinu(Widget):
    pass

class TopDownShooterGame(Widget):

    tir = ObjectProperty(None)
    joueur = ObjectProperty(None)
    enemiea = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(TopDownShooterGame, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):

        if keycode[1] == 'd':
            self.joueur.center_x += 10
        elif keycode[1] == 'q':
            self.joueur.center_x -= 10
        elif keycode[1] == 'right':
            self.joueur.center_x += 10
        elif keycode[1] == 'left':
            self.joueur.center_x -= 10
        elif keycode[1] == 'spacebar':
            self.tir.center_x = self.joueur.center_x
            self.tir.center_y = self.joueur.center_y
        return True

    def update(self, dt):
        self.tir.move()
        self.enemiea.move()
        self.tir.kill(self.enemiea, self.joueur)



class TopDownShooterApp(App):
    def build(self):
        game = TopDownShooterGame()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game

if __name__ == '__main__':
    TopDownShooterApp().run()
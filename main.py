from kivy. app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import NumericProperty, ReferenceListProperty, \
    ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
import numpy as np
import random as rd



class Tir1(Widget):

    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(7)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

    def killA(self, target, player):
        if self.collide_widget(target):
            target.velocity_y *= 1.05
            player.score += target.value
            target.pos[1] = 700

    def killB(self, target, player):
        if self.collide_widget(target):
            player.score += target.value
            target.move()

class Tir2(Widget):

    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(7)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

    def killA(self, target, player):
        if self.collide_widget(target):
            target.velocity_y *= 1.05
            player.score += target.value
            target.pos[1] = 700

    def killB(self, target, player):
        if self.collide_widget(target):
            player.score += target.value
            target.move()

class Joueur(Widget):
    score = NumericProperty(0)
    temps = NumericProperty(100)

    def time(self,dt):
        self.temps -= dt

class EnemieA(Widget):
    t = 0
    velocity_y = NumericProperty(0.1)
    value =  100
    real_y = 0


    def move(self):
        self.t+=1
        self.real_y = self.pos[1]-self.velocity_y
        self.pos[1] = int(self.real_y)
        print(self.pos)
        self.pos[0] = self.pos[0]+int(10*(np.cos(((self.t%180)/180)*2*np.pi)))




class EnemieB(Widget):
    t = 0
    value = 100

    def move(self):
        self.t += 1
        self.pos[1] = rd.randint(0, 600)
        self.pos[0] = rd.randint(200,600)


class CM(Widget):
    pass


class TopDownShooterGame(Widget):

    tir1 = ObjectProperty(None)
    tir2 = ObjectProperty(None)
    joueur = ObjectProperty(None)
    enemiea = ObjectProperty(None)
    enemieb = ObjectProperty(None)
    compteur_tir = 0

    def __init__(self, **kwargs):
        super(TopDownShooterGame, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self.My_Clock = Clock
        self.My_Clock.schedule_interval(self.update, 1 / 60.)

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
            if int(self.joueur.temps) != 0:
                if self.compteur_tir ==0:
                    self.tir1.center_x = self.joueur.center_x
                    self.tir1.center_y = self.joueur.center_y
                    self.compteur_tir = 1
                else:
                    self.tir2.center_x = self.joueur.center_x
                    self.tir2.center_y = self.joueur.center_y
                    self.compteur_tir = 0
        elif keycode[1] == 'escape':
            App.get_running_app().stop()
        return True

    def update(self, dt):
        self.tir1.move()
        self.tir2.move()
        self.enemiea.move()
        self.tir1.killA(self.enemiea, self.joueur)
        self.tir2.killA(self.enemiea, self.joueur)
        self.tir1.killB(self.enemieb, self.joueur)
        self.tir2.killB(self.enemieb, self.joueur)
        self.joueur.time(dt)
        if int(self.joueur.temps) == 0:
            self.My_Clock.unschedule(self.update)



class TopDownShooterApp(App):

    dt = 1.0/60.0
    def build(self):
        game = TopDownShooterGame()
        return game

if __name__ == '__main__':
    #Window.fullscreen = True
    TopDownShooterApp().run()
from kivy. app import App
from kivy.uix.widget import Widget

class ValidationGame(Widget):
    pass

class ValidationApp(App):
    def build(self):
        return ValidationGame()

if __name__ == '__main__':
    ValidationApp().run()
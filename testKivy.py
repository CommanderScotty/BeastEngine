from kivy.app import App
from kivy.uix.button import Button
from kivy.graphics import *
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

class GameWindow(App):
    def build(self):
        return Button(text='Hello World')

GameWindow().run()

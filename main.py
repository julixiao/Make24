import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label

class Make24(App):

    def build(self):
        return Label(text='Make 24 Card Game')


if __name__ == '__main__':
    Make24().run()
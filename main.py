#!/usr/bin/env python
import kivy
from kivy.config import Config
kivy.require('1.0.6') # replace with your current kivy version !

Config.set('kivy', 'log_level', 'debug')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput 

import random

class StartPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1

        self.add_widget(Label(text="Make 24!"))

        # Display 4 random cards
        cards = random.sample(range(1, 52), 4)
        image_layout = BoxLayout(orientation='horizontal')
        image_layout.add_widget(Image(source=f"cards/{cards[0]}.png", allow_stretch=True))
        image_layout.add_widget(Image(source=f"cards/{cards[1]}.png", allow_stretch=True))
        image_layout.add_widget(Image(source=f"cards/{cards[2]}.png", allow_stretch=True))
        image_layout.add_widget(Image(source=f"cards/{cards[3]}.png", allow_stretch=True))

        self.add_widget(image_layout)

        # Add text box for input
        self.answer = TextInput(multiline=False)
        self.add_widget(self.answer)

        # Submit button
        self.submit_button = Button(text="Submit")
        self.submit_button.bind(on_press=self.eval_expression)
        self.add_widget(self.submit_button)

    # Function to determine if submitted expression sums to 24
    def eval_expression(self, instance):
        expression = eval(self.answer.text)

        if (expression == 24):
            print("Output evaluated correctly!")
        else:
            print(f"Output evaluated to {expression}, please try again.")

class Make24(App):

    def build(self):
        return StartPage()


if __name__ == '__main__':
    Make24().run()
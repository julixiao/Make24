import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput 
from kivy.uix.button import Button

class StartPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1

        self.add_widget(Label(text="Cards: Make 24"))
        self.answer = TextInput(multiline=False)
        self.add_widget(self.answer)

        self.submit_button = Button(text="Submit")
        self.submit_button.bind(on_press=self.eval_expression)
        self.add_widget(self.submit_button)

    def eval_expression(self, instance):
        expression = eval(self.answer.text)

        if expression == 24:
            print("Output evaluated correctly!")
        else:
            print(f"Output evaluated to {expression}, please try again.")

class Make24(App):

    def build(self):
        return StartPage()


if __name__ == '__main__':
    Make24().run()
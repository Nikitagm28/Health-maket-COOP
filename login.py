from kivy.app import App
from kivy.core.window import Window

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen

class LoginScreen(Screen):
    pass


class LoginApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return LoginScreen()


if __name__ == '__main__':
    LoginApp().run()
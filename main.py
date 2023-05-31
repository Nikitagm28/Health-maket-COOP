from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class LoginScreen(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = 'vertical'
        self.spacing = 10

        self.email = TextInput(
            hint_text='Email',
            size_hint=(None, None),
            width=200,
            height=50
        )
        self.add_widget(self.email)

        self.password = TextInput(
            hint_text='Password',
            password=True,
            size_hint=(None, None),
            width=200,
            height=50
        )
        self.add_widget(self.password)

        self.login_button = Button(
            text='Login',
            size_hint=(None, None),
            width=200,
            height=50,
            on_press=self.login
        )
        self.add_widget(self.login_button)

    def login(self, instance):
        print('Logged in successfully')


class LoginApp(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    LoginApp().run()

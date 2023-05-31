from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.widget import Widget


class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.orientation = "vertical"
        Window.clearcolor = (1, 1, 1, 1)
        self.spacing = 20
        # self.background_color = [1, 1, 1, 1] # здесь нулевое значение позволит видеть фон

        # добавляем лого
        image = Image(source="Logo.png", size_hint=(1, 1))
        image.pos_hint = {"center_x": 0.5, "center_y": 0.5} # позиционируем лого по центру экрана
        self.add_widget(image)

        # располагаем текстовые поля в центре экрана
        login_layout = BoxLayout(size_hint=(0.5, None), height=50, pos_hint={"center_x": 0.5})
        login_layout.add_widget(TextInput(hint_text="Логин", multiline=False))
        self.add_widget(login_layout)

        password_layout = BoxLayout(size_hint=(0.5, None), height=50, pos_hint={"center_x": 0.5})
        password_layout.add_widget(TextInput(hint_text="Пароль", password=True, multiline=False))
        self.add_widget(password_layout)

        # добавляем кнопку
        button_layout = BoxLayout(size_hint=(0.5, None), height=50, pos_hint={"center_x": 0.5})
        button_layout.add_widget(Button(text="Войти", background_color = (0, 1, 0, 1)))
        self.add_widget(button_layout)

        button_layout = BoxLayout(size_hint=(0.5, None), height=50, pos_hint={"center_x": 0.5})
        button_layout.add_widget(Button(text="Регистрация", background_color = (0, 0.5, 0, 1)))
        self.add_widget(button_layout)

        spacer = Widget(size_hint=(1, None), height=50)
        self.add_widget(spacer)

class LoginApp(App):
    def build(self):
        return LoginScreen()


LoginApp().run()


class LoginApp(App):
    def build(self):
        return LoginScreen()


LoginApp().run()

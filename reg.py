from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Color, Line
from kivy.uix.textinput import TextInput
from kivy.properties import NumericProperty



class RegisterScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(RegisterScreen, self).__init__(**kwargs)
        self.orientation = "vertical"
        Window.clearcolor = (1, 1, 1, 1)
        self.spacing = 20

        # добавляем лого
        image = Image(source="Logo.png", size_hint=(1, 1))
        image.pos_hint = {"center_x": 0.5, "center_y": 0.5}  # позиционируем лого по центру экрана
        self.add_widget(image)

        # располагаем текстовые поля в центре экрана
        # Имя
        name_layout = BoxLayout(size_hint=(0.5, None), height=50, pos_hint={"center_x": 0.5})
        name_input = (TextInput(hint_text="Name", multiline=False))
        self.add_widget(name_layout)
        # Фамилия
        firstname_layout = BoxLayout(size_hint=(0.5, None), height=50, pos_hint={"center_x": 0.5})
        firstname_layout.add_widget(TextInput(hint_text="Фамилия", password=True, multiline=False))
        self.add_widget(firstname_layout)
        # Возраст
        age_layout = BoxLayout(size_hint=(0.5, None), height=50, pos_hint={"center_x": 0.5})
        age_layout.add_widget(TextInput(hint_text="Возраст", password=True, multiline=False))
        self.add_widget(age_layout)
        # Гр. крови
        bloody_layout = BoxLayout(size_hint=(0.5, None), height=50, pos_hint={"center_x": 0.5})
        bloody_layout.add_widget(TextInput(hint_text="Группа крови", password=True, multiline=False))
        self.add_widget(bloody_layout)
        # Заболевания
        password_layout = BoxLayout(size_hint=(0.5, None), height=50, pos_hint={"center_x": 0.5})
        password_layout.add_widget(TextInput(hint_text="Заболевания", password=True, multiline=False))
        self.add_widget(password_layout)
        # Аллергия
        password_layout = BoxLayout(size_hint=(0.5, None), height=50, pos_hint={"center_x": 0.5})
        password_layout.add_widget(TextInput(hint_text="Аллергические реакции", password=True, multiline=False))
        self.add_widget(password_layout)
        # Вес
        weight_layout = BoxLayout(size_hint=(0.5, None), height=50, pos_hint={"center_x": 0.5})
        weight_layout.add_widget(TextInput(hint_text="Вес", password=True, multiline=False))
        self.add_widget(weight_layout)

        # кнопка "Зарегистрироваться"
        button_layout = BoxLayout(size_hint=(0.5, None), height=50, pos_hint={"center_x": 0.5})
        button = Button(text="Зарегистрироваться", background_color=(0, 1, 0, 0.9))
        button.bind(on_press=self.on_button_press)
        button.bind(on_release=self.on_button_release)
        button_layout.add_widget(button)
        self.add_widget(button_layout)

        # сохраняем ссылку на кнопку
        self.button = button

    def on_button_press(self, instance):
        # изменяем цвет обводки на черный
        self.button.canvas.before.clear()
        with self.button.canvas.before:
            Color(0, 0, 0)
            self.border = Line(rectangle=(self.button.x, self.button.y, self.button.width, self.button.height),
                               width=1)

    def on_button_release(self, instance):
        # очищаем обводку при отпускании кнопки
        self.button.canvas.before.clear()


class LoginApp(App):
    def build(self):
        return RegisterScreen()


LoginApp().run()

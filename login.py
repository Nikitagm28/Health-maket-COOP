from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class RegistrationScreen(BoxLayout):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # добавляем лого
        self.add_widget(Image(source="Logo.png",size_hint=(1, 1), pos_hint={"center_x": 0.5, "center_y": 0.5}))

        # текстовые поля в центре экрана
        for hint_text in ["Name", "Фамилия", "Возраст", "Группа крови", "Заболевания", "Аллергические реакции", "Вес"]:
            self.add_widget(BoxLayout(size_hint=(0.5, None), height=50, pos_hint={"center_x": 0.5} TextInput(hint_text=hint_text, multiline=False)))
        
        # кнопка "Зарегистрироваться"
        self.add_widget(BoxLayout(size_hint=(0.5, None), height=50,  pos_hint={"center_x": 0.5} Button(text="Зарегистрироваться",  background_color=(0, 1, 0, 0.9),  on_press=self.on_button_press,  on_release=self.on_button_release)))
        
    def on_button_press(self, button):
        # действия при нажатии кнопки (e.g. собрать данные с текстовых полей)
        pass
    
    def on_button_release(self, button):
        # действия при отпускании кнопки (e.g. отправить данные на сервер)
        pass
from kivy.app import App

class RegistrationApp(App):
    def build(self):
        return RegistrationScreen()

if __name__ == "__main__":
    RegistrationApp().run()

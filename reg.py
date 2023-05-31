from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.graphics import Color, Line
from kivy.properties import NumericProperty


class RegisterScreen(BoxLayout):
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


class RegApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return RegisterScreen()


if __name__ == '__main__':
    RegApp().run()

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget
from kivy.graphics import Line


class TimerApp(App):
    def build(self):
        # устанавливаем размер окна
        Window.size = (375, 600)
        # создаем BoxLayout для размещения виджетов вертикально
        self.layout = BoxLayout(orientation='vertical')
        # создаем GridLayout с пятью строками и двумя столбцами
        self.top_layout = GridLayout(
            cols=2, rows=5, padding=10, spacing=10, size_hint_y=None, height=200
        )

        with self.layout.canvas.before:
            # устанавливаем фоновый цвет
            Color(1, 1, 1, 1)
            self.rect = Rectangle(size=self.layout.size, pos=self.layout.pos)
        self.layout.bind(size=self._update_rect, pos=self._update_rect)

        # Создаем виджет круга
        self.circle_widget = CircleWidget()

        # добавляем виджеты в сетку
        self.top_layout.add_widget(
            Label(
                text="Введите время (в формате ЧЧ:ММ):",
                size_hint=(0.5, None),
                height=30,
                halign='right',
                valign='middle',
                color=(0, 0, 0, 1)
            )
        )
        self.input = TextInput(
            multiline=False,
            size_hint=(0.5, None),
            height=30,
            foreground_color=(0, 0, 0, 1)
        )
        self.top_layout.add_widget(self.input)
        self.start_button = Button(
            text="Запустить таймер",
            size_hint=(0.5, None),
            height=30,
            color=(0, 0, 0, 1)
        )
        self.start_button.bind(on_press=self.add_timer)
        self.top_layout.add_widget(self.start_button)
        self.time_label = Label(
            text="",
            size_hint=(0.5, None),
            height=30,
            halign='center',
            valign='middle',
            color=(0, 0, 0, 1)
        )
        self.top_layout.add_widget(self.time_label)
        self.label = Label(
            text="",
            size_hint=(0.5, None),
            height=30,
            halign='center',
            valign='middle',
            color=(0, 0, 0, 1)
        )
        self.top_layout.add_widget(self.label)

        # добавляем GridLayout и CircleWidget в BoxLayout
        self.layout.add_widget(self.top_layout)
        self.layout.add_widget(self.circle_widget)

        self.timers = []  # список для хранения таймеров
        self.update_circle_timers()  # обновление состояния круговых таймеров

        return self.layout

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def add_timer(self, instance):
        try:
            time_str = self.input.text
            hours, minutes = map(int, time_str.split(":"))
            seconds = hours * 3600 + minutes * 60

            if seconds < 60:
                self.label.text = "Минимальное время - 1 минута"
                return

        except ValueError:
            self.label.text = "Некорректный ввод"
            return

        self.timers.append({'seconds': seconds, 'initial_seconds': seconds})
        self.update_circle_timers()
        self.label.text = "Таймер запущен"
        self.input.text = ""

    def update_circle_timers(self):
        remaining_timers = [timer for timer in self.timers if timer['seconds'] > 0]

        if len(remaining_timers) > 0:
            remaining_timers.sort(key=lambda x: x['seconds'])
            self.start_timers()

    def start_timers(self):
        self.circle_widget.clear()
        self.circle_widget.update_circle_color((0, 0.5, 0, 1))

        for timer in self.timers:
            seconds = timer['seconds']
            initial_seconds = timer['initial_seconds']
            progress = 1 - (seconds / initial_seconds)
            self.circle_widget.update_circle(seconds, initial_seconds, progress)

        self.timer = Clock.schedule_interval(self.timer_callback, 1)

    def timer_callback(self, dt):
        for timer in self.timers:
            seconds = timer['seconds']
            seconds -= 1
            timer['seconds'] = seconds

            if seconds == 0:
                self.timer.cancel()
                self.timers.remove(timer)
                self.update_circle_timers()
                self.label.text = "Время вышло!"
                break

        self.update_time_label()

    def update_time_label(self):
        time_labels = []

        for timer in self.timers:
            seconds = timer['seconds']
            hours = seconds // 3600
            minutes = (seconds % 3600) // 60

            if hours == 0 and minutes == 0:
                time_labels.append("меньше минуты")
            else:
                time_labels.append(f"{hours:02d}:{minutes:02d}")

        self.time_label.text = "Осталось времени: " + ", ".join(time_labels)

    def on_stop(self):
        if hasattr(self, 'timer'):
            self.timer.cancel()

    def on_pause(self):
        if hasattr(self, 'timer'):
            self.timer.cancel()
        return True

    def on_resume(self):
        self.start_timers()


class CircleWidget(Widget):
    def __init__(self, **kwargs):
        super(CircleWidget, self).__init__(**kwargs)
        self.center = (Window.width / 2, Window.height / 2)
        self.initial_radius = min(Window.width, Window.height) * 0.35
        self.radius = self.initial_radius
        self.circle_color = (0, 0.5, 0, 1)
        self.draw_circle()

    def clear(self):
        self.canvas.clear()

    def update_circle_color(self, new_color):
        self.circle_color = new_color
        self.draw_circle()

    def draw_circle(self):
        with self.canvas:
            Color(*self.circle_color)
            Line(circle=self.center + [self.radius, 0, 360], width=4)

    def erase_circle_section(self, start_angle, end_angle):
        with self.canvas:
            Color(1, 1, 1)
            Line(circle=self.center + [self.radius, start_angle, end_angle], width=4)
            Color(*self.circle_color)

    def update_circle(self, seconds, initial_seconds, progress=1):
        self.clear()
        self.erase_circle_section(0, 360 * (1 - progress))
        self.radius = self.initial_radius * progress
        self.draw_circle()


if __name__ == '__main__':
    TimerApp().run()

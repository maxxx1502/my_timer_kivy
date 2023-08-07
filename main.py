from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from threading import Timer

Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '300')

class TimerEx(BoxLayout):
    start_btn = ObjectProperty(None)
    stop_btn = ObjectProperty(None)
    text_input = ObjectProperty(None)
    time_text = ObjectProperty(None)
    time_count = 0
    t = None

    def set_time(self):
        self.time_count = int(self.text_input.text)
        self.time_text.text = str(self.time_count)
        self.start_btn.disabled = False

    def start_timer(self):
        self.t = Timer(1, self.countdown)
        self.t.start()
        self.start_btn.disabled = True
        self.stop_btn.disabled = False
        self.text_input.disabled = True

    def countdown(self):
        if (self.time_count == 0):
            self.stop_btn.disabled = True
            self.time_count = int(self.text_input.text)
            self.time_text.text = str(self.time_count)
            self.start_btn.disabled = False
            self.text_input.disabled = False
            self.t = None
        else:
            self.time_count -= 1
            self.time_text.text = str(self.time_count)
            self.t = Timer(1, self.countdown)
            self.t.start()

    def stop_timer(self):
        self.text_input.disabled = False
        self.t.cancel()
        self.start_btn.disabled = False
        self.stop_btn.disabled = True
        self.time_count = int(self.text_input.text)
        self.time_text.text = str(self.time_count)

class TimerApp(App):
    def build(self):
        timer = TimerEx()
        return timer

if __name__ == '__main__':
    TimerApp().run()
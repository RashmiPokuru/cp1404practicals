"""
CP1404/ CP5632 practical 08
Convert miles to kilometers
"""

from kivy.app import App
from kivy.lang import Builder


class MilesConverterApp(App):
    def build(self):
        self.title = "Covert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')


MilesConverterApp().run()

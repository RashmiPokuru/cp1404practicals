"""
CP1404/ CP5632 practical 08
Convert miles to kilometers
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class MilesConverterApp(App):
    number_of_kilometers = StringProperty()

    def build(self):
        self.title = "Covert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.number_of_kilometers = '1.6'
        return self.root

    def handle_convert(self):
        try:
            self.number_of_kilometers = str(float(self.root.ids.input_miles.text) * 1.60934)
        except ValueError:
            pass


MilesConverterApp().run()

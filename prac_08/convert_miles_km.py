"""
CP1404/ CP5632 practical 08
Convert miles to kilometers
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KILOMETER = 1.60934


class MilesConverterApp(App):
    number_of_kilometers = StringProperty()

    def build(self):
        self.title = "Covert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.number_of_kilometers = '1.6'
        return self.root

    def handle_convert(self):
        self.number_of_kilometers = str(self.get_valid_number() * MILES_TO_KILOMETER)

    def handle_update(self, value):
        self.root.ids.input_miles.text = str(self.get_valid_number() + value)

    def get_valid_number(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0.0


MilesConverterApp().run()

"""
CP1404/ CP5632 practical 08
Convert miles to kilometers
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KILOMETER = 1.60934


class MilesConverterApp(App):
    """Kivy App to convert input miles to kilometers"""
    number_of_kilometers = StringProperty()

    def build(self):
        """Build kivy app from kv file"""
        self.title = "Covert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.number_of_kilometers = '1.6'
        return self.root

    def handle_convert(self):
        """Convert valid input miles to kilometers"""
        self.number_of_kilometers = str(self.get_valid_number() * MILES_TO_KILOMETER)

    def handle_increment(self, value):
        """Increase number of miles by value when user press Up/Down button"""
        self.root.ids.input_miles.text = str(self.get_valid_number() + value)

    def get_valid_number(self):
        """Get text input of number of miles. Return 0 if error, else return float value of input"""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesConverterApp().run()

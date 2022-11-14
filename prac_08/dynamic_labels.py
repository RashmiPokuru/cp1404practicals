"""
CP1404/CP5632 Prac 08 Kivy
App to display list of names. Each name is represented as label.
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Main program - Kivy app  to create dynamic widgets."""

    def __init__(self, **kwargs):
        """Construct main app"""
        super().__init__(**kwargs)
        self.names = ['Rashmi', 'Surya', 'Usha', 'Krishna']

    def build(self):
        """Build kivy GUI"""
        self.title = "Names"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create label widgets from list"""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()

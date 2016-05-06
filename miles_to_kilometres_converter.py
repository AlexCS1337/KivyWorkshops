from kivy.app import App
from kivy.lang import Builder

class MilesToKilometresConverter(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('miles_to_kilometres_converter.kv')
        return self.root

    def handle_up(self):
        print("test")
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    def handle_down(self):
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = ''

    def handle_convert(self):
        self.root.ids.output_label = ''

MilesToKilometresConverter().run()
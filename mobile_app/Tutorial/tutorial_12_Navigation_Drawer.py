from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (300, 500)

navigation_helper = """



"""

class DemoApp(MDApp):
    def build(self):
        screen = Builder.load_string(navigation_helper)
        return screen


DemoApp().run()
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (300, 500)
screen_helper = """
Screen:
    BoxLayout:
        orientation: 'vertical'
        
        MDToolbar:
            title: 'Demo' # ชื่อหัวข้อ
            left_action_items: [['menu',lambda x: app.navigation_draw()]]
            right_action_items: [['clock',lambda x: app.navigation_draw()]]
            elevation: 8 # เงา
        
            
       
        MDLabel:
            text: 'Hello world'
            halign: 'center'
            
        MDBottomAppBar:
            
            MDToolbar:
                title: 'Help' # ชื่อหัวข้อ
                left_action_items: [['coffee',lambda x: app.navigation_draw()]]
                mode: 'end'
                type: 'bottom'
                icon: 'coffee'
                on_action_button: app.navigation_draw()
                
"""


class DemoApp(MDApp):


    def build(self):
        self.theme_cls.primary_palette = 'Green'
        screen = Builder.load_string(screen_helper)
        #screen = Screen()
        return screen

    def navigation_draw(self):
        print('Navigation')


DemoApp().run()
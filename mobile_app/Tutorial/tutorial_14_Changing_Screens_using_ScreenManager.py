from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

names = 'Chaiwat'
screen_helper = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    UploadScreen:

<MenuScreen>:
    name: 'menu'
    MDRectangleFlatButton:
        text: 'Profile'
        pos_hint: {'center_x': 0.5, 'center_y':0.5}
        on_press: root.manager.current = 'profile'
    MDRectangleFlatButton:
        text: 'Upload'
        pos_hint: {'center_x': 0.5, 'center_y':0.6}
        on_press: root.manager.current = 'upload'
        

<ProfileScreen>:
    name: 'profile'
    MDLabel:
        text: 'Welcome Chaiwat!!!'
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y':0.2}    
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, 'center_y':0.5}
        on_press: root.manager.current = 'menu'
        
<UploadScreen>:
    name: 'upload'
    MDLabel:
        text: 'Lets upload some file!'
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y':0.2}    
    

        
"""

class MenuScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass

class UploadScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(MenuScreen(name='profile'))
sm.add_widget(MenuScreen(name='upload'))


class DemoApp(MDApp):
    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen


DemoApp().run()
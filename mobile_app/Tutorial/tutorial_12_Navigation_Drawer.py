from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager


Window.size = (300, 500)
screen_helper = """
ScreenManger:
    MenuScreen:
    ProfileScreen:
    
<MenuScreen>:
    name: 'menu'
    MDRectangkeFlatButton:
        text: 'Profile'
        pos_hint: {'center_x': 0.5, 'center_y':0.5}
        on_press: root.manager.current = 'profile'
        
<ProfileScreen>:
    name: 'profile'
    MDLabel:
        text: 'Welcome Chaiwat'
        halign: 'center'    
    
"""

navigation_helper = """
Screen:
    NavigationLayout
        ScreenManager:
            Screen:

                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Demo Application'
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation:10
                    Widget:

        MDNavigationDrawer:
            id: nav_drawer

            BoxLayout:
                orientation: 'vertical'

                Image:
                    source: 'chaiwat.jpg'

                MDLabel:
                    text: ' Chaiwat'
                    font_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]

                MDLabel:
                    text: ' chaiwat.klaew@gmail.com'
                    font_style: 'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]

                ScrollView:
                    MDList:
                        OneLineIconListItem:    
                            text: 'Profile'
                            IconLeftWidget:
                                icon: 'face-profile'
                        OneLineIconListItem:    
                            text: 'Upload'
                            IconLeftWidget:
                                icon: 'file-upload'
                        OneLineIconListItem:
                            text: 'Logout'
                            IconLeftWidget:
                                icon: 'file-plus' 

"""
class MenuScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(MenuScreen(name='profile'))

class DemoApp(MDApp):
    def build(self):
        screen = Builder.load_string(navigation_helper)
        return screen


DemoApp().run()
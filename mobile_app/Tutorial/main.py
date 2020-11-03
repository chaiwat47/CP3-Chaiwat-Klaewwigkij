from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton


class DemoApp(MDApp):

    def build(self):
        screen = Screen()
        btn_flat = MDRectangleFlatButton(text='Hi world',
                                pos_hint={'center_x':0.5, 'center_y':0.5})
        icon_btn = MDFloatingActionButton(icon='android', pos_hint={'center_x':0.5, 'center_y':0.5})
        screen.add_widget(icon_btn)
        return screen


DemoApp().run()

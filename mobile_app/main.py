from kivymd.app import MDApp # ShowApp
from kivymd.uix.screen import Screen # ShowScreen
from kivymd.uix.textfield import MDTextField # ป้อน Text ตัวอักษร


# สร้าง class
class DemoApp(MDApp):

    def build(self):
        screen = Screen() # สร้าง obj มารับผลหน้าจอ
        username = MDTextField(text='กรุณาใส้username',
                               pos_hint={'center_y':0.5})
        screen.add_widget(username) # เพิ่ม widget กรอกusername
        return screen
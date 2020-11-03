from kivymd.app import MDApp # ShowApp
from kivymd.uix.screen import Screen # ShowScreen
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField # ป้อน Text ตัวอักษร
from kivy.lang import Builder
from helper import username_helper

# ใส่ตัวแนะนำว่าต้องใส่ข้อมูลอะไร

class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette= 'Green'
        # username = MDTextField(
        #    text = 'Enter username',
        #    pos_hint = {'center_x':0.5, 'center_y':0.5},
        #    size_hint_x = None, widtg = 300
        # )
        button = MDRectangleFlatButton(text='Show', pos_hint = {'center_x':0.5, 'center_y':0.4},
                                       on_release= self.show_data)

        self.username = Builder.load_string(username_helper)
        screen.add_widget(self.username)
        screen.add_widget(button)
        return screen
    def show_data(self, obj):
        # สร้างเงื่อนไขสำหรับตรวจสอบ str
        if self.username.text is "":
            check_string = 'Please enter a username' # กรุณาใส่ username
        else:
            check_string = self.username.text + ' does not exist'

        close_btton = MDFlatButton(text='Close', on_release=self.close_dialog)
        more_button = MDFlatButton(text='More')
        self.dialog = MDDialog(title='Username Check',text=check_string, # แสดงชื่อตามตัวแปรที่รับมา โดยตรวจสอบเงื่อนไขก่อน
                          size_hint= (0.5, 1), # ปรับขนาด
                          buttons = [close_btton, more_button]) # แสดงปุ่มยืนยัน หรือปุ่มปิด
        self.dialog.open()

    # ฟังก์ชันสำหรับปิด dialog
    def close_dialog(self, obj):
        self.dialog.dismiss()

# รัน App
DemoApp().run()
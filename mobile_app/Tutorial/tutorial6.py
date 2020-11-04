from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import MDList,OneLineListItem, TwoLineListItem, ThreeLineListItem #list 3 ตัวอักษร
from kivymd.uix.list import ThreeLineIconListItem # list+icon
from kivymd.uix.list import ThreeLineAvatarListItem # list+ avatar
from kivymd.uix.list import IconLeftWidget # แสดง icon ทางด้านซ้าย
from kivymd.uix.list import ImageLeftWidget # แสดง icon ทางด้านขวา
from kivy.uix.scrollview import ScrollView

class DemoApp(MDApp):

    def build(self):
        screen = Screen() # สร้าง obj หน้าจอ

        scroll = ScrollView() # สร้าง scroll bar
        list_view = MDList() # สร้าง obj รายชื่อไอเทม
        scroll.add_widget(list_view) # เพิ่มรายชื่อไอเท็ม

        # for-loop สร้าง item20 ชิ้น
        for i in range(20):
            image = ImageLeftWidget(source='like.png')
            #icon = IconLeftWidget(icon= 'android')
            items = ThreeLineIconListItem(text='Item ' + str(i), secondary_text='Hi world', tertiary_text='Hi')
            #items = ThreeLineIconListItem(text='Item '+ str(i), secondary_text='Hi world', tertiary_text='Hi') # แสดง list 3 แถวใน1 item

            items.add_widget(image)
            list_view.add_widget(items)
            #items.add_widget(icon) # add widget icon android



        screen.add_widget(scroll)

        return screen

DemoApp().run()
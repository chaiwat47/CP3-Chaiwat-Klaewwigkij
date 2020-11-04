from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp


class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        table = MDDataTable(
                            pos_hint = {'center_x': 0.5, 'center_y': 0.5},
                            size_hint=(0.9, 0.6),

                            rows_num = 12,
                            # สร้างคอลัมน์
                            column_data=[
                                ('No.', dp(18)),
                                ('Name', dp(20)),
                                ('Count', dp(20)),
                                ('Time', dp(20))
                            ],
                            check=True,  # ทำเครื่องหมายเช็คหน้าตาราง
                            # สร้าง data ตาม row
                            row_data = [
                                ('1', 'Mind', '01', '18.30'),
                                ('2', 'Nuch', '02', '18.00'),
                                ('3', 'Mind', '03', '18.30'),
                                ('4', 'Nuch', 'q', '18.00'),
                                ('5', 'Mind', 'a', '18.30'),
                                ('6', 'Nuch', 'g', '18.00'),
                                ('7', 'Mind', 't', '18.30'),
                                ('8', 'Nuch', 'a', '18.00'),
                                ('9', 'Mind', 'a', '18.30'),
                                ('10', 'Nuch', 'a', '18.00'),
                                ('11', 'Mind', 'a', '18.30'),
                                ('12', 'Nuch', 'a', '18.00')
                            ]
                            )
        table.bind(on_check_press= self.check_press)
        table.bind(on_check_press=self.row_press)
        screen.add_widget(table)
        return screen

    # check และ un checkได้
    def check_press(self, instance_table, current_row):
        print(instance_table, current_row)

    def row_press(self, instance_table, current_row):
        print(instance_table, current_row)


DemoApp().run()

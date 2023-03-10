from flet import *
from script import *
import flet as ft
import pyperclip


def main(page : Page):
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.title = "Encoder & Decoder"
    page.window_width = 1000
    page.window_height = 1000
    page.bgcolor = "#40513B"
    page.fonts = {
        "Tilt Neon":"/fonts/TiltNeon.ttf"
    }
    def close_banner(e):
        page.banner.open = False
        page.update()
    page.banner = ft.Banner(
        bgcolor=ft.colors.AMBER_500,
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40),
        content=ft.Text(
            "Oops, there were some errors while converting."
        ),
        actions=[
            ft.ElevatedButton("ok",bgcolor=ft.colors.AMBER_500,color="white", on_click=close_banner),
        ],
    )
    def show_banner_click(e):
        page.banner.open = True
        page.update()
    def encode(e):
        if Encode(tf.value) == None:
            show_banner_click(page.controls)
        else:
            # print(Encode(tf.value))
            pyperclip.copy(Encode(tf.value))
            show_bs(page.controls)
            
    def bs_dismissed(e):
        print("Dismissed!")
    def close_bs(e):
        bs.open = False
        bs.update()
    def show_bs(e):
        bs.open = True
        bs.update()
    def decode(e):
        try:
            # print(Decode(tf2.value))
            shotext.value = Decode(tf2.value)
            # shotext.visible = True
            page.update()
        except:
            show_banner_click(page.controls)
    def clear(e):
        shotext.value = ""
        page.update()
    def change(e):
        index = e.control.selected_index
        if index == 0:
            t.visible = True
            t2.visible = False
            page.update()
        else:
            t.visible = False
            t2.visible = True
            page.update()
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.CODE_ROUNDED, label="Encode",selected_icon=True),
            ft.NavigationDestination(icon=ft.icons.CODE_OFF_ROUNDED, label="Decode"),
            
        ],
        bgcolor="#609966",
        on_change=change,
    )
    t = Column(horizontal_alignment=CrossAxisAlignment.CENTER,spacing=50,controls=[Text("Encode",size=50,font_family="Tilt Neon"),(Row(controls=[tf := TextField(border_color="#40513B",cursor_color="#40513B",color="#40513B",hint_text="Enter..."),ElevatedButton(text="Submit",bgcolor="#40513B",color="#EDF1D6",on_click=encode)],alignment=MainAxisAlignment.CENTER)),Text("",font_family="Tilt Neon",size=50)])
    t2 = Column(horizontal_alignment=CrossAxisAlignment.CENTER,spacing=50,visible=False,controls=[Text("Decode",size=50,font_family="Tilt Neon"),Row(controls=[tf2 := TextField(border_color="#40513B",cursor_color="#40513B",color="#40513B",hint_text="Enter..."),ElevatedButton(text="Submit",bgcolor="#40513B",color="#EDF1D6",on_click=decode),ElevatedButton(text="Clear",bgcolor="#40513B",color="#EDF1D6",on_click=clear)],alignment=MainAxisAlignment.CENTER),shotext := Text("",font_family="Tilt Neon",size=50)])
    bs = ft.BottomSheet(
        ft.Container(
            ft.Column(
                [
                    ft.Text("The Code Copied Into Your Clipboard"),
                    ft.ElevatedButton("Ok", on_click=close_bs),
                ],
                tight=True,
            ),
            padding=10,
        ),
        on_dismiss=bs_dismissed,
    )
    page.overlay.append(bs)
    MainCont = Container(
            width=700,
            alignment=alignment.center,
            height=700,
            bgcolor="#9DC08B",
            border_radius=15,
            content=(
                maincol := Column(
                    controls=[
                        # maincolumn := Column(
                            t,
                            t2,
                            
                    ],
                    alignment=MainAxisAlignment.CENTER
                )
            )
        )
    # page.add(MainCont)
    
    page.add(
        MainCont
    )
    page.update()



app(target=main,view=WEB_BROWSER,port=8080,assets_dir="assest")


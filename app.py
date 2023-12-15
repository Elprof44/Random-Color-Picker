import flet as ft
import random , time 
import pyperclip


def main(page: ft.Page):
   color = random.choice([ft.colors.TRANSPARENT,ft.colors.WHITE,ft.colors.GREY])
   page.title = "Random Color Picker"
   page.vertical_alignment = ft.MainAxisAlignment.CENTER
   page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
   page.window_height =700
   page.window_width = 200
   page.window_min_width = 200
   page.window_min_height = 700 / 1.5
   page.window_max_width = 250 * 1.2
   page.window_max_height= 700
   page.window_focused = True
   page.window_bgcolor = color
   page.bgcolor = color
   page.window_left = 700
   page.window_always_on_top = True

   listGrid = ft.GridView(expand=True ,max_extent=120 , spacing = 5 , run_spacing=5, padding=20 ,col=2 , child_aspect_ratio=2.5,)
  
   def random_colors ():
        return [f'#{random.randint(0,0xFFFFFF):06x}' for i in range(100)] 
   
   def copy(e):
       pyperclip.copy(e.control.content.value)
       initial = e.control.content.value 
       page.snack_bar = ft.SnackBar(content=ft.Text("copied") ,duration=100 ,bgcolor=ft.colors.TRANSPARENT)
       page.snack_bar.open = True
       e.control.scale = 1.1
       e.control.content.value = "copied"
       page.update()
       time.sleep(0.4)
       e.control.scale = 1
       e.control.content.value = initial
       page.update()
   
   def gn(e = 0):
        listGrid.clean()
        for i in random_colors():
            listGrid.controls.append(
           ft.Container(bgcolor=i , border_radius=10 , margin=7 , content=ft.Text(i.upper() , color=ft.colors.WHITE) ,
                        alignment=ft.alignment.center , on_click= copy ,scale=ft.transform.Scale(scale=1),
        animate_scale=ft.animation.Animation(600, ft.AnimationCurve.BOUNCE_OUT),))
        page.update()


   btm = ft.ElevatedButton("🔎Random" , on_click= gn)
   col =ft.Row([btm ],wrap=True)
   
   page.add(listGrid , col )
   gn()

ft.app(target=main , name="Random Color Picker")

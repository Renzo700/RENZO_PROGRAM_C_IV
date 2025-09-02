import flet as ft

def main(page: ft.Page):
    page.title = "segunda clase programacion concurrente"
    page.add(ft.Text("welcome to flet!"))
    
ft.app(target=main)
import flet as ft

def main(page: ft.Page):
    page.title = "Hello, Flet!"
    page.window_width = 350 
    page.window_height = 600
    page.add(ft.Text("Welcome to Flet!"))

# Run the application
ft.app(target=main)

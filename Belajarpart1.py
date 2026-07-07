import flet as ft

def main(page: ft.Page):
    def button_click(e):
        page.controls.append(ft.Text("Clicked!"))
        # no need to call page.update() — it happens automatically

    page.controls.append(ft.Button("Click me", on_click=button_click))
    # no need to call page.update() here either

ft.run(main)
import flet as ft

def main(page:ft.Page):

    message = ft.Text("Hello!")
    insert_name = ft.TextField(label="Insert your name",text_size=10)

    def button(e):
        message.value = f'Hi {insert_name.value}!'
        page.update()

    button_1 = ft.ElevatedButton(
        "Click me!",
        on_click=button
    )

    page.add(
        message,
        input,
        button_1
    )

ft.run(main)

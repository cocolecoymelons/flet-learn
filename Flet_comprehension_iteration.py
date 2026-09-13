import flet as ft

def main(page):

    message_list = ["a",'b','c','d','e']

    message_show = ft.Column()

    for i in message_list:
        message_show.controls.append(ft.Text(i))

    page.add(
        message_show
    )

ft.run(main)

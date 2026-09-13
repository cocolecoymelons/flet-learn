import flet as ft
from code3_ATD import add_task_definer
from discard_task_file import discard_tasks_button

def main(page):

    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER

    list_of_tasks_list = []

    show_task_message = ft.Column()

    first_message = ft.Text("What should we do today?",
            text_align=ft.MainAxisAlignment.CENTER,
            size=20)

    def clear_task_textfieldvalue(e):# CTTFV func
        add_task_popup.content.value = ''
        page.update()

    def close_atp_popup(e):
        page.pop_dialog()

    add_task_popup = ft.AlertDialog(
        title="Add Task",
        content=ft.TextField(label="Add task, ex: Take out trash"),
        actions=[
            ft.ElevatedButton(content="Add",on_click=lambda e: add_task_definer(
                e,list_of_tasks_list,show_task_message,add_task_popup.content,close_atp_popup
            )
                ),
            ft.ElevatedButton(content="Cancel",on_click=close_atp_popup)
        ],
        on_dismiss=clear_task_textfieldvalue
    )

    def open_atp_popup(e):
        page.show_dialog(add_task_popup)
        page.update()


    add_task_button = ft.ElevatedButton(
        content="Add Task",
        on_click=open_atp_popup
    )

    discard_button = ft.ElevatedButton(
        content='Discard seleceted task',
        on_click= lambda e: discard_tasks_button(e, show_task_message.controls)
    )

    page.add(
        first_message,
        add_task_button,
        discard_button,
        show_task_message
    )

ft.run(main)

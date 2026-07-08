import flet as ft

class ToDo:
    def __init__(self):
        self.todo_list = []
    def add_todo(self, x):
        self.todo_list.append(x)

TODO = ToDo()

def main(page: ft.Page):
    page.title = "To Do List Apk"
    
    # Buat todo_input dan todo_add_button di sini, sebelum display_todo_list
    todo_input = ft.TextField(
        label="What's the plan today?", 
        hint_text="Doing my homework",
        width=300  # Atur lebar agar terlihat lebih baik
    )

    def add_todo(e):
        if todo_input.value.strip():
            TODO.add_todo(todo_input.value)
            todo_input.value = ""
            display_todo_list()
    
    todo_add_button = ft.FilledButton(
        text="Add",
        on_click=add_todo
    )

    def display_todo_list():
        page.clean()
        
        # Container untuk todo list
        todo_items = []
        if not TODO.todo_list:
            todo_items.append(ft.Text("You don't have any activities to do!"))
        else:
            for i in TODO.todo_list:
                todo_items.append(ft.Text(i))
        
        # Input area - di tengah
        input_area = ft.Column(
            [todo_input, todo_add_button],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10  # Jarak antara TextField dan Button
        )
        
        # Main content
        page.add(
            ft.Column(
                todo_items + [
                    ft.Divider(),  # Pemisah
                    input_area
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        )
        page.update()

    display_todo_list()

ft.run(main)
import flet as ft

def discard_tasks_button(e,showtask_var):
    showtask_var = [
        new_tasks for new_tasks in showtask_var if not new_tasks
    ]
    print(f"delete punya = {showtask_var}")
    e.page.update()
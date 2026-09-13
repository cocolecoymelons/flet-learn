import flet as ft

def add_task_into_showtaskmessage(e,list_of_tasks_parameter,showtask_var): #ATISTM func

        if not list_of_tasks_parameter:
            return

        showtask_var.controls.clear()
        showtask_var.controls.extend(
            ft.Checkbox(
                label=task,
                label_position=ft.LabelPosition.LEFT,
                value=False
            ) 
                for task in list_of_tasks_parameter

        )
        print(f"yang cehckbox{showtask_var}")
        e.page.update()
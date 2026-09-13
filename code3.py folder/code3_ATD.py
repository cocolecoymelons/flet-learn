import flet as ft
from code3_ATISTM import add_task_into_showtaskmessage


def add_task_definer(e,list_of_tasks_parameter,showtask_var,task_field,close_atp_popup): # ATD func
        task_value = task_field.value.strip()
        if not task_value:
            task_value.label = "Task must not be empty!"
            e.page.update()
            return

        list_of_tasks_parameter.append(task_value)
        add_task_into_showtaskmessage(e,list_of_tasks_parameter,showtask_var)

        print(f"yang definer{showtask_var}")
        close_atp_popup(e)
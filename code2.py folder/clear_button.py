import flet as ft

def clear_after_enter(first_number,second_number,e):
    first_number.value = ""
    second_number.value = ""

    e.page.update()

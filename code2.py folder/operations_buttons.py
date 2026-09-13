import flet as ft

from clear_button import clear_after_enter

def operations_buttons_function(first_number,second_number,result,what_operator):

    def evaluator_button(e):
        try:

            operations = {
                'addition':lambda a,b: a + b,
                'substraction':lambda a,b: a - b,
                'multiplication':lambda a,b: a*b,
                'division':lambda a,b: a/b
            }

            operate = operations[what_operator]

            result.value = f"| {operate(int(first_number.value),int(second_number.value))}"

            e.page.update()

        except ZeroDivisionError:

            result.value = "Can't divide with 0"
            e.page.update()

        except ValueError:
            
            result.value = "Input a Number!"
            e.page.update()
            
    return evaluator_button
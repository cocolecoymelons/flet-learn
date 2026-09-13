import flet as ft
from operations_buttons import operations_buttons_function
from clear_button import clear_after_enter

def main(page:ft.Page):


    result = ft.Text(f'| 0',size=25,color=ft.Colors.GREEN,weight=ft.FontWeight.W_500)

    number_1 = ft.TextField(
        label="Insert first number",
        width=250
    )
    number_2 = ft.TextField(
        label="Insert second number",
        width=250
    )

    st_displays_buttons_list = [('+','addition'),
                             ('-','substraction')]
    nd_displays_buttons_list = [('*','multiplication'),
                             ('/','division')]

    clear_button = ft.ElevatedButton(
        "C",
        on_click=lambda e: clear_after_enter(number_1, number_2, e)
    )

    page.add(
        ft.Column(
            [
                ft.Container(content=result,
                             border_radius=5,
                             padding=5,
                             bgcolor=ft.Colors.WHITE_10,
                             width=500,
                             alignment=ft.alignment.Alignment.CENTER_RIGHT,
                             ),
                ft.Row(
                    [
                        number_1,number_2
                    ],
                ),
                ft.Row(
                    [
                        ft.Column([
                            ft.ElevatedButton(
                                operator_symbol,
                                on_click=operations_buttons_function(number_1,number_2,result,operator),
                                width=70,
                                height=45,
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))
                                ) for operator_symbol, operator in st_displays_buttons_list
                        ]),
                        ft.Column([ft.ElevatedButton(
                                operator_symbol,
                                on_click=operations_buttons_function(number_1,number_2,result,operator),
                                width=70,
                                height=45,
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))
                                ) for operator_symbol, operator in nd_displays_buttons_list]),
                        ft.Column(
                            [
                                clear_button
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.END,
                        expand=True
                        )
                    ],
                    width=500,
                )
        ]
    )
)

ft.app(target=main)
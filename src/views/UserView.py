# src/views/UserView.py

import flet as ft

def UserView(page, auth_controller):

    page.title = "Perfil"

    user = getattr(page, "user_data", None)

    return ft.View(

        route="/perfil",

        appbar=ft.AppBar(

            title=ft.Text(
                f"Perfil de {user['nombre'] if user else 'Usuario'}"
            ),

            bgcolor=ft.Colors.BLUE_GREY_900,

            color="white",

            actions=[

                ft.IconButton(
                    ft.Icons.DASHBOARD,
                    on_click=lambda e: page.go("/dashboard")
                ),

                ft.IconButton(
                    ft.Icons.EXIT_TO_APP,
                    on_click=lambda e: page.go("/")
                )

            ]

        ),

        controls=[

            ft.Container(

                padding=30,

                bgcolor=ft.Colors.BLUE_GREY_900,

                border_radius=12,

                content=ft.Column(

                    [

                        ft.Text(
                            "Información del usuario",
                            size=28,
                            weight="bold",
                            color=ft.Colors.RED_900
                        ),

                        ft.Divider(),

                        ft.Text(
                            f"Nombre: {user['nombre'] if user else ''}",
                            size=20
                        ),

                        ft.Text(
                            f"Correo: {user['correo'] if user else ''}",
                            size=20
                        ),

                        ft.Text(
                            f"Teléfono: {user['telefono'] if user else ''}",
                            size=20
                        )

                    ],

                    spacing=15

                )
            )

        ],

        bgcolor=ft.Colors.BLACK

    )
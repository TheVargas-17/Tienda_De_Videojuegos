import flet as ft

def DashboardView(page, game_controller):

    page.title = "Tienda"

    user = getattr(page, "user_data")

    juegos = game_controller.obtener_juegos()

    cards = []

    for juego in juegos:

        cards.append(

            ft.Container(

                bgcolor=ft.Colors.BLUE_GREY_900,

                padding=15,

                margin=10,

                content=ft.Column(

                    [

                        ft.Text(
                            juego["nombre"],
                            size=20,
                            weight="bold"
                        ),

                        ft.Text(
                            f"Consola: {juego['nombre_consola']}"
                        ),

                        ft.Text(
                            f"Precio: ${juego['precio']}"
                        ),

                        ft.Text(
                            f"Stock: {juego['stock']}"
                        ),

                        ft.ElevatedButton(
                            "Comprar"
                        )

                    ]

                )

            )

        )

    return ft.View(

        route="/dashboard",

        appbar=ft.AppBar(

            title=ft.Text(
                f"Tienda de {user['nombre']}"
            ),

            bgcolor=ft.Colors.BLUE_GREY_900,

            color="white",

            actions=[

                ft.IconButton(
                    ft.Icons.PERSON,
                    on_click=lambda _: page.go("/perfil")
                ),

                ft.IconButton(
                    ft.Icons.EXIT_TO_APP,
                    on_click=lambda _: page.go("/")
                )

            ]

        ),

        bgcolor=ft.Colors.BLACK,

        controls=[

            ft.Container(

                padding=20,

                content=ft.Column(

                    [

                        ft.Text(
                            "Catálogo de videojuegos",
                            size=25,
                            weight="bold",
                            color=ft.Colors.RED_900
                        ),

                        ft.Column(
                            cards,
                            scroll=ft.ScrollMode.ALWAYS
                        )

                    ]

                )

            )

        ]

    )
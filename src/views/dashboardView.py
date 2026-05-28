import flet as ft

def DashboardView(page, game_controller):

    page.title = "Tienda"

    user = getattr(page, "user_data")

    juegos = game_controller.obtener_juegos()

    cards = []
    def comprar(juego):

        game_controller.comprar_juego(
            user["id_cliente"],
            juego["id_juego"],
            juego["id_consola"]
        )

        page.snack_bar = ft.SnackBar(
            ft.Text("Compra realizada")
        )

        page.snack_bar.open = True

        page.update()


    for juego in juegos:

        card = ft.Container(
            width=260,
            bgcolor="#1e1e2f",
            border_radius=15,
            padding=12,
            margin=8,

            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=10,
                color=ft.Colors.BLACK54,
                offset=ft.Offset(0, 4)
            ),

            content=ft.Column(
                spacing=8,

                controls=[

                    ft.Container(
                        height=120,
                        bgcolor="#2b2b40",
                        border_radius=12,
                        alignment=ft.Alignment(0, 0),

                        content=ft.Image(
                            src=""      ,
                            size=60,
                            color="#ff1744"
                        )
                    ),

                    ft.Text(
                        juego["nombre"],
                        size=18,
                        weight=ft.FontWeight.BOLD,
                        color="white"
                    ),

                    ft.Text(
                        f"Consola: {juego['nombre_consola']}",
                        color="#d6d6d6"
                    ),

                    ft.Text(
                        f"Precio: ${juego['precio']}",
                        color="#00e676",
                        weight=ft.FontWeight.BOLD
                    ),

                    ft.Text(
                        f"Stock: {juego['stock']}",
                        color="#64b5f6"
                    ),

                    ft.ElevatedButton(
                        "Comprar",
                        on_click=lambda e, j=juego: comprar(j),

                        style=ft.ButtonStyle(
                            bgcolor="#ff1744",
                            color="white",
                            shape=ft.RoundedRectangleBorder(radius=10)),
                        width=220)]) )

        cards.append(
            ft.Container(
                content=card,
                col={"sm": 12, "md": 6, "lg": 4}))
    return ft.View(
        route="/dashboard",
        bgcolor="#121212",
        appbar=ft.AppBar(
            title=ft.Text(
                f"Tienda de {user['nombre']}",
                color="white"),
            bgcolor="#1e1e2f",
            actions=[

    ft.IconButton(
        icon=ft.Icons.SHOPPING_BAG,
        icon_color="white",
        on_click=lambda _: page.go("/compras")
    ),

    ft.IconButton(
        icon=ft.Icons.PERSON,
        icon_color="white",
        on_click=lambda _: page.go("/perfil")
    ),

    ft.IconButton(
        icon=ft.Icons.EXIT_TO_APP,
        icon_color="white",
        on_click=lambda _: page.go("/")
    )

]),
        controls=[
            ft.Container(
                padding=20,
                expand=True,
                content=ft.Column(
                    spacing=15,
                    controls=[
                        ft.Text(
                            "Catálogo de videojuegos",
                            size=28,
                            weight=ft.FontWeight.BOLD,
                            color="#ff1744"),
                        ft.ResponsiveRow(
                            controls=cards,
                            spacing=10,
                            run_spacing=10)],
                    scroll=ft.ScrollMode.ALWAYS))])
import flet as ft


def ComprasView(page, game_controller):

    user = getattr(page, "user_data")

    ventas = game_controller.obtener_compras(user["id_cliente"])

    def eliminar_compra(id_venta):

        game_controller.eliminar_compra(id_venta)

        page.snack_bar = ft.SnackBar(
            content=ft.Text("Compra eliminada")
        )

        page.snack_bar.open = True

        page.go("/compras")

        page.update()

    def cambiar_estado(id_venta):

        game_controller.cambiar_estado(id_venta)

        page.snack_bar = ft.SnackBar(
            content=ft.Text("Estado actualizado")
        )

        page.snack_bar.open = True

        page.go("/compras")

        page.update()

    compras = []

    for venta in ventas:

        id_actual = venta["id_venta"]

        compras.append(

            ft.Container(

                bgcolor="#1e1e2f",

                border_radius=15,

                padding=15,

                margin=8,

                content=ft.Column(

                    spacing=10,

                    controls=[

                        ft.Text(
                            venta["juego"],
                            size=20,
                            weight=ft.FontWeight.BOLD,
                            color="white"
                        ),

                        ft.Text(
                            f"Consola: {venta['consola']}",
                            color="#d6d6d6"
                        ),

                        ft.Text(
                            f"Fecha: {venta['fecha']}",
                            color="#64b5f6"
                        ),

                        ft.Text(
                            f"Estado: {venta['estado']}",
                            color="#00e676"
                        ),

                        ft.Row(
                            spacing=10,
                            controls=[
                                ft.ElevatedButton(
                                    "Cambiar estado",
                                    bgcolor="#2979ff",
                                    color="white",
                                    on_click=lambda e, id_venta=id_actual: cambiar_estado(id_venta)
                                ),
                                ft.ElevatedButton(
                                    "Eliminar",
                                    bgcolor="#ff1744",
                                    color="white",
                                    on_click=lambda e, id_venta=id_actual: eliminar_compra(id_venta))])])))

    return ft.View(

        route="/compras",
        bgcolor="#121212",
        appbar=ft.AppBar(
            leading=ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                icon_color="white",
                on_click=lambda _: page.go("/dashboard")
            ),

            title=ft.Text(
                "Mis compras",
                color="white"
            ),
            bgcolor="#1e1e2f"
        ),
        controls=[

            ft.Container(
                expand=True,
                padding=20,
                content=ft.Column(
                    controls=compras,
                    scroll=ft.ScrollMode.ALWAYS,
                    expand=True))])
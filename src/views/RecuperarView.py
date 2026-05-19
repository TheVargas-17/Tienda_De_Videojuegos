import flet as ft

def RecuperarView(page: ft.Page, auth_controller):

    def mostrar(msg):
        page.snack_bar = ft.SnackBar(ft.Text(msg))
        page.snack_bar.open = True
        page.update()

    correo = ft.TextField(
        label="Correo",
        width=280,
        prefix_icon=ft.Icons.EMAIL
    )

    nueva = ft.TextField(
        label="Nueva contraseña",
        width=280,
        password=True,
        can_reveal_password=True,
        prefix_icon=ft.Icons.LOCK
    )

    confirmar = ft.TextField(
        label="Confirmar contraseña",
        width=280,
        password=True,
        can_reveal_password=True,
        prefix_icon=ft.Icons.LOCK
    )

    def cambiar(e):

        if not correo.value or not nueva.value or not confirmar.value:
            mostrar("Complete todos los campos")
            return

        if nueva.value != confirmar.value:
            mostrar("Las contraseñas no coinciden")
            return

        success, msg = auth_controller.recuperar_contrasena(
            correo.value,
            nueva.value
        )

        mostrar(msg)

        if success:
            page.go("/")

    return ft.View(
        route="/recuperar",

        appbar=ft.AppBar(
            title=ft.Text("Recuperar contraseña"),
            bgcolor=ft.Colors.BLUE_GREY_900,
            color="white",
            center_title=True
        ),

        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,

        controls=[

            ft.Container(
                width=320,
                bgcolor=ft.Colors.WHITE,
                border_radius=12,
                padding=25,

                content=ft.Column(
                    [

                        ft.Text(
                            "Recuperar contraseña",
                            size=22,
                            weight="bold"
                        ),

                        correo,

                        nueva,

                        confirmar,

                        ft.ElevatedButton(
                            "Actualizar contraseña",
                            width=280,
                            on_click=cambiar
                        ),

                        ft.TextButton(
                            "Volver al login",
                            on_click=lambda e: page.go("/")
                        )

                    ],

                    spacing=15,

                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )
        ]
    )
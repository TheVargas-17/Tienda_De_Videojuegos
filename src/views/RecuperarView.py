import flet as ft


def RecuperarView(page: ft.Page, auth_controller):

    def mostrar(msg):

        page.snack_bar = ft.SnackBar(
            ft.Text(msg)
        )

        page.snack_bar.open = True

        page.update()

    correo = ft.TextField(
        label="Correo",
        width=280,
        color=ft.Colors.WHITE,
        label_style=ft.TextStyle(color=ft.Colors.WHITE),
        text_style=ft.TextStyle(color=ft.Colors.WHITE)
    )

    codigo = ft.TextField(
        label="Código de verificación",
        width=280,
        color=ft.Colors.WHITE,
        label_style=ft.TextStyle(color=ft.Colors.WHITE),
        text_style=ft.TextStyle(color=ft.Colors.WHITE)
    )

    nueva = ft.TextField(
        label="Nueva contraseña",
        width=280,
        password=True,
        can_reveal_password=True,
        color=ft.Colors.WHITE,
        label_style=ft.TextStyle(color=ft.Colors.WHITE),
        text_style=ft.TextStyle(color=ft.Colors.WHITE)
    )

    confirmar = ft.TextField(
        label="Confirmar contraseña",
        width=280,
        password=True,
        can_reveal_password=True,
        color=ft.Colors.WHITE,
        label_style=ft.TextStyle(color=ft.Colors.WHITE),
        text_style=ft.TextStyle(color=ft.Colors.WHITE)
    )

    def enviar_codigo(e):

        if not correo.value:

            mostrar("Ingrese un correo")

            return

        success, msg = auth_controller.enviar_codigo_recuperacion(
            correo.value
        )

        mostrar(msg)

    def cambiar(e):

        if (
            not correo.value
            or not codigo.value
            or not nueva.value
            or not confirmar.value
        ):

            mostrar("Complete todos los campos")

            return

        if nueva.value != confirmar.value:

            mostrar("Las contraseñas no coinciden")

            return

        success, msg = auth_controller.recuperar_contrasena(
            correo.value,
            codigo.value,
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

        bgcolor=ft.Colors.BLACK,

        controls=[

            ft.Container(
                width=320,
                bgcolor=ft.Colors.BLUE_GREY_900,
                border_radius=12,
                padding=25,
                content=ft.Column(
                    [

                        ft.Text(
                            "Recuperar contraseña",
                            size=22,
                            weight="bold",
                            color=ft.Colors.RED_900
                        ),

                        correo,

                        ft.ElevatedButton(
                            "Enviar código",
                            width=280,
                            on_click=enviar_codigo
                        ),

                        codigo,

                        nueva,

                        confirmar,

                        ft.ElevatedButton(
                            "Actualizar contraseña",
                            width=280,
                            bgcolor=ft.Colors.RED_700,
                            color=ft.Colors.WHITE,
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
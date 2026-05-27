import flet as ft


def LoginView(page: ft.Page, auth_controller):

    def mostrar_mensaje(msg):

        page.snack_bar = ft.SnackBar(
            ft.Text(msg)
        )

        page.snack_bar.open = True

        page.update()

    def login_click(e):

        if not correo.value or not contra.value:

            mostrar_mensaje(
                "Por favor, complete todos los campos"
            )

            return

        user, msg = auth_controller.login(
            correo.value,
            contra.value
        )

        if user:

            page.user_data = user

            page.go("/dashboard")

        else:

            mostrar_mensaje(msg)

    def registro(e):

        page.go("/registro")

    correo = ft.TextField(

        label="Correo",

        width=280,

        prefix_icon=ft.Icons.PERSON,

        color=ft.Colors.BLACK

    )

    contra = ft.TextField(

        label="Contraseña",

        width=280,

        password=True,

        can_reveal_password=True,

        prefix_icon=ft.Icons.LOCK,

        color=ft.Colors.BLACK

    )

    iniciar = ft.ElevatedButton(

        "Iniciar sesión",

        width=280,

        bgcolor=ft.Colors.RED_700,

        color="white",

        on_click=login_click

    )

    registrarse = ft.TextButton(

        "Crear cuenta",

        on_click=registro

    )

    recuperar = ft.TextButton(

        "¿Olvidaste tu contraseña?",

        width=280,

        on_click=lambda e: page.go("/recuperar")

    )

    contenido = ft.Container(

        bgcolor=ft.Colors.BLUE_GREY_900,

        content=ft.Column(

            [

                ft.Text(
                    "Acceso",
                    size=22,
                    weight="bold",
                    color=ft.Colors.RED_900
                ),

                correo,

                contra,

                iniciar,

                registrarse,

                recuperar

            ],

            spacing=15,

            horizontal_alignment=ft.CrossAxisAlignment.CENTER

        ),

        padding=25,

        border_radius=12,

        width=320

    )

    return ft.View(

        route="/",

        appbar=ft.AppBar(

            title=ft.Text("Login"),

            bgcolor=ft.Colors.BLUE_GREY_900,

            color="white",

            center_title=True

        ),

        vertical_alignment=ft.MainAxisAlignment.CENTER,

        horizontal_alignment=ft.CrossAxisAlignment.CENTER,

        bgcolor=ft.Colors.BLACK,

        controls=[contenido]

    )
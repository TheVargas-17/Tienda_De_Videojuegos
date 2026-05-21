import flet as ft


def RegistroView(page: ft.Page, auth_controller):

    def mostrar(msg):
        page.snack_bar = ft.SnackBar(ft.Text(msg))
        page.snack_bar.open = True
        page.update()

    nombre = ft.TextField(
        label="Nombre",
        width=280,
        prefix_icon=ft.Icons.BADGE
    )

    telefono = ft.TextField(
        label="Teléfono",
        width=280,
        prefix_icon=ft.Icons.CALL
    )

    correo = ft.TextField(
        label="Correo",
        width=280,
        prefix_icon=ft.Icons.PERSON
    )

    contrasena = ft.TextField(
        label="Contraseña",
        width=280,
        password=True,
        can_reveal_password=True,
        prefix_icon=ft.Icons.LOCK
    )

    def registra(e):

        if not nombre.value or not correo.value or not contrasena.value or not telefono.value:
            mostrar("Por favor, complete todos los campos")
            return

        try:

            user, msg = auth_controller.registrar_usuario(
                nombre.value,
                telefono.value,
                correo.value,
                contrasena.value
            )

            print(user)
            print(msg)

            mostrar(msg)

            if user:
                page.go("/")

        except Exception as ex:

            print("ERROR:", ex)

            mostrar("Error al registrar")

    registrar = ft.ElevatedButton(
        "Registrarse",
        width=280,
        bgcolor=ft.Colors.RED_700,
        color="white",
        on_click=registra
    )

    reversa = ft.TextButton(
        "Volver al login",
        on_click=lambda e: page.go("/")
    )

    contenido = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "Crear cuenta",
                    size=22,
                    weight="bold",
                    color=ft.Colors.RED_900
                ),

                nombre,

                telefono,

                correo,

                contrasena,

                registrar,

                reversa

            ],

            spacing=15,

            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),

        padding=25,

        border_radius=12,

        bgcolor=ft.Colors.WHITE,

        width=320
    )

    return ft.View(
        route="/registro",

        appbar=ft.AppBar(
            title=ft.Text("Registro"),

            bgcolor=ft.Colors.BLUE_GREY_900,

            color="white",

            center_title=True
        ),

        vertical_alignment=ft.MainAxisAlignment.CENTER,

        horizontal_alignment=ft.CrossAxisAlignment.CENTER,

        bgcolor=ft.Colors.BLACK,

        controls=[contenido]
    )
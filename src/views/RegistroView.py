import flet as ft


def RegistroView(page: ft.Page, auth_controller):

    def mostrar(msg):
        page.snack_bar = ft.SnackBar(ft.Text(msg))
        page.snack_bar.open = True
        page.update()

    nombre = ft.TextField(label="Nombre", width=135, prefix_icon=ft.Icons.BADGE)

    apellido = ft.TextField(label="Apellido", width=135)

    telefono = ft.TextField(label="Teléfono", width=280, prefix_icon=ft.Icons.CALL)

    correo = ft.TextField(label="Correo", width=280, prefix_icon=ft.Icons.PERSON)

    contrasena = ft.TextField(
        label="Contraseña",
        width=280,
        password=True,
        can_reveal_password=True,
        prefix_icon=ft.Icons.LOCK
    )

    def registra(e):

        if not nombre.value or not apellido.value or not correo.value or not contrasena.value or not telefono.value:
            mostrar("Por favor, complete todos los campos")
            return


        user, msg = auth_controller.registrar_usuario(
            nombre.value,
            telefono.value,   
            apellido.value,  
            correo.value,
            contrasena.value
        )

        mostrar(msg)

        if user:
            page.go("/")

    registrar = ft.ElevatedButton(
        "Registrarse",
        width=280,
        on_click=registra
    )

    reversa = ft.TextButton("Volver al login", on_click=lambda e: page.go("/"))

    contenido = ft.Container(
        content=ft.Column(
            [
                ft.Text("Crear cuenta", size=22, weight="bold"),
                ft.Row([nombre, apellido], alignment=ft.MainAxisAlignment.CENTER),
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
        controls=[contenido]
    )
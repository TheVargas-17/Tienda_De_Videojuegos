import flet as ft
from controllers.GameController import GameController
from controllers.UserController import AuthController
from views.LoginView import LoginView
from views.dashboardView import DashboardView
from views.RegistroView import RegistroView
from views.UserView import UserView
from views.RecuperarView import RecuperarView
from views.ComprasView import ComprasView


def start(page: ft.Page):

    page.title = "LOGIN"

    page.window_width = 450
    page.window_height = 700

    auth_ctrl = AuthController()
    game_ctrl = GameController()

    def route_change(e):

        page.views.clear()

        if page.route == "/":

            page.views.append(
                LoginView(page, auth_ctrl)
            )

        elif page.route == "/dashboard":

            page.views.append(
                DashboardView(page, game_ctrl)
            )

        elif page.route == "/registro":

            page.views.append(
                RegistroView(page, auth_ctrl)
            )

        elif page.route == "/perfil":

            page.views.append(
                UserView(page, auth_ctrl)
            )

        elif page.route == "/recuperar":

            page.views.append(
                RecuperarView(page, auth_ctrl)
            )

        elif page.route == "/compras":

            page.views.append(
                ComprasView(page, game_ctrl)
            )

        page.update()

    def view_pop(e):

        if len(page.views) > 1:

            page.views.pop()

            page.update()

            top_view = page.views[-1]

            page.go(top_view.route)

    page.on_route_change = route_change

    page.on_view_pop = view_pop

    if page.route == "/":

        route_change(None)

    else:

        page.go("/")


def main():

    ft.app(start)


if __name__ == "__main__":

    main()
import flet as ft
import os
import sys
import subprocess

def main(page: ft.Page):
    if not page.web:
        page.window.width = 400
        page.window.height = 300
        page.window.center()
        page.window.resizable = False

    page.title = "Login - Sistema de Viajes"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Campos de entrada
    user_input = ft.TextField(label="Usuario", width=250)
    pass_input = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=250)
    mensaje = ft.Text("", color="red")

    # Función para abrir dashboard
    def abrir_dashboard():
        page.window.close()
        ruta_dashboard = os.path.join(os.path.dirname(__file__), "dashboard.py")
        subprocess.Popen([sys.executable, ruta_dashboard])
    def abrir_deliverys():
        page.window.close()
        ruta_dashboard = os.path.join(os.path.dirname(__file__), "deliverys.py")
        subprocess.Popen([sys.executable, ruta_dashboard])
    def abrir_cliente():
        page.window.close()
        ruta_dashboard = os.path.join(os.path.dirname(__file__), "cliente.py")
        subprocess.Popen([sys.executable, ruta_dashboard])
    def abrir_administrador():
        page.window.close()
        ruta_dashboard = os.path.join(os.path.dirname(__file__), "administrador.py")
        subprocess.Popen([sys.executable, ruta_dashboard])


    # Función para validar login
    def validar_login(e):
        if user_input.value == "USUARIO_7" and pass_input.value == "123":
            mensaje.value = "✅ Acceso correcto"
            page.update()
            abrir_dashboard()
        if user_input.value == "DELIVERY_7" and pass_input.value == "123":
            mensaje.value = "✅ Acceso correcto"
            page.clean()
            abrir_deliverys()
        if user_input.value == "CLIENTE_7" and pass_input.value == "12345":
            mensaje.value = "✅ Acceso correcto"
            page.clean()
            abrir_cliente()
        if user_input.value == "ADMINISTRADOR_7" and pass_input.value == "777":
            mensaje.value = "✅ Acceso correcto"
            page.clean()
            abrir_administrador()
        else:
            mensaje.value = "❌ Usuario o contraseña incorrectos"
            page.update()

    # Botón de login
    btn_login = ft.ElevatedButton(
        text="Ingresar",
        bgcolor="#05EF91",
        color="white",
        width=250,
        on_click=validar_login
    )

    # Layout del login
    page.add(
        ft.Column(
            [
                ft.Text("🔑SISTEMAS DE INICIO DE SESION DELIVERY RENZO🍔", size=25, weight=ft.FontWeight.BOLD, color="#F34121E8"),
                user_input,
                pass_input,
                btn_login,
                mensaje
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        )
    )

if __name__ == "__main__":
    ft.app(target=main)

import flet as ft

def main(page: ft.Page):
    page.window.width = 800
    page.window.height = 600
    page.window.resizable = True
    page.window.center()
    page.title = "Dashboard - Sistema de Ventas"
    
    # Contenido principal del Dashboard
    contenido_dashboard = ft.Column([
        ft.Text("🎯 DASHBOARD PRINCIPAL", size=30, weight=ft.FontWeight.BOLD, color="#2196F3"),
        ft.Divider(height=20),
        ft.Text("Bienvenido al sistema de gestión de ventas", size=18),
        ft.Divider(height=30),
        ft.Row([
            ft.ElevatedButton("Ver Reportes"),
            ft.ElevatedButton("Gestionar Productos"),
            ft.ElevatedButton("Clientes"),
        ], spacing=20),
        ft.Divider(height=30),
        ft.ElevatedButton("Volver al Inicio", on_click=lambda e: volver_inicio(e))
    ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    # 🔹 Fondo oscuro con gradiente (puedes ajustarlo si prefieres otro estilo)
    layout_dashboard = ft.Container(
        content=contenido_dashboard,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=["#1a237e", "#0d47a1"]  # azul oscuro → más oscuro
        ),
        expand=True,
        padding=20
    )

    page.add(layout_dashboard)

    # 🔹 Función para volver al login
    def volver_inicio(e):
        import logeo   # importa tu login (logeo.py debe estar en la misma carpeta)
        page.clean()   # limpia la pantalla
        logeo.main(page)  # vuelve a cargar el login en la misma ventana
    
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
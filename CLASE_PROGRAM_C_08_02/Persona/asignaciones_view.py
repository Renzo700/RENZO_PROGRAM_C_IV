import flet as ft


class AsignacionesView(ft.Container):
    """Vista placeholder para Asignaciones Semanales.

    Muestra un título, un botón "Volver" y una tabla vacía que se puede
    completar más adelante con las columnas reales de asignaciones.
    """
    def __init__(self, page, volver_atras):
        super().__init__(expand=True)
        self.page = page
        self.volver_atras = volver_atras

        self.titulo = ft.Text("🗂️ Asignaciones Semanales", size=22, weight="bold")

        self.tabla = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("ID")),
                ft.DataColumn(ft.Text("Docente")),
                ft.DataColumn(ft.Text("Curso")),
                ft.DataColumn(ft.Text("Aula")),
                ft.DataColumn(ft.Text("Semana")),
            ],
            rows=[]
        )

        self.btn_volver = ft.ElevatedButton("⬅️ Volver", on_click=lambda e: self.volver_atras())
        self.btn_actualizar = ft.ElevatedButton("🔄 Actualizar", on_click=lambda e: self._actualizar())

        self.content = ft.Column(
            [
                self.titulo,
                ft.Row([self.btn_volver, self.btn_actualizar], alignment=ft.MainAxisAlignment.START),
                ft.Container(self.tabla, expand=True, border_radius=10, padding=10, bgcolor=ft.Colors.BLUE_50)
            ],
            spacing=15,
            expand=True,
            scroll=ft.ScrollMode.AUTO
        )

    def _actualizar(self):
        # Placeholder: más tarde conectar con la base de datos
        self.page.snack_bar = ft.SnackBar(ft.Text("Actualización no implementada aún"))
        self.page.snack_bar.open = True
        self.page.update()

import flet as ft

from Persona.personas_view import PersonasView
from Persona.docentes_view import DocentesView
from Persona.asignaciones_view import AsignacionesView
from Usuario.usuarios_view import UsuariosView

class DashboardView(ft.Container):
    def __init__(self, page, cambiar_vista):
        super().__init__(expand=True)
        self.page = page
        self.cambiar_vista = cambiar_vista

        titulo = ft.Text("📘 Panel Principal – Sistema de Horarios Marello", size=24, weight="bold")

        tablas = [
            ("Personas", "Datos básicos (base de la identidad)"),
            ("Usuarios", "Cuentas, credenciales, y roles (enlace a personas)"),
            ("Especialidades", "Campos de estudio (Informática, Contabilidad, etc.)"),
            ("Ciclos", "Los 6 niveles académicos (I, II, III, etc.)"),
            ("Cursos", "Materias que se dictan"),
            ("Aulas", "Recurso físico limitado"),
            ("Docentes", "Quién enseña (enlace a Personas)"),
            ("Horarios_Base", "Slots fijos de tiempo"),
            ("Semanas", "Las 18 semanas del ciclo"),
            ("Estructura_Curricular", "Regla curricular (Curso–Ciclo–Especialidad)"),
            ("Asignaciones_Semanales", "Asignación final Docente + Curso + Aula + Semana")
        ]

        grid = ft.GridView(
            expand=True,
            runs_count=3,
            max_extent=280,
            child_aspect_ratio=1.2,
            spacing=10,
            run_spacing=10
        )

        # 🔧 Aquí se corrige el uso de on_click:
        for nombre, descripcion in tablas:
            card_content = ft.Container(
                content=ft.Column(
                    [
                        ft.Text(nombre, size=18, weight="bold"),
                        ft.Text(descripcion, size=13, color=ft.Colors.GREY)
                    ],
                    spacing=5
                ),
                padding=15,
                border_radius=10,
                bgcolor=ft.Colors.BLUE_50,
                ink=True,  # efecto visual al hacer clic
                on_click=lambda e, n=nombre: self.mostrar_tabla(n)
            )

            grid.controls.append(ft.Card(content=card_content, elevation=3))

        self.content = ft.Column(
            [
                titulo,
                grid
            ],
            expand=True,
            scroll=ft.ScrollMode.AUTO,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.START
        )

    # Evento al hacer clic en una tarjeta
    def mostrar_tabla(self, nombre_tabla):
        if nombre_tabla == "Personas":
            # Pasamos la función cambiar_vista para que la vista pueda navegar tanto a edición como volver al dashboard
            personas_vista = PersonasView(self.page, self.cambiar_vista)
            self.cambiar_vista(personas_vista)

        elif nombre_tabla == "Usuarios":
            usuarios_vista = UsuariosView(self.page, volver_atras=lambda: self.cambiar_vista(DashboardView(self.page, self.cambiar_vista)))
            self.cambiar_vista(usuarios_vista)

        elif nombre_tabla == "Docentes":
            docentes_vista = DocentesView(self.page, volver_atras=lambda: self.cambiar_vista(DashboardView(self.page, self.cambiar_vista)))
            self.cambiar_vista(docentes_vista)

        # 'Inscripciones' eliminado: no hay vista dedicada ahora

        elif nombre_tabla == "Asignaciones_Semanales":
            asign_vista = AsignacionesView(self.page, volver_atras=lambda: self.cambiar_vista(DashboardView(self.page, self.cambiar_vista)))
            self.cambiar_vista(asign_vista)

        else:
            dlg = ft.AlertDialog(
                title=ft.Text("Tabla no implementada"),
                content=ft.Text(f"La vista para '{nombre_tabla}' aún no está disponible."),
                actions=[ft.TextButton("Cerrar", on_click=lambda e: self.page.dialog.close())]
            )
            self.page.dialog = dlg
            dlg.open = True
            self.page.update()
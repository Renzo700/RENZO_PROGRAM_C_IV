from conexion import ConexionDB


def prueba_crud():
    db = ConexionDB()
    conexion = db.conectar()
    if not conexion:
        print("No se pudo conectar a la BD para pruebas")
        return

    cur = conexion.cursor()
    try:
        # INSERT temporal
        cur.execute("INSERT INTO personas (nombres, apellidos, numero_documento, telefono) VALUES (%s,%s,%s,%s)",
                    ("PruebaNombre", "PruebaApellido", "00000000", "999999999"))
        conexion.commit()
        print("INSERT realizado")

        # SELECT el último insert
        cur.execute("SELECT persona_id, nombres, apellidos FROM personas WHERE numero_documento=%s", ("00000000",))
        row = cur.fetchone()
        print("SELECT ->", row)

        if row:
            pid = row[0]
            # DELETE el registro de prueba
            cur.execute("DELETE FROM personas WHERE persona_id=%s", (pid,))
            conexion.commit()
            print("DELETE realizado para id", pid)
        else:
            print("No se encontró registro insertado")

    except Exception as e:
        print("Error en pruebas CRUD:", e)
    finally:
        cur.close()
        db.cerrar(conexion)


if __name__ == '__main__':
    prueba_crud()

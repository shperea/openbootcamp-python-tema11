# En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas: la columna id
# de tipo entero, la columna nombre que será de tipo texto y la columna apellido que también será de tipo texto.
# Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.
# Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.

# He ampliado el ejercicio añadiendo la columna nota y una funcion donde se pueda consultar el identificador y la nota
# de cada alumno buscando por nombre y apellidos

import sqlite3


def main():

    nombre = input("Nombre del alumno: ").lower()
    apellido1 = input("Primer apellido del alumno: ").lower()
    apellido2 = input("Segundo apellido del alumno: ").lower()
    consultar_id_nota(nombre, apellido1, apellido2)
    # insertar_alumno(9, "miguel", "gutierrez", "gomez", "6.5")


def consultar_id_nota(nombre, apellido1, apellido2):
    conn = sqlite3.connect('ficheroalumnos.db', isolation_level=None)
    cursor = conn.cursor()

    query1 = f"SELECT id FROM alumnos WHERE nombre='{nombre}' AND apellido1='{apellido1}' AND apellido2='{apellido2}'"
    query2 = f"SELECT nota FROM alumnos WHERE nombre='{nombre}' AND apellido1='{apellido1}' AND apellido2='{apellido2}'"

    data1 = cursor.execute(query1).fetchone()
    data2 = cursor.execute(query2).fetchone()

    cursor.close()
    conn.close()

    if data1 is None:
        print("No hay ningun alumno con ese nombre")
    else:
        print(f"El identificador de {nombre.title()} {apellido1.title()} {apellido2.title()} es el {(list(data1))[0]}"
              f" y su nota es un {(list(data2))[0]}")


def insertar_alumno(id, nombre, apellido1, apellido2, nota):
    conn = sqlite3.connect('ficheroalumnos.db')
    cursor = conn.cursor()

    query = '''INSERT INTO alumnos(id, nombre, apellido1, apellido2, nota) VALUES(?, ?, ?, ?, ?)'''

    rows = cursor.execute(query, (id, nombre.lower(), apellido1.lower(), apellido2.lower(), nota))

    conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()

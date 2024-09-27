print("Examen Kaylee Alejandra Luevano Molina 22308051281248")
class musickey:

    def diccionario_instrumentos1248(self):
        print("Diccionario instrumentos")
        instrumentos =	{
        "codigo": "123456",
        "tipo": "acustico",
        "precio": 2000,
        "color": "rojo",
        "marca": "ibanez",
        "nombre": "guitarra",
        "tamaño": 124
    }
        print(instrumentos)
        for instrumento1, instrumento2  in instrumentos.items():
            print(instrumento1, instrumento2)

    def diccionario_Usuarios1248(self):
        print("Diccionario usuarios")
        usuarios =	{
        "id_usuario": "22308051281248",
        "historias": "guitarra, bajo",
        "nombre": "Kaylee Luevano",
        "tipo_pago": "Tarjeta",
        "Tickets": 3,
        "Productos adquiridos": "bateria",
        "Saldo": 2345
    }
        print(usuarios)
        for usser1, usser2  in usuarios.items():
            print(usser1, usser2)

    def diccionario_Mantenimiento1248(self):
        print("Diccionario Mantenimiento")
        Mantenimiento =	{
        "Horarios": "7:30a-10pm",
        "Pisos": "palnta1, planta2",
        "Intrumentos": " bateria, microfono, teclado",
        "oficinas": "administracion, muestra",
        "empleados": "Juan, Marta",
        "Materiales": "Trapo, destornillador",
        "tiempo_realizado": "3 horas"
    }
        print(Mantenimiento)
        for man1, man2  in Mantenimiento.items():
            print(man1, man2)
    def diccionario_Proveedores1248(self):
        print("Diccionario Proveedores")
        Proveedores =	{
        "id_proveedores": "124234234",
        "transporte": "camion",
        "contacto": "tus_proveedores_music",
        "telefono": 6564454848,
        "correo": "proveedor@gmail.com",
        "hora-llegada": 7.0,
        "hora salida": 9.0
    }
        print(Proveedores)
        for pro1, pro2  in Proveedores.items():
            print(pro1, pro2)


tablas= musickey()

tablas.diccionario_instrumentos1248()
tablas.diccionario_Usuarios1248()
tablas.diccionario_Mantenimiento1248()
tablas.diccionario_Proveedores1248()
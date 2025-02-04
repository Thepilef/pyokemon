persona = {"nombre": "andres", "edad": "21"}
print(persona)

persona["ciudad"] = "Madrid"
print(persona)

persona.pop("ciudad")
print(persona)

del persona["edad"]
print(persona)
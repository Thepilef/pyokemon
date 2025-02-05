#tipo string (cadenas de caracteres). strings delimitados por comillas dobles.
cadena_a = "hola"
print(cadena_a)
cadena_b = "mundo"
print(cadena_b)

#uso del operador "+" para concatenar
print(cadena_a + " " + cadena_b)

#tambien es posible escribir strings multi-linea facilmente
string_multi_1 = "esto es un string escrito en \
dos lineas. En este caso el string se interpreta como una solo linea"
print(string_multi_1)

string_multi_2 = '''triples comillas: esto es tambien un string escrito en dos lineas.
en este caso se conserva la separacion en lineas original.'''
print(string_multi_2)

string_multi_3 = """triples comillas: esto tambien es un string escrito en dos linesas.
En este caso se conserva la separacion en lineas original """
print(string_multi_3)
#declara una variable con tu edad. luego usa esta variable para calcular cuantos meses, dias,
#horas, minutos y segundos has vivido (aproximadamente)

# año = int(input("que año naciste: "))
# mes = int(input("en ue numero de mes naciste: "))
# dia = int(input("que dia naciste: "))
# print(f"naciste en la fecha " + str(dia).zfill(2) + "/" +  str(mes).zfill(2) + "/" + str(año))

# añoActual = int(input("que año es actualmente: "))
# mesActual = int(input("que numero de mes es actualmente: "))
# diaActual = int(input("que dia es actualmente: "))
# print(f"hoy es " + str(diaActual).zfill(2) + "/" + str(mesActual).zfill(2) + "/" + str(añoActual))

año = int(2003)
mes = int(5)
dia = int(20)
añoActual = int(2025)
mesActual = int(2)
diaActual = int(4)

añosvividos = añoActual - año 

mesesVividos = (añosvividos * 12) - mes + mesActual 

print(mesesVividos)

añosvividos = mesesVividos // 12
mesesParaAño = mesesVividos % 12

diasVividos = (mesesVividos * 30) 

print(f"has vivido {añosvividos} años, con {mesesParaAño} meses")
print(f"has vivido {diasVividos} dias") 
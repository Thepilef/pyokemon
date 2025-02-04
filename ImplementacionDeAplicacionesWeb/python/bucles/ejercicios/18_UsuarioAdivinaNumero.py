import random 

numero = random.randint(1,20)
num = 0
print(numero)

while True:
    num = int(input("escribe un numero del 1 al 20: ")) 
    if num == numero:
        break
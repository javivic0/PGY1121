#ejemplo de uso repositorio 

print("datos personales")
print("----------------")
nom=str(input("ingrese su nombre: "))
while True:
    try:
        edad=int(input("ingrese su edad: "))
        break
    except:
        print("valor no corresponde.")

print("-----------------------------")
print(f"su nombre es: {nom}")
print(f"su edad es:   {edad}")
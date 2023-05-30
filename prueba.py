entr1=0
entr2=0
entr3=0
total1=0
total2=0
total3=0
lol=1
print("--------------------------------")
print("   Bienvenido a CineDuoc")
print("--------------------------------")
while lol==1:
  print("selecciona tu categoria...")
  print("seccion:")
  print("1.niño   {1 a 13 años}")
  print("2.joven  {14 a 21 años}")
  print("3.adulto {mayor 22 años}")
  print("--------------------------------")
  op=int(input("selecciona.."))
  if op==1: 
    print("su categoria es niño")
    print("precio $5500")
    entrd=int(input("¿cuantas entradas va a llevar? "))
    trd=entrd*5500
    total1=trd
    entr1=entrd
    print(".............................................")
    print("             Boleta CineDuoc")
    print(f"categoria:  {op} niño")
    print(f"lleva       {entrd} entradas")
    print(f"total:     ${trd}")
    lol=int(input("Desea continuar? 1.si 2.no"))
  if op==2: 
    print("su categoria es joven")
    print("precio $7000")
    entrd=int(input("¿cuantas entradas va a llevar? "))
    trd=entrd*7000
    total2=trd
    entr2=entrd
    print(".............................................")
    print("             Boleta CineDuoc")
    print(f"categoria:  {op} joven")
    print(f"lleva       {entrd} entradas")
    print(f"total:     ${trd}")
    lol=int(input("Desea continuar? 1.si 2.no"))
  if op==3: 
    print("su categoria es adulto")
    print("precio $9000")
    entrd=int(input("¿cuantas entradas va a llevar? "))
    trd=entrd*9000
    total3=trd
    entr3=entrd
    print(".............................................")
    print("             Boleta CineDuoc")
    print(f"categoria:  {op} adulto")
    print(f"lleva       {entrd} entradas")
    print(f"total:      ${trd}")
    lol=int(input("Desea continuar? 1.si 2.no"))
print("----------------------------------------------------------")
print(" venta de categorias: ")
print(f"niño:  {entr1}")
print(f"joven: {entr2}")
print(f"adulto {entr3}")
print(f"total de ventas: {total1+total2+total3}")

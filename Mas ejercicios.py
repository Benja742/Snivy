
ent=" Barry pokemon"

pkm1=6

ent2="Lance champion"
pkm2=7

# if pkm2<=6:
#     print("Puede acceder a la liga pokemon")
# else:
#     print("Tiene mas pokemons de lo necesario")

# print(len(entrenador))

# print("El entrenador", entrenador, "tiene", pkm1, "pokemons")
# print("El entrenador", entrenador2, "tiene", pkm2, "pokemons")
# print(f"El entrenador {entrenador2} \ntiene {pkm2} pokemons")
# print("El entrenador "+ entrenador2+ " tiene 7 pokemons")

# print(f"Hola {entrenador} "*3)
#    -3-2-1
# name="ANA"
#     012
# print(ent.strip())
# print(ent.lower())
# print(ent2.upper())
# print(ent2.replace("champion", "campeon"))
# print(ent2.find("champion"))
# print(ent2.split())


# passw="SHAZAM"
# clave=input("Porfavor ingrese la clave ")

# if passw==clave.upper():
#     print("Bienvenido al sistema")
# else:
#     print("Clave invalida")


# nombre=input("Porfavor ingrese un nombre de usuario ")

# if len(nombre)<4:
#     print("Muy pocos caracteres use mas de 4")
# elif len(nombre)>10:
#     print("Tiene muchos caracteres use 10 o menos")
# else:
#     print("Ususario creado correctamente")


pin=input("Ingrese un PIN de 4 digitos ")

if len(pin)==4:
    print("PIN ingrdado correctamente")
    pin=int(pin)
else:
    print("PIN no acceptado")
# # Ejercicio 1
# op=0
# puntos=100000
# while op!=3:
#     print("1.- Ver mis puntos")
#     print("2.- Gastar mis puntos")
#     print("3.- Salir")
#     try:
#         op=int(input("Selecciones una opcion: "))
#         match op:
#             case 1:
#                 print(f"le quedan {puntos} puntos")
#             case 2:
#                 if puntos>=10000:
#                     print("1.- Giftcard de $10.000, valor de: 10.000 puntos")
#                     print("2.- Secadora de pelo, valor de: 25.000 puntos")
#                     print("3.- Disco duro portátil, valor de: 30.000 puntos")
#                     try:
#                         continu=int(input("Ingrese lo que quiera canjear: "))
#                         match continu:
#                             case 1:
#                                 print("Perfecto, la giftcard le llegara mañana")
#                                 puntos-=10000
#                             case 2:
#                                 if puntos>=25000:
#                                     print("OK, la secadora le llegara en unos cuantos dias")
#                                     puntos-=25000
#                                 else:
#                                     print("Puntos insuficientes para este productos")
#                             case 3:
#                                 if puntos>=30000:
#                                     print("Nice, el disco duro le llegara en aproximadamente 4 dias")
#                                     puntos-=30000
#                                 else:
#                                     print("no tiene puntos para este producto")
#                             case _:
#                                 print("Opcion invalida")
#                     except:
#                         print("numeros enteros solamente")
#                 else:
#                     print("Puntos insuficientes")
#             case 3:
#                 print("Saliendo el programa.")
#             case _:
#                 print("Opcion invalida")
#     except:
#         print("Numeros enteros solamente")

# # ejercicio 2
op=0
while op!=3:
    print("1.- Ver mi Saldo")
    print("2.- Retirar Dinero")
    print("3.- Salir")
    try:
        op=int(input("Seleccione una opcion: "))
        match op:
            case 1:
                print("Tiene un saldo de 500000")
            case 2:
                print("Retiro exitoso")
            case 3:
                print("Cierre exitoso, que tenga un buen dia.")
            case _:
                print("Opcion invalida")
    except:
        print("Numeros enteros solamente")
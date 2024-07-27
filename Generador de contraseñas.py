import random
cararcteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input("Numero de caracteres en la contraseña:"))

contrasena = ""
for i in range(longitud):
    x = random.choice(cararcteres)
    contrasena += x
print (contrasena)



import random
import time

words = ["a","b","c","d","e","f","g","h","i","j","k","l","n","o","p","q","r","s","t","u","v","w","x","y","z"]
words_mayus = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = ["1","2","3","4","5","6","7","8","9","0"]
symbols = ["+","-","/","*","!","&","$","#","?","=","@"]
caracters = words + words_mayus + numbers + symbols

long_contrasena = int(input("Introduce la longitud de tu contraseña:"))
contrasena = str()

for i in range(long_contrasena):
    number = random.randint(0, len(caracters)-1)
    contrasena = contrasena + caracters[number]

print("Esta es tu contraseña nueva:" + contrasena)

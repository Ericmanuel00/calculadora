import telebot
import os 

API_TOKEN = "token-telegram"

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands-['start'])
def send_welcome(message):
    bot.reply_to(message, "Bienvenido a este bot-calculadora,desarrollado por Eric Manuel")

@bot.message_handler(commands-['menu'])
def send_welcome(message):
    bot.reply_to(message, "Home")



#Contenido 
n1 = float(input("Introduce tu primer número: ") )
n2 = float(input("Introduce tu segundo número: ") )

opcion = 0
while True:
    print("""
    Dime, ¿qué quieres hacer?
    1) Sumar los dos números
    2) Restar los dos números
    3) Multiplicar los dos números
    4) Dividir los números 
    5) Elevar un número
    """)  opcion = int(input("Elige una opción: ") )     
if opcion == 1:
        print(" ")
        print("RESULTADO: La suma de",n1,"+",n2,"es igual a",n1+n2)
elif opcion == 2:
        print(" ")
        print("RESULTADO: La resta de",n1,"-",n2,"es igual a",n1-n2)
elif opcion == 3:
        print(" ")
        print("RESULTADO: El producto de",n1,"*",n2,"es igual a",n1*n2)
 elif opcion == 4:
        print(" ")
        print("RESULTADO: La división de",n1,"/",n2,"es igual a",n1/n2)
 elif opcion == 5:
        print(" ")
        print("RESULTADO: El producto de",n1,"**",n2,"es igual a",n1**n2)
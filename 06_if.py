edad = int(input("Introduce tu edad: "))

if edad < 18:
    print("Eres menor de edad.")
elif 18 <= edad < 65:
    print("Eres adulto.")
else:
    print("Eres adulto mayor.")

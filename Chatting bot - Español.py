import time

def greet(bot_name, birth_year):
    print(f"¡Hola!, Mi nombre es {bot_name}.\nFui creado en el año {birth_year}.")

def remind_name():
    print("Por favor, recuerdame tu nombre.")
    name = input()
    print(f"Que nombre tan genial, {name}!")

def guess_age():
    print("Déjame adivinar tu edad.\nIntroduzca el resto de dividir su edad por 3, 5 y 7.")

    rem3 = int(input("\nResto de edad por 3: "))
    rem5 = int(input("Resto de edad por 5: "))
    rem7 = int(input("Resto de edad por 7: "))
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print(f"\nTu edad es {age}; ¡Esa es una buena edad para empezar a programar!")

def count():
    print("Ahora te demostraré que puedo contar hasta el número que quieras.")

    num = int(input())
    curr = 0
    while curr <= num:
        time.sleep(1)
        print(f"{curr} !")
        curr += 1

def test():
    print(f"Vamos a evaluar tus conocimientos en programación.\n¿Para qué usamos los métodos?")
    print("""1. Para repetir una declaración varias veces.
2. Para descomponer un programa en varios subprocesos pequeños.
3. Para determinar el tiempo de ejecución del programa.
4. Para interrumpir la ejecució de un programa.""")
    answer = 0
    answer = int(input())
    while answer != 2:
      print("Por favor, inténtalo de nuevo.")
      answer = int(input())
    print("Verificando...")
    time.sleep(1)
    print("\n¡Completado, ten un grandioso día!")

def end():
    print(f"¡Felicitaciones!, ten un buen día!")

greet('H3O', '2021')
remind_name()
guess_age()
count()
test()
end()
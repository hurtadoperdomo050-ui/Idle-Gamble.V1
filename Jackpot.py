import random
apostar = 1
apostar == 1
print("--- Kashimo te lastimo de muerte!---")
print("Has Activado Idle Gamble!, piensa rapido!")
tu_movimiento = int(input("Escoge un Numero para obtener el Jackpot! 1/3: "))

Jackpot = random.randint(1, 3)
print(f"El Domain Escogio que es... {Jackpot}")

if tu_movimiento == Jackpot:
   print("Jackpot! Ahora ve y derrota a Kashimo!")

else:
 print("Has perdido...")

Determinacion = int(input(" Rendirse/Seguir 1 o 2: "))
if Determinacion == 2:
 print("La determinacion te mantiene de pie, Expansion de Dominio!")
else:
 print("Destruido pero estas Determinado a Vencer, Expansion de Dominio!")
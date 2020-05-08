import random
import matplotlib.pyplot as plt


print("Kast med en tärning")
antal_kast = input("Antal kast?")

listan = [0, 0, 0, 0, 0, 0]

for x in range(int(antal_kast)):
    resultat = random.randint(1,6)
    listan[resultat-1] += 1

print(listan)

plt.bar([1,2,3,4,5,6],listan)
plt.ylabel('Antal')
plt.xlabel('Utfall')
plt.show()

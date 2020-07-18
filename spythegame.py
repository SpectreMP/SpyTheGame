import random
file = open("locations.txt","r",encoding="utf-8")
locations = file.read().split(",")
location = random.choice(locations)
number = int(input("Напишите количество игроков: "))
for i in range(number):
    playerfile = open("game/player"+str(i+1)+".txt","w",encoding="utf-8")
    playerfile.write(location)
    playerfile.close()
file = open("game/player"+str(random.randint(1,number))+".txt","w",encoding="utf-8")
file.write("Шпион")
file.close()
#Dungeon Spiel Emanuel
import random
eg=("Mmh...","Mhh...","Schmatz...","Mampf...")
lg=("Lecker!","Das war aber gut!")
dungeon="........................w............$...........w............€...........w............€...........w............€...........w............$...........w........................"
hero="@"
herox=0
hero_Gold=0
hero_Wurstsemmel=0
hero_hunger=0
level=list(dungeon)
while hero_hunger<30 and hero_hunger>-1:
    hero_hunger+=random.choice((0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2))
    for x,c in enumerate(level):
        if x==herox:
            print(hero,end="")
        else:
            print (c,end="")
    print()
    command=input("Gold:{} \nWurstsemmeln:{} \nHunger:{}\n?".format(hero_Gold,hero_Wurstsemmel,hero_hunger))
    if command=="a":
        herox-=1
    if command=="d":
        herox+=1
    if command=="e":
        if hero_Wurstsemmel>0:
            hero_hunger-= random.randint(4,20)
            hero_Wurstsemmel-=1
            print(random.choice(eg)+"\n"+random.choice(lg))
        else:
            print("Hilfe!!!\nkein essen mehr!!")
        #Aufheben
    stuff=level[herox]
    if stuff=="€" or stuff=="$":
        hero_Gold+=1
        level[herox]="."
    if stuff=="w":
        hero_Wurstsemmel+=1
        level[herox]="."
        

        

print("Game Over!")
    

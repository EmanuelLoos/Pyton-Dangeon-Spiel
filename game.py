#Dungeon Spiel Emanuel
import random
eg=("Mmh...","Mhh...","Schmatz...","Mampf...")
lg=("Lecker!","Das war aber gut!")
kg=("Du Opfer!","Du Lappen","Du Lauch","Hahaha du schwächling","Du bit richtig sclecht!","Du Hundesohn")
#dungeon="..w..K.w.G...K.w.G..K..w..K..G.w.K.$..K.w.G.K.w.w.K.w.G.K.€.K.G.w.K..wKG.K.G.K.€.G.K.G.K.w.G.K.G.K..€.G.K.G.K.w..K.G.w.K.w.$.w.K.w.G.K.p"
dungeon1="""
############################################################################################################################
#.<################################################################################################.#######.################
##.#########################################################################################################################
##.#########################################################################################################################
##.###.............*..............H...........*......G.....K.................H...............H.H.................###########
##K###.###############H#########################################################################################.###########
##G###..K..###########*HHHH.#####HH#############################################################################.###########
##.#######..##########*####HHH.H.##HH###########################################################################.###########
##.#####...###########K#########################################################################################.###########
##.#####.#############K#########################################################################################k###########
##.#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#########.###########
#->....k.*...#......*..#......*..#........*#..........*#.......*.#.......*.#.........*.#....*#..*#...<B#########*###########
####d#d#s#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#d#########.###########
########p#####k#*#*#K#K#########################################################################################.###########
################K#K#K#K#########################################################################################.###########
################*#K#K#K#########################################################################################.###########
################*#G#K#K############################################################################.#######.####.###########
################H#*#G#K#########################################################################################.###########
################.........*......*........*.....................G.......K.........................................###########
############################################################################################################################
############################################################################################################################
############################################################################################################################
############################################################################################################################
############################################################################################################################
############################################################################################################################
############################################################################################################################
############################################################################################################################
"""
dungeon2="""
############################################################################################################################
#.>HHGGKKKK.................................HHH.........................:..........#.......⬆........#######.....#######....#
#..HHGGKKKK...............................H.....H..................................#................#..#...........#.......#
#HHHHGGKKKK..............................H.......H................................#................#...#...........#.......#
#HHHHGGKKKK..............................H.......H...............................#................#..l.#...........#.......#
#GGKKKK...................................H.....H................................#...............#...w.#...........#.......#
#GGKKKK.....................................HHH..................................#..............#....b.#...........#.......#
#KKKKKK...........................................................................#............#....h..#...........#.......#
#KKKKKK...........................................................................##..........#....r.###...........#.......#
#KKKKKK..........................................................................#..#........#....c.####...........#.......#
#...............................................................................#....#......#....e.###.#...........#.......#
-->.............................................................................#.....#....#....r.###..#...........#.......#
#..............................................................................#.......#..#......###...#...........#.......#
#...............................................................................#.....#..#......###....#...........#.......#
#....................................................##.###.###.####.###.####.####.#####.#####.###.....#HHHHHHHHHHH#.......#
#....................................................#.................................................#HHHHHHHHHHH#.......#
#...................................................#######################################################.....>######....#
#..................................................HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH............#########......#
#HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH########...............#
#K.K.K.K.K.K.K.K.K.K.K.GK.K.K.K.K.K.GK.K.K.K.K.K.K.K.K.K.K.K.K.K.K.K.K.K.K.K.K.K.K.K.K.K.K.K.K.GK.K.K.K.K.K................#
#HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH...............#
#HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH...............#
#HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH...............#
#HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH...............#
#HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH...............#
#..........................................................................................................................#
############################################################################################################################
"""
dungeon3="""
############################################################################################################################
#..........................................................................................#######..#######..#######.......#
#.............................................................................................#........#........#..........#
#.............................................................................................#........#........#..........#
#.............................................................................................#........#........#..........#
#.............................................................................................#........#........#..........#
#.............................................................................................#........#........#..........#
#.............................................................................................#........#........#..........#
#.............................................................................................#........#........#..........#
#.............................................................................................#........#........#..........#
#.............................................................................................#........#........#..........#
--><..........................................................................................#........#........#..........#
#.............................................................................................#........#........#..........#
#.............................................................................................#........#........#..........#
#.............................................................................................#........#........#..........#
#.............................................................................................#........#........#..........#
#..........................................................................................#######..#######..#######.......#
#..........................................................................................................................#
#..........................................................................................................................#
#..........................................................................................................................#
#..........................................................................................................................#
#..........................................................................................................................#
#..........................................................................................................................#
#..........................................................................................................................#
#..........................................................................................................................#
#..........................................................................................................................#
############################################################################################################################
"""
l="""
##########################################################
#........................................................~
#........................................................#
##########################################################
#wwwwwwwww#w#wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww#
#wwwwwwwww###wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww#
#wwwwwwwww#wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww#
#wwwwwwwww#wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww#
###########wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww#
#wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww#
#wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww#
##########################################################
"""
hero="@"
herox=1
heroy=2
heroz=0
hero_Gold=0
hero_Wurstsemmel=50
hero_hunger=0
hero_hp=2500
hero_key=0
hero_special_key=0

#level=list(dungeon)
level=[]
for d in (dungeon1,dungeon2,dungeon3,l):
    l=[]
    for line in d.splitlines():
        l.append(list(line))
    level.append(l)
    
    

while True:
    if hero_hunger>38:
       print("Du bist verhungert!\nVersager")
       break
    if hero_hunger<-1:
       print("Dein Bauch ist geplatzt!\nVersager")
       break
    hero_hunger+=random.choice((0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,2))
    #for x,c in enumerate(level):
    #    if x==herox:
    #        print(hero,end="")
    #    else:
    #        print (c,end="")
    #print()
    for y, line in enumerate(level[heroz]):
        for x,c in enumerate(line):
            if x==herox and y==heroy:
                print(hero,end="")
            else:
                print(c,end="")
        print()
    
    command=input("Gold:{} \nWurstsemmeln:{} \nHunger:{}\nLeben:{}\nKeys:{}\n?".format(hero_Gold,hero_Wurstsemmel,hero_hunger,hero_hp,hero_key))
    
    
    dx=0
    dy=0
    if command=="a":
        #herox-=1
        dx=-1
    if command=="d":
        #herox+=1
        dx=1
        
    if command=="s":
        #heroy-=1
        dy=1
        
    if command=="w":
        #heroy+=1
        dy=-1
    
    if command=="e":
        if hero_Wurstsemmel>0:
            hero_hunger-= random.randint(4,20)
            hero_Wurstsemmel-=1
            print(random.choice(eg)+"\n"+random.choice(lg))
        else:
            print("Hilfe!!!\nkein essen mehr!!")
    if command=="Zaubertrank":
        hero_hp+=100
    if command=="Schlüssel+":
        hero_key+=10
    if command=="Semmel+":
        hero_wurstsemmel+=10
    if command=="fly up":
        if heroz==0:
            print("Du bist schon im obersten Level")
        else:
            heroz-=1
    if command=="fly down":
        if heroz==len(level)-1:
            print("Du bist schon im untersten Level")
        else:
            heroz+=1
    
    # ---in Wand gelaufen---
    target=level[heroz][heroy+dy][herox+dx]
    if target=="#":
        dx=0
        dy=0
        print("Autch ich bin in eine Mauer gelaufen!\nIch werde von einem Trottel kontrolliert!!")
    #In Teleporter gelaufen---
    elif target=="*":
        #try to find legal field
        for v in range(100):
            tx=random.randint(-5,5)+herox
            ty=random.randint(-4,4)+heroy
            
            if level[heroz][ty][tx]=="." or level[heroz][ty][tx]=="*":
                herox=tx
                dx=0
                heroy=ty
                dy=0
                break
        else:
            dx=0
            dy=0
        #print("Der teleporter katapultiert dich woanders hin!")
        #dx=random.randint(-5,5)
        #dy=random.randint(-5,5)
    # ---- Ausgang anfang ----
    elif target=="~":
        heroz==1
        heroy==2
        herox==102
    # ---- in türe gelaufen ? -----
    # ---- Lebensmittelgeschäft anfang ----
    elif target=="l":
        heroz==3
        heroy==1
        herox==1
    # ---- Lebensmittelgeschäft Ende ----
    elif target=="d":
        if hero_key>0:
            hero_key-=1
            level[heroz][heroy+dy][herox+dx]="H"
        else:
            dx=0
            dy=0
            print("Hife!\nIch bin gegen eine geslossene Tür ohne Schlüssel gelaufen!\nIch werde von einem Trottel kontrolliert!!")
          
    #----In Spezialtüre gelaufen?----
    elif target=="s":
        if hero_special_key>0:
            hero_special_key-=1
            level[heroz][heroy+dy][herox+dx]="H"
        else:
            dx=0
            dy=0
            print("Hife!\nIch bin gegen eine geslossene Tür ohne Schlüssel gelaufen!\nIch werde von einem Trottel kontrolliert!!")
          
    # in Monster gelaufen?
    #target=level[herox+dx]
    #---Gorilla anfang---
    if target=="G":
        print("Ein Gorilla blockiert deinen Weg!")    
        print("Der Gorilla schlägt dich mit einer Banane!")
        schaden=random.randint(1,10)
        hero_hp-=schaden
        print("Du erleidest {} Schaden".format(schaden))
        if hero_hp<1:
             print:("Du stirbst!\nVersager!")
             break
        sieg=0.333333
        if random.random() < sieg:
            level[heroz][heroy+dy][herox+dx]="."
            print("Du erledigst heldenhaft den Gorilla!!")
        else:
            print("Du Verlierst!")
            dx=0
            dy=0
    # -------- gorilla ende ---------
    #---Boss anfang---
    if target=="B":
        print("Der Boss hat die Prinnzessin enntführt!")    
        print("Der Boss kämpft proffessionell!")
        schaden=random.randint(100,1500)
        hero_hp-=schaden
        print("Du erleidest {} Schaden".format(schaden))
        if hero_hp<1:
             print:("Du stirbst!\nVersager!")
             break
        sieg=0.1
        if random.random() < sieg:
            level[heroz][heroy+dy][herox+dx]="H"
            print("Du erledigst heldenhaft den Boss!!")
            hero_special_key+=1
        else:
            print("Du Verlierst!")
            dx=0
            dy=0
     #---kobold anfang---
    if target=="K":
        print("Ein Kobold blockiert deinen Weg!")    
        print("Der Kobold piekst dich mit einer Gabel!")
        schaden=random.randint(10,20)
        hero_hp-=schaden
        print("Du erleidest {} Schaden".format(schaden))
        if hero_hp<1:
             print:("Du stirbst!\nVersager!")
             break
        sieg=0.7
        if random.random() < sieg:
            print("Du erledigst heldenhaft den Kobold!!")
            level[heroz][heroy+dy][herox+dx]="."
        else:
            print("Du Verlierst!")
            dx=0
            dy=0
    # -------- kobold ende ---------
    # -------- Hexe Anfang ---------
    if target=="H":
        print("Eine Hexe blockiert deinen Weg!")    
        print("Die Hexe verletzt dich mit einem Zauberball!")
        schaden=random.randint(100,300)
        hero_hp-=schaden
        print("Du erleidest {} Schaden".format(schaden))
        if hero_hp<1:
             print:("Du stirbst!\nVersager!")
             break
        sieg=0.2
        if random.random() < sieg:
            level[heroz][heroy+dy][herox+dx]="."
            print("Du erledigst heldenhaft die Hexe!!")
        else:
            print("Du Verlierst!")
            dx=0
            dy=0
    herox+=dx
    heroy+=dy
    #--------Hexe Ende-------
    #Aufheben
    stuff=level[heroz][heroy][herox]
    if stuff=="€" or stuff=="$":
        hero_Gold+=1
        level[heroz][heroy][herox]="H"
    if stuff=="w":
        hero_Wurstsemmel+=1
        level[heroz][heroy][herox]="H"
    if stuff=="p":
        print("Du hast die Prinzessin befreit!")
        level[heroz][heroy][herox]="p"
        break
    if stuff=="<":
       command2=input("Du bist auf einer Treppe gelandet.\nWillst du ein Stockwerk tiefer gehen?")
       if command2=="y":
           heroz+=1
       else:
           print("Ok, dann eben nicht.")
    if stuff==">":
       command3=input("Du bist auf einer Treppe gelandet.\nWillst du ein Stockwerk höher gehen?")
       if command3=="y":
           heroz-=1
       else:
           print("Ok, dann eben nicht.")
    if stuff=="k":
        hero_key+=1
        level[heroz][heroy][herox]="H"

print("Ende")
    

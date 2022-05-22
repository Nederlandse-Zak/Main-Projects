#Script verder afmaken
#optie in menu toevoegen: naar huis lopen!
#als water, food < 0, dan stopt het spel


# import only system from os
from os import system, name
  
# import sleep to show output for some time period
from time import sleep
  


# define our clear function
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
  
# now call function we defined above
clear()
















from re import A
import time
import random


print()
print()
print("welkom bij text-adventure")
print()
print("Made by Kyan")
print("het doel van deze game is om veilig thuis te komen, zonder uit te hongeren of uit te drogen")
print()
print("door 1,2,3,4 in te tikken, kun je verschillende menu's openen")
print("LET OP: wanneer je een verkeerde waarde intoetst, kan het programma crashen.")
print("je moet het programma dan opnieuw laden en afspelen")
print()

time.sleep(0)

water = 100
food = 100
health = 100

steak = 0
hamlapje = 0
vis = 0

leegflesje = 0
volflesje = 2
viesflesje = 1
lucifers = 3
ehbokit = 1
energyreep = 1


afstand = 1000
var = random.randint(1,2)
while True:
    eetwaren = steak+hamlapje+vis
    print("MENU'S:")
    print("1: jagen")
    print("2: inventory")
    print("3: drink")
    print("4: eet")
    print("5: gebruik lucifers om water te zuiveren","   " "(je hebt nog", lucifers, "lucifers)")
    print("6: naar huis lopen")
    print("7: gebruik ander item")
    print("8: status")
    
    if var == 1:
        print("9: waterflesje vullen bij sloot")
    
    print()
    if var ==1:
        ans = int(input("kies 1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 of 9   "))
    else:
        ans = int(input("kies 1, 2, 3, 4, 5 ,6 ,7 of 8  "))
    
    clear()
    if ans == 1: 
        food = food-random.randint(5,10)
        time.sleep(0.001)
        var = random.randint(1,5)
        if var == 1:
            steak = steak+1
            print("je hebt een koe gevangen!   steak+1")
        if var == 2:
            hamlapje = hamlapje+1
            print("je hebt een varken gevangen!   hamlapje+1")
        if var == 3:
            vis = vis+1
            print("je hebt een vis gevangen!   vis+1")
        if var == 4:
            var = random.randint(15, 25)
            health = health - var
            print("je bent aangevallen!    health-", var)
        if var == 5:
            var = random.randint(1,3)
            if var ==1:
                print("helaas, je hebt niks gevangen")
            elif var ==2:
                print("het zit niet mee, je hebt niks gevangen")
            elif var ==3:
                print("hmmm, je hebt niks gezien")
        print("steak: ", steak)
        print("hamlapje: ", hamlapje)
        print("vis: ", vis)
        print("eten: ", food)
        print("water: ", water)
        print("gezondheid: ", health)
        print()
        
        var = random.randint(1,2)
    


    if ans == 2:
        print("Inventaris:")
        print("Steak:  ", steak)
        print("hamlapje:  ", hamlapje)
        print("vis:   ", vis)
        print("lege flesjes:   ", leegflesje)
        print("vol flesje water:   ", volflesje)
        print("vies flesje water:   ", viesflesje)
        print("lucifers:   ", lucifers)
        print("EHBO-Kit", ehbokit)
        print("energyreep:  ", energyreep)
        time.sleep(2)
        
    
    if ans == 3:
        if volflesje>0:
            water = water+20
            volflesje = volflesje-1
            leegflesje = leegflesje+1
            print("je hebt een flesje water opgedronken!")
        elif viesflesje>0:
            print("je hebt op dit moment geen drinkwater")
            print("je kunt wel een lucifer gebruiken om vies water te zuiveren")
            print("wil je dit?       ja/nee")
            ans = input()
            if ans == "ja":
                lucifers = lucifers-1
                volflesje = volflesje+1
                viesflesje = viesflesje-1
                print("je hebt 1 lucifer gebruikt om 1 flesje water te zuiveren")
                print("wil je deze meteen opdrinken?   ja/nee")
                ans = input()
                if ans == "ja":
                    water = water+20
                    volflesje = volflesje-1
                    leegflesje = leegflesje+1
        else:
            print("je hebt geen flesjes water meer!")
        print("vol flesje: ", volflesje)
        print("vies flesje: ", viesflesje)
        print("leeg flesje: ", leegflesje)
        
        
    if ans == 4:
        if eetwaren>0:
            print("je hebt", steak, "steaks,", hamlapje, "hamlapjes en", vis, "vissen")
            print("wat wil je opeten?")    
            print("1=steak")
            print("2=hamlapje")
            print("3=vis")
            ans =int(input())
            if ans == 1:
                if steak>0:
                    steak = steak-1
                    food = food+random.randint(25,35)
                    print("je hebt een steak opgegeten")
                else:
                    print("je hebt geen steak meer")
            if ans == 2:
                if hamlapje>0:
                    hamlapje = hamlapje-1
                    food = food+random.randint(15,25)
                    print("je hebt een hamlapje opgegeten")
                else:
                    print("je hebt geen hamlapjes meer")
            if ans == 3:
                if vis>0:
                    vis = vis-1
                    food = food+random.randint(15,20)
                    print("je hebt een vis opgegeten")
                else:
                    print("je hebt geen vissen meer")
        else:
            print("je hebt niks meer om op te eten!")
        print("eten: ", food)
        print("water: ", water)
        print("gezondheid: ", health)
        


    if ans == 5:
        if lucifers>0:
            if viesflesje>0:
                lucifers = lucifers-1
                volflesje = volflesje+1
                viesflesje = viesflesje-1
                print("je hebt een lucifer gebruikt om een flesje water te zuiveren")
            else:
                print("je hebt op dit moment geen ongezuiverde flesjes water")
        else:
            print("je hebt geen lucifers meer")
        
    
    if ans == 6:
        var = int(random.randint(20,60))
        afstand = afstand-var
        food = food-(random.randint(2, 3)*(0.2*var))
        water = water - (random.randint(1, 2)*(0.4*var))
        print("je bent", var, "meter naar huis gelopen" )
        print()
        print("eten: ", food)
        print("water: ", water)
        print("gezondheid: ", health)
        var = random.randint(1,2)

    if ans == 7:
        print("Andere items:")
        print("energyreep: ", energyreep)
        print("EHBO-kit:   ", ehbokit)
        print()
        print()
        print("welk item wil je gebruiken?    1=energyreep   2=EHBO-kit   3=terug")
        var = int(input())
        if var == 1:
            if energyreep>0:
                food = food + 50
                energyreep = energyreep-1
                print("je hebt een energyreep opgegeten")
            else:
                print("je hebt geen energyreep meer")
        elif var == 2:
            if ehbokit>0:
                ehbokit=ehbokit-1
                health = health+60
                print("je hebt een EHBO-kit gebruikt", "   health= ", health)
            else:
                print("je hebt geen EHBO-kit meer")
        print("eten: ", food)
        print("water: ", water)
        print("gezondheid: ", health)
        
    
    if ans == 9:
        if var ==1:
            if leegflesje>0:
                var = leegflesje
                leegflesje=leegflesje-var
                viesflesje=viesflesje+var
                print("flesjes gevuld")
            else:
                print("je hebt geen lege flesjes meer")
        if var == 2:
            print("er is geen sloot in de buurt, loop verder om een sloot tegen te komen!")
        var = random.randint(1,2)

    if ans == 8:
        print("health: ", health)
        print("water: ", water)
        print("food: ", food)
        print("afstand tot huis: ", afstand)
        

    
        


    if health<0:
        cause = "h"
        break
    if food<0:
        cause = "f"
        break
    if water<0:
        cause = "w"
        break
    if afstand<0:
        cause = "a"
        break
    
    print()
    print()
    time.sleep(1)

if cause == "h":
    print("je bent doodgegaan aan je verwondingen")
if cause == "f":
    print("je bent doodgegaan van de honger")
if cause == "w":
    print("je bent doodgegaan van de dorst")
if not cause == "a":
    print("je afstand tot huis was", afstand)
if cause == "a":
    print("je hebt gewonnen!")

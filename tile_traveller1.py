# Notandi ert staðsettur á reit 1,1 á x og y ás. 
# Notandi velur átt af þeim áttum sem hann á möguleika á því að fara í 
# reitirnir eru 3x3 og eftirfarandi er ekki hægt
# þegar x er 1 þá er ekki hægt að fara til vinstri
# þegar x er 3 þá er ekki hægt að fara til hægri
# þegar y er 1 er ekki hægt að fara niður 
# Þegar y er 3 þá er ekki hægt að fara upp
# ef x = 1 og y er 1 þá er einungis hægt að fara upp
# ef x = 2 og y = 1  þá er einungis hægt að fara upp
# ef x= 3 og y =1 þá er einungis hægt að fara upp
# ef x=2 og y = 2 þá er ekki hægt að fara til hægri eða upp
# ef x= 3, og y = 2 þá er einungis hægt að fara niður og upp.  
# ef notandi nær gildinu x= 3 og y = 1 þá er hann búinn að vinna leikinn

x,y = 1,1
victory = False
options = "N"

print("You can travel: (N)orth.")
while victory == False:
    chose = input("Direction: ")
    chose = chose.upper()

    if chose in options:
    
        if chose == "E":
            x += 1
        elif chose == "S":
            y -= 1
        elif chose == "W":
            x -= 1
        elif chose == "N":
            y += 1
    else:
        print("Not a valid direction!")

    if x == 3 and y == 1:
            victory = True
            print("Victory!")
            break
    else:
           
        if x == 1 and y == 1:
            options = "N"
            string = "(N)orth."
        elif x == 1 and y == 2:
            options = "NES"
            string= "(N)orth or (E)ast or (S)outh."
        elif x == 1 and y == 3:
            options = "ES"
            string = "(E)ast or (S)outh."
        elif x == 2 and y == 1:
            options = "N"
            string = "(N)orth."
        elif x == 2 and y == 2:
            options = "SW"
            string = "(S)outh or (W)est."
        elif x == 2 and y == 3:
            options = "EW"
            string = "(E)ast or (W)est."
        elif x == 3 and y == 2:
            options = "NS"
            string = "(N)orth or (S)outh."
        elif x == 3 and y == 3:
            options = "SW"
            string = "(S)outh or (W)est."
        print("You can travel:", string)
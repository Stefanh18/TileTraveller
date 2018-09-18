# Notandi ert staðsettur á reit 1,1 á x og y ás.
# Notandi velur átt af þeim áttum sem hann á möguleika á því að fara í. Ef valið er átt sem er ekki til kemur invalid input
# reitirnir eru 3x3 og eftirfarandi er ekki hægt
# þegar x er 1 þá er ekki hægt að fara til vinstri
# þegar x er 3 þá er ekki hægt að fara til hægri
# þegar y er 1 er ekki hægt að fara niður 
# þegar y er 3 þá er ekki hægt að fara upp
# ef x = 1 og y er 1 þá er einungis hægt að fara upp
# ef x = 2 og y = 1  þá er einungis hægt að fara upp
# ef x=2 og y = 2 þá er hægt að fara til vinstir eða niður
# ef x= 3, og y = 2 þá er einungis hægt að fara niður og upp.  
# ef notandi nær gildinu x= 3 og y = 1 þá er hann búinn að vinna leikinn

def move(user_input):
    if user_input == "n" or user_input == "e":
        movement = 1
    elif user_input == "s" or user_input == "w":
        movement -= 1'
    
    return movement


def insturctions(x, y):
    if X == 1 and y == 1:
        direction = "(N)orth"
    elif x == 1 and y == 2:
        direction = "(N)orth or (E)ast or (S)outh"
    elif x == 1 and y == 3:
        direction = "(E)ast or (S)outh"
    elif X == 2 and y == 1:
        direction = "(N)orth"
    elif x == 2 and y == 2:
        direction = "(W)est or (S)outh"
    elif X == 2 and y == 3:
        direction = "(W)est or (E)ast"
    elif x == 3 and y == 3:
        direction = "(W)est or (S)outh"
    elif x == 3 and y == 2:
        direction = "(N)orth or (S)outh"

    return direction


x = 1
y = 1
while (x != 3 and y != 1) or (x < 4 and y < 4):





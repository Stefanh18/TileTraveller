#1. Which implementation was easier and why?
# Erfitt að segja en líklegast seinni kóðinn það er bæði auðveldara að lesa hann og meiri möguleikar í að bæta kóðann.
#2. Which implementation is more readable and why?
# Seinni með functions vegna þess að þú lest kóðann sem þú þarft að skilja en það sem er inn í function er einnig skipt niður í verkefni og því auðveldara að skilja.
#3. Which problems in the first implementations were you able to solve with the latter
#   implementation?
# not many 

def chose_ESWN():
    """Spyr um átt ESNW og skilar út áttinni með stórum staf"""
    chose = input("Direction: ")
    chose = chose.upper()

    return chose
def direction_pos(x,y):   
            if x == 1 and y == 1:
                options = "N"
                str_1 = "(N)orth."
            elif x == 1 and y == 2:
                options = "NES"
                str_1= "(N)orth or (E)ast or (S)outh."
            elif x == 1 and y == 3:
                options = "ES"
                str_1 = "(E)ast or (S)outh."
            elif x == 2 and y == 1:
                options = "N"
                str_1 = "(N)orth."
            elif x == 2 and y == 2:
                options = "SW"
                str_1 = "(S)outh or (W)est."
            elif x == 2 and y == 3:
                options = "EW"
                str_1 = "(E)ast or (W)est."
            elif x == 3 and y == 2:
                options = "NS"
                str_1 = "(N)orth or (S)outh."
            elif x == 3 and y == 3:
                options = "SW"
                str_1 = "(S)outh or (W)est."
            print("You can travel:", str_1)
            return options,str_1

def move(chose,x,y):
        if chose == "E":
            x +=1
        elif chose == "S":
            y -=1
        elif chose == "W":
            x -=1
        elif chose == "N":
            y +=1
        return x, y
   
x,y = 1,1
victory_boolean = False
options= "N"

print("You can travel: (N)orth.")
while victory_boolean == False:
    chose = chose_ESWN()
    if chose in options:
       x, y = move(chose,x,y) 
    else:
        print("Not a valid direction!")
        continue

    if x == 3 and y == 1:
            victory = True
            print("Victory!")
            break
    else:
        options,str_1 = direction_pos(x,y)
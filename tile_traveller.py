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
def possible_directions(location_x,location_y):   
            if location_x == 1 and location_y == 1:
                options = "N"
                string = "(N)orth."
            elif location_x == 1 and location_y == 2:
                options = "NES"
                string= "(N)orth or (E)ast or (S)outh."
            elif location_x == 1 and location_y == 3:
                options = "ES"
                string = "(E)ast or (S)outh."
            elif location_x == 2 and location_y == 1:
                options = "N"
                string = "(N)orth."
            elif location_x == 2 and location_y == 2:
                options = "SW"
                string = "(S)outh or (W)est."
            elif location_x == 2 and location_y == 3:
                options = "EW"
                string = "(E)ast or (W)est."
            elif location_x == 3 and location_y == 2:
                options = "NS"
                string = "(N)orth or (S)outh."
            elif location_x == 3 and location_y == 3:
                options = "SW"
                string = "(S)outh or (W)est."
            print("You can travel:", string)
            return options,string

def move(chose,location_x,location_y):
        if chose == "E":
            location_x +=1
        elif chose == "S":
            location_y -=1
        elif chose == "W":
            location_x -=1
        elif chose == "N":
            location_y +=1
        return location_x, location_y
   
location_x,location_y = 1,1
victory_boolean = False
options= "N"

print("You can travel: (N)orth.")
while victory_boolean == False:
    chose = chose_ESWN()
    if chose in options:
       location_x, location_y = move(chose,location_x,location_y) 
    else:
        print("Not a valid direction!")
        continue

    if location_x == 3 and location_y == 1:
            victory = True
            print("Victory!")
            break
    else:
        options,string = possible_directions(location_x,location_y)
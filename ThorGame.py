
#POWEROFTHOR
#In this puzzle, you need to compare different values. 
#The aim is to build a program able to allow Thor to reach the light of power

#Thor moves on a map which is 40 wide by 18 high. Note that the coordinates (X and Y) start at the top left! 
##This means the most top left cell has the coordinates "X=0,Y=0" and the most bottom right one has the coordinates "X=39,Y=17".
#Once the program starts you are given:
#the variable lightX: the X position of the light of power that Thor must reach.
#the variable lightY: the Y position of the light of power that Thor must reach.
#the variable initialTX: the starting X position of Thor.
#the variable initialTY: the starting Y position of Thor.
#At the end of the game turn, you must output the direction in which you want Thor to go among:
N (North)
NE (North-East)
E (East)
SE (South-East)
S (South)
SW (South-West)
W (West)
NW (North-West)



#Initial variables
light_x,light_y, InitialTx, InitialTy =[int(i) for i in input().split()]
thor_x, thor_y = Initial_tx, Initial_ty

# game loop
while 1:
    remaining_turns = int(input())
    
    direction_x = ""
    direction_y = ""
    
    if thor_x > light_x:
        direction_x = "W"
        thor_x -= 1
    elif thor_x < light_x:
        direction_x = "E"
        thor_x += 1
        
    if thor_y > light_y:
        direction_y = "N"
        thor_y -= 1
    elif thor_y < light_y:
        direction_y = "S"
        thor_y += 1
    
    # A single line providing the move to be made either: N NE E SE S SW W or NW
    print(direction_y + direction_x)

##Problem solved

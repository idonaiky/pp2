def solve(numheads,numlegs):
   rabbits = numlegs // 4
   chicken = numheads - rabbits
   print ("Rabbits: " + str(rabbits) + " Chicken: " + str(chicken))
 solve(int(input()),int(input()))
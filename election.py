from random import randint
wins = 0

for i in range(10000): #repeat the process a thousand times
  regions=0
  if randint(1,100) <= 87:#region 1
    regions = regions + 1 #add to the amount of wins
   if randint(1,100) <= 65:#region 2
    regions = regions + 1 #add to the amount of wins
   if randint(1,100) <= 17:#region 3
    regions = regions + 1 #add to the amount of wins
  if regions >= 2:
    wins = wins + 1

percent = (wins/float(10000)) *100
print "You won the election %s percent of the time" %(percent)

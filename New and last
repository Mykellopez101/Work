from gopigo import *
import time

 def turn_right(): 
   enc_tgt(1,0,15) 
   time.sleep(.1) 
   right() 
   time.sleep(2) 
 
 def turn_left(): 
   enc_tgt(0,1,15) 
   time.sleep(.1) 
   left() 
   time.sleep(2) 

while 1<2:
  while us_dist(15)>20:
    fwd()
  stop()
  servo(0)
  left= us_dist(15)
  servo(180)
  right= us_dist(15)
  if left < right 
    servo(180)
  else 
     servo(0)

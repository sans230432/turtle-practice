import turtle

turtle.shape("turtle")



whileLoop = True
while(whileLoop == True):
 userInput = int(input("how many sides do you want?: "))
 if(userInput >= 3 and userInput <= 10):
   whileLoop = false
  else:
    print("Error not right")




for i in range(userInput):
  turtle.forward(100)
  turtle.right(360/userInput)

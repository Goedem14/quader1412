import turtle
t = turtle.Turtle()



#Draw stairs 

def stairs (pixel,nb):
    t.fd(pixel)
  
    for i in range (0, nb):
        t.lt(90)
        t.fd(pixel)
        t.rt(90)
        t.fd(pixel)

# Draws square
def square (pixel):
    for i in range (0,4):
        t.fd(pixel)
        t.lt(90)
        
        


#eingabe_pixel = int(input("Wieviel Pixel sollen die Stufen haben: "))
#eingabe_stufen = int(input("Wieviel Stufen, wollen Sie zeichnen:"))

#stairs(eingabe_pixel,eingabe_stufen)


size = 100
for i in range (0,4):
    square(size)
    size -=20



turtle.done()

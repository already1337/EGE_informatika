import turtle
import turtle as t
k = 30 # масштаб
t.left( 90 ) # развернуть Черепаху "на север"
for i in range(7):
    t.forward( 10*k )
    t.right( 120 )
t.up()
for x in range(0, 11):
    for y in range(0, 11):
        t.goto( x*k, y*k )
        t.dot( 4 )

turtle.exitonclick()

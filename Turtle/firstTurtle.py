from tracemalloc import start
from turtle import *

color("red", "yellow")
begin_fill()
bgcolor("black")

while True:
    forward(500)
    left(150)
    if abs(pos()) < 1:
        break

# left(90)
# forward(100)

# left(-160)
# forward(100)

# right(-160)
# forward(100)

# left(-160)
# forward(100)

end_fill()
done()

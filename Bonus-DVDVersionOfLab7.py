from gfxhat import lcd
from gfxhat import backlight
from FunctionLibrary import displayObject
from FunctionLibrary import deleteObject
from FunctionLibrary import moveObject
from FunctionLibrary import checkCollision

backlight.set_all(190,190,190)
backlight.show()
lcd.clear()
lcd.show()

dvd =  [
[1,1,1,1,1,1,1,0,1,1,1,1,1,0,0],
[0,0,0,1,0,1,1,0,1,1,0,0,0,1,0],
[1,0,0,0,1,0,1,0,1,0,1,0,0,0,1],
[1,0,0,1,0,0,1,0,1,0,1,0,0,1,0],
[1,1,1,0,0,0,0,1,0,0,1,1,1,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,1,1,1,1,1,1,1,1,1,1,1,0,0],
[1,1,1,1,1,1,0,0,0,1,1,1,1,1,1],
[1,1,1,1,1,0,0,0,0,0,1,1,1,1,1],
[1,1,1,1,1,1,0,0,0,1,1,1,1,1,1],
[0,0,1,1,1,1,1,1,1,1,1,1,1,0,0]
]


print("Look at the GFX Hat and you will see a ball bouncing around the screen.")
print("Press Ctrl C to stop the program.")

xValue = 0
yValue = 0
xSpeed = 1
ySpeed = 1

while True:
    deleteObject(dvd, x=xValue, y=yValue)

    moveReturn = moveObject(dvd, x=xValue, y=yValue, vx=xSpeed, vy=ySpeed)
    xValue = moveReturn[0]
    yValue = moveReturn[1]

    newSpeeds = checkCollision(dvd, x=xValue, y=yValue, vx=xSpeed, vy=ySpeed)
    xSpeed = newSpeeds[0]
    ySpeed = newSpeeds[1]

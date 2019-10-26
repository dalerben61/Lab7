from gfxhat import lcd

lcd.clear()
lcd.show()

ball =  [
[0,0,0,1,1,0,0,0],
[0,0,1,1,1,1,0,0],
[0,1,1,1,1,1,1,0],
[1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,0],
[0,0,1,1,1,1,0,0],
[0,0,0,1,1,0,0,0]
]

def deleteObject(obj, x=0, y=0):
    positionx = x
    positiony = y
    for i in obj:
        for j in i:
            if j == 1:
                lcd.set_pixel(positionx, positiony, 0)
            positionx += 1
        positiony+=1
        positionx = x

def moveObject(obj, x=0, y=0, vx=0, vy=0):
    x = x + vx
    y = y + vy
    return x
    return y

def checkCollision(obj, x=0, y=0, vx=0, vy=0, Sx=128, Sy=64):
    positionx = x
    positiony = y

    if vx < 0:
        Sx = 0-1
    if vy < 0:
        Sy = 0-1

    for i in obj:
        if positiony == Sy:
            vy = 0 - vy
            y = y + vy
            break
        #only serves as a check if vertical speed is negative

        for j in i:
            if positionx == Sx:
                break
            #serves as a check if horizontal speed is negative

            positionx += 1
            if positionx == Sx:
                break
            #only breaks from the inside for loop, positive horizontal speed check

        positiony+=1
        if positionx == Sx:
            vx = 0 - vx
            x = x + vx
            break
        #sets the new horizontal speed and x position if needed

        if positiony == Sy:
            vy = 0 - vy
            y = y + vy
            break
        positionx = x
        #sets the new vertical speed and y position if needed
    
    return x
    return y
    return vx
    return vy

def displayObject(obj, x, y):
    positionx = x
    positiony = y
    for i in obj:
        for j in i:
            if j == 1:
                lcd.set_pixel(positionx, positiony, 1)
            positionx += 1
        positiony+=1
        positionx = x
    lcd.show()

displayObject(ball, 0, 0)


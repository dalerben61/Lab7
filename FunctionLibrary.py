from gfxhat import lcd

def displayObject(obj, x, y):
    positionx = x
    positiony = y
    for i in obj:
        for j in i:
            if j == 1:
                lcd.set_pixel(positionx, positiony, 1)
            positionx += 1
        positiony += 1
        positionx = x
    lcd.show()

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
    lcd.show()

def moveObject(obj, x=0, y=0, vx=0, vy=0):
    x = x + vx
    y = y + vy    
    positionx = x
    positiony = y
    displayObject(obj, positionx, positiony)
    return x, y

def checkCollision(obj, x=0, y=0, vx=0, vy=0, Sx=128, Sy=64):
    nextPositionx = x + vx
    nextPositiony = y + vy
    nextPositionEndx = x + vx + len(obj[0])
    nextPositionEndy = y + vy + len(obj)
    limitx = Sx
    limity = Sy

    if nextPositionEndx == limitx:
        vx = vx * -1
    elif nextPositionx < 0:
        vx = vx * -1
    
    if nextPositionEndy == limity:
        vy = vy * -1
    elif nextPositiony < 0: 
        vy = vy * -1

    return vx, vy
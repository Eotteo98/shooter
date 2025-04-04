import pgzrun
WIDTH = 800
HEIGHT = 600

shooter = Actor("space_ship.png")
shooter.pos = (WIDTH/2, HEIGHT -60)
bug = Actor("bug.png")
speed = 10
bullets = []
bugs = []

for x in range(8):
    for y in range(4):
        bugs.append(Actor("bug.png"))
        bugs[-1].x = 100 + 50 * x
        bugs[-1].y = 80 + 50 * y

score = 0
direction = 1
shooter.dead = False
shooter.countdown = 90

def display_score():
    screen.draw.text("Your score is   " + str(score),(70, 50))

def game_over():
    screen.draw.text("Game Over", (400, 300))

def on_key_down(key):
    if shooter.dead == False:
        if key == keys.SPACE:
            bullets.append(Actor("bullet.png"))
            bullets[-1].x = shooter.x
            bullets [-1].y = shooter.y -50
        

def update():
    global score, direction
    move_down = False
    #ship_movement
    if shooter.dead == False:
        if keyboard.left:
            shooter.x -= speed 
            if shooter.x <= 0:
                shooter.x = 0
        elif keyboard.right:
            shooter.x += speed 
            if shooter.x >= WIDTH:
                shooter.x = WIDTH
    
    for bullet in bullets:
        if bullet.y <= 0:
            bullets.remove(bullet)
        else:
            bullet.y -= 10
    
    if len(bugs) == 0:
        game_over()
    
    if len(bugs) >0 and (bugs[-1].x > WIDTH - 60 or bugs [0].x < 60):
        move_down = True
        direction = direction * -1
    
    for bug in bugs:
        bug.x += 5 * direction
        if move_down == True:
            bug.y += 80

        if bug.y > HEIGHT:
            bugs.remove(bug)
        
        for bullet in bullets:
            if bug.colliderect(bullet):
                score += 100
                bullets.remove(bullet)
                bugs.remove(bug)
                if len(bugs) == 0:
                    game_over()
        
        if bug.colliderect(shooter):
            shooter.dead = True
    if shooter.dead:
        shooter.countdown -= 1
    if shooter.countdown == 0:
        shooter.dead = False
        shooter.countdown = 60

def draw():
    screen.clear()
    screen.blit("space", (0,0))
    for bullet in bullets:
        bullet.draw()
    for bug in bugs:
        bug.draw()
    if shooter.dead == False:
        shooter.draw()
    display_score()

    if len(bugs) == 0:
        game_over()

pgzrun.go()

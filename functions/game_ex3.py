import pgzrun 
from random import randint

HEIGHT = 600
WIDTH = 1200

p = Actor('ironman',center=(WIDTH//2,HEIGHT//2))
c = Actor('cookie_img',(randint(0,WIDTH),randint(0,HEIGHT)))

title = "IRON-MAN GAME"
score = 0
#musics.play('bg')
music.play('bgm')

def draw():
    screen.fill('white')
    screen.draw.text(title, center=(WIDTH//2,30), fontsize =60,color ='yellow', 
                     align='center',shadow=(.2,1),scolor="black")
    screen.draw.text(f'score: {score}',(10,10),fontsize=10, color ='black')
    p.draw()
    c.draw()
    
def p_move():
    
    if keyboard.right and p.right < WIDTH:
        p.x += 3
        p.angle = -10
    elif keyboard.left and p.left > 0:
        p.x -=3
        p.angle = 10
    else:
        p.angle = 0
    if keyboard.up and p.top >0:
        p.y -=3
    if keyboard.down and p.bottom < HEIGHT:
        p.y +=3
    
        

def update():
    global score # tells python, that we want to change the value of global variable score
    p_move() # function calle when player
    #handle_boundary()# function call
    if p.colliderect(c):
        score +=1
        c.pos = (randint(0, WIDTH),randint(0,HEIGHT))
    
    print(p.x, p.y, p.angle)
pgzrun.go()

# v1 : pareil mais au moins on peut sortir du programme
# avec la touche 'q', ou avec la souris en fermant la fenêtre

from random import randint
import pygame as pg

dirin = (1, 0)
direction = (1, 0)
width = 20 # largeur du rectangle en pixels
height = 20 # hauteur du rectangle en pixels
pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()

white = (255, 255, 255)
autre = (245, 200, 200)
black = (0, 0, 0)
rouge = (230, 100, 100)
snake = [
    (10, 15),
    (11, 15),
    (12, 15),
]   
fruit = (randint(0, 30), randint(0, 30))
def somme(u, v):
    return (u[0] + v[0], u[1] + v[1])

def chgt_direction(snake, direction, dirin):
    if somme(direction, dirin) != (0, 0):
        if direction == (1, 0):
            snake[0:-1]=snake[1:]
            snake[-1]=(snake[-1][0] + 1, snake[-1][1])

        elif direction == (-1, 0):
            snake[0:-1]=snake[1:]
            snake[-1]=(snake[-1][0] - 1, snake[-1][1])

        elif direction == (0, 1):
            snake[0:-1]=snake[1:]
            snake[-1]=(snake[-1][0], snake[-1][1] + 1)

        elif direction == (0, -1):
            snake[0:-1]=snake[1:]
            snake[-1]=(snake[-1][0], snake[-1][1] - 1)
    else:
        direction = dirin
        chgt_direction(snake, direction, direction)
    return direction


def draw_snake(snake):
    for line, col in snake:
            rect = pg.Rect(line*20, col*20, width, height)
            pg.draw.rect(screen, black, rect)


# on rajoute une condition à la boucle: si on la passe à False le programme s'arrête
running = True

while running:
    for i in range(30):
        for j in range(30):
            # les coordonnées de rectangle que l'on dessine
            x = i*20 # coordonnée x (colonnes) en pixels
            y = j*20 # coordonnée y (lignes) en pixels
            rect = pg.Rect(x, y, width, height)
            # appel à la méthode draw.rect()
            if (i+j)%2 == 0:
                pg.draw.rect(screen, autre, rect)
            else:
                pg.draw.rect(screen, white, rect)
    clock.tick(1)

        


    draw_snake(snake)
    pg.display.update()

    # on itère sur tous les évênements qui ont eu lieu depuis le précédent appel
    # ici donc tous les évènements survenus durant la seconde précédente
    for event in pg.event.get():
        # chaque évênement à un type qui décrit la nature de l'évênement
        # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
        if event.type == pg.QUIT:
            running = False
        # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
        elif event.type == pg.KEYDOWN:
            # si la touche est "Q" on veut quitter le programme
            if event.key == pg.K_q:
                running = False
            elif event.key == pg.K_LEFT:
                direction = (-1, 0)
                
            elif event.key == pg.K_RIGHT:
                direction = (1, 0)
                
            elif event.key == pg.K_DOWN:
                direction = (0, 1)
                
            elif event.key == pg.K_UP:
                direction = (0, -1)
                
    dirin = chgt_direction(snake, direction, dirin)

# Enfin on rajoute un appel à pg.quit()
# Cet appel va permettre à Pygame de "bien s'éteindre" et éviter des bugs sous Windows
pg.quit()
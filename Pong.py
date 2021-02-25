"""
This game was created after following a number of tutorials with links listed below and the image used for the background

https://www.youtube.com/watch?v=Qf3-aDXG8q4&t=188s&ab_channel=ClearCode
https://www.youtube.com/watch?v=dGwmmBBMlKs&ab_channel=buildwithpython
https://www.youtube.com/watch?v=Fp1dudhdX8k&feature=emb_title&ab_channel=buildwithpython
https://www.google.com/url?sa=i&url=https%3A%2F%2Fwallpapercave.com%2Fatari-retro-wallpapers&psig=AOvVaw0DU1O9LWfEJWliOShAnPhg&ust=1614309851508000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCJj39_yKhO8CFQAAAAAdAAAAABAD
"""
import pygame, sys, random

# We moved our ball movement code from within our block that registered user input to above here. There reason for this being that it allows us to add additional logic if we want without cluttering our loop
def ball_animation ():
    global ball_speed_x, ball_speed_y, player1_score, computer_score
   
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    
    if ball.left <= 0:
        player1_score += 1
        ball_restart()
    
    if ball.right >= screen_width:
        computer_score += 1
        ball_restart()
        
    if ball.colliderect(player1) or ball.colliderect(computer):
        ball_speed_x *= -1
            
# We did a similar movement for player animation just like we did for ball animation
def player_animation():
    player1.y = player1_speed  
    if player1.bottom >= screen_height:
        player1.bottom = screen_height
    if player1.top <= 0:
        player1.top = 0
     
def computer_ai():
    if computer.centery < ball.y:
        computer.centery += computer_speed
    if computer.bottom > ball.y:
        computer.bottom -= computer_speed
    if computer.bottom >= screen_height:
        computer.bottom = screen_height
    if computer.top <= 0:
        computer.top = 0
       
def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2,screen_height/2)
    ball_speed_y *= random.choice((1,-1))
    ball_speed_x *= random.choice((1,-1))

# We will begin with the setup of the game since Pygame is basically separated in two blocks - the general setup of the game itself and a loop to let the game run and update score

pygame.init()

#You need the above line to run any sort of game using Pygame. The below lines Setup our time, screen and load our own custom image as athe background

clock = pygame.time.Clock()
screen_width = 1920
screen_height = 1020
screen = pygame.display.set_mode((screen_width,screen_height))
image = pygame.image.load('Atari.png')
pygame.display.set_icon(image)


#Now, lets make our ball. In order to do this we will use a rectangle, which lets you basically have a box around drawings, images or shapes
ball = pygame.Rect(screen_width/2 - 20,screen_height/2 - 20,40,40)
player1 = pygame.Rect(screen_width - 20,screen_height/2 - 70,10,140)
computer = pygame.Rect(10,screen_height/2 - 70,10,140)

#Funfact: The below color code is from the Xbox's color palette 
xbox_green = (16,124,16)


#We created our rectangles above, and below we slapped them on to our screen. the block below will make them move!
ball_speed_x = 15 * random.choice((1,-1))
ball_speed_y = 15 * random.choice((1,-1))
player1_speed = 0
computer_speed = 15


# Text Variables for score counting
player1_score = 0
computer_score = 0
pong_font = pygame.font.Font("freesansbold.ttf",32)

def show_score(x,y):
    player1_text = pong_font.render(f"{player1_score}", False, xbox_green)
    screen.blit(player1_text,(980, 510))
    
    computer_text = pong_font.render(f"{computer_score}", False, xbox_green)
    screen.blit(computer_text,(930, 510))
    
#This block registers user input, like X-ing out of the game to quit
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player1_speed += 15
            if event.key == pygame.K_UP:
                player1_speed -= 15

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player1_speed -= 15
            if event.key == pygame.K_UP:
                player1_speed += 15
  
                
    ball_animation()
    player_animation()
    computer_ai()
    #We're making the rectangles we made earlier, order matters a lot here because if screen.blit is on the bottom all we will see is the background color
    screen.blit(image,(0,0))
    pygame.draw.rect(screen,xbox_green,player1)
    pygame.draw.rect(screen,xbox_green,computer)
    pygame.draw.ellipse(screen,xbox_green,ball)
    pygame.draw.aaline(screen,xbox_green,(screen_width/2,0),(screen_width/2,screen_height))
    show_score(570,480)

    
    pygame.display.flip()
    clock.tick(60)
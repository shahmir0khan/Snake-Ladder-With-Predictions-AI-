import pygame
import random
import time
from collections import Counter

pygame.init()
screen = pygame.display.set_mode((650, 500))

white = (255, 255, 255)
pygame.display.set_caption("Snakes And Ladders With Prediction Challenge")
# ladder= [(309,447),(505,398),(505,300),(603,251),(211,251),(211,153),(456,104)]
# snakes=[(456,349),(162,251),(260,251),(456,202),(407,153),(358,104),(554,55),(211,6)]

# bckground image
bckimg = pygame.image.load('bckimg.jpg')
img = pygame.image.load('dice (6).png')
arrow = pygame.image.load('arr.png')
stg = pygame.image.load('cool.jpg')

# playersz
r1 = pygame.image.load('pin (1).png')
b1 = pygame.image.load('placeholder.png')

rx = 162
ry = 447

# b1x = 162
# b1y = 447
b1x = 260
b1y = 6
bx = 155
by = 5

def bck():
    screen.blit(stg, (0, 0))
    screen.blit(bckimg, (bx, by))
    screen.blit(arrow, (10, 50))

def rplayer(x, y):
    screen.blit(r1, (x, y))

def bplayer(x, y):
    screen.blit(b1, (x, y))


button = pygame.Rect(10, 50, 40, 40)



score_font = pygame.font.SysFont("comicsansms", 35)
score_font1 = pygame.font.SysFont("comicsansms", 25)
score_font2 = pygame.font.SysFont("comicsansms", 20)

clock = pygame.time.Clock()

def players():

    value2= score_font1.render("AI", True, (255, 0, 0))
    screen.blit(value2, [5, 251])
    value3= score_font1.render("Player ", True, (0, 0, 255))
    screen.blit(value3, [5, 362])

def rollr():
    val1= score_font2.render("Your turn", True, (255, 255, 255))
    screen.blit(val1, [25, 288])
def rollb():
    val= score_font2.render("Your turn", True, (255, 255, 255))
    screen.blit(val, [25, 399])

# ****************************************** Prediction
# Lists to store predictions and dice outcomes
red_predicted_numbers = []
blue_predicted_numbers = []
dice_outputs = []
# Bonus points
red_bonus_points = 0
blue_bonus_points = 0

# Function to show prediction choices (1 to 6) on the screen for the player
def display_prediction_options(player):
    font = pygame.font.SysFont("comicsansms", 20)
    base_x = 250  
    base_y = 230  
    spacing = 50  

    # Draw background label for prompt
    label_rect = pygame.Rect(base_x - 10, base_y - 60, 300, 30)
    pygame.draw.rect(screen, (200, 200, 200), label_rect)  # fill color
    pygame.draw.rect(screen, (0, 0, 0), label_rect, 2)  # outline

    # Draw prompt message above the boxes
    prompt_text = font.render(f"Predict next outcome  ", True, (0, 0, 0))
    screen.blit(prompt_text, (280, base_y - 58))

    # Draw 6 number boxes (1 to 6)
    for i in range(6):
        rect = pygame.Rect(base_x + i * spacing, base_y, 40, 40)
        pygame.draw.rect(screen, (200, 200, 200), rect)  # draw gray box
        pygame.draw.rect(screen, (0, 0, 0), rect, 2)  # black outline
        number_text = font.render(str(i + 1), True, (0, 0, 0))  # render the number
        text_rect = number_text.get_rect(center=rect.center)  # center the text in the box
        screen.blit(number_text, text_rect)  # draw the text

    pygame.display.update()  


# Function to get the player's prediction (click on a number box)
def get_prediction(player):
    font = pygame.font.SysFont("comicsansms", 20)
    base_x = 250
    base_y = 230
    spacing = 50
    predicting = True  # stays True until player clicks a number
    prediction = None

    while predicting:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()  # get mouse position
                for i in range(6):
                    # check if mouse clicked within the box area
                    rect = pygame.Rect(base_x + i * spacing, base_y, 40, 40)
                    if rect.collidepoint(x, y):
                        prediction = i + 1  # save prediction (1 to 6)
                        predicting = False  # exit loop
            elif event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.time.wait(100)  
    return prediction



# Function to show bonus choice if prediction is correct (click-based)
def handle_correct_prediction(player_turn, correct_player):
    global red_bonus_points, blue_bonus_points
    font = pygame.font.SysFont("comicsansms", 20)

    # Options text
    if player_turn == correct_player:
        option1 = "Double your move"
        option2 = "+10 bonus points"
        
    else:
        option1 = "Skip opponent's move"
        option2 = "+10 bonus points"
    head_text=f" {correct_player.upper()} is Correct"

    option1_rect = pygame.Rect(260, 360+40, 250, 45)
    option2_rect = pygame.Rect(260, 410+40, 250, 45)
    head = pygame.Rect(280, 310+40, 210, 45)

    choosing = True
    while choosing:
        

        # Draw clickable option boxes with black fill and white border/text
        pygame.draw.rect(screen, (0, 0, 0), option1_rect)  # fill black
        pygame.draw.rect(screen, (0, 0, 0), option2_rect)
        pygame.draw.rect(screen, (200, 200, 200), head)
        pygame.draw.rect(screen, (255, 255, 255), option1_rect, 2)  # white border
        pygame.draw.rect(screen, (255, 255, 255), option2_rect, 2)
        pygame.draw.rect(screen, (0, 0, 0), head, 2) 
        # Render text in white
        text1 = font.render(option1, True, (255, 255, 255))
        text2 = font.render(option2, True, (255, 255, 255))
        text3 = font.render(head_text, True, (0,0,0))
        screen.blit(text3, (head.x + 10, head.y + 10))
        screen.blit(text1, (option1_rect.x + 10, option1_rect.y + 10))
        screen.blit(text2, (option2_rect.x + 10, option2_rect.y + 10))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if option1_rect.collidepoint(x, y):
                    if player_turn != correct_player:
                        return "skip"
                    else:
                        return "double"
                elif option2_rect.collidepoint(x, y):
                    # if correct_player == "red":
                    #     red_bonus_points += 10
                    # else:
                    blue_bonus_points += 10
                    return "bonus"
            elif event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.time.wait(100)


#*************************************AI ***********

def predict_next(history):
    # if not history:
    #     return random.randint(1, 6)  
    # # freq = Counter(history)
    # most_common = freq.most_common(1)[0][0]
    return 3

def display_ai_prediction(predicted_number):
    font = pygame.font.SysFont("comicsansms", 24)
    
    # Box location
    box_x = 250
    box_y = 300
    box_width = 250
    box_height = 40

    # Draw background rectangle
    ai_rect = pygame.Rect(box_x, box_y, box_width, box_height)
    pygame.draw.rect(screen, (180, 230, 180), ai_rect)  # light green fill
    pygame.draw.rect(screen, (0, 100, 0), ai_rect, 2)    # dark green border

    # Render the AI prediction message
    prediction_text = font.render(f"AI predicted: {predicted_number}", True, (0, 100, 0))
    text_rect = prediction_text.get_rect(center=ai_rect.center)
    screen.blit(prediction_text, text_rect)

    pygame.display.update()
    pygame.time.delay(100)



def display_ai_choice(choose):
    # Reduced font sizes
    font = pygame.font.SysFont("comicsansms", 18)  # Smaller font for subtext
    font_heading = pygame.font.SysFont("comicsansms", 20, bold=True)  # Smaller heading font

    # Box location
    box_x = 200
    box_y = 280
    box_width = 400
    box_height = 80

    # Draw background rectangle
    ai_rect = pygame.Rect(box_x, box_y, box_width, box_height)
    pygame.draw.rect(screen, (180, 230, 180), ai_rect)  # light green fill
    pygame.draw.rect(screen, (0, 100, 0), ai_rect, 2)    # dark green border

    # Heading
    heading_text = font_heading.render("AI PREDICTED CORRECTLY", True, (0, 100, 0))
    heading_rect = heading_text.get_rect(center=(box_x + box_width // 2, box_y + 20))
    screen.blit(heading_text, heading_rect)

    # Subheading with updated font size
    sub_text = font.render(f"AI chose to {choose}", True, (0, 100, 0))
    sub_rect = sub_text.get_rect(center=(box_x + box_width // 2, box_y + 50))
    screen.blit(sub_text, sub_rect)

    pygame.display.update()
    pygame.time.delay(100)



def AI_choice(turn, rx, ry, diceroll, b1x, b1y):
    if turn == 'red':
        new_rx, new_ry, _ = cal_move(diceroll, rx, ry, turn)
        newd_rx, newd_ry, _ = cal_move(2 * diceroll, rx, ry, turn)

        if (new_rx, new_ry) in [(309, 447), (505, 398), (505, 300), (603, 251), (211, 251), (211, 153), (456, 104)] or \
           (newd_rx, newd_ry) in [(456, 349), (162, 251), (260, 251), (456, 202), (407, 153), (358, 104), (554, 55), (211, 6)] or \
           temp != blue_prediction:
            choose = 'bonus'
        elif (newd_rx, newd_ry) in [(309, 447), (505, 398), (505, 300), (603, 251), (211, 251), (211, 153), (456, 104)] or \
             (new_rx, new_ry) in [(456, 349), (162, 251), (260, 251), (456, 202), (407, 153), (358, 104), (554, 55), (211, 6)]:
            choose = 'double'
        elif ry < b1y or (ry == b1y and rx < b1x):
            choose = 'double'
        else:
            choose = 'bonus'

    elif turn == 'blue':
        new_bx, new_by, _ = cal_move(diceroll, b1x, b1y, turn)
        newd_bx, newd_by, _ = cal_move(2 * diceroll, b1x, b1y, turn)

        if (new_bx, new_by) in [(309, 447), (505, 398), (505, 300), (603, 251), (211, 251), (211, 153), (456, 104)] or \
           (new_bx, new_by) not in [(456, 349), (162, 251), (260, 251), (456, 202), (407, 153), (358, 104), (554, 55), (211, 6)] or \
           ry < b1y or (ry == b1y and rx < b1x):
            choose = 'skip'
        elif temp == blue_prediction and (
            (newd_bx, newd_by) in [(309, 447), (505, 398), (505, 300), (603, 251), (211, 251), (211, 153), (456, 104)] or
            (newd_bx, newd_by) not in [(456, 349), (162, 251), (260, 251), (456, 202), (407, 153), (358, 104), (554, 55), (211, 6)]
        ):
            choose = 'skip'
        else:
            choose = 'bonus'

    return choose


def snake_attack(rtx, rty):
    if rtx == 456 and rty == 349:
        rtx = 358
        rty = 447
    elif rtx == 162 and rty == 300:
        rtx = 260
        rty = 447
    elif rtx == 260 and rty == 251:
        rtx = 260
        rty = 398
    elif rtx == 456 and rty == 202:
        rtx = 603
        rty = 300
    elif rtx == 407 and rty == 153:
        rtx = 358
        rty = 251
    elif rtx == 358 and rty == 104:
        rtx = 260
        rty = 202
    elif rtx == 554 and rty == 55:
        rtx = 505
        rty = 202
    elif rtx == 211 and rty == 6:
        rtx = 162
        rty = 251
    return rtx, rty


def ai_neutralize(rxx, ryy, red_bonus_points):
    
    snake_heads = [(456, 349), (162, 251), (260, 251), (456, 202),
                   (407, 153), (358, 104), (554, 55), (211, 6)]

    if (rxx, ryy) in snake_heads and red_bonus_points >= 20:
        
        red_bonus_points -= 20
        
        # Display neutralization message
        font = pygame.font.SysFont("comicsansms", 24)
        box_x = 250
        box_y = 350
        box_width = 300
        box_height = 40

        neutral_rect = pygame.Rect(box_x, box_y, box_width, box_height)
        pygame.draw.rect(screen, (255, 220, 180), neutral_rect)  # light orange
        pygame.draw.rect(screen, (200, 80, 0), neutral_rect, 2)   # dark orange border
       
        neutral_text = font.render("AI neutralized the snake!", True, (200, 80, 0))
        text_rect = neutral_text.get_rect(center=neutral_rect.center)
        screen.blit(neutral_text, text_rect)
        
        pygame.display.update()
        
        pygame.time.delay(100)
       
        # return rxx, ryy, red_bonus_points
    else:
        # print(f"before{rxx}{ryy}")
        rxx, ryy = snake_attack(rxx, ryy)
        
        # print(f"after{rxx}{ryy}")
        # return rxx, ryy, red_bonus_points
    print(f"after{rxx}{ryy}")
    return rxx, ryy, red_bonus_points

def handle_blue_snake_choice(b1x, b1y, blue_bonus_points):
    snake_heads = [(456, 349), (162, 251), (260, 251), (456, 202),
                   (407, 153), (358, 104), (554, 55), (211, 6)]
    check=True
    print(f"below neutralize{check}")
    if (b1x, b1y) in snake_heads and blue_bonus_points >= 20 and check:
        font = pygame.font.SysFont("comicsansms", 20)

        option1 = "Neutralize Snake"
        option2 = "Don't Neutralize"
        head_text = "You hit a snake!"
        
        option1_rect = pygame.Rect(260, 400, 250, 45)
        option2_rect = pygame.Rect(260, 450, 250, 45)
        head_rect = pygame.Rect(280, 350, 210, 45)

        choosing = True
        while choosing:
            pygame.draw.rect(screen, (0, 0, 0), option1_rect)
            pygame.draw.rect(screen, (0, 0, 0), option2_rect)
            pygame.draw.rect(screen, (200, 200, 200), head_rect)

            pygame.draw.rect(screen, (255, 255, 255), option1_rect, 2)
            pygame.draw.rect(screen, (255, 255, 255), option2_rect, 2)
            pygame.draw.rect(screen, (0, 0, 0), head_rect, 2)

            text1 = font.render(option1, True, (255, 255, 255))
            text2 = font.render(option2, True, (255, 255, 255))
            text3 = font.render(head_text, True, (0, 0, 0))

            screen.blit(text3, (head_rect.x + 10, head_rect.y + 10))
            screen.blit(text1, (option1_rect.x + 10, option1_rect.y + 10))
            screen.blit(text2, (option2_rect.x + 10, option2_rect.y + 10))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if option1_rect.collidepoint(x, y):
                        blue_bonus_points -= 20
                        choosing=False
                        check=False
                        print(f"{option1}")
                        return b1x, b1y, blue_bonus_points
                         # Do nothing, snake neutralized
                    elif option2_rect.collidepoint(x, y):
                        b1x, b1y = snake_attack(b1x, b1y)  # Call snake attack
                        print(f"{option2}")
                        return b1x, b1y, blue_bonus_points
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            pygame.display.update()
            pygame.time.wait(100)

    else:
        return b1x, b1y, blue_bonus_points,True # No snake or not enough bonus points

# *******************************************
def pickNumber():
    
    diceroll = random.randint(2, 2)
    
    
    if diceroll == 1:
        dice = pygame.image.load("d1.png")

    elif diceroll == 2:
        dice = pygame.image.load("d2.png")

    elif diceroll == 3:
        dice = pygame.image.load("d3.png")
    elif diceroll == 4:
        dice = pygame.image.load("d4.png")

    elif diceroll == 5:
        dice = pygame.image.load("d5.png")

    elif diceroll == 6:
        dice = pygame.image.load("d6.png")

    return (dice,diceroll)


    
# game loop

running = True

turn='red'



def cal_move(diceroll,rtx,rty,turnn):
    turnn_old=turnn
    turnn='red'
    new_turnn='blue'
    if pickNumber() and turnn=='red':
                
                
                
                turnn='blue'
                # if diceroll == 6 and rtx<162 and rty==251:
                if  rtx<162 and rty==251:
                    rtx=rtx+62
                    rty=447
                    
                    turnn='red'
                    
                elif rtx>=162 and rtx<358 and(rty==447 or rty==349 or rty==251 or rty==153 or rty==55)and diceroll!=6:
                    
                    
                    rtx=rtx+(49*diceroll)
                    
                    if rtx==309 and rty==447:
                        rtx=358
                        rty=349
                    # elif rtx==456 and rty==349:
                    #     rtx=358
                    #     rty=447
                    elif rtx==211 and rty==251:
                        rtx=260
                        rty=153
                    elif rtx==211 and rty==153:
                        rtx=162
                        rty=55
                    # elif rtx==260 and rty==251:
                    #     rtx=260
                    #     rty=398
                    elif rtx==603 and rty==251:
                        rtx=554
                        rty=153
                    # elif rtx==407 and rty==153:
                    #     rtx=358
                    #     rty=251
                    # elif rtx==554 and rty==55:
                    #     rtx=505
                    #     rty=202
                elif rtx>=162 and rtx<358 and(rty==447 or rty==349 or rty==251 or rty==153 or rty==55)and diceroll==6:
                    rtx=rtx+(49*diceroll)
                    
                   
                    if rtx==309 and rty==447:
                        rtx=358
                        rty=349
                    # elif rtx==456 and rty==349:
                    #     rtx=358
                    #     rty=447
                    elif rtx==211 and rty==251:
                        rtx=260
                        rty=153
                    elif rtx==211 and rty==153:
                        rtx=162
                        rty=55
                    # elif rtx==260 and rty==251:
                    #     rtx=260
                    #     rty=398
                    elif rtx==603 and rty==251:
                        rtx=554
                        rty=153
                    # elif rtx==407 and rty==153:
                    #     rtx=358
                    #     rty=251
                    # elif rtx==554 and rty==55:
                    #     rtx=505
                    #     rty=202
                    turnn='red'
                    

                
                elif rtx>=358 and rtx<407 and diceroll!=6 and (rty==447 or rty==349 or rty==251 or rty==153 or rty==55):
                    
                    
                    rtx=rtx+(49*diceroll)
                    # if rtx==456 and rty==349:
                    #     rtx=358
                    #     rty=447
                    if rtx==603 and rty==251:
                        rtx=554
                        rty=153
                    # elif rtx==407 and rty==153:
                    #     rtx=358
                    #     rty=251
                    elif rtx==554 and rty==55 and diceroll==4:
                        rtx=505
                        rty=202
                elif rtx>=358 and rtx<407 and diceroll==6 and (rty==447 or rty==349 or rty==251 or rty==153 or rty==55):
                    rtx=rtx+(49*5)-(49*(diceroll-6))
                    rty=rty-49
                    turnn='red'
                    
                        
                           
                elif rtx>=407 and rtx<456 and diceroll<=4 and (rty==447 or rty==349 or rty==251 or rty==153 or rty==55):#7
                    
                    rtx=rtx+(49*diceroll)
                    # if rtx==456 and rty==349:
                    #     rtx=358
                    #     rty=447
                    if rtx==603 and rty==251:
                        rtx=554
                        rty=153
                    elif rtx==554 and rty==55 and diceroll==3:
                        rtx=505
                        rty=202
                elif rtx>=407 and rtx<456 and diceroll>4 and diceroll!=6 and (rty==447 or rty==349 or rty==251 or rty==153 or rty==55):
                    
                    
                    rtx=rtx+(49*4)-(49*(diceroll-5))
                    rty=rty-49
                elif rtx>=407 and rtx<456 and diceroll==6 and (rty==447 or rty==349 or rty==251 or rty==153 or rty==55):
                    
                    rtx=rtx+(49*4)-(49*(diceroll-5))
                    rty=rty-49
                    turnn='red'
                    

                elif rtx>=456 and rtx<505 and diceroll<=3 and (rty==447 or rty==349 or rty==251 or rty==153 or rty==55):#8
                    
                    rtx=rtx+(49*diceroll)
                    if rtx==603 and rty==251:
                        rtx=554
                        rty=153
                    elif rtx==554 and rty==55 and diceroll==2:
                        rtx=505
                        rty=202
                elif rtx>=456 and rtx<505 and diceroll>3 and diceroll!=6 and (rty==447 or rty==349 or rty==251 or rty==153 or rty==55):
                    rtx=rtx+(49*3)-(49*(diceroll-4))
                    rty=rty-49
                    if rtx==505 and rty==398:
                        rtx=407
                        rty=251
                    elif rtx==505 and rty==300:
                        rtx=554
                        rty=251
                elif rtx>=456 and rtx<505 and diceroll==6 and (rty==447 or rty==349 or rty==251 or rty==153 or rty==55):
                    rtx=rtx+(49*3)-(49*(diceroll-4))
                    rty=rty-49
                    if rtx==505 and rty==398:
                        rtx=407
                        rty=251
                    elif rtx==505 and rty==300:
                        rtx=554
                        rty=251
                    turnn='red'
                    
                elif rtx>=505 and rtx<554 and diceroll<=2 and (rty==447 or rty==349 or rty==251 or rty==153 or rty==55):#9
                    
                    rtx=rtx+(49*diceroll)
                    if rtx==603 and rty==251:
                        rtx=554
                        rty=153
                    elif rtx==554 and rty==55 and diceroll==1:
                        rtx=505
                        rty=202
                elif rtx>=505 and rtx<554 and diceroll>2 and diceroll!=6 and (rty==447 or rty==349 or rty==251 or rty==153 or rty==55):
                    rtx=rtx+(49*2)-(49*(diceroll-3))
                    rty=rty-49
                    if rtx==505 and rty==398:
                        rtx=407
                        rty=251
                    elif rtx==505 and rty==300:
                        rtx=554
                        rty=251
                    # elif rtx==456 and rty==202:
                    #     rtx=603
                    #     rty=300
                    elif rtx==456 and rty==104:
                        rtx=554
                        rty=6
                elif rtx>=505 and rtx<554 and diceroll==6 and (rty==447 or rty==349 or rty==251 or rty==153 or rty==55):
                    rtx=rtx+(49*2)-(49*(diceroll-3))
                    rty=rty-49
                    if rtx==505 and rty==398:
                        rtx=407
                        rty=251
                    elif rtx==505 and rty==300:
                        rtx=554
                        rty=251
                    # elif rtx==456 and rty==202:
                    #     rtx=603
                    #     rty=300
                    elif rtx==456 and rty==104:
                        rtx=554
                        rty=6
                    turnn='red'
                    
                elif rtx>=554 and rtx<603 and diceroll==1 and (rty==447 or rty==349 or rty==251 or rty==153 or rty==55): #10
                    
                    rtx=rtx+(49*diceroll)
                    if rtx==603 and rty==251:
                        rtx=554
                        rty=153
                elif rtx>=554 and rtx<603 and diceroll>1 and diceroll!=6 and (rty==447 or rty==349 or rty==251 or rty==153 or rty==55):
                    rtx=rtx+(49*1)-(49*(diceroll-2))
                    rty=rty-49
                    if rtx==505 and rty==398:
                        rtx=407
                        rty=251
                    elif rtx==505 and rty==300:
                        rtx=554
                        rty=251
                    # elif rtx==456 and rty==202:
                    #     rtx=603
                    #     rty=300
                    elif rtx==456 and rty==104:
                        rtx=554
                        rty=6
                elif rtx>=554 and rtx<603 and diceroll==6 and (rty==447 or rty==349 or rty==251 or rty==153 or rty==55):
                    rtx=rtx+(49*1)-(49*(diceroll-2))
                    rty=rty-49
                    if rtx==505 and rty==398:
                        rtx=407
                        rty=251
                    elif rtx==505 and rty==300:
                        rtx=554
                        rty=251
                    # elif rtx==456 and rty==202:
                    #     rtx=603
                    #     rty=300
                    elif rtx==456 and rty==104:
                        rtx=554
                        rty=6
                    turnn='red'
                
                    
                elif rtx>=603 and (rty==447 or rty==349 or rty==251 or rty==153 or rty==55)and diceroll!=6:
                    rtx=rtx-(49*(diceroll-1))
                    rty=rty-49
                    if rtx==505 and rty==398:
                        rtx=407
                        rty=251
                    elif rtx==505 and rty==300:
                        rtx=554
                        rty=251
                    # elif rtx==456 and rty==202:
                    #     rtx=603
                    #     rty=300
                    elif rtx==456 and rty==104:
                        rtx=554
                        rty=6
                    # elif rtx==358 and rty==104:
                    #     rtx=260
                    #     rty=202
                elif rtx>=603 and (rty==447 or rty==349 or rty==251 or rty==153 or rty==55)and diceroll==6:
                    rtx=rtx-(49*(diceroll-1))
                    rty=rty-49
                    if rtx==505 and rty==398:
                        rtx=407
                        rty=251
                    elif rtx==505 and rty==300:
                        rtx=554
                        rty=251
                    # elif rtx==456 and rty==202:
                    #     rtx=603
                    #     rty=300
                    elif rtx==456 and rty==104:
                        rtx=554
                        rty=6
                    # elif rtx==358 and rty==104:
                    #     rtx=260
                    #     rty=202
                    turnn='red'


                #c2 starts from here

                    
                elif rtx>358 and rtx<=603 and (rty==398 or rty==300 or rty==202 or rty==104 or rty==6) and diceroll!=6:
                    rtx=rtx-(49*diceroll)
                    if rtx==505 and rty==398:
                        rtx=407
                        rty=251
                    elif rtx==505 and rty==300:
                        rtx=554
                        rty=251
                    # elif rtx==456 and rty==202:
                    #     rtx=603
                    #     rty=300
                    elif rtx==456 and rty==104:
                        rtx=554
                        rty=6
                    # elif rtx==162 and rty==300:
                    #     rtx=260
                    #     rty=447
                    # elif rtx==358 and rty==104:
                    #     rtx=260
                    #     rty=202
                    
                
                elif rtx>407 and rtx<=603 and diceroll!=6 and (rty==398 or rty==300 or rty==202 or rty==104 or rty==6):
                    rtx=rtx-(49*diceroll)
                    # if rtx==211 and rty==6:
                    #     rtx=162
                    #     rty=251
                    # elif rtx==162 and rty==300:
                    #     rtx=260
                    #     rty=447
                    # elif rtx==211 and rty==6:
                    #     rtx=162
                    #     rty=251
                elif rtx>407 and rtx<=603 and diceroll==6 and (rty==398 or rty==300 or rty==202 or rty==104 or rty==6):
                    rtx=rtx-(49*diceroll)
                    # if rtx==211 and rty==6:
                    #     rtx=162
                    #     rty=251
                    # elif rtx==162 and rty==300:
                    #     rtx=260
                    #     rty=447
                    # if rtx==211 and rty==6:
                    #     rtx=162
                    #     rty=251
                    turnn='red'
                    
                elif rtx==407 and (rty==398 or rty==300 or rty==202 or rty==104) and diceroll!=6:
                    rtx=rtx-(49*diceroll)
                    # if rtx==358 and rty==104:
                    #     rtx=260
                    #     rty=202
                    # if rtx==211 and rty==6:
                    #     rtx=162
                    #     rty=251
                        

                elif rtx==407 and (rty==398 or rty==300 or rty==202 or rty==104) and diceroll==6:
                    rtx=rtx-(49*5)
                    rty=rty-49
                    # if rtx==162 and rty==300:
                    #     rtx=260
                    #     rty=447
                    turnn='red'
                
                elif rtx==358 and (rty==398 or rty==300 or rty==202 or rty==104 ) and diceroll<5:
                    rtx=rtx-(49*diceroll)
                    # if rtx==162 and rty==300:
                    #     rtx=260
                    #     rty=447
                elif rtx==358 and (rty==398 or rty==300 or rty==202 or rty==104 ) and diceroll==5:
                    rtx=rtx-(49*4)+(49*(diceroll-5))
                    rty=rty-49
                    if rtx==211 and rty==251:
                        rtx=260
                        rty=153
                    elif rtx==211 and rty==153:
                        rtx=162
                        rty=55
                elif rtx==358 and (rty==398 or rty==300 or rty==202 or rty==104 ) and diceroll==6:
                    rtx=rtx-(49*4)+(49*(diceroll-5))
                    rty=rty-49
                    if rtx==211 and rty==251:
                        rtx=260
                        rty=153
                    elif rtx==211 and rty==153:
                        rtx=162
                        rty=55
                    turnn='red'
                elif rtx==309 and (rty==398 or rty==300 or rty==202 or rty==104) and diceroll<4:
                    rtx=rtx-(49*diceroll)
                    # if rtx==162 and rty==300:
                    #     rtx=260
                    #     rty=447
                elif rtx==309 and (rty==398 or rty==300 or rty==202 or rty==104) and diceroll>=4 and diceroll!=6:
                    rtx=rtx-(49*3)+(49*(diceroll-4))
                    rty=rty-49
                    if rtx==211 and rty==251:
                        rtx=260
                        rty=153
                    elif rtx==211 and rty==153:
                        rtx=162
                        rty=55
                    # elif rtx==260 and rty==251:
                    #     rtx=260
                    #     rty=398
                elif rtx==309 and (rty==398 or rty==300 or rty==202 or rty==104) and diceroll==6:
                    rtx=rtx-(49*3)+(49*(diceroll-4))
                    rty=rty-49
                    if rtx==211 and rty==251:
                        rtx=260
                        rty=153
                    elif rtx==211 and rty==153:
                        rtx=162
                        rty=55
                    # elif rtx==260 and rty==251:
                    #     rtx=260
                    #     rty=398
                    turnn='red'
                elif rtx==260 and (rty==398 or rty==300 or rty==202 or rty==104 ) and diceroll<3:
                    rtx=rtx-(49*diceroll)
                    # if rtx==162 and rty==300:
                    #     rtx=260
                    #     rty=447
                elif rtx==260 and (rty==398 or rty==300 or rty==202 or rty==104 ) and diceroll>=3 and diceroll!=6:
                    rtx=rtx-(49*2)+(49*(diceroll-3))
                    rty=rty-49
                    if rtx==211 and rty==251:
                        rtx=260
                        rty=153
                    elif rtx==211 and rty==153:
                        rtx=162
                        rty=55
                    # elif rtx==260 and rty==251:
                    #     rtx=260
                    #     rty=398
                elif rtx==260 and (rty==398 or rty==300 or rty==202 or rty==104 ) and diceroll==6:
                    rtx=rtx-(49*2)+(49*(diceroll-3))
                    rty=rty-49
                    if rtx==211 and rty==251:
                        rtx=260
                        rty=153
                    elif rtx==211 and rty==153:
                        rtx=162
                        rty=55
                    # elif rtx==260 and rty==251:
                    #     rtx=260
                    #     rty=398
                    turnn='red'
                elif rtx==211 and (rty==398 or rty==300 or rty==202 or rty==104 ) and diceroll<2:
                    rtx=rtx-(49*diceroll)
                    # if rtx==162 and rty==300:
                    #     rtx=260
                    #     rty=447
                elif rtx==211 and (rty==398 or rty==300 or rty==202 or rty==104) and diceroll!=6 and diceroll>=2:
                    rtx=rtx-49+(49*(diceroll-2))
                    rty=rty-49
                    if rtx==211 and rty==251:
                        rtx=260
                        rty=153
                    elif rtx==211 and rty==153:
                        rtx=162
                        rty=55
                    # elif rtx==260 and rty==251:
                    #     rtx=260
                    #     rty=398
                elif rtx==211 and (rty==398 or rty==300 or rty==202 or rty==104) and diceroll==6 :
                    rtx=rtx-49+(49*(diceroll-2))
                    rty=rty-49
                    if rtx==211 and rty==251:
                        rtx=260
                        rty=153
                    elif rtx==211 and rty==153:
                        rtx=162
                        rty=55
                    # elif rtx==260 and rty==251:
                    #     rtx=260
                    #     rty=398
                    turnn='red'

                
                elif rtx==162 and (rty==398 or rty==300 or rty==202 or rty==104 ) and diceroll!=6:
                    rtx=rtx+(49*(diceroll-1))
                    rty=rty-49
                    if rtx==211 and rty==251:
                        rtx=260
                        rty=153
                    elif rtx==211 and rty==153:
                        rtx=162
                        rty=55
                    # elif rtx==260 and rty==251:
                    #     rtx=260
                    #     rty=398
                    # elif rtx==407 and rty==153:
                    #     rtx=358
                    #     rty=251
                elif rtx==162 and (rty==398 or rty==300 or rty==202 or rty==104 ) and diceroll==6:
                    rtx=rtx+(49*(diceroll-1))
                    rty=rty-49
                    if rtx==211 and rty==251:
                        rtx=260
                        rty=153
                    elif rtx==211 and rty==153:
                        rtx=162
                        rty=55
                    # elif rtx==260 and rty==251:
                    #     rtx=260
                    #     rty=398
                    # elif rtx==407 and rty==153:
                    #     rtx=358
                    #     rty=251
                    turnn='red'


                    

                #final row
                elif rty==6 and (rtx==554 or rtx==603) and diceroll!=6:
                    rtx=rtx-(49*diceroll)
                elif rty==6 and (rtx==554 or rtx==603) and diceroll==6:
                    rtx=rtx-(49*diceroll)
                    turnn='red'
                elif rty==6 and rtx==456 and diceroll<5:
                    rtx=rtx-(49*diceroll)
                elif rty==6 and rtx==456 and diceroll==5:
                    rtx=rtx-(49*diceroll)
                    if rtx==211 and rty==6 and diceroll==5:
                        rtx=162
                        rty=251
                elif rty==6 and rtx==456 and diceroll==6:
                    rtx=rtx
                elif rty==6 and rtx==505 and diceroll!=6:
                    rtx=rtx-(49*diceroll)
                elif rty==6 and rtx==505 and diceroll==6:
                    rtx=rtx-(49*diceroll)
                    if rtx==211 and rty==6 and diceroll==6:
                        rtx=162
                        rty=251

                    
                
                elif rty==6 and rtx==407 and diceroll <6:
                    rtx=rtx-(49*diceroll)
                    if rtx==211 and rty==6 and diceroll==4:
                        rtx=162
                        rty=251
                elif rty==6 and rtx==407 and rtx>=162  and diceroll ==6:
                    rtx=rtx
                    

                elif rty==6 and rtx==358 and rtx>=162  and diceroll >=5:
                    rtx=rtx
                elif rty==6 and rtx==358 and rtx>=162  and diceroll <5:
                    rtx=rtx-(49*diceroll)
                    if rtx==211 and rty==6 and diceroll==3:
                        rtx=162
                        rty=251
                
                elif rty==6 and rtx==309 and rtx>=162  and diceroll >=4:
                    rtx=rtx
                elif rty==6 and rtx==309 and rtx>=162  and diceroll <4:
                    rtx=rtx-(49*diceroll)
                    if rtx==211 and rty==6 and diceroll==2:
                        rtx=162
                        rty=251
                elif rty==6 and rtx==260 and rtx>=162  and diceroll >=3:
                    rtx=rtx
                elif rty==6 and rtx==260 and rtx>=162  and diceroll <3:
                    rtx=rtx-(49*diceroll)
                    if rtx==211 and rty==6 and diceroll==1:
                        rtx=162
                        rty=251
                elif rty==6 and rtx==211 and rtx>162 and diceroll >=2:
                    rtx=rtx
    
    if turnn_old=='red':
        new_turnn=turnn
    else:
        # if turnn=='red':
        #     new_turnn ='blue'
        # if turnn=='red':
        new_turnn='red'
    return rtx,rty,new_turnn


#game loop
while running:
    screen.fill((0, 255, 195))
    
    bck()
    players()
    rplayer(rx, ry)
    bplayer(b1x, b1y)    
    
    if turn=='red':
        rollr()
    
    if turn=='blue':
        rollb()   
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if button.collidepoint(mouse_pos):
                
                bck()  # call your background function first
                players()  # draw player pieces or labels
                rplayer(rx, ry)
                bplayer(b1x, b1y)
                if turn=='red':
                    rollr()
    
                if turn=='blue':
                    rollb()
                
                
                display_prediction_options("blue")
                blue_prediction = get_prediction("blue")
                blue_predicted_numbers.append(blue_prediction)
                print(f"Blue prediction {blue_predicted_numbers} ")
                

                # display_prediction_options("red")
                # red_prediction = get_prediction("red")
                red_prediction=predict_next(dice_outputs)
                red_predicted_numbers.append(red_prediction)
                display_ai_prediction(red_prediction)
                print(f"Red prediction {red_predicted_numbers} ")
                
                dice,diceroll = pickNumber()
                dice_outputs.append(diceroll)
                print(f"outputs {dice_outputs} ")                
                screen.blit(dice, (58, 48))
                
                temp=diceroll  

                if temp == blue_prediction:
                    choose=handle_correct_prediction(turn, 'blue') 
                    if choose =='skip':
                        diceroll = diceroll -temp
                    elif choose =='double':
                        diceroll=diceroll+temp
                    
                    print(choose, diceroll)
                    
                print(diceroll)

                if temp ==red_prediction:
                    choose=AI_choice(turn,rx,ry,diceroll,b1x,b1y)
                    if choose =='skip':
                        diceroll = 0
                        choose='Skip the Players Move'
                    elif choose =='double':
                        diceroll=temp+temp 
                        choose='Double his Move'
                    elif choose=='bonus':
                        red_bonus_points += 10  
                        choose='Take the BONUS POINTS'    
                    print(choose, diceroll)

                    display_ai_choice(choose) 
                snake_heads = [(456, 349), (162, 251), (260, 251), (456, 202),(407, 153), (358, 104), (554, 55), (211, 6)]
                if turn == 'red':   

                    rx,ry,turn=cal_move(diceroll,rx,ry,turn)
                    if (rx, ry) in snake_heads :
                        print("below checking")
                        rx,ry,red_bonus_points=ai_neutralize(rx,ry,red_bonus_points)
                elif turn =='blue':

                    # print(f"b previous value{b1x} {b1y} {turn}")
                    b1x,b1y,turn=cal_move(diceroll,b1x,b1y,turn)
                    # print(f"b new value{b1x} {b1y} {turn}")
                    if (b1x, b1y) in snake_heads and blue_bonus_points >= 20 and turn =='red':
                        print("below neutralize")
                        b1x,b1y,blue_bonus_points=handle_blue_snake_choice(b1x, b1y, blue_bonus_points)
                
  
        
    rplayer(rx, ry)
    bplayer(b1x, b1y)
    pygame.display.update()
    
    time.sleep(1) 
    if rx==162 and ry==6 :
        screen.fill((50, 153, 213))
        value = score_font.render("AI won", True, (255, 255, 102))
        
        screen.blit(value, [250, 200])
        pygame.display.update() 
        
        time.sleep(10)
        running = False
        
    if b1x==162 and b1y==6 :
        screen.fill((50, 153, 213))
        value = score_font.render("Blue WON", True, (255, 255, 102))
        
        screen.blit(value, [250, 200])
        pygame.display.update() 
        time.sleep(10)
        running = False


    time.sleep(2)
        
    
 
    
pygame.display.update()
clock.tick(40)
pygame.quit()
quit()
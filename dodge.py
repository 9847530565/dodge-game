import pygame
import random
pygame.init()
font1=pygame.font.SysFont(pygame.font.get_fonts()[27],30,False,False)
font2=pygame.font.SysFont(pygame.font.get_fonts()[33],60,False,False)
screen_width,screen_height=600,600
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("music player")
clock=pygame.time.Clock()
def textdisplay(content,cordinates):
    text1=font1.render(content,1,(0,0,0))
    screen.blit(text1,cordinates)
def textdisplay2(content,cordinates):
    text1=font2.render(content,1,(0,0,0))
    screen.blit(text1,cordinates)
def imagedisplay(image,cordinates):
    screen.blit(image,cordinates)
class game:
    @staticmethod
    def gameloop():
        image1=pygame.image.load("files/ground_inscene.png")
        image1=pygame.transform.scale(image1,(screen_width,screen_height))
        exit_game,game_over,gameplay,mainmenu=False,False,False,True
        pressed_right,pressed_left,pressed_space=False,False,False
        xcord=0
        spritenumber=0
        fps=15
        score=0
        travel=5
        relmotion=-10
        pos=random.randint(0,4)
        objectx,objecty=650,7*screen_height/12
        image2=pygame.image.load("files/standing.png")
        image3=pygame.transform.scale(image2,(90,90))
        positionx,positiony=0,7*screen_height/12
        obstacles=[pygame.image.load("files/ob1.png"),pygame.image.load("files/ob2.png"),pygame.image.load("files/ob3.png"),pygame.image.load("files/ob4.png"),pygame.image.load("files/ob5.png")]
        movement=[pygame.image.load("files/R1.png"),pygame.image.load("files/R2.png"),pygame.image.load("files/R3.png"),pygame.image.load("files/R4.png"),pygame.image.load("files/R5.png"),pygame.image.load("files/R6.png"),pygame.image.load("files/R7.png"),pygame.image.load("files/R8.png"),pygame.image.load("files/R9.png")]
        options={"PLAY":(screen_width/12,23*screen_height/60),"EXIT":(3*screen_width/4,23*screen_height/60)}
        while not(exit_game):
            if mainmenu:
                screen.fill((255,255,255))
                screen.blit(image1,(0,0))
                textdisplay2("DODGE",(11*screen_width/30,screen_height/120))
                imagedisplay(image3,(5*screen_width/12,screen_height/6))
                for i in options:
                    pygame.draw.rect(screen,(34,139,34),(options[i][0]-10,options[i][1]-5,screen_width/4,screen_height/10))
                if options["PLAY"][0]<=pygame.mouse.get_pos()[0]<=options['PLAY'][0]+screen_width/4 and options['PLAY'][1]<=pygame.mouse.get_pos()[1]<=options['PLAY'][1]+screen_height/10:
                    pygame.draw.rect(screen,(32,178,170),(options['PLAY'][0]-10,options['PLAY'][1]-5,screen_width/4,screen_height/10))
                elif options["EXIT"][0]<=pygame.mouse.get_pos()[0]<=options['EXIT'][0]+screen_width/4 and options['EXIT'][1]<=pygame.mouse.get_pos()[1]<=options['EXIT'][1]+screen_height/10:
                    pygame.draw.rect(screen,(32,178,170),(options['EXIT'][0]-10,options['EXIT'][1]-5,screen_width/4,screen_height/10))
                for i in options:
                    textdisplay(i,options[i])
                if positionx+35>=screen_width:
                    travel=-5
                    movement=[pygame.image.load("files/L1.png"),pygame.image.load("files/L2.png"),pygame.image.load("files/L3.png"),pygame.image.load("files/L4.png"),pygame.image.load("files/L5.png"),pygame.image.load("files/L6.png"),pygame.image.load("files/L7.png"),pygame.image.load("files/L8.png"),pygame.image.load("files/L9.png")]
                    spritenumber=0
                    positionx+=travel
                elif positionx<-20:
                    travel=5
                    movement=[pygame.image.load("files/R1.png"),pygame.image.load("files/R2.png"),pygame.image.load("files/R3.png"),pygame.image.load("files/R4.png"),pygame.image.load("files/R5.png"),pygame.image.load("files/R6.png"),pygame.image.load("files/R7.png"),pygame.image.load("files/R8.png"),pygame.image.load("files/R9.png")]
                    positionx+=travel
                    spritenumber=0
                if spritenumber>8:
                    spritenumber=0
                imagedisplay(movement[spritenumber],(positionx,positiony))
                spritenumber+=1
                positionx+=travel
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        exit_game=True
                    elif event.type==pygame.MOUSEBUTTONDOWN:
                        if options["PLAY"][0]<=pygame.mouse.get_pos()[0]<=options['PLAY'][0]+screen_width/4 and options['PLAY'][1]<=pygame.mouse.get_pos()[1]<=options['PLAY'][1]+screen_height/10:
                            mainmenu=False
                            gameplay=True
                            positionx,positiony=0,7*screen_height/12
                            movement=[pygame.image.load("files/R1.png"),pygame.image.load("files/R2.png"),pygame.image.load("files/R3.png"),pygame.image.load("files/R4.png"),pygame.image.load("files/R5.png"),pygame.image.load("files/R6.png"),pygame.image.load("files/R7.png"),pygame.image.load("files/R8.png"),pygame.image.load("files/R9.png")]
                        elif options["EXIT"][0]<=pygame.mouse.get_pos()[0]<=options['EXIT'][0]+screen_width/4 and options['EXIT'][1]<=pygame.mouse.get_pos()[1]<=options['EXIT'][1]+screen_height/10:
                            exit_game=True
                    elif event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_RETURN:
                            mainmenu=False
                            gameplay=True
                            positionx,positiony=0,7*screen_height/12
                            movement=[pygame.image.load("files/R1.png"),pygame.image.load("files/R2.png"),pygame.image.load("files/R3.png"),pygame.image.load("files/R4.png"),pygame.image.load("files/R5.png"),pygame.image.load("files/R6.png"),pygame.image.load("files/R7.png"),pygame.image.load("files/R8.png"),pygame.image.load("files/R9.png")]
            elif gameplay:
                screen.fill((255,255,255))
                if xcord+screen_width<0:
                    xcord=0
                screen.blit(image1,(xcord,0))
                screen.blit(image1,(screen_width+xcord,0))
                xcord-=10
                textdisplay("score:{}".format(score),(0,2))
                if objectx>=-50:
                    objectx-=15
                elif objectx<-50:
                    pos=random.randint(0,4)
                    objectx=650
                    score+=20
                obstacles[pos]=pygame.transform.scale(obstacles[pos],(70,70))
                imagedisplay(obstacles[pos],(objectx,objecty))
                if (objectx<=positionx+32<=objectx+70 or objectx<=positionx<=objectx+70) and (objecty<=positiony<=objecty+70 or objecty<=positiony+32<=objecty+70):
                    game_over=True
                    gameplay=False
                    pygame.mixer_music.load("files/salamisound-6762623-heardbeat-vibration.wav")
                    pygame.mixer_music.play(1)
                if pressed_space:
                    if 5*screen_height/12<=positiony<=7*screen_height/12:
                        positiony+=relmotion
                    elif positiony<5*screen_height/12:
                        relmotion=10
                        positiony+=relmotion
                    elif positiony>7*screen_height/12:
                        pressed_space=False
                        relmotion=-10
                        positiony=7*screen_height/12
                    imagedisplay(image2,(positionx,positiony))
                elif not(pressed_space):
                    if spritenumber>8:
                        spritenumber=0
                    imagedisplay(movement[spritenumber],(positionx,positiony))
                    spritenumber+=1
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        exit_game=True
                    elif event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_RIGHT:
                            pressed_right=True
                        elif event.key==pygame.K_LEFT:
                            pressed_left=True
                        elif event.key==pygame.K_SPACE:
                            pressed_space=True
                    elif event.type==pygame.KEYUP:
                        if event.key==pygame.K_RIGHT:
                            pressed_right=False
                            fps=15
                        elif event.key==pygame.K_LEFT:
                            pressed_left=False
                            fps=15
                if pressed_right:
                    if positionx+54<=screen_width:
                        positionx+=1
                        fps=20
                elif pressed_left:
                    if positionx>=0:
                        positionx-=1
                        fps=10
            elif game_over:
                textdisplay("GAME OVER",(screen_width/3,screen_height/3))
                textdisplay("Press Enter to retry",(screen_width/3,screen_height/2))
                textdisplay("Press Esc to Quit",(screen_width/3,2*screen_height/3))
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        exit_game=True
                    elif event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_RETURN:
                            xcord=0
                            score=0
                            spritenumber=0
                            fps=15
                            relmotion=-10
                            pos=random.randint(0,4)
                            objectx,objecty=650,7*screen_height/12
                            positionx,positiony=0,7*screen_height/12
                            game_over,gameplay=False,True
                            pressed_right,pressed_left,pressed_space=False,False,False
                        elif event.key==pygame.K_ESCAPE:
                            exit_game=True
            pygame.display.update()
            clock.tick(fps)
        pygame.quit()
game.gameloop()

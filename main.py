import pygame ,random

class Dice():
    def __init__(self,x,y,en,boy):
        self.imagies = [pygame.image.load('dice1.png'),
                        pygame.image.load('dice2.png'),
                        pygame.image.load('dice3.png'),
                        pygame.image.load('dice4.png'),
                        pygame.image.load('dice5.png'),
                        pygame.image.load('dice6.png')]
        self.image = self.imagies[0]
        self.x = x
        self.y = y
        self.en = en
        self.boy = boy
        self.rect = pygame.Rect(self.x,self.y,self.en,self.boy)
    
    def draw(self):
        ekran.blit(self.image,self.rect)

pygame.init()

w,h=300,200

ekran = pygame.display.set_mode((w,h))
pygame.display.set_caption('Dice Roll')
fps = pygame.time.Clock()

font = pygame.font.Font(None,80)

dice1 = Dice(x=60,y=95,en=64,boy=64)
dice2 = Dice(x=180,y=95,en=64,boy=64)

text_rool = font.render('Roll',True,(0,0,0))
rool_rect = pygame.Rect(100,20,100,48)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            if rool_rect.collidepoint(mouse_pos): 
                dice1.image = dice1.imagies[random.randint(0,5)]
                dice2.image = dice2.imagies[random.randint(0,5)]

    ekran.fill((255,255,255))
    ekran.blit(text_rool,(98,20))
    dice1.draw()
    dice2.draw()
    pygame.display.flip()
    fps.tick(60)
pygame.quit()
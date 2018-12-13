import pygame
import random



pygame.init()
pygame.display.set_caption("Car Dodging!")


class MainGame():
	def __init__(self):
		self.gameDisplay=pygame.display.set_mode((840,880))
		self.clock=pygame.time.Clock()
		
		self.img=pygame.image.load('./images/startscreen.png')
		self.img2=pygame.image.load('./images/gameover.png')
		self.img3=pygame.image.load('./images/gamepause.png')
		self.policeimg=pygame.image.load('./images/police.png')
		self.carimg1=pygame.image.load('./images/1.png')
		self.carimg2=pygame.image.load('./images/2.png')
		self.carimg3=pygame.image.load('./images/3.png')
		self.carimg4=pygame.image.load('./images/4.png')
		self.carimg5=pygame.image.load('./images/5.png')
		self.carimg6=pygame.image.load('./images/6.png')
		self.carimg7=pygame.image.load('./images/7.png')
		self.carimg8=pygame.image.load('./images/8.png')
		self.carimg9=pygame.image.load('./images/9.png')
		self.carimg10=pygame.image.load('./images/10.png')
		self.treeimg=pygame.image.load('./images/trees.png')
		self.i=0
		self.i1=5
		
		self.red=(200,0,0)
		self.white=(255,255,255)
		self.green=(0,128,0)
		self.light_green=(30,103,9)
		self.black=(42,42,42)
		
		self.lead_x=294
		self.lead_y=720
		self.obstacle_x=random.choice([160,294,456,590])
		self.obstacle_y=-160
		self.obstacle_x2=random.choice([160,294,456,590])
		self.obstacle_y2=-860
		self.obstacle_y_change=4
		self.vec_x=0
		self.obstacle_acc=0.25
		self.road_y=[0,195.5,391,586.5,782]
		self.tree_x=24
		self.tree_y=138
		self.tree_x2=759
		self.tree_y2=-340

		self.flag=0
		self.flag2=0
		self.flagbonus1=0
		self.flagb1=0
		self.bonus1=0
		self.flagbonus2=0
		self.flagb2=0
		self.bonus2=0
		
		self.pause=False
		self.gamestart=True
		self.gameover=False
		self.NotExit=True
		
		self.score=0
		self.highscore=0

		
	def GameLoop(self):
		while self.gamestart:
			self.start_screen()
		while self.NotExit:
			self.car_moment()
			while self.pause: 
				self.pause_screen()
			while self.gameover: 
				self.GameOver()


	def start_screen(self):
		self.high_score()
		self.gameDisplay.blit(self.img,(0,0))
		self.message_to_screen(str(self.highscore),self.white,105,-385,46)
		self.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_p:
					self.gamestart=False
			if event.type == pygame.QUIT:
				self.gamestart=False
				self.NotExit=False

	
	def high_score(self):
		file=open('highscore.txt','r')
		l=map(int,file.read().split())
		self.highscore=l[0]
		file.close()
		if self.score>self.highscore:
			with open('highscore.txt','w') as f:
				f.write(str(self.score))
			self.highscore=self.score

		
	def pause_screen(self):
		self.gameDisplay.blit(self.img3,(0,0))
		self.message_to_screen(str(self.score),self.white,105,-78,54)
		self.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_r:
					self.pause=False
				if event.key == pygame.K_q:
					self.gameover=True
					self.pause=False
			if event.type == pygame.QUIT:
				self.gameover=False
				self.gamepause=False
				self.NotExit=False


	def GameOver(self):
		self.high_score()
		self.gameDisplay.blit(self.img2,(0,0))
		self.message_to_screen(str(self.score),self.white,98,-85,54)
		self.message_to_screen(str(self.highscore),self.white,144,16,48)
		self.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.gameover=False
				self.NotExit=False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					self.gameover=False
					self.NotExit=False
				if event.key==pygame.K_p:
					self.lead_x=294
					self.lead_y=720
					self.obstacle_x=random.choice([160,294,456,590])
					self.obstacle_y=-160
					self.obstacle_x2=random.choice([160,294,456,590])
					self.obstacle_y2=-860
					self.obstacle_y_change=4
					self.vec_x=0
					self.obstacle_acc=0.25
					self.road_y=[0,195.5,391,586.5,782]
					self.tree_x=24
					self.tree_y=138
					self.tree_x2=759
					self.tree_y2=-340

					self.flag=0
					self.flag2=0
					self.flagbonus1=0
					self.flagb1=0
					self.bonus1=0
					self.flagbonus2=0
					self.flagb2=0
					self.bonus2=0
					
					self.pause=False
					self.gamestart=True
					self.gameover=False
					self.NotExit=True
					
					self.score=0
					self.highscore=0

					self.high_score()


	def Gameover_condition(self):
		if (self.obstacle_y>=self.lead_y-160 and self.obstacle_y<=self.lead_y+160) and (self.obstacle_x>=self.lead_x-90 and self.obstacle_x<=self.lead_x+90):
			self.gameover=True
		if (self.obstacle_y2>=self.lead_y-160 and self.obstacle_y2<=self.lead_y+160) and (self.obstacle_x2>=self.lead_x-90 and self.obstacle_x2<=self.lead_x+90):
			self.gameover=True

	
	def text_object(self,text,colour,size):
		self.font=pygame.font.SysFont(None, size)
		textSurface=self.font.render(text,True,colour)
		return textSurface,textSurface.get_rect()


	def message_to_screen(self,msg,colour,text_x,text_y,size):
		textSurf,textRect=self.text_object(msg,colour,size)
		textRect.center=(420+text_x),(440+text_y)
		self.gameDisplay.blit(textSurf,textRect)
		pygame.display.update()

	
	def car_moment(self):
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.type == pygame.QUIT:
					self.NotExit=False
				if event.key == pygame.K_LEFT:
					self.vec_x=-6
					self.flag=1
				if event.key == pygame.K_RIGHT:
					self.vec_x=6
					self.flag2=1
				if event.key == pygame.K_p:
					self.pause=True
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					self.vec_x=0
					self.flag=0
				if event.key == pygame.K_RIGHT:
					self.vec_x=0
					self.flag2=0

		if self.lead_x>132 and self.lead_x<618:
			self.lead_x+=self.vec_x

		if self.lead_x<=132 and self.flag2==1:
			self.lead_x+=self.vec_x

		if self.lead_x>=618 and self.flag==1:
			self.lead_x+=self.vec_x

		self.gameDisplay.fill(self.light_green)
		pygame.draw.rect(self.gameDisplay,self.black,[105,0,630,900])
		pygame.draw.rect(self.gameDisplay,self.white,[125,0,5,900])
		pygame.draw.rect(self.gameDisplay,self.white,[710,0,5,900])
		self.roadline()
		self.tree()
		self.gameDisplay.blit(self.policeimg,(self.lead_x,self.lead_y))
		self.Gameover_condition()
		self.bonus()
		self.bonus_1()
		self.obstacle()
		self.obstacle2()
		self.message_to_screen("Score : "+str(self.score),self.red,-360,-420,38)
		self.update()

	
	def bonus(self):
		if self.obstacle_y<560:
			self.flagb1=1
		if self.flagb1==1:
			if self.obstacle_y>=560 and self.obstacle_y<=880:
				if self.obstacle_x<=self.lead_x+130 and self.obstacle_x>=self.lead_x-130:
					self.flagbonus1=1
				else:
					self.flagbonus1=0
					self.flagb1=0
		if self.obstacle_y>880 and self.flagbonus1==1:
			self.bonus1=1
			self.flagbonus1=0

	
	def bonus_1(self):
		if self.obstacle_y2<560:
			self.flagb2=1
		if self.flagb2==1:
			if self.obstacle_y2>=560 and self.obstacle_y2<=880:
				if self.obstacle_x2<=self.lead_x+130 and self.obstacle_x2>=self.lead_x-130:
					self.flagbonus2=1
				else:
					self.flagbonus2=0
					self.flagb2=0
		if self.obstacle_y2>880 and self.flagbonus2==1:
			self.bonus2=1
			self.flagbonus2=0
	
	
	def obstacle(self):
		a=[self.carimg1,self.carimg2,self.carimg3,self.carimg4,self.carimg5,self.carimg6,self.carimg7,self.carimg8,self.carimg9,self.carimg10]
		self.gameDisplay.blit(a[self.i],(self.obstacle_x,self.obstacle_y))
		self.obstacle_y+=self.obstacle_y_change
		if self.obstacle_y>1240:
			self.obstacle_x=random.choice([160,294,456,590])
			self.obstacle_y=-160
			self.obstacle_y_change+=self.obstacle_acc
			self.score+=5
			if self.i>=4:self.i=0
			else:self.i+=1

		if self.bonus1==1:
			self.score+=2
			self.bonus1=0
		if self.bonus2==1:
			self.score+=2
			self.bonus2=0


	def obstacle2(self):
		a=[self.carimg1,self.carimg2,self.carimg3,self.carimg4,self.carimg5,self.carimg6,self.carimg7,self.carimg8,self.carimg9,self.carimg10]
		self.gameDisplay.blit(a[self.i1],(self.obstacle_x2,self.obstacle_y2))
		self.obstacle_y2+=self.obstacle_y_change
		if self.obstacle_y2>1240:
			self.obstacle_x2=random.choice([160,294,456,590])
			self.obstacle_y2=-160
			self.obstacle_y_change+=self.obstacle_acc	
			self.score+=5
			if self.i1>=9:self.i1=5
			else:self.i1+=1


	def roadline(self):
		for i in range(5):
			pygame.draw.rect(self.gameDisplay,self.white,[414,self.road_y[i],12,98])
			self.road_y[i]+=self.obstacle_y_change
			if self.road_y[0]>=98:
				self.road_y[-1]
				self.road_y.insert(0,int(self.road_y[0]-195.5))
				self.road_y[1]-=self.obstacle_y_change

	
	def tree(self):
		self.gameDisplay.blit(self.treeimg,(self.tree_x,self.tree_y))
		self.gameDisplay.blit(self.treeimg,(self.tree_x2,self.tree_y2))
		self.tree_y+=self.obstacle_y_change
		self.tree_y2+=self.obstacle_y_change
		if self.tree_y>=880:
			self.tree_y=-605
		if self.tree_y2>=880:
			self.tree_y2=-605

	
	def update(self):
		pygame.display.update()
		self.clock.tick(60)




game=MainGame()
game.GameLoop()

WIDTH = 700
HEIGHT = 900
X1=10
X2 =20
y=40
dy=65
dx=10

class alien:
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h

    def first_display_alien(self,canevas):
        self.alien_id = canevas.create_rectangle(
        self.x,
        self.y,
        self.x + self.h,
        self.y + self.w,
        fill="green"
        )
        return self.alien_id

    def mouvement_alien(self):
    
        if self.dx == abs(self.dx) :
            if self.X2 >= self.WIDTH:
                self.dx = -10
                self.y = self.y+10
                self.dy = self.dy+10
        if self.dx == -abs(self.dx) :
            if self.X1 <= 0:
                self.dx = 10
                self.y = self.y+10
                self.dy = self.dy+10

        self.X1=self.X1+self.dx
        self.X2=self.X2+self.dx
        self.Canevas.coords(self.alien,self.X1,self.y,self.X2,self.dy)
        self.w.after(100,self.mouvement_alien)

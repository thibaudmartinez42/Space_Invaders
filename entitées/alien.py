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
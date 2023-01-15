class Player:
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h

    def first_display_player(self,canevas):
        self.player_id = canevas.create_rectangle(
        self.x,
        self.y,
        self.x + self.h,
        self.y + self.w,
        fill="black"
        )
        return self.player_id
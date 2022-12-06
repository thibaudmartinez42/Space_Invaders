from .player import Player
from .alien import alien

class world:
    player_coords_x=250
    player_coords_y=700
    player_height=200
    player_width=100
    alien_coords_x=10
    alien_coords_y=40
    alien_height=30
    alien_width=15


    def __init__(self,canevas):
        self.init_world(canevas)

    def init_world(self,canevas):
        p = Player(
            self.player_coords_x,
            self.player_coords_y,
            self.player_width,
            self.player_height
        )
        a = alien(
            self.alien_coords_x,
            self.alien_coords_y,
            self.alien_width,
            self.alien_height
        )
        p.first_display_player(canevas)
        self.p=p
        a.first_display_alien(canevas)
        self.a=a

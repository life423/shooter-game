SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600
FPS           = 60
TITLE         = "Shooter"

# Colors
BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
CYAN  = (0,   255, 255)
YELLOW = (255, 255, 0)

# Player
PLAYER_SPEED    = 4        # thrust force per frame
ROTATE_SPEED    = 4        # degrees per frame
FRICTION        = 0.97     # velocity multiplier each frame (1.0 = no friction)
PLAYER_SIZE     = 18       # half-height of triangle, px

# Bullet
BULLET_SPEED    = 10       # px per frame, added on top of player velocity
BULLET_LIFETIME = 60       # frames before bullet is removed
BULLET_RADIUS   = 3

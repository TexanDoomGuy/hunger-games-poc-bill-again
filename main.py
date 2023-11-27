@namespace
class SpriteKind:
    Player_2 = SpriteKind.create()
    Projectile_2 = SpriteKind.create()
    Arrow_1 = SpriteKind.create()
    Arrow_2 = SpriteKind.create()
    Health_1 = SpriteKind.create()
    sword = SpriteKind.create()
"""

Todo: Make health pickups

"""

def on_on_overlap(sprite, otherSprite):
    info.player2.change_life_by(-1)
    sprites.destroy(Arrow)
    sprites.destroy(sword2)
sprites.on_overlap(SpriteKind.Player_2, SpriteKind.projectile, on_on_overlap)

def on_player2_button_a_pressed():
    global Arrow
    Arrow = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . 
                    . . . . . . . . 
                    . c c b b b b . 
                    f 3 d d 5 1 5 b 
                    f 3 d d 5 1 5 b 
                    . c c b b b b . 
                    . . . . . . . . 
                    . . . . . . . .
        """),
        Player2,
        p2_a,
        0)
    Arrow.x += p2_b
controller.player2.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player2_button_a_pressed)

def Send_Player_2_to_the_shadow_realm():
    for index in range(15):
        Player2.x += 1e+21
def Send_Player_1_to_the_shadow_realm2():
    for index2 in range(15):
        Player1.x += 1e+21

def on_on_overlap2(sprite2, otherSprite2):
    info.player1.change_life_by(-1)
    sprites.destroy(Arrow)
    sprites.destroy(sword2)
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_on_overlap2)

def on_player2_button_right_pressed():
    global p2_a, p2_b
    p2_a = 50
    p2_b = 15
controller.player2.on_button_event(ControllerButton.RIGHT,
    ControllerButtonEvent.PRESSED,
    on_player2_button_right_pressed)

def on_player2_button_left_pressed():
    global p2_a, p2_b
    p2_a = -50
    p2_b = -15
controller.player2.on_button_event(ControllerButton.LEFT,
    ControllerButtonEvent.PRESSED,
    on_player2_button_left_pressed)

def on_player1_button_right_pressed():
    global P1_a, P1_b
    P1_a = 50
    P1_b = 15
controller.player1.on_button_event(ControllerButton.RIGHT,
    ControllerButtonEvent.PRESSED,
    on_player1_button_right_pressed)

def on_player1_button_a_pressed():
    global Arrow
    Arrow = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . 
                    . . . . . . . . 
                    . c c b b b b . 
                    f 3 d d 5 1 5 b 
                    f 3 d d 5 1 5 b 
                    . c c b b b b . 
                    . . . . . . . . 
                    . . . . . . . .
        """),
        Player1,
        P1_a,
        0)
    Arrow.x += P1_b
controller.player1.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player1_button_a_pressed)

def on_player1_life_zero():
    sprites.destroy(Pointer_1)
    Send_Player_1_to_the_shadow_realm2()
info.player1.on_life_zero(on_player1_life_zero)

def on_player2_life_zero():
    sprites.destroy(Pointer_2)
    Send_Player_2_to_the_shadow_realm()
info.player2.on_life_zero(on_player2_life_zero)

def on_player2_connected():
    controller.player2.move_sprite(Player2)
controller.player2.on_event(ControllerEvent.CONNECTED, on_player2_connected)

def on_player1_button_b_pressed():
    global sword2
    if P1_b > 0:
        sword2 = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . f f f 
                            . . . . . . . . . . . . f 9 9 f 
                            . . . . . . . . . . . f 9 6 9 f 
                            . . . . . . . . . . f 9 6 9 f . 
                            . . . . . . . . . f 9 6 9 f . . 
                            . . . . . . . . f 9 6 9 f . . . 
                            . . f f . . . f 9 6 9 f . . . . 
                            . . f 9 f . f 9 6 9 f . . . . . 
                            . . . f 9 f 9 6 9 f . . . . . . 
                            . . . f 9 9 f 9 f . . . . . . . 
                            . . . . f 9 9 f . . . . . . . . 
                            . . . e e f 9 9 f . . . . . . . 
                            . . e e e . f f 9 f . . . . . . 
                            f f e e . . . . f f . . . . . . 
                            f 9 f . . . . . . . . . . . . . 
                            f f f . . . . . . . . . . . . .
            """),
            Player1,
            P1_b * 5,
            0)
    else:
        sword2 = sprites.create_projectile_from_sprite(img("""
                f f f . . . . . . . . . . . . . 
                            f 9 9 f . . . . . . . . . . . . 
                            f 9 6 9 f . . . . . . . . . . . 
                            . f 9 6 9 f . . . . . . . . . . 
                            . . f 9 6 9 f . . . . . . . . . 
                            . . . f 9 6 9 f . . . . . . . . 
                            . . . . f 9 6 9 f . . . f f . . 
                            . . . . . f 9 6 9 f . f 9 f . . 
                            . . . . . . f 9 6 9 f 9 f . . . 
                            . . . . . . . f 9 f 9 9 f . . . 
                            . . . . . . . . f 9 9 f . . . . 
                            . . . . . . . f 9 9 f e e . . . 
                            . . . . . . f 9 f f . e e e . . 
                            . . . . . . f f . . . . e e f f 
                            . . . . . . . . . . . . . f 9 f 
                            . . . . . . . . . . . . . f f f
            """),
            Player1,
            P1_b * 5,
            0)
    sword2.x += P1_b
    pause(100)
    sprites.destroy(sword2)
controller.player1.on_button_event(ControllerButton.B,
    ControllerButtonEvent.PRESSED,
    on_player1_button_b_pressed)

def on_player1_connected():
    controller.player1.move_sprite(Player1)
controller.player1.on_event(ControllerEvent.CONNECTED, on_player1_connected)

def on_player1_button_left_pressed():
    global P1_a, P1_b
    P1_a = -50
    P1_b = -15
controller.player1.on_button_event(ControllerButton.LEFT,
    ControllerButtonEvent.PRESSED,
    on_player1_button_left_pressed)

P1_a = 0
P1_b = 0
p2_a = 0
p2_b = 0
sword2: Sprite = None
Pointer_2: Sprite = None
Pointer_1: Sprite = None
Player2: Sprite = None
Player1: Sprite = None
Arrow: Sprite = None
scene.set_background_color(0)
Arrow = sprites.create(img("""
        . . . . . . . . 
            . . . . . . . . 
            . c c b b b b . 
            f 3 d d 5 1 5 b 
            f 3 d d 5 1 5 b 
            . c c b b b b . 
            . . . . . . . . 
            . . . . . . . .
    """),
    SpriteKind.projectile)
Arrow_22 = sprites.create(img("""
        . . . . . . . . 
            . . . . . . . . 
            . c c b b b b . 
            f 3 d d 5 1 5 b 
            f 3 d d 5 1 5 b 
            . c c b b b b . 
            . . . . . . . . 
            . . . . . . . .
    """),
    SpriteKind.Projectile_2)
Player1 = sprites.create(img("""
        . . . . . . f f f f . . . . . . 
            . . . . f f f 2 2 f f f . . . . 
            . . . f f f 2 2 2 2 f f f . . . 
            . . f f f e e e e e e f f f . . 
            . . f f e 2 2 2 2 2 2 e e f . . 
            . . f e 2 f f f f f f 2 e f . . 
            . . f f f f e e e e f f f f . . 
            . f f e f b f 4 4 f b f e f f . 
            . f e e 4 1 f d d f 1 4 e e f . 
            . . f e e d d d d d d e e f . . 
            . . . f e e 4 4 4 4 e e f . . . 
            . . e 4 f 2 2 2 2 2 2 f 4 e . . 
            . . 4 d f 2 2 2 2 2 2 f d 4 . . 
            . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
            . . . . . f f f f f f . . . . . 
            . . . . . f f . . f f . . . . .
    """),
    SpriteKind.player)
Player2 = sprites.create(img("""
        . . . . . f f 4 4 f f . . . . . 
            . . . . f 5 4 5 5 4 5 f . . . . 
            . . . f e 4 5 5 5 5 4 e f . . . 
            . . f b 3 e 4 4 4 4 e 3 b f . . 
            . . f 3 3 3 3 3 3 3 3 3 3 f . . 
            . f 3 3 e b 3 e e 3 b e 3 3 f . 
            . f 3 3 f f e e e e f f 3 3 f . 
            . f b b f b f e e f b f b b f . 
            . f b b e 1 f 4 4 f 1 e b b f . 
            f f b b f 4 4 4 4 4 4 f b b f f 
            f b b f f f e e e e f f f b b f 
            . f e e f b d d d d b f e e f . 
            . . e 4 c d d d d d d c 4 e . . 
            . . e f b d b d b d b b f e . . 
            . . . f f 1 d 1 d 1 d f f . . . 
            . . . . . f f b b f f . . . . .
    """),
    SpriteKind.Player_2)
sprites.destroy(Arrow)
sprites.destroy(Arrow_22)
Pointer_1 = sprites.create(img("""
        . . 7 . . 
            . . 7 . . 
            7 7 7 7 7 
            . . 7 . . 
            . . 7 . .
    """),
    SpriteKind.Arrow_1)
Pointer_2 = sprites.create(img("""
        . . 7 . . 
            . . 7 . . 
            7 7 7 7 7 
            . . 7 . . 
            . . 7 . .
    """),
    SpriteKind.Arrow_2)
info.player2.set_life(3)
info.player1.set_life(3)
sword2 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.sword)
p2_b = 99999999
p2_a = 99999990
P1_b = 9999999
P1_a = 999999999

def on_forever():
    Pointer_1.set_position(Player1.x + P1_b, Player1.y)
forever(on_forever)

def on_forever2():
    Pointer_2.set_position(Player2.x + p2_b, Player2.y)
forever(on_forever2)

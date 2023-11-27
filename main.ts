namespace SpriteKind {
    export const Player_2 = SpriteKind.create()
    export const Projectile_2 = SpriteKind.create()
    export const Arrow_1 = SpriteKind.create()
    export const Arrow_2 = SpriteKind.create()
    export const Health_1 = SpriteKind.create()
    export const sword = SpriteKind.create()
}
// Todo: Make health pickups
sprites.onOverlap(SpriteKind.Player_2, SpriteKind.Projectile, function (sprite, otherSprite) {
    info.player2.changeLifeBy(-1)
    sprites.destroy(Arrow)
    sprites.destroy(sword2)
})
controller.player2.onButtonEvent(ControllerButton.A, ControllerButtonEvent.Pressed, function () {
    Arrow = sprites.createProjectileFromSprite(img`
        . . . . . . . . 
        . . . . . . . . 
        . c c b b b b . 
        f 3 d d 5 1 5 b 
        f 3 d d 5 1 5 b 
        . c c b b b b . 
        . . . . . . . . 
        . . . . . . . . 
        `, Player2, p2_a, 0)
    Arrow.x += p2_b
})
function Send_Player_2_to_the_shadow_realm () {
    for (let index = 0; index < 15; index++) {
        Player2.x += 1e+21
    }
}
function Send_Player_1_to_the_shadow_realm2 () {
    for (let index = 0; index < 15; index++) {
        Player1.x += 1e+21
    }
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Projectile, function (sprite2, otherSprite2) {
    info.player1.changeLifeBy(-1)
    sprites.destroy(Arrow)
    sprites.destroy(sword2)
})
controller.player2.onButtonEvent(ControllerButton.Right, ControllerButtonEvent.Pressed, function () {
    p2_a = 50
    p2_b = 15
})
controller.player2.onButtonEvent(ControllerButton.Left, ControllerButtonEvent.Pressed, function () {
    p2_a = -50
    p2_b = -15
})
controller.player1.onButtonEvent(ControllerButton.Right, ControllerButtonEvent.Pressed, function () {
    P1_a = 50
    P1_b = 15
})
controller.player1.onButtonEvent(ControllerButton.A, ControllerButtonEvent.Pressed, function () {
    Arrow = sprites.createProjectileFromSprite(img`
        . . . . . . . . 
        . . . . . . . . 
        . c c b b b b . 
        f 3 d d 5 1 5 b 
        f 3 d d 5 1 5 b 
        . c c b b b b . 
        . . . . . . . . 
        . . . . . . . . 
        `, Player1, P1_a, 0)
    Arrow.x += P1_b
})
info.player1.onLifeZero(function () {
    sprites.destroy(Pointer_1)
    Send_Player_1_to_the_shadow_realm2()
})
info.player2.onLifeZero(function () {
    sprites.destroy(Pointer_2)
    Send_Player_2_to_the_shadow_realm()
})
controller.player2.onEvent(ControllerEvent.Connected, function () {
    controller.player2.moveSprite(Player2)
})
controller.player1.onButtonEvent(ControllerButton.B, ControllerButtonEvent.Pressed, function () {
    if (P1_b > 0) {
        sword2 = sprites.createProjectileFromSprite(img`
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
            `, Player1, P1_b * 5, 0)
    } else {
        sword2 = sprites.createProjectileFromSprite(img`
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
            `, Player1, P1_b * 5, 0)
    }
    sword2.x += P1_b
    pause(100)
    sprites.destroy(sword2)
})
controller.player1.onEvent(ControllerEvent.Connected, function () {
    controller.player1.moveSprite(Player1)
})
controller.player1.onButtonEvent(ControllerButton.Left, ControllerButtonEvent.Pressed, function () {
    P1_a = -50
    P1_b = -15
})
let P1_a = 0
let P1_b = 0
let p2_a = 0
let p2_b = 0
let sword2: Sprite = null
let Pointer_2: Sprite = null
let Pointer_1: Sprite = null
let Player2: Sprite = null
let Player1: Sprite = null
let Arrow: Sprite = null
scene.setBackgroundColor(0)
Arrow = sprites.create(img`
    . . . . . . . . 
    . . . . . . . . 
    . c c b b b b . 
    f 3 d d 5 1 5 b 
    f 3 d d 5 1 5 b 
    . c c b b b b . 
    . . . . . . . . 
    . . . . . . . . 
    `, SpriteKind.Projectile)
let Arrow_22 = sprites.create(img`
    . . . . . . . . 
    . . . . . . . . 
    . c c b b b b . 
    f 3 d d 5 1 5 b 
    f 3 d d 5 1 5 b 
    . c c b b b b . 
    . . . . . . . . 
    . . . . . . . . 
    `, SpriteKind.Projectile_2)
Player1 = sprites.create(img`
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
    `, SpriteKind.Player)
Player2 = sprites.create(img`
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
    `, SpriteKind.Player_2)
sprites.destroy(Arrow)
sprites.destroy(Arrow_22)
Pointer_1 = sprites.create(img`
    . . 7 . . 
    . . 7 . . 
    7 7 7 7 7 
    . . 7 . . 
    . . 7 . . 
    `, SpriteKind.Arrow_1)
Pointer_2 = sprites.create(img`
    . . 7 . . 
    . . 7 . . 
    7 7 7 7 7 
    . . 7 . . 
    . . 7 . . 
    `, SpriteKind.Arrow_2)
info.player2.setLife(3)
info.player1.setLife(3)
sword2 = sprites.create(img`
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
    `, SpriteKind.sword)
p2_b = 99999999
p2_a = 99999990
P1_b = 9999999
P1_a = 999999999
forever(function () {
    Pointer_2.setPosition(Player2.x + p2_b, Player2.y)
})
forever(function () {
    Pointer_1.setPosition(Player1.x + P1_b, Player1.y)
})

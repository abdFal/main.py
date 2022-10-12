import pygame
## init
pygame.init()
# variable running game
isRun = True

window_lebar = 400
window_panjang = 400
window = pygame.display.set_mode((window_lebar,window_panjang))

# object game
x = 250
y = 250

# ukuran
panjang = 15
lebar = 15

speed = 5

while isRun:
    pygame.time.delay(10)

    # user input, database input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
    
    if keys[pygame.K_RIGHT] and x < window_lebar-lebar:
        x += speed

    if keys[pygame.K_DOWN] and y < window_panjang-panjang:
        y += speed

    if keys[pygame.K_UP] and y > 0:
        y -= speed

    # game dynamic
    
    # update asset
    window.fill((153,51,255))
    pygame.draw.rect(window,(0,255,255,),(x,y,lebar,panjang))
    # render ke display
    pygame.display.update()

pygame.quit()
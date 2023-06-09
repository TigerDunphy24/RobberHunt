import pygame
import random
import os
import time

# Initialize pygame
pygame.init()

# Initialize the mixer module
pygame.mixer.init()

# Set the window size
window_size = (800, 530)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the window title
pygame.display.set_caption("Robber Hunt")

# Load the player image
player_image = pygame.image.load("player.png")

# Scale the player image down to 50% of its original size
player_image = pygame.transform.scale(player_image, (player_image.get_width() // 3, player_image.get_height() // 3))
player_rect = player_image.get_rect()

# Initialize pygame
pygame.init()

# Initialize the mixer module
pygame.mixer.init()

# Set the window size
window_size = (800, 530)

# Load the player image
player_image = pygame.image.load("player.png")

# Scale the player image down to 50% of its original size
player_image = pygame.transform.scale(player_image, (player_image.get_width() // 3, player_image.get_height() // 3))
player_rect = player_image.get_rect()

# Load the player image
eater_image = pygame.image.load("eater.png")

# Scale the player image down to 50% of its original size
eater_image = pygame.transform.scale(eater_image, (eater_image.get_width() // 2, eater_image.get_height() // 2))
eater_rect = eater_image.get_rect()

# Generate a random position for the boost
eater_rect.x = random.randint(0, window_size[0])
eater_rect.y = random.randint(0, window_size[1])

eater_speed = 2

# Load the player image
Freeze_image = pygame.image.load("Freeze.png")

# Scale the player image down to 50% of its original size
Freeze_image = pygame.transform.scale(Freeze_image, (Freeze_image.get_width() // 2, Freeze_image.get_height() // 2))
Freeze_rect = Freeze_image.get_rect()

# Generate a random position for the boost
Freeze_rect.x = random.randint(0, window_size[0])
Freeze_rect.y = random.randint(0, window_size[1])

# Load the player image
doubler_image = pygame.image.load("doubler.png")

# Scale the player image down to 50% of its original size
doubler_image = pygame.transform.scale(doubler_image, (eater_image.get_width() // 1, doubler_image.get_height() // 2))
doubler_rect = doubler_image.get_rect()

# Load the player image
shield_image = pygame.image.load("shield.png")

# Scale the player image down to 50% of its original size
shield_image = pygame.transform.scale(shield_image, (shield_image.get_width() / 2.5, shield_image.get_height() / 2.5))
shield_rect = shield_image.get_rect()

# Generate a random position for the boost
shield_rect.x = random.randint(0, window_size[0])
shield_rect.y = random.randint(0, window_size[1])

# Generate a random position for the boost
doubler_rect.x = random.randint(0, window_size[0])
doubler_rect.y = random.randint(0, window_size[1])
doubler_speed = 1

player_boost_image = pygame.image.load("player_boost.png")
# Scale the player image down to 50% of its original size
player_boost_image = pygame.transform.scale(player_boost_image, (player_boost_image.get_width() // 3, player_boost_image.get_height() // 3))
player_boost_rect = player_boost_image.get_rect()

# Load the enemy image
enemy_image = pygame.image.load("enemy.png")

# Scale the enemy image down to 50% of its original size
enemy_image = pygame.transform.scale(enemy_image, (enemy_image.get_width() // 3, enemy_image.get_height() // 3))
enemy_rect = enemy_image.get_rect()

# Load the boost image
boost_image = pygame.image.load("boost.png")

# Scale the boost image down to 50% of its original size
boost_image = pygame.transform.scale(boost_image, (boost_image.get_width() // 3, boost_image.get_height() // 3))
boost_rect = boost_image.get_rect()

# Set the boost's starting position
boost_rect = boost_image.get_rect()
boost_rect.x = 200
boost_rect.y = 200

# Load the boost image
slower_image = pygame.image.load("slower.png")

# Scale the boost image down to 50% of its original size
slower_image = pygame.transform.scale(slower_image, (boost_image.get_width() // 1, slower_image.get_height() // 3))
slower_rect = slower_image.get_rect()

# Set the boost's starting position
slower_rect = slower_image.get_rect()
slower_rect.x = 100
slower_rect.y = 100


# Set the players's starting position
player_rect = player_image.get_rect()
player_rect.x = 0
player_rect.y = 368

# Load the background image
background_image = pygame.image.load("background.png")

# Scale the image up to 200% of its original size
background_image = pygame.transform.scale(background_image, (background_image.get_width() * 2, background_image.get_height() * 2))

# Create a rectangle object for the background image
background_rect = background_image.get_rect()

# Set the position of the background image
background_rect.x = 0
background_rect.y = 0

# Load the background image
background2_image = pygame.image.load("background2.png")

# Scale the image up to 200% of its original size
background2_image = pygame.transform.scale(background2_image, (background2_image.get_width() * 2, background2_image.get_height() * 2))

# Create a rectangle object for the background image
background2_rect = background2_image.get_rect()

# Set the position of the background image
background2_rect.x = 0
background2_rect.y = 0


# Load the player image
bomb_image = pygame.image.load("bomb.png")

# Scale the player image down to 50% of its original size
bomb_image = pygame.transform.scale(bomb_image, (bomb_image.get_width() / 1.8, bomb_image.get_height() / 1.8 ))

bomb_rect = bomb_image.get_rect()
# Generate a random position for the boost
bomb_rect.x = random.randint(0, window_size[0])
bomb_rect.y = random.randint(0, window_size[1])

# Load the coin image
coin_image = pygame.image.load("coin.png")

# Scale the coin image down to 50% of its original size
coin_image = pygame.transform.scale(coin_image, (coin_image.get_width() // 2, coin_image.get_height() // 2))

score_multiplier = 1

# Create a list to store the coin rectangles
coins = []

# Set the number of coins to spawn
num_coins = 10

# Spawn the coins
for i in range(num_coins):
    # Create a rectangle object for the coin image
    coin_rect = coin_image.get_rect()
    
    # Generate a random position for the coin
    coin_rect.x = random.randrange(0, window_size[0])
    coin_rect.y = random.randrange(0, window_size[1])
    
    # Add the coin rectangle to the list
    coins.append(coin_rect)

# Create a list to store the coin rectangles
bomb = []

# Set the number of coins to spawn
num_bombs = 5

# Spawn the bomb
for i in range(num_bombs):
    # Create a rectangle object for the coin image
    bomb_rect = bomb_image.get_rect()
    
    # Generate a random position for the coin
    bomb_rect.x = random.randrange(0, window_size[0])
    bomb_rect.y = random.randrange(0, window_size[1])
    
    # Add the coin rectangle to the list
    bomb.append(bomb_rect)


# Load the main menu background image
menu_background_image = pygame.image.load("menu_background.png")

# Create a rectangle object for the background image
menu_background_rect = menu_background_image.get_rect()

# Scale the image up
menu_background_image = pygame.transform.scale(menu_background_image, (menu_background_image.get_width() * 2, menu_background_image.get_height() * 2))

# Set the player's starting score to 0
score = 0

# Set the high score to 0
high_score = 0

# Set the player's starting speed
player_speed = 5

# Set the boost speed multiplier
boost_multiplier = 2

# Set the boost duration (in number of game loop iterations)
boost_duration = 60

# Set the boost expiration counter to 0
boost_expiration = 0

# Set the shield duration (in number of game loop iterations)
shield_duration = 10 * 60  # 10 seconds * 60 frames per second

# Set the shield expiration counter to 0
shield_expiration = 0

freeze_time = 0
freeze_duration = 2

# Set the enemy's speed
enemy_speed = 2

# Set the delay time (in milliseconds)
delay_time = 20

# Set the font
font = pygame.font.Font(None, 36)

# Dateipfad und Name der Datei, in der der Highscore gespeichert wird
HIGHSCORE_FILE = "highscore.py"

# Funktion, um den aktuellen Highscore zu laden
def load_highscore():
    if os.path.exists(HIGHSCORE_FILE):
        with open(HIGHSCORE_FILE, "r") as f:
            highscore = int(f.read())
    else:
        highscore = 0
    return highscore

def save_highscore(new_highscore):
    with open('highscore.txt', 'r') as f:
        highscore = int(f.read())

    if new_highscore > highscore:
        with open('highscore.txt', 'w') as f:
            f.write(str(new_highscore))

# Beispielcode zum Aktualisieren des Highscores
def update_highscore(new_score):
    highscore = load_highscore()
    if new_score > highscore:
        highscore = new_score
        save_highscore(highscore)
        print("Neuer Highscore: {}".format(highscore))
    else:
        print("Aktueller Highscore: {}".format(highscore))



def show_main_menu():
    # Display the main menu background image
    screen.blit(menu_background_image, menu_background_rect)
    pygame.display.flip()

    # Set the menu loop flag
    menu_loop = True

    # Run the menu loop
    while menu_loop:
        # Handle events¦¦¦¦¦¦¦¦¦
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_loop = False
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                # Quit the game
                    menu_loop = False
                    running = False
                elif event.key == pygame.K_SPACE:
                    # Start the game
                    menu_loop = False



# Run the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if player_rect.colliderect(eater_rect):
        score_multiplier = 0.5
    
    if player_rect.colliderect(doubler_rect):
        score_multiplier = 2
    
    # Check if the player is colliding with any of the coins
    for coin in coins:
        if player_rect.colliderect(coin):
            # Increment the player's score
            score += 1 * score_multiplier

            enemy_speed += 0.02

            # Remove the coin from the list
            coins.remove(coin)

            # Spawn a new coin
            coin_rect = coin_image.get_rect()
            coin_rect.x = random.randrange(0, window_size[0])
            coin_rect.y = random.randrange(0, window_size[1])
            coins.append(coin_rect)

    # Check if the player's score is greater than the high score
    if score > high_score:
        # Update the high score
        high_score = score

    if score > 50:
        background_image = background2_image
    
    # Render the high score text
    high_score_text = font.render(f"High Score: {high_score}", True, (255, 255, 255))
    
    if player_rect.colliderect(boost_rect):
        player_image = player_boost_image
        boost_expiration = boost_duration

         # Check if the player and shield are colliding
    if shield_rect.colliderect(player_rect):
        shield_expiration = shield_duration
        # Generate a new random position for the shield
        shield_rect.x = random.randint(0, window_size[0])
        shield_rect.y = random.randint(0, window_size[1])

    if player_rect.colliderect(Freeze_rect):
        # Generate a new random position for the shield
        Freeze_rect.x = random.randint(0, window_size[0])
        Freeze_rect.y = random.randint(0, window_size[1])
        enemy_speed = 0
        freeze_time = pygame.time.get_ticks()  # Aktuelle Zeit in Millisekunden speichern

    current_time = pygame.time.get_ticks()  # Aktuelle Zeit in Millisekunden abrufen
    elapsed_time = (current_time - freeze_time) / 1000  # Vergangene Zeit in Sekunden umrechnen

    if elapsed_time >= freeze_duration:
        enemy_speed = 2

    # Check if the shield is active
    if shield_expiration > 0:
        shield_expiration -= 1

       # Check if the player and enemy are colliding
    if player_rect.colliderect(enemy_rect):
        if shield_expiration <= 0:  # Check if shield is not active
            # Display the "game over" message
            game_over_text = font.render("Game Over !", True, (255, 255, 255))
            screen.blit(game_over_text, (325, 200))
            pygame.display.update()

            enemy_speed = 2
        
            # Display the "Press r to play again, Press l to go to the main menu " message
            game_over_text = font.render("Press r to play again, Press e to go to the main menu ", True, (255, 255, 255))
            screen.blit(game_over_text, (132, 300))
            pygame.display.update()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                # Play again if the player presses 'r'
                if event.key == pygame.K_r:
                   
                   # Reset the player's position
                    player_rect.x = 0
                    player_rect.y = 368
                    # Reset the enemy's position
                    enemy_rect.x = 736
                    enemy_rect.y = 0
                    boost_rect.x = random.randint(0,window_size[0])
                    boost_rect.x = random.randint(0,window_size[1])
                    # Reset the coin's position
                    coin_rect.x = 400
                    coin_rect.y = 200
                    # Generate a random position for the boost
                    bomb_rect.x = random.randint(0, window_size[0])
                    bomb_rect.y = random.randint(0, window_size[1])
                   # Generate a random position for the eater
                    eater_rect.x = random.randint(0, window_size[0])
                    eater_rect.y = random.randint(0, window_size[1])
                    # Generate a random position for the eater
                    slower_rect.x = random.randint(0, window_size[0])
                    slower_rect.y = random.randint(0, window_size[1])
                    
                    shield_rect.x = random.randint(0, window_size[0])
                    shield_rect.y = random.randint(0, window_size[1])

                    Freeze_rect.x = random.randint(0, window_size[0])
                    Freeze_rect.y = random.randint(0, window_size[1])


                    score_multiplier = 1

                    # Reset the player's score
                    score = 0
                    # Reset the player's speed
                    player_speed = 5
                    # Reset the boost expiration counter
                    boost_expiration = 0
                    
                # Quit the game if the player presses 'l'
                elif event.key == pygame.K_e:
                    running = False
                    show_main_menu()


    # Check if the player and bomb are colliding
    elif player_rect.colliderect(bomb_rect):
        if shield_expiration <= 0:  # Check if shield is not active
            # Display the "game over" message
            game_over_text = font.render("Game Over !", True, (255, 255, 255))
            screen.blit(game_over_text, (325, 200))
            pygame.display.update()

            enemy_speed = 2
        
            # Display the "Press r to play again, Press l to go to the main menu " message
            game_over_text = font.render("Press r to play again, Press e to go to the main menu ", True, (255, 255, 255))
            screen.blit(game_over_text, (132, 300))
            pygame.display.update() 

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                # Play again if the player presses 'r'
                if event.key == pygame.K_r:
                    # Reset the player's position
                    player_rect.x = 0
                    player_rect.y = 368
                    # Reset the enemy's position
                    enemy_rect.x = 736
                    enemy_rect.y = 0
                    boost_rect.x = random.randint(0,window_size[0])
                    boost_rect.x = random.randint(0,window_size[1])
                    # Reset the coin's position
                    coin_rect.x = 400
                    coin_rect.y = 200
                    # Generate a random position for the boost
                    bomb_rect.x = random.randint(0, window_size[0])
                    bomb_rect.y = random.randint(0, window_size[1])
                   # Generate a random position for the eater
                    eater_rect.x = random.randint(0, window_size[0])
                    eater_rect.y = random.randint(0, window_size[1])
                    # Generate a random position for the eater
                    slower_rect.x = random.randint(0, window_size[0])
                    slower_rect.y = random.randint(0, window_size[1])
                    
                    shield_rect.x = random.randint(0, window_size[0])
                    shield_rect.y = random.randint(0, window_size[1])

                    Freeze_rect.x = random.randint(0, window_size[0])
                    Freeze_rect.y = random.randint(0, window_size[1])

                    score_multiplier = 1

                    # Reset the player's score
                    score = 0
                    # Reset the player's speed
                    player_speed = 5
                    # Reset the boost expiration counter
                    boost_expiration = 0
                # Quit the game if the player presses 'l'
                elif event.key == pygame.K_e:
                    running = False
                    show_main_menu()
    else:
        # Check for key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if player_rect.x - player_speed >= 0:
                player_rect.x -= player_speed * 1.2
        if keys[pygame.K_RIGHT]:
            if player_rect.x + player_speed <= 768:
                player_rect.x += player_speed * 1.2
        if keys[pygame.K_UP]:
            if player_rect.y - player_speed >= 0:
                player_rect.y -= player_speed
        if keys[pygame.K_DOWN]:
            if player_rect.y + player_speed <= 498:
                player_rect.y += player_speed

        # Check if the player is colliding with the boost
        if boost_rect.colliderect(player_rect):
            player_image = player_boost_image
            # Increase the player's speed
            player_speed *= boost_multiplier
            # Set the boost expiration counter
            boost_expiration = boost_duration
            # Remove the boost from the screen
            boost_rect.x = -100
            boost_rect.y = -100
            # Generate a random position for the boost
            boost_rect.x = random.randint(0, window_size[0])
            boost_rect.y = random.randint(0, window_size[1])

        # Check if the player is colliding with the boost
        if slower_rect.colliderect(player_rect):
            # Increase the player's speed
            player_speed /= 2
            # Set the boost expiration counter
            boost_expiration = boost_duration
            # Remove the boost from the screen
            slower_rect.x = -100
            slower_rect.y = -100
            # Generate a random position for the boost
            slower_rect.x = random.randint(0, window_size[0])
            slower_rect.y = random.randint(0, window_size[1])
        
        # Decrement the boost expiration counter
        if boost_expiration > 0:
            boost_expiration -= 1
            
            
        # Reset the player's speed if the boost has expired
        elif player_speed > 5:
            player_speed = 5
            

        # Move the enemy towards the player
        if player_rect.x > enemy_rect.x:
            enemy_rect.x += enemy_speed
        if player_rect.x < enemy_rect.x:
            enemy_rect.x -= enemy_speed
        if player_rect.y > enemy_rect.y:
            enemy_rect.y += enemy_speed
        if player_rect.y < enemy_rect.y:
            enemy_rect.y -= enemy_speed

        # Move the eater towards the player
        if player_rect.x > eater_rect.x:
            eater_rect.x += eater_speed
        if player_rect.x < eater_rect.x:
            eater_rect.x -= eater_speed
        if player_rect.y > eater_rect.y:
            eater_rect.y += eater_speed
        if player_rect.y < eater_rect.y:
            eater_rect.y -= eater_speed

        # Move the eater towards the player
        if player_rect.x > doubler_rect.x:
            doubler_rect.x += doubler_speed
        if player_rect.x < doubler_rect.x:
            doubler_rect.x -= doubler_speed
        if player_rect.y > doubler_rect.y:
            doubler_rect.y += doubler_speed
        if player_rect.y < doubler_rect.y:
            doubler_rect.y -= doubler_speed

        # Clear the screen
        screen.fill((255, 255, 255))

        # Update the display
        screen.blit(background_image, background_rect)
        screen.blit(player_image, player_rect)
        screen.blit(eater_image, eater_rect)
        screen.blit(enemy_image, enemy_rect)
        screen.blit(boost_image, boost_rect)
        screen.blit(bomb_image, bomb_rect)
        screen.blit(doubler_image, doubler_rect)
        screen.blit(slower_image, slower_rect)
        screen.blit(shield_image, shield_rect)
        screen.blit(Freeze_image, Freeze_rect)
        for coin_rect in coins:
            screen.blit(coin_image, coin_rect)



        # Draw the player's score
        score_text = font.render("Score: {}".format(score), True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        # Blit the high score text onto the screen
        screen.blit(high_score_text, (10, 50))

        # Update the display
        pygame.display.update()

        # Delay the game loop
        pygame.time.delay(delay_time)

#Quit pygame
pygame.quit() 


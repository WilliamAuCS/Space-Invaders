import pygame.font


class Button:
    def __init__(self, screen, msg, msg1):
        """Initialize button attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set dimensions and properties of button
        # msg
        self.width, self.height = 400, 50
        self.button_color = (0, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 40)

        # msg1
        self.width1, self.height1 = 400, 50
        self.button_color1 = (0, 0, 0)
        self.text_color1 = (255, 255, 255)
        self.font1 = pygame.font.SysFont(None, 40)

        # Alien_1 score
        self.alien1_width, self.alien1_height = 150, 50
        self.alien1_button_color = (0, 0, 0)
        self.alien_text_color = (255, 255, 255)
        self.alien_font = pygame.font.SysFont("comicsansms", 20)

        # Build the button's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.centery = self.screen_rect.centery + 150

        # msg1
        self.rect1 = pygame.Rect(0, 0, self.width1, self.height1)
        self.rect1.center = self.screen_rect.center
        self.rect1.centery = self.screen_rect.centery + 200

        # Alien1 score
        self.alien1_rect = pygame.Rect(0, 0, self.alien1_width, self.alien1_height)
        self.alien1_rect.center = self.screen_rect.center
        self.alien1_rect.centerx = self.screen_rect.centerx + 70
        self.alien1_rect.centery = self.screen_rect.centery - 150
        alien1_msg = "=   50 points"
        # Alien2 score
        self.alien2_rect = pygame.Rect(0, 0, self.alien1_width, self.alien1_height)
        self.alien2_rect.center = self.screen_rect.center
        self.alien2_rect.centerx = self.screen_rect.centerx + 70
        self.alien2_rect.centery = self.screen_rect.centery - 50
        alien2_msg = " =   100 points"
        # Alien3 score
        self.alien3_rect = pygame.Rect(0, 0, self.alien1_width, self.alien1_height)
        self.alien3_rect.center = self.screen_rect.center
        self.alien3_rect.centerx = self.screen_rect.centerx + 70
        self.alien3_rect.centery = self.screen_rect.centery + 50
        alien3_msg = " =   150 points"

        # Prepping the button message
        self.prep_msg(msg, msg1, alien1_msg, alien2_msg, alien3_msg)

        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

        # msg1

        self.msg_image1 = self.font1.render(msg1, True, self.text_color1, self.button_color1)
        self.msg_image1_rect = self.msg_image1.get_rect()
        self.msg_image1_rect.center = self.rect1.center

        # Alien1
        self.image_alien1 = pygame.image.load("images/alien.png")
        self.rect_alien1 = self.image_alien1.get_rect()
        # Alien2
        self.image_alien2 = pygame.image.load("images/alien2.png")
        self.rect_alien2 = self.image_alien2.get_rect()
        # Alien3
        self.image_alien3 = pygame.image.load("images/alien3.png")
        self.rect_alien3 = self.image_alien3.get_rect()

        # Top logo
        self.logo_image = pygame.image.load('images/Space Invaders.PNG')
        self.logo_stretched = pygame.transform.scale(self.logo_image, (450, 200))
        self.rect_logo = self.logo_stretched.get_rect()

        # Alien1 Score

        self.alien1_msg = self.alien_font.render(alien1_msg, True, self.alien_text_color, self.alien1_button_color)
        self.alien1_msg_rect = self.alien1_msg.get_rect()
        self.alien1_msg_rect.center = self.alien1_rect.center
        # Alien2 score
        self.alien2_msg = self.alien_font.render(alien2_msg, True, self.alien_text_color, self.alien1_button_color)
        self.alien2_msg_rect = self.alien2_msg.get_rect()
        self.alien2_msg_rect.center = self.alien2_rect.center
        # Alien3 score
        self.alien3_msg = self.alien_font.render(alien3_msg, True, self.alien_text_color, self.alien1_button_color)
        self.alien3_msg_rect = self.alien3_msg.get_rect()
        self.alien3_msg_rect.center = self.alien3_rect.center

        # Display new alien at the top middle of the screen
        # Alien1
        self.rect_alien1.center = self.screen_rect.center
        self.rect_alien1.centery = self.screen_rect.centery - 150
        self.rect_alien1.centerx = self.screen_rect.centerx - 50
        # Alien2
        self.rect_alien2.center = self.screen_rect.center
        self.rect_alien2.centery = self.screen_rect.centery - 50
        self.rect_alien2.centerx = self.screen_rect.centerx - 50
        # Alien3
        self.rect_alien3.center = self.screen_rect.center
        self.rect_alien3.centerx = self.screen_rect.centerx - 50
        self.rect_alien3.centery = self.screen_rect.centery + 50

        # Top Logo
        self.rect_logo.center = self.screen_rect.center
        self.rect_logo.centery = self.screen_rect.centery - 300

    def prep_msg(self, msg, msg1, alien1_msg, alien2_msg, alien3_msg):
        """Turn message into rendered image and center onto screen"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

        # msg1
        self.msg_image1 = self.font.render(msg1, True, self.text_color1, self.button_color1)
        self.msg_image1_rect = self.msg_image1.get_rect()
        self.msg_image1_rect.center = self.rect.center

        # Alien1 score
        self.alien1_msg = self.alien_font.render(alien1_msg, True, self.alien_text_color, self.alien1_button_color)
        self.alien1_msg_rect = self.alien1_msg.get_rect()
        self.alien1_msg_rect.center = self.alien1_msg_rect.center
        # Alien2 score
        self.alien2_msg = self.alien_font.render(alien2_msg, True, self.alien_text_color, self.alien1_button_color)
        self.alien2_msg_rect = self.alien2_msg.get_rect()
        self.alien2_msg_rect.center = self.alien2_msg_rect.center
        # Alien3
        self.alien3_msg = self.alien_font.render(alien3_msg, True, self.alien_text_color, self.alien1_button_color)
        self.alien3_msg_rect = self.alien3_msg.get_rect()
        self.alien3_msg_rect.center = self.alien3_rect.center

    def draw_button(self):
        """Draw blank button, then message"""
        self.screen.fill((0, 0, 0))
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

        # msg1
        self.screen.fill(self.button_color1, self.rect1)
        self.screen.blit(self.msg_image1, self.msg_image1_rect)

        # Alien1
        self.screen.blit(self.image_alien1, self.rect_alien1)
        # Alien2
        self.screen.blit(self.image_alien2, self.rect_alien2)
        # Alien3
        self.screen.blit(self.image_alien3, self.rect_alien3)

        # Alien1 Score
        self.screen.fill(self.alien1_button_color, self.alien1_rect)
        self.screen.blit(self.alien1_msg, self.alien1_msg_rect)
        # Alien2 Score
        self.screen.fill(self.alien1_button_color, self.alien2_rect)
        self.screen.blit(self.alien2_msg, self.alien2_msg_rect)
        # Alien3 Score
        self.screen.fill(self.alien1_button_color, self.alien3_rect)
        self.screen.blit(self.alien3_msg, self.alien3_msg_rect)

        # Top Logo
        self.screen.blit(self.logo_stretched, self.rect_logo)

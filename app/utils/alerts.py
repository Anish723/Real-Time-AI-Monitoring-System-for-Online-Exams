import pygame
import time

class AlertSystem:
    def __init__(self):
        pygame.mixer.init()
        self.sound = pygame.mixer.Sound("assets/alert.wav")
        self.last_play = 0

    def play_alert(self):
        current_time = time.time()

        # 🔇 Cooldown (2 seconds)
        if current_time - self.last_play > 2:
            self.sound.play()
            self.last_play = current_time
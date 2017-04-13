import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():

	# Initializes pygame, settings, and screen object.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	play_button = Button(ai_settings, screen, "Play")

	# Game statistic.
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)

	# Create ship.
	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	# Starting the main game cycle.
	while True:

		# Tracking keyboard and mouse events.
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, 
			aliens, bullets)
		
		if stats.game_active:

			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb, 
				ship, aliens, bullets)
			gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
				bullets)

		# Each time the loop is run, the screen is redrawn.
		# Displays the last drawn screen.
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, 
			bullets, play_button)		

run_game()
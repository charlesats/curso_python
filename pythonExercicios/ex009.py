# Faça um programa em Python que abra e reproduza
# o áudio de um arquivo MP3

import pygame
import os


pygame.init()

pygame.mixer.music.load('bololo.mp3')
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play()
pygame.event.wait()



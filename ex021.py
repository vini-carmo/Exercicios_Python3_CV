import pygame
pygame.init()
pygame.mixer.music.load('ex021.wav')
pygame.mixer.music.play()
# Mantém o programa rodando enquanto toca a música
input("Pressione Enter para encerrar...")

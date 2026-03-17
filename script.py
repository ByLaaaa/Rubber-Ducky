import os
import sys
import subprocess

# Fungsi untuk menginstal library secara otomatis dengan aman
def install_and_import(package):
    try:
        __import__(package)
    except ImportError:
        # --only-binary : mencegah pip mencoba meng-compile dari source (penyebab error 3.14 tadi)
        subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--only-binary=:all:"])
        __import__(package)

# Eksekusi instalasi pygame
try:
    install_and_import('pygame')
except Exception as e:
    print(f"Gagal menginstal dependensi: {e}")
    sys.exit(1)

import pygame
import random

# Inisialisasi Pygame
pygame.init()
info = pygame.display.Info()
screen = pygame.display.set_mode((info.current_w, info.current_h), pygame.NOFRAME)

font = pygame.font.SysFont("Arial", 64)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F4 and (pygame.key.get_mods() & pygame.KMOD_ALT):
                pygame.quit()
                sys.exit()

    text_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    text = font.render(":-) RUBBER DUCKS WILL TAKE OVER THE OCEANS! (-:", True, text_color)
    
    text_rect = text.get_rect(center=(info.current_w // 2, info.current_h // 2))
    
    # Efek getar
    text_rect.x += random.randint(-5, 5)
    text_rect.y += random.randint(-5, 5)

    screen.fill((0, 0, 0))
    screen.blit(text, text_rect)
    pygame.display.flip()
    clock.tick(30) # Membatasi FPS agar tidak membebani CPU
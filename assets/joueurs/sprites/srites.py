import pygame
import os

# Initialisation de Pygame
pygame.init()

# Charger l'image
spritesheet_path = "spritesheet.png"  # Mets ici le bon chemin si besoin
sheet = pygame.image.load(spritesheet_path).convert_alpha()

# Dimensions de chaque sprite
sprite_width = 32
sprite_height = 36

# Nombre de sprites (lignes et colonnes)
rows = 8
cols = 12

# Dossier de sortie
output_folder = "sprites_decoupés"
os.makedirs(output_folder, exist_ok=True)

# Direction mapping
directions = [
    "down_1", "down_2", "left_1", "left_2",
    "right_1", "right_2", "up_1", "up_2",
    "idle_down", "idle_left", "idle_right", "idle_up"
]

# Boucle de découpage
for row in range(rows):
    for col in range(cols):
        rect = pygame.Rect(col * sprite_width, row * sprite_height, sprite_width, sprite_height)
        sprite = sheet.subsurface(rect)

        # Crée un nom pour le sprite
        character_name = f"character_{row}"
        direction = directions[col] if col < len(directions) else f"direction_{col}"
        filename = f"{character_name}_{direction}.png"

        # Sauvegarder le sprite
        pygame.image.save(sprite, os.path.join(output_folder, filename))

print("Découpage terminé !")

self.walls = []
for obj in self.tmx_data.objects:
    if obj.type == "collisions":
        rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
        self.walls.append(rect)



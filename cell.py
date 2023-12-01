import pygame

class Cell:

    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketch_value = 0
        self.initial = False
        self.selected = False

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketch_value = value

    def draw(self):
        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.col * 100, self.row * 100, 100, 100), 6)

        if (self.sketch_value != 0) and (self.value == 0):
            num_font = pygame.font.Font(None, 50)
            num_surf = num_font.render(str(self.sketch_value), 0, (83, 83, 83))
            num_rect = num_surf.get_rect(center=(self.col * 100 + 100 // 2, self.row * 100 + 100 // 2))
            self.screen.blit(num_surf, num_rect)

        elif (self.value != 0) and (self.sketch_value == 0):
            num_font = pygame.font.Font(None, 150)
            num_surf = num_font.render(str(self.value), 0, (0, 0, 0))
            num_rekt = num_surf.get_rect(center=(self.col * 100 + 100 // 2, self.row * 100 + 100 // 2))
            self.screen.blit(num_surf, num_rekt)
            self.initial = True

        elif (self.value != 0) and (self.sketch_value != 0):
            num_font = pygame.font.Font(None, 150)
            num_surf = num_font.render(str(self.value), 0, (0, 0, 255))
            num_rect = num_surf.get_rect(center=(self.col * 100 + 100 // 2, self.row * 100 + 100 // 2))
            self.screen.blit(num_surf, num_rect)

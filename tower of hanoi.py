import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 400
PEG_WIDTH = 20
DISK_HEIGHT = 20
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Disk colors for three pegs

# Function to draw the current state of the Tower of Hanoi
def draw_tower(pegs):
    screen.fill((255, 255, 255))  # White background

    for i, peg in enumerate(pegs):
        x = (i + 1) * WIDTH // 4  # Distribute pegs equally
        pygame.draw.rect(screen, (0, 0, 0), (x - PEG_WIDTH // 2, 0, PEG_WIDTH, HEIGHT))  # Draw peg

        for j, disk in enumerate(peg):
            pygame.draw.rect(screen, COLORS[disk - 1], (x - disk * 10, HEIGHT - (j + 1) * DISK_HEIGHT, disk * 20, DISK_HEIGHT))

    pygame.display.flip()

# Recursive function to solve Tower of Hanoi and update animation
def tower_of_hanoi_animation(n, source, target, auxiliary):
    if n > 0:
        # Move n-1 disks from source to auxiliary peg
        tower_of_hanoi_animation(n - 1, source, auxiliary, target)

        # Move the nth disk from source to target peg
        pegs[source - 1].pop()
        pegs[target - 1].append(n)
        draw_tower(pegs)
        time.sleep(0.5)  # Add a delay for better visualization

        # Move the n-1 disks from auxiliary to target peg
        tower_of_hanoi_animation(n - 1, auxiliary, target, source)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower of Hanoi Animation")

# Number of disks
num_disks = 3

# Initialize pegs
pegs = [[] for _ in range(3)]
pegs[0] = list(range(num_disks, 0, -1))  # Source peg starts with all disks

# Run the animation
tower_of_hanoi_animation(num_disks, 1, 3, 2)

# Quit Pygame
pygame.quit()
sys.exit()
passimport random
import os

# Terminal colors (ANSI codes)
COLORS = [
    "\033[41m",  # Red background
    "\033[42m",  # Green background
    "\033[43m",  # Yellow background
    "\033[44m",  # Blue background
    "\033[45m",  # Magenta background
    "\033[46m",  # Cyan background
    "\033[47m",  # White background
    "\033[100m", # Bright black/gray background
]

RESET = "\033[0m"

def mosaic(rows=20, cols=40, tile_size=2):
    """Generate a mosaic pattern in the terminal."""
    for _ in range(rows):
        line = ""
        for _ in range(cols):
            color = random.choice(COLORS)
            line += color + " " * tile_size + RESET
        print(line)

if __name__ == "__main__":
    os.system("clear")  # Clear terminal before drawing
    mosaic(rows=20, cols=40, tile_size=2)
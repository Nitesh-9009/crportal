"""Generate an 8-bit pixel-art female engineering student portrait
matching the hero avatar style (glasses + college hoodie + IITB badge)."""
from PIL import Image, ImageDraw
import random

CELL = 20
GW, GH = 32, 40
W, H = GW * CELL, GH * CELL

# Palette (night-skin inspired, same as the male avatar's world)
BG      = (18, 20, 38)
BG_GRID = (28, 31, 56)
HAIR    = (42, 30, 23)
HAIR_HI = (74, 55, 40)
SKIN    = (232, 168, 124)
SKIN_SH = (201, 136, 96)
GLASS   = (36, 255, 205)   # cyan frames
LENS    = (10, 16, 28)
HOODIE  = (242, 78, 30)    # coral
HOOD_SH = (198, 58, 18)
HOOD_HI = (255, 122, 82)
YELLOW  = (255, 208, 38)
GREEN   = (0, 255, 102)
WHITE   = (226, 226, 235)
BLACK   = (0, 0, 0)
LIPS    = (214, 84, 79)

random.seed(26)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# Blueprint grid backdrop
for x in range(0, W, CELL * 2):
    d.line([(x, 0), (x, H)], fill=BG_GRID)
for y in range(0, H, CELL * 2):
    d.line([(0, y), (W, y)], fill=BG_GRID)


def px(gx, gy, color, w=1, h=1):
    d.rectangle([gx * CELL, gy * CELL, (gx + w) * CELL - 1, (gy + h) * CELL - 1], fill=color)


def outline_rect(gx, gy, w, h, color):
    px(gx, gy, color, w, 1)
    px(gx, gy + h - 1, color, w, 1)
    px(gx, gy, color, 1, h)
    px(gx + w - 1, gy, color, 1, h)


# ---------------- Long hair backdrop ----------------
for gy in range(6, 30):
    width = 13 if gy < 12 else 12
    px(16 - width // 2 - 1, gy, HAIR, width + 2, 1)
# hair shine strands
px(6, 9, HAIR_HI, 2, 8)
px(24, 9, HAIR_HI, 2, 8)
px(8, 20, HAIR_HI, 1, 6)
px(23, 20, HAIR_HI, 1, 6)

# ---------------- Face ----------------
px(10, 9, SKIN, 12, 12)
px(10, 9, SKIN_SH, 12, 1)          # hairline shadow
px(10, 20, SKIN_SH, 12, 1)         # chin shade
px(9, 11, SKIN, 1, 6)              # ears
px(22, 11, SKIN, 1, 6)
px(9, 13, SKIN_SH, 1, 2)
px(22, 13, SKIN_SH, 1, 2)

# front fringe / bangs
px(10, 8, HAIR, 12, 2)
px(11, 10, HAIR, 2, 1)
px(19, 10, HAIR, 2, 1)
px(15, 10, HAIR, 2, 1)

# ---------------- Pixel glasses (cyan, same vibe as male) ----------------
def glasses_arm(x, y):
    px(x, y, GLASS)

# left lens
outline_rect(10, 12, 5, 4, GLASS)
px(11, 13, LENS, 3, 2)
px(11, 13, WHITE, 1, 1)
# right lens
outline_rect(17, 12, 5, 4, GLASS)
px(18, 13, LENS, 3, 2)
px(18, 13, WHITE, 1, 1)
# bridge + arms
px(15, 13, GLASS, 2, 1)
glasses_arm(9, 13)
glasses_arm(22, 13)

# ---------------- Nose + smile ----------------
px(15, 17, SKIN_SH, 2, 1)
px(14, 18, LIPS, 4, 1)   # smile

# ---------------- Hoodie (coral) with collar ----------------
px(4, 22, HOODIE, 24, 12)
px(4, 22, HOOD_SH, 24, 1)
px(4, 33, HOOD_SH, 24, 1)
px(4, 22, HOODIE, 2, 12)
px(26, 22, HOOD_SH, 2, 12)
# shoulders highlight
px(6, 23, HOOD_HI, 3, 1)
px(23, 23, HOOD_HI, 3, 1)
# hood collar around neck
px(13, 21, HOOD_SH, 6, 2)
px(14, 20, SKIN, 4, 1)
# zipper line
px(15, 24, HOOD_SH, 1, 9)
px(15, 24, YELLOW, 1, 1)

# ---------------- IITB badge ----------------
outline_rect(20, 25, 7, 5, BLACK)
px(21, 26, YELLOW, 5, 3)
px(22, 27, BLACK, 3, 1)  # mark text hint

# ---------------- Left pocket print (aakaar arc) ----------------
px(7, 26, WHITE, 4, 1)
px(6, 27, WHITE, 1, 1)
px(11, 27, WHITE, 1, 1)
px(6, 28, GREEN, 1, 1)
px(11, 28, GREEN, 1, 1)

# ---------------- Background sparkle pixels ----------------
for _ in range(14):
    gx, gy = random.randint(1, GW - 2), random.randint(1, GH - 2)
    if img.getpixel((gx * CELL + 2, gy * CELL + 2)) == BG:
        px(gx, gy, random.choice([GREEN, YELLOW, (36, 255, 205)]))

# ---------------- Frame border ----------------
outline_rect(0, 0, GW, GH, BLACK)
outline_rect(1, 1, GW - 2, GH - 2, (36, 255, 205))

img.save("static/img/px-avatar-female.png")
print("saved static/img/px-avatar-female.png", img.size)

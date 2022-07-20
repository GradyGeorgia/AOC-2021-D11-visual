import pygame

# get input from file
with open("input.txt") as f:
  inp = f.read()

# initialize pygame and parameters
pygame.init()

screenWidth = 500
screenHeight = 500
fontSize = 22

# change the speed of the visual here
speed = 5

screen = pygame.display.set_mode((screenWidth + 100, screenHeight))
clock = pygame.time.Clock()
pygame.display.set_caption("Advent of Code - Day 11")
font = pygame.font.Font(None, fontSize)

# code to solve advent of code problem
m = [[int(x) for x in line] for line in inp.split("\n")]

height = len(m)
width = len(m[0])
rDif = [1,1,1,0,-1,-1,-1,0]
cDif = [-1,0,1,1,1,0,-1,-1]
steps = 0
total = 0

# fill screen, draw octos, and update the text
def updateScreen():
  screen.fill(0)
  drawOctos()
  updateText()
  pygame.display.update()

# draw a circle for each octopus with color representing the light level
def drawOctos():
  for r in range(height):
    for c in range(width):
      octo = m[c][r]
      if octo <= 9:
        brightness = 255//10 * (octo + 1)
        color = (brightness, brightness, brightness)
      else:
        color = (235, 219, 52)        
      pygame.draw.circle(screen, color, (.1 * screenHeight * (r + .5), .1 * screenWidth * (c + .5)), screenHeight//25)

# udpdate the total and steps text
def updateText():
  totalTextHeader = font.render("Total flashes:", 1,(255,255,255))
  totalText = font.render(str(total), 1,(255,255,255))
  stepsTextHeader = font.render("Steps:", 1,(255,255,255))
  stepsText = font.render(str(steps), 1,(255,255,255))
  screen.blit(totalTextHeader, (screenWidth, 0))
  screen.blit(totalText, (screenWidth, fontSize))
  screen.blit(stepsTextHeader, (screenWidth, fontSize*3))
  screen.blit(stepsText, (screenWidth, fontSize*4))

# flash each octopus that needs to and update the screen
def flash(r, c):
  pygame.time.wait(10 // speed)
  updateScreen()

  global total
  if steps <= 100:
    total += 1
  flashed.add((r, c))
  for i in range(8):
    newR = r + rDif[i]
    newC = c + cDif[i]
    if newR >= 0 and newR < height and newC >= 0 and newC < width and (newR, newC) not in flashed:
      m[newR][newC] += 1
      if m[newR][newC] > 9:
        pygame.time.wait(50 // speed)
        flash(newR, newC)

# run loop to solve problem and display the visual
for i in range(1000):
  pygame.time.wait(250 // speed)
  updateScreen()

  steps += 1
  for r in range(height):
    for c in range(width):
      m[r][c] += 1

  pygame.time.wait(250 // speed)
  updateScreen()

  flashed = set()
  for r in range(height):
    for c in range(width):
      if m[r][c] > 9 and (r, c) not in flashed:
        flash(r, c)
  
  for r in range(height):
    for c in range(width):
      if (r, c) in flashed:
        m[r][c] = 0

  if len(flashed) >= width * height:
    break

# stop pygame from closing after the loop finishes
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
  updateScreen()

from opcua import Server

import pygame, time
import time
import math
import random



# setup do servidor OPC UA
SP, KP, KI = 200, 0.1, 0.02
server = Server(); server.set_endpoint("opc.tcp://localhost:4840/"); ns = server.register_namespace("Controle de Nível de Tanque")
node = server.get_objects_node().add_object(ns, "Tank")
level_var = node.add_variable(ns, "Level", 0)
level_var.set_writable()


pygame.init(); clock = pygame.time.Clock()
width, height = 1000, 400; screen = pygame.display.set_mode((width, height))
white, black, gray, red, blue = (255, 255, 255), (0, 0, 0), (128, 128, 128), (255, 0, 0), (0, 0, 255)
level, integral_error = 0, 0; font = pygame.font.SysFont(None, 30)
background_image = pygame.image.load("tanque.png").convert_alpha(); pygame.display.set_caption("Controle de Nível de Tanque")
last_sp_change = pygame.time.get_ticks()
running = True


# iniciando o servidor
server.start()
print("Servidor OPC UA Iniciado. URL!")
level_var.set_value(level)

while running:
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   running = False

 level += random.randint(-5, 5)
 if pygame.time.get_ticks() - last_sp_change >= 15000:
  if SP == 200:
   SP = 150
  else:
   SP = 200
 last_sp_change = pygame.time.get_ticks()
 error = SP - level
 integral_error += error
 output = KP * error + KI * integral_error
 level += output; level = max(min(level, 400), 0)
 # OPC UA server
 level_var.set_value(level)


 screen.blit(background_image, (20, 0))
 pygame.draw.rect(screen, gray, (20, 0, 500, 300))
 pygame.draw.rect(screen, blue, (20, 350 - level, 500, level))
 pygame.draw.line(screen, black, (20, 0), (20, 350), 3)
 pygame.draw.line(screen, black, (20, 350), (550, 350), 3)
 pygame.draw.line(screen, red, (20, 350 - SP), (550, 350 - SP), 2)

 level_text = font.render("Level: {:.4f}".format(level), True, black)
 sp_text = font.render("SP: " + str(SP), True, black)
 lab_text = font.render("Controle de Nível (PI) - TANQUE 1", True, black)

 screen.blit(level_text, (700, 50))
 screen.blit(sp_text, (700, 150))
 screen.blit(lab_text, (100, 360))

 pygame.display.update()
 clock.tick(60)

pygame.quit()
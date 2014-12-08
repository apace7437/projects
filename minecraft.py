### Basic teleporter in minecraft-pi

import time,mcpi.minecraft as mc #adds mcpi modules
game = mc.Minecraft.create() #connects to a minecraft game and calls it game

time.sleep(10)
game.postToChat("hello world")

game.player.setPos(50,25,75)

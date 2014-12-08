import time,mcpi.minecraft as mcpi
mc = mcpi.Minecraft.create()

time.sleep(5)
mc.postToChat("3")
time.sleep(1)
mc.postToChat("2")
time.sleep(1)
mc.postToChat("1")
time.sleep(1)

while True :
 time.sleep(10)
 mc.player.setPos(60,0,60)
 time.sleep(10)
 mc.player.setPos(90,17,5)
 time.sleep(10)
 mc.player.setPos(0,150,0)
 time.sleep(10)

import random,time,mcpi.minecraft as minecraft
mc=minecraft.Minecraft.create()

while True:
  pos = mc.player.getPos()
  x=pos.x
  y=pos.y
  z=pos.z
  
  yg = y +50
  xg = random.randit(x-10,x+10)
  zg = random.randit(z-10,z+10)
  mc.setBlock(x,y+50,z,13)
  


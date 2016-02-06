#Imports

import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
import mcpi.block as block
import time
import random

size = random.randint(1,3)

#Assigning block variables

houseBlock1 = 5
houseBlock2 = 17
glass = 20
triggerBlock = block.WOOL

#Grabbing the player's current position and assigning it to the variable
#'pos'. It will also allow the program to build the house around the player.

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z


while True:
    if mc.getBlock(x, y - 1, z) == triggerBlock:
        #Building house size one
        if size == 1:
            mc.setBlocks(x, y - 1, z, x + 2, y - 1, z, houseBlock1)
            mc.setBlocks(x, y - 1, z, x + -2, y - 1, z, houseBlock1)
            mc.setBlocks(x, y - 1, z, x, y - 1, z + 2, houseBlock1)
            mc.setBlocks(x, y - 1, z, x, y - 1, z + -2, houseBlock1)
            mc.setBlocks(x - 1, y - 1, z - 1, x - 2, y - 1, z - 2, houseBlock1)
            mc.setBlocks(x - 1, y - 1, z - 1, x + 2, y - 1, z + 2, houseBlock1)
            mc.setBlocks(x - 1, y - 1, z - 1, x - 2, y - 1, z + 2, houseBlock1)
            mc.setBlocks(x - 2, y - 1, z - 2, x + 2, y, z - 2, houseBlock1)
            mc.setBlocks(x + 2, y - 1, z - 2, x + 2, y, z + 2, houseBlock1)
            mc.setBlocks(x - 2, y - 1, z + 2, x - 2, y, z - 1, houseBlock1)
            mc.setBlocks(x + 1, y - 1, z + 2, x - 1, y + 1, z + 2, houseBlock1)
            mc.setBlocks(x - 2, y + 1, z - 2, x + 2, y + 1, z - 2, houseBlock1)
            mc.setBlocks(x + 2, y + 1, z - 2, x + 2, y + 1, z + 2, houseBlock1)
            mc.setBlock(x - 2, y + 1, z + 2, houseBlock1)
            mc.setBlocks(x + 2, y + 1, z - 1, x + 2, y + 1, z + 1, glass)
            mc.setBlocks(x - 2, y + 1, z + 1, x - 2, y + 1, z - 1, glass)
            mc.setBlocks(x + 2, y + 2, z + 2, x + 2, y + 2, z - 2, 53)
            mc.setBlocks(x + 1, y + 2, z - 2, x - 2, y + 2, z + 2, 53)
        elif size == 2:
    
            #Building house size two
    
            mc.setBlocks(x - 2, y - 1, z + 2, x + 1, y, z - 3, houseBlock1)
            mc.setBlocks(x - 1, y, z + 1, x, y, z - 2, 0)
            mc.setBlock(x - 1, y, z + 2, 64)
            mc.setBlocks(x + 1, y +1, z + 2, x + 1, y +1, z - 3, houseBlock2)
            mc.setBlocks(x, y + 1, z - 3, x - 1, y + 1, z - 3, glass)
            mc.setBlocks(x - 2, y + 1, z - 3, x - 2, y + 1, z + 2, houseBlock2)
            mc.setBlock(x, y + 1, z + 2, houseBlock2)
            mc.setBlock(x, y, z + 1, 58)
            mc.setBlock(x, y + 1, z + 1, 51)
            mc.setBlocks(x, y, z - 1, x, y, z - 2, 54)
            mc.setBlocks(x + 1, y + 2, z + 2, x - 2, y + 2, z - 3, 5,2)
        elif size == 3:
    
            #Building house size three
    
            mc.setBlocks(x + 3, y - 1, z + 4, x - 3, y - 1, z - 4, houseBlock2)
            mc.setBlocks(x + 3, y, z + 4, x - 3, y, z - 4, houseBlock1,2)
            mc.setBlocks(x + 2, y, z + 3, x - 2, y, z - 3, 0)
            mc.setBlocks(x + 3, y + 1, z + 4, x - 3, y + 1, z - 4, houseBlock2,2)
            mc.setBlocks(x + 2, y + 1, z + 3, x - 2, y + 1, z - 3, 0)
            mc.setBlocks(x + 3, y + 2, z + 4, x - 3, y + 2, z - 4, houseBlock1,2)
            mc.setBlocks(x + 2, y + 2, z + 3, x - 2, y + 2, z - 3, 0)
            mc.setBlocks(x + 3, y + 3, z + 4, x - 3, y + 3, z - 4, houseBlock2,2)
            mc.setBlocks(x + 2, y + 3, z + 3, x - 2, y + 3, z - 3, 0)
            mc.setBlocks(x + 3, y + 4, z + 4, x - 3, y + 4, z - 4, houseBlock1,2)
            mc.setBlocks(x + 2, y + 4, z + 3, x - 2, y + 4, z - 3, 0)
            mc.setBlocks(x + 3, y + 5, z + 4, x - 3, y + 5, z - 4, houseBlock2,2)
            mc.setBlocks(x + 2, y + 5, z + 3, x - 2, y + 5, z - 3, 0)
            mc.setBlocks(x + 2, y + 6, z + 3, x - 2, y + 6, z - 3, 45)
            mc.setBlocks(x + 1, y + 1, z - 4, x - 1, y + 2, z - 4, glass)
            mc.setBlocks(x + 1, y + 1, z + 4, x - 1, y + 2, z + 4, glass)
            mc.setBlocks(x + 3, y + 1, z - 2, x + 3, y + 1, z + 2, glass)
            mc.setBlock(x - 3, y, z, block.DOOR_WOOD.id)
            mc.setBlock(x - 3, y + 1, z, 0)

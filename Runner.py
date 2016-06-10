#Imports
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
import time

#Blocks
triggerBlock = 35
originalBlock = 2
block2 = 57
block3 = 41
block4 = 42
block5 = 4

gameOver = False

#Game
mc.postToChat("Welcome to Runner. Place and step on the trigger block that you defined.")
while True:
	if mc.getBlock(mc.player.getPos().x, mc.player.getPos().y - 1, mc.player.getPos().z) == triggerBlock:
		
		gameOver = False
		
		#Grabs the players position and assigns it to a variable for later
		pos = mc.player.getPos()
		x = pos.x
		y = pos.y
		z = pos.z
		
		#Deletes the trigger block
		mc.setBlock(x, y - 1, z, 0)
		
		#Building the arena
		mc.setBlocks(x - 3, y, z - 3, x + 10, y + 3, z + 3, 20)
		mc.setBlocks(x - 2, y, z - 2, x + 9, y + 3, z + 2, 0)
		mc.setBlocks(x - 2, y - 1, z - 2, x + 9, y - 1, z + 2, originalBlock)
		mc.setBlocks(x - 2, y - 2, z - 2, x + 9, y - 2, z + 2, 11)
		
		time.sleep(1)
		
		#How to play
		mc.postToChat("This is a game called Runner, based of the")
		mc.postToChat("Minecraft PC game on Mineplex called Runner.")
		time.sleep(3)
		mc.postToChat("This object of this game is to survive for as long")
		mc.postToChat("as possible, and then you can try again. And again.")
		mc.postToChat("And again! When you run over a block, it goes up a damage")
		mc.postToChat("stage, and will change appearance. When the block is destroyed,")
		mc.postToChat("it shows the lava below.")
		time.sleep(5)
		mc.postToChat("Grass - Neutral")
		mc.postToChat("Diamond - Stage 1")
		mc.postToChat("Gold - Stage 2")
		mc.postToChat("Iron - Stage 3")
		mc.postToChat("Cobblestone - Stage 4")
		mc.postToChat("Air - Destroyed")
		time.sleep(5)
		
		#Start the game
		mc.postToChat("3")
		time.sleep(1)
		mc.postToChat("2")
		time.sleep(1)
		mc.postToChat("1")
		time.sleep(1)
		mc.postToChat("GO!")
		while True:
			if gameOver == False:
				if mc.getBlock(x, y - 1, z) == originalBlock:
					mc.setBlock(x, y - 1, z, block2)
				elif mc.getBlock(x, y - 1, z) == block2:
					mc.setBlock(x, y - 1, z, block3)
				elif mc.getBlock(x, y - 1, z) == block3:
					mc.setBlock(x, y - 1, z, block4)
				elif mc.getBlock(x, y - 1, z) == block4:
					mc.setBlock(x, y - 1, z, block5)
				elif mc.getBlock(x, y - 1, z) == block5:
					mc.setBlock(x, y - 1, z, 0)
				if mc.getBlock(x, y, z) == 11:
					#Clean up the arena, and finish the game
					gameOver = True
					mc.postToChat("GAME OVER")
					mc.setBlocks(x - 3, y, z - 3, x + 10, y + 3, z + 3, 0)

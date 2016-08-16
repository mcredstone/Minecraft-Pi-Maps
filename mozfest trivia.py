######################
#COMPLEXITY: BEGINNER#
######################

#These are the LIBRARIES that I have imported to use inside my program. If I didn't do this, when I ask the program to use FUNCTIONS inside this library, it will have
#no idea what I mean.

#This LIBRARY allows me to control Minecraft from Python.
from mcpi.minecraft import Minecraft
#This LIBRARY gives me constant VARIABLES of each Minecraft block ID to reference more easily.
from mcpi import block

#This is a VARIABLE. It is a value stored in a data section to be used later. Later in the program, you will see me reference this variable to control Minecraft
#itself!
mc = Minecraft.create()

#This is a FUNCTION. It is a chunk of code that is stored like a VARIABLE that can be CALLED later in the program many times
def init():
    pass

#A FUNCTION called question, the main bit of the program. This FUNCTION has arguments, or parentheses, stored as unassigned VARIABLES inside some BRACKETS separated by
#commas. When you CALL the FUNCTION, it will ask you to give a value to these empty VARIABLES. Here, it is asking you what you want the question to be, what the
#possible answers are and what index in the ARRAY of possible answers that the correct answer is. An ARRAY is a list of items. For example:
#question("What is this script for?", ["Trivia", "Teaching"], 1). "What is this script for?" is the question value, stored in a STRING. A STRING is a word or a
#sentence. It is another type of VARIABLE. ["Trivia", Teaching] is the ARRAY that contains the 2 possible answers. Finally, 1 is the ARRAY INDEX of the correct answer,
#"Teaching", stored in an INTEGER. Each item in an ARRAY has it's own INDEX inside that ARRAY. You would think that the first item in the list is INDEX 1, second is
#INDEX 2, etc., but that is not the case. In fact, in Python, ARRAY INDEXES start at 0. So 1 is the second item in the list.
def question(question, answers, answerIndex):
    #This uses the player.getPos() FUNCTION to assign the new VARIABLE pos to the player's current position.
    pos = mc.player.getPos()
    
    #This uses the setBlocks FUNCTION from the mcpi.minecraft LIBRARY, stored in the VARIABLE mc. Its SYNTAX (the way it is used) is setBlocks(x1, y1, z1, x2, y2, z2,
    #block). x1, y1 and z1 determines the first corner using xyz coordinates. x2, y2 and z2 determine the other corner. block determines the block it is filled with.
    #This call of setBlocks clears the area.
    mc.setBlocks(pos.x + 5, pos.y - 1, pos.z - 2, pos.x - 5, pos.y + 5, pos.z + 10, block.AIR)

    #This block of code will create the walls and the floor.
    mc.setBlocks(pos.x + 5, pos.y - 1, pos.z - 2, pos.x - 5, pos.y + 5, pos.z + 10, block.IRON_BLOCK)
    mc.setBlocks(pos.x + 4, pos.y, pos.z - 1, pos.x - 4, pos.y + 5, pos.z + 9, block.AIR)

    #This block of code will create the blocks to stand on to select the answer. It will use the setBlock(x, y, z, block) command to only set 1 block.
    mc.setBlock(pos.x + 4, pos.y, pos.z - 2, block.WOOL)
    mc.setBlock(pos.x + 4, pos.y, pos.z, block.LIME_WOOL)
    mc.setBlock(pos.x + 4, pos.y, pos.z + 2, block.BLUE_WOOL)

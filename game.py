# Main game file

from characters.player import *
from commands import *
from util import *


commands = {
    'help' : help,
    'exit' : exit
}


player = Player("Default", 1, 1)


def nameInput(prompt):
    name = raw_input(prompt)
    return name.strip()

def getName():
    tempName = ""
    while 1:
        tempName = nameInput("What is your name? \n")

        if len(tempName) < 1:
            continue

        yes = yesOrNo(tempName + ", is that your name? (Y/N)? ")

        if yes is True:
            return tempName
            print "OK, %s" % (tempName)
        else:
            continue

def help(player, args):
    for command in commands:
        print command

def isValidCMD(cmd):
    if cmd in commands:
        return True
    return False

def runCMD(cmd, args, player):
    commands[cmd](player, args)

def main (player):

    player.name = getName()

    while (not player.dead):
        line = raw_input(">> ")
        input = line.split()
        input.append("EOI")

        if isValidCMD(input[0]):
            runCMD(input[0], input[1], player)

main(player)
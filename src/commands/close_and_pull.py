#!/usr/bin/env python3
"Open claw and shoots the ball in the same movment."

from commands.punch import Punch
from commands.open_claw import OpenClaw
from commands.close_claw import CloseClaw
from commands.pull import Pull
from wpilib.command.commandgroup import CommandGroup
from wpilib.command.waitcommand import WaitCommand

class CloseAndPull(CommandGroup):
    """Open claw and punch."""
    def __init__(self, robot):
        super().__init__()

        self.addParallel(CloseClaw(robot=robot))
        self.addSequential(Pull(robot=robot))

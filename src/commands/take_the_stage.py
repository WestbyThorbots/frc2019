#!/usr/bin/env python3
"""
Take the Stage
"""
from wpilib.command import CommandGroup
class TakeTheStage(CommandGroup):
    def __init__(self, robot):
        super().__init__()

        self.addSequential()
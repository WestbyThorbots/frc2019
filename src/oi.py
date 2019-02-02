#!/usr/bin/python3
import wpilib

from commands.differentialdrive_with_xbox import DifferentialDriveWithXbox

class OI:
    def __init__(self, robot):
        """
        The robot constructor
        """

        self.xbox0 = wpilib.XboxController(0)

    def getXbox0(self):
        return self.xbox0

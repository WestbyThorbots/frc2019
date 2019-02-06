#!/usr/bin/python3
import wpilib
import hal
from wpilib.interfaces.generichid import GenericHID

from commands.differentialdrive_with_xbox import DifferentialDriveWithXbox

class OI:
    """
    The constructor
    """
    def __init__(self, robot):

        self.xbox0 = wpilib.XboxController(0)

    def getXbox0(self):
        return self.xbox0

    def getLeftTrigger(self):
        return self.xbox0.getTriggerAxis(GenericHID.Hand.kLeft)

    def getRightTrigger(self):
        return self.xbox0.getTriggerAxis(GenericHID.Hand.kRight)

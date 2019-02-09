#!usr/bin/python3
from wpilib import XboxController
from wpilib.interfaces.generichid import GenericHID
from wpilib.buttons import Button

class TriggerButton(Button):
    def __init__(self, xbox, threshold):
        super().__init__()

        self.xbox = xbox
        self.threshold = threshold

    def get(self):
        return self.xbox.getTriggerAxis(GenericHID.Hand.kLeft) > self.threshold
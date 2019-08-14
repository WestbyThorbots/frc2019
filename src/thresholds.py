#!usr/bin/python3
'''thresholds.py - Set various thresholds for use with the robot.'''

from wpilib import XboxController
from wpilib.interfaces.generichid import GenericHID
from wpilib.buttons import Button

class TriggerButton(Button):
    '''Set the minimum threshold at which either the left or the right
    Xbox controller "triggers" become "engaged". We use this in
    :class:`OI` to determine when to pay attention to the "triggers".'''

    def __init__(self, xbox: XboxController, threshold: float) -> None:
        '''Save the controller and trigger threshold for this instance.'''
        super().__init__()

        self.xbox = xbox
        self.threshold = threshold

    def get(self) -> bool:
        '''What you think it does.'''
        return (self.xbox.getTriggerAxis(GenericHID.Hand.kLeft) > self.threshold or
                self.xbox.getTriggerAxis(GenericHID.Hand.kRight) > self.threshold)

class StickButton(Button):

    def __init__(self, xbox: XboxController, threshold: float) -> None:

        super().__init__()

        self.xbox = xbox
        self.threshold = threshold

    def get(self) -> bool:
        return (abs(self.xbox.getX(GenericHID.Hand.kLeft)) > self.threshold or
                abs(self.xbox.getY(GenericHID.Hand.kLeft)) > self.threshold)

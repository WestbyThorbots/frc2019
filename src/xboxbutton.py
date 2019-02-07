# validated: 2017-10-19 AA e1195e8b9dab edu/wpi/first/wpilibj/buttons/JoystickButton.java
# ----------------------------------------------------------------------------
# Copyright (c) FIRST 2008-2017. All Rights Reserved.
# Open Source Software - may be modified and shared by FRC teams. The code
# must be accompanied by the FIRST BSD license file in the root directory of
# the project.
# ----------------------------------------------------------------------------

from wpilib.buttons import Button
from wpilib import XboxController
from wpilib.interfaces.generichid import GenericHID

__all__ = ["XboxButton"]


class XboxButton(Button):
    """A :class:`.button.Button` that gets its state from a :class:`.GenericHID`."""

    def __init__(self, xbox: XboxController, buttonNumber: int) -> None:
        """Create a joystick button for triggering commands.

        :param xbox: The XboxController object that has the button (e.g.
                         :class:`.Joystick`, :class:`.KinectStick`, etc)
        :param buttonNumber: The button number
                             (see :meth:`.GenericHID.getRawButton`)
        """
        super().__init__()
        self.xbox = xbox
        self.buttonNumber = buttonNumber

    def get(self) -> bool:
        """Gets the value of the xbox button.

        :returns: The value of the xbox button
        """
        if (self.buttonNumber == 1):
            return self.xbox.getAbutton()
        elif (self.buttonNumber == 2):
            return self.xbox.getBButton()
        elif (self.buttonNumber == 3):
            return self.xbox.getXButton()
        elif (self.buttonNumber == 4):
            return self.xbox.getYButton()
        elif (self.buttonNumber == 5):
            return self.xbox.getBumper(XboxController.Hand.kLeft)
        elif (self.buttonNumber == 6):
            return self.xbox.getBumper(XboxController.Hand.kRight)
        elif (self.buttonNumber == 8):
            return self.xbox.getStartButton()
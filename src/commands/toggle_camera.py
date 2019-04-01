#/usr/bin/python3

import networktables
from wpilib.command import Command

class ToggleCamera(Command):

    def __init__(self, robot):
        super().__init__()

        self.table = networktables.NetworkTables.getTable("/CameraPublisher")

    def initialize(self):
        pass

    def execute(self):
        """Execute the toggle command.
	Toggle the active camera in the Dashboard using the bitwise Exclusive Or
        (XOR) of the current value of "selected" to "invert" the value
        (or toggle between 0 and 1).
	(see https://wiki.python.org/moin/BitwiseOperators for a discussion
        of bit operators). Convert the value returned by table.getNumber() to
        an integer in order for the XOR to work.
        See also, the code in /home/pi/switched_cameraserver.py running on the Raspberry Pi.
        """
        self.table.putNumber('selected', int(self.table.getNumber('selected', 0)) ^ 1)

    def isFinished(self):
        """Make this return true when this Command no longer needs to run execute()"""
        return True

    def end(self):
        """Called once after isFinished returns true"""

    def interrupted(self):
        """Called when another Command which requires one or more of the same
           subsystems is scheduled to run"""
        self.end()


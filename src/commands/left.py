#!/usr/bin/python3

from wpilib.command.commandgroup import CommandGroup
from wpilib.command.waitcommand import WaitCommand

from commands.drive_straight import DriveStraight
from commands.invert_front import InvertFront
from commands.limelight_led_blink import LimeLightLEDblink
from commands.limelight_led_off import LimeLightLEDoff
from commands.limelight_led_on import LimeLightLEDon
from commands.park import Park
from commands.turn import Turn

class Left(CommandGroup):

    def __init__(self, robot):
        super().__init__()
        self.addSequential(InvertFront(robot))
        self.addSequential(DriveStraight(robot, 10, .5))
        self.addSequential(Turn(robot, 90, .5))
        #self.addSequential(LimeLightLEDon(robot))
        self.addSequential(Park(robot))
        #self.addSequential(LimeLightLEDblink(robot))
        self.addSequential(WaitCommand(timeout=2))
        self.addSequential(InvertFront(robot))
        #self.addSequential(LimeLightLEDoff(robot))

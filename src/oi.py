#!/usr/bin/python3
'''Operator Interface - one class: OI.
This is where the rubber meets the road: make the Xbox controller
do what we want it to do.
'''
from commands.punch import Punch
from commands.pull import Pull
from commands.move_arm_with_triggers import MoveArmWithTriggers
from commands.intake_cargo import IntakeCargo
from commands.cover_hatch import CoverHatch
from commands.lift_winch import LiftWinch
from commands.lower_winch import LowerWinch
from commands.punch_rear import PunchRear
from commands.pull_rear import PullRear
from commands.invert_front import InvertFront
from commands.eject_cargo import EjectCargo
from wpilib.interfaces.generichid import GenericHID

from wpilib.buttons import JoystickButton
from wpilib import XboxController
import wpilib
from thresholds import TriggerButton

class OI:
    '''Operator Interface - all button assignments and other human interface elements
    '''

    def __init__(self, robot):
        '''The Constructor - assign Xbox controller buttons to specific Commands.
        '''

        print("In OI:__init__")

        robot.xbox0 = wpilib.XboxController(0)
        robot.xbox1 = wpilib.XboxController(1)

        triggerbutton = TriggerButton(robot.xbox0, .1)
        punch = JoystickButton(robot.xbox0, XboxController.Button.kY)
        hatch = JoystickButton(robot.xbox0, XboxController.Button.kX)

        intake = JoystickButton(robot.xbox1, XboxController.Button.kA)
        liftwinch = JoystickButton(robot.xbox1, XboxController.Button.kBumperRight)
        lowerwinch = JoystickButton(robot.xbox1, XboxController.Button.kBumperLeft)
        ejectcargo = JoystickButton(robot.xbox1, XboxController.Button.kX)
        invertfront = JoystickButton(robot.xbox1, XboxController.Button.kStickRight)
        punchrear = JoystickButton(robot.xbox1, XboxController.Button.kY)

        triggerbutton.whenPressed(MoveArmWithTriggers(robot))
        intake.toggleWhenPressed(IntakeCargo(robot))
        ejectcargo.toggleWhenPressed(EjectCargo(robot))
        punch.whenPressed(Punch(robot))
        punch.whenReleased(Pull(robot))
        hatch.toggleWhenPressed(CoverHatch(robot))
        liftwinch.whileHeld(LiftWinch(robot))
        lowerwinch.whileHeld(LowerWinch(robot))
        punchrear.whenPressed(PunchRear(robot))
        punchrear.whenReleased(PullRear(robot))
        invertfront.toggleWhenPressed(InvertFront(robot))

#!/usr/bin/python3
'''Operator Interface - one class: OI.
This is where the rubber meets the road: make the Xbox controller
do what we want it to do.
'''
from commands.cover_hatch import CoverHatch
from commands.eject_cargo import EjectCargo
from commands.intake_cargo import IntakeCargo
from commands.lift_front import LiftFront
from commands.lift_rear import LiftRear
from commands.lift_winch import LiftWinch
from commands.lower_rear import LowerRear
from commands.lower_winch import LowerWinch
from commands.move_arm_with_triggers import MoveArmWithTriggers
from commands.toggle_camera import ToggleCamera
from commands.punch_rear import PunchRear
from commands.pull_rear import PullRear
from commands.park import Park
from commands.invert_front import InvertFront
import wpilib
from wpilib.interfaces.generichid import GenericHID
from wpilib.buttons import JoystickButton
from wpilib import XboxController
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

        hatch = JoystickButton(robot.xbox0, XboxController.Button.kX)
        park = JoystickButton(robot.xbox0, XboxController.Button.kBack)
        togglecamera = JoystickButton(robot.xbox0, XboxController.Button.kStart)
        triggerbutton = TriggerButton(robot.xbox0, .1)

        ejectcargo = JoystickButton(robot.xbox1, XboxController.Button.kX)
        intakecargo = JoystickButton(robot.xbox1, XboxController.Button.kA)
        frontlift = JoystickButton(robot.xbox1, XboxController.Button.kStart)
        rearlift = JoystickButton(robot.xbox1, XboxController.Button.kBack)
        invertfront = JoystickButton(robot.xbox1, XboxController.Button.kStickRight)
        liftwinch = JoystickButton(robot.xbox1, XboxController.Button.kBumperRight)
        lowerwinch = JoystickButton(robot.xbox1, XboxController.Button.kBumperLeft)
        punchrear = JoystickButton(robot.xbox1, XboxController.Button.kY)

        hatch.toggleWhenPressed(CoverHatch(robot))
        park.whileHeld(Park(robot))
        togglecamera.whenPressed(ToggleCamera(robot))
        triggerbutton.whenPressed(MoveArmWithTriggers(robot))

        ejectcargo.toggleWhenPressed(EjectCargo(robot))
        intakecargo.toggleWhenPressed(IntakeCargo(robot))
        frontlift.toggleWhenPressed(LiftFront(robot))
        rearlift.toggleWhenPressed(LiftRear(robot))
        invertfront.toggleWhenPressed(InvertFront(robot))
        liftwinch.whileHeld(LiftWinch(robot))
        lowerwinch.whileHeld(LowerWinch(robot))
        punchrear.whenReleased(PullRear(robot))
        punchrear.whenPressed(PunchRear(robot))

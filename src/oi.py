#!/usr/bin/python3
'''Operator Interface - one class: OI.
This is where the rubber meets the road: make the Xbox controller
do what we want it to do.
'''
from commands.punch import Punch
from commands.pull import Pull
from commands.open_claw import OpenClaw
from commands.close_claw import CloseClaw
from commands.move_arm_with_triggers import MoveArmWithTriggers
from commands.intake_cargo import IntakeCargo
from commands.cover_hatch import CoverHatch
from commands.lift_winch import LiftWinch
from commands.lower_winch import LowerWinch
from commands.release_and_punch import ReleaseAndPunch
from commands.close_and_pull import CloseAndPull
from commands.punch_rear import PunchRear
from commands.park import Park
from commands.eject_cargo import EjectCargo
from wpilib.interfaces.generichid import GenericHID

from commands.lift import Lift
from commands.lower import Lower
from commands.lift_rear import LiftRear
from commands.lower_rear import LowerRear
from commands.lift_front import LiftFront
from commands.lower_front import LowerFront
from commands.lift_left import LiftLeft
from commands.lower_left import LowerLeft
from commands.lift_right import LiftRight
from commands.lower_right import LowerRight

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

        #liftleft = JoystickButton(robot.xbox1, XboxController.Button.kA)
        release_and_punch = JoystickButton(robot.xbox0, XboxController.Button.kA)
        close_and_pull = JoystickButton(robot.xbox0, XboxController.Button.kA)
        # liftleft = JoystickButton(robot.xbox1, XboxController.Button.kA)
        # lowerleft = JoystickButton(robot.xbox1, XboxController.Button.kB)
        # liftright = JoystickButton(robot.xbox1, XboxController.Button.kX)
        # lowerright = JoystickButton(robot.xbox1, XboxController.Button.kY)
        # liftfront = JoystickButton(robot.xbox1, XboxController.Button.kStickLeft)
        # lowerfront = JoystickButton(robot.xbox1, XboxController.Button.kStickRight)
        # liftrear = JoystickButton(robot.xbox1, XboxController.Button.kBumperRight)
        # lowerrear = JoystickButton(robot.xbox1, XboxController.Button.kBumperLeft)
        # lift = JoystickButton(robot.xbox1, XboxController.Button.kStart)
        # lower = JoystickButton(robot.xbox1, XboxController.Button.kBack)


        punchrear = JoystickButton(robot.xbox1, XboxController.Button.kY)
        intake = JoystickButton(robot.xbox1, XboxController.Button.kA)
        eject = JoystickButton(robot.xbox1, XboxController.Button.kB)
        # liftwinch = JoystickButton(robot.xbox1, XboxController.Button.kBumperRight)
        # lowerwinch = JoystickButton(robot.xbox1, XboxController.Button.kBumperLeft)
        park = JoystickButton(robot.xbox1, XboxController.Button.kX)
        
        triggerbutton = TriggerButton(robot.xbox0, .1)
        punch = JoystickButton(robot.xbox0, XboxController.Button.kY)
        open_claw = JoystickButton(robot.xbox0, XboxController.Button.kB)
        close_claw = JoystickButton(robot.xbox0, XboxController.Button.kB)
        hatch = JoystickButton(robot.xbox0, XboxController.Button.kX)
        # liftwinch = JoystickButton(robot.xbox0, XboxController.Button.kBumperRight)
        # lowerwinch = JoystickButton(robot.xbox0, XboxController.Button.kBumperLeft)

        # liftleft.whileHeld(LiftLeft(robot))
        # lowerleft.whileHeld(LowerLeft(robot))
        # liftright.whileHeld(LiftRight(robot))
        # lowerright.whileHeld(LowerRight(robot))
        # liftfront.whileHeld(LiftFront(robot))
        # lowerfront.whileHeld(LowerFront(robot))
        # liftrear.whileHeld(LiftRear(robot))
        # lowerrear.whileHeld(LowerRear(robot))
        # lift.whileHeld(Lift(robot))
        # lower.whileHeld(Lower(robot))

        triggerbutton.whenPressed(MoveArmWithTriggers(robot))
        intake.toggleWhenPressed(IntakeCargo(robot))
        eject.toggleWhenPressed(EjectCargo(robot))
        # claw.toggleWhenPressed(OpenClaw(robot))
        punch.whenPressed(Punch(robot))
        punch.whenReleased(Pull(robot))
        hatch.toggleWhenPressed(CoverHatch(robot))
        # liftwinch.whileHeld(LiftWinch(robot))
        # lowerwinch.whileHeld(LowerWinch(robot))
        release_and_punch.whileHeld(ReleaseAndPunch(robot))
        close_and_pull.whenReleased(CloseAndPull(robot))
        open_claw.whenPressed(OpenClaw(robot))
        close_claw.whenPressed(CloseClaw(robot))
        punchrear.whileHeld(PunchRear(robot))
        park.whileHeld(Park(robot))

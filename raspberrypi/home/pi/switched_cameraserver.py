#!/usr/bin/env python3
#
# Uses the CameraServer class to automatically capture video from two USB
# webcams and send one of them to the dashboard without doing any processing.
# To switch between the cameras, change the /CameraPublisher/selected value in NetworkTables
#
# Warning: If you're using this with a python-based robot, do not run this
# in the same program as your robot code!
#

from cscore import CameraServer, UsbCamera
import networktables


def main():
    cs = CameraServer.getInstance()
    cs.enableLogging()

    usb0 = UsbCamera('Camera 0', 0)
    usb1 = UsbCamera('Camera 1', 1)

    cams = [usb0, usb1]

    # Add a "Switched" camera opject to Network Tables,
    # and set the source to the first camera (0)
    server = cs.addSwitchedCamera('Switched')
    server.setSource(cams[0])

    # Use networktables to switch the camera source.
    #
    # We set the camera source to the camera object in the "cams"
    # dictionary.
    #
    # "value" MUST be 0 (zero) or 1 (one) in order for this to work
    def _listener(source, key, value, isNew):
        server.setSource(cams[value])

    table = networktables.NetworkTables.getTable('/CameraPublisher')
    table.putNumber('selected', 0)
    table.addEntryListener(_listener, key='selected')

    cs.waitForever()


if __name__ == '__main__':

    # To see messages from networktables, you must setup logging
    import logging

    logging.basicConfig(level=logging.DEBUG)

    # You should change this to connect to the RoboRIO
    networktables.NetworkTables.initialize(server='10.59.3.2')

    main()

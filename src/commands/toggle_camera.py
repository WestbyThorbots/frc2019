#/usr/bin/python3

import cscore

class ToggleCamera:

    def toggleCamera(self, robot):
        if self.currentCam == "1":
            self.cs.startAutomaticCapture(name = "2")
            self.currentCam = "2"
        else:
            self.cs.startAutomaticCapture(name = "1")
            self.currentCam = "1"

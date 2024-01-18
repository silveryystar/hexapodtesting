from pipython import GCSDevice
from time import sleep
from operational import home


def range_req(pidevice, direction, value):
    """
    Command the hexapod to move to its home position.
    Record the values of X, Y, and Z.
    Command the hexapod to move at least 500 microns in z-prime.
    Verify from the measured values of (X, Y, Z) that the range was achieved.
    Repeat for -500 microns in z-prime.
    Command the hexapod to move at least 118 microns in x-prime.
    Verify from the measured values of (X, Y, Z) that the range was achieved.
    Repeat for -118 microns in x-prime.
    Repeat for y-prime.
    """
    home(pidevice)
    pidevice.MOV({direction: value})
    print(pidevice.qPOS())
    sleep(1)

    home(pidevice)
    pidevice.MOV({direction: -value})
    print(pidevice.qPOS())
    sleep(1)


with GCSDevice("C-184") as pidevice:
    pidevice.InterfaceSetupDlg()
    range_req(pidevice, "Z", 0.500)
    range_req(pidevice, "X", 0.118)
    range_req(pidevice, "Y", 0.118)

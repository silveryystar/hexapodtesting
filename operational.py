from pipython import GCSDevice
from time import sleep

# TODO: "operational.py" serves as "main.py" for "TODO" purposes.

# TODO: Upload to GitHub for safe-keeping.
# TODO: Script "Measuring pitch, yaw, and roll angles".
# TODO: Script "Measuring flexure of the hexapod".

# TODO: Fix variable "pidevice" confusion in all ".py" files.
# TODO: Verify whether ".MOV()" positions are in millimeters (mm).
# TODO: Verify whether ".InterfaceSetupDlg()" requires "key=".
# TODO: Consider simplification of ".MOV(), print(), sleep()" commonality.
# TODO: Check code for accuracy and precision as per "Procedures".
# TODO: Find method to test code, then test code.
# TODO: Create README.md specifying installation process.
# TODO: Confirm hexapod is "C-184" ("C-3PO" would have been cooler...).


def home(pidevice):
    """
    Command the hexapod to move to its home position.
    """
    pidevice.MOV({"X": 0, "Y": 0, "Z": 0})  # TODO: Verify positions are in millimeters.
    print(pidevice.qPOS())  # Prints hexapod's self-identified position.


def increment_req(pidevice, direction):
    """
    Command the hexapod to move to its home position.
    Reset value on indicator.
    Command the hexapod to move an increment of 0.2 microns in the centerline axis direction.
    Record an indicator reading.
    Repeat for a total overall motion of 50 microns.
    Record final position.
    """
    home(pidevice)
    a = 0
    while a != 0.05:  # Final position.
        a += 0.002  # Increments to obtain final position.
        pidevice.move({direction: a})
        print(pidevice.qPOS())
        sleep(1)  # Prevents hexapod from instantly moving to 50 microns. Units: (second).


with GCSDevice("C-184") as pidevice:  # "pidevice" is the hexapod.
    pidevice.InterfaceSetupDlg()  # TODO: Key?
    increment_req(pidevice, "X")
    increment_req(pidevice, "Y")
    increment_req(pidevice, "Z")

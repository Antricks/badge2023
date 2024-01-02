import board
from time import sleep
from busio import I2C
from PN7150 import PN7150

if True:
    # Fast 400KHz I2C
    i2c = I2C(board.SCL, board.SDA, frequency = 400000)
else:
    # Regular 100kHz I2C
    i2c = board.I2C()

nfc = PN7150(i2c, board.IRQ, board.VEN, debug=True)

assert nfc.connect()
print("Connected.")

assert nfc.emulation_setup_nfca()
print("Set up as 37c3 test card emulator")

while True:
    nfc.dropInput()
    sleep(0.01)

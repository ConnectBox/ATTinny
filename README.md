# ATTinny
Code for battery management of CM4 design

This code runs on the AT Tiny processor on the Battery Board of the CM4 design.  It manages the batterie switching and communicates with the CM4 to get battery voltages from tthe AXP209.  This code works in a symbiotic way with the CM4 code.

ATTinny code can be burned into the process in system over the SPI bus.  The CM4 is loaded with Averdude to do this programming.
The CM4 communicates with the AT Tiny over the I2C bus at address 0x14

The ATTiny has the following address registers on I2C for read/write:

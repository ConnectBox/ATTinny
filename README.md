# ATTinny
Code for battery management of CM4 design

This code runs on the AT Tiny processor on the Battery Board of the CM4 design.  It manages the batterie switching and communicates with the CM4 to get battery voltages from tthe AXP209.  This code works in a symbiotic way with the CM4 code.

ATTinny code can be burned into the process in system over the SPI bus.  The CM4 is loaded with Averdude to do this programming.
The CM4 communicates with the AT Tiny over the I2C bus at address 0x14

The ATTiny has the following address registers on I2C for read/write:

Registers:
 Current command table: 

 *  COMMAND        
 *   0x10    Request for revision of this code
 *   
 *   0x21    Read / Write battery voltage of Battery 1
 *   0x22    Read / Write battery voltage of Battery 2
 *   0x23    Read / Write battery voltage of Battery 3
 *   0x24    Read / Write battery voltage of Battery 4
 *   
 *   0x29    Read voltage of Charger 5V line (LSB) (mV)
 *   0x2A    Read voltage of Charger 5V line (USB) (mV)
 *   
 *   0x30    Read number of batteries attached
 *   0x31    Read number of the battery currently in use [1 -> 4]
 *   0x32    Read battery positions populated (binary, bit 0-3 => battery 1 -> 4)
 *   
 *   0x40   Heartbeat... set to 1 each time CM4 reads register 0x31 
 *   
 *   0x50 and higher used for testing and debug 

 *  Battery Voltage Math: we need to have CM4 send battery voltages in mv up to 4100 (0x1004)
 *  If we limit our voltages to 4096mV, then the CM4 can divide the mv of a battery by 16, ship that
 *  number as the battery voltage, then on this end we can multiply by 16 to get the 
 *  battery voltage in mv. (Actually 255*16 = 4080 so if actual V is greater, we just send 0xFF (255))
 *  Example: Battery V = 3700 mv, we do 3700 / 16 =231 (0xE7) so we send 0xE7 
 *  SO... Battery voltage stored in mV with resolution of 16 mV lets us use a single byte for storage.  
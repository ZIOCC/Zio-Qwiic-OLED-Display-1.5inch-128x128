from machine import Pin,I2C
import ssd1327


i2c = I2C(sda=Pin("Y8"), scl=Pin("Y6"))
display = ssd1327.SSD1327_I2C(128, 128, i2c)

# Unlock
display.write_cmd(0xFD)
display.write_cmd(0x12)
#
# # Display off
# display.write_cmd(0xAE)

# Set column address 0-127
display.write_cmd(0x15)
display.write_cmd(0x00) # was 0x08 on 96x96 ((128-width)/depth)=8
display.write_cmd(0x7F) # was 0x37 on 96x96 (63-((128-width)/depth))=55

# Set row address 0-127
display.write_cmd(0x75)
display.write_cmd(0x00)
display.write_cmd(0x7F) # was 0x5F on 96x96 (height-1=95)

# Set start line = 0
display.write_cmd(0xA1)
display.write_cmd(0x00)

# Display offset = 0
display.write_cmd(0xA2)
display.write_cmd(0x00) # was 0x20 on 96x96 (128-height=32)

# Display normal
display.write_cmd(0xA4)

# Set multiplex ratio
display.write_cmd(0xA8)
display.write_cmd(0x7F) # was 0x5F on 96x96 (height-1=95)

# Test
display.fill(0)
display.text('ABCDEFGHIJKLMNOP',0,0*8,15)
display.text('b Line 2',0,1*8,15)
display.text('c Line 3',0,2*8,15)
display.text('d Line 4',0,3*8,15)
display.text('e Line 5',0,4*8,15)
display.text('f Line 6',0,5*8,15)
display.text('g Line 7',0,6*8,15)
display.text('h Line 8',0,7*8,15)
display.text('i Line 9',0,8*8,15)
display.text('j Line 10',0,9*8,15)
display.text('k Line 11',0,10*8,15)
display.text('l Line 12',0,11*8,15)
display.text('m Line 13',0,12*8,15)
display.text('n Line 14',0,13*8,15)
display.text('o Line 15',0,14*8,15)
display.text('p Line 16',0,15*8,15)
display.show()

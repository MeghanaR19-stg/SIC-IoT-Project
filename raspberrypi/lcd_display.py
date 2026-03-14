from RPLCD.i2c import CharLCD

# initialize LCD
lcd = CharLCD('PCF8574', 0x27)

def show_status(name, heart_rate, temperature):

    lcd.clear()

    # show patient name
    lcd.write_string(name)

    # move to second line
    lcd.cursor_pos = (1,0)

    # check alert condition
    if heart_rate > 120 or temperature > 37.8:

        lcd.write_string("ALERT!")

        print("ALERT:", name)

    else:

        lcd.write_string("Normal")

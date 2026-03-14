from RPLCD.i2c import CharLCD

lcd = CharLCD('PCF8574', 0x27)

def show_alert(name, message):
    lcd.clear()
    lcd.write_string(name)
    lcd.crlf()
    lcd.write_string(message)

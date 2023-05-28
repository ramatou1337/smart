def on_logo_touched():
    global passwd_enter
    pins.servo_write_pin(AnalogPin.P8, 0)
    I2C_LCD1602.clear()
    I2C_LCD1602.show_string("entrer le mot de passe", 0, 0)
    passwd_enter = ""
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

def on_bluetooth_connected():
    global connect, ble_val, window_flag
    basic.show_icon(IconNames.HAPPY)
    connect = 1
    while connect == 1:
        ble_val = bluetooth.uart_read_until(serial.delimiters(Delimiters.HASH))
        serial.write_string("" + (ble_val))
        serial.write_line("")
        if ble_val == "a":
            pins.digital_write_pin(DigitalPin.P16, 1)
        elif ble_val == "b":
            pins.digital_write_pin(DigitalPin.P16, 0)
        elif ble_val == "c":
            pins.servo_write_pin(AnalogPin.P8, 180)
        elif ble_val == "d":
            pins.servo_write_pin(AnalogPin.P8, 0)
        elif ble_val == "e":
            window_flag = 0
            pins.servo_write_pin(AnalogPin.P9, 0)
        elif ble_val == "f":
            pins.servo_write_pin(AnalogPin.P9, 125)
            window_flag = 1
        elif ble_val == "g":
            I2C_LCD1602.backlight_off()
            basic.clear_screen()
            basic.pause(100)
            pins.analog_write_pin(AnalogPin.P12, 1023)
            pins.analog_write_pin(AnalogPin.P13, 300)
        elif ble_val == "h":
            pins.analog_write_pin(AnalogPin.P12, 0)
            pins.analog_write_pin(AnalogPin.P13, 0)
            I2C_LCD1602.backlight_on()
            basic.show_icon(IconNames.HAPPY)
        neopixel_mode()
        face_mode()
        sensor_mode()
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    basic.show_icon(IconNames.SAD)
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def on_button_pressed_a():
    global passwd_enter
    passwd_enter = "" + passwd_enter + "."
    I2C_LCD1602.show_string(passwd_enter, 0, 1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def face_mode():
    if ble_val == "1":
        basic.show_icon(IconNames.HAPPY)
    elif ble_val == "2":
        basic.show_icon(IconNames.SAD)
    elif ble_val == "3":
        basic.show_icon(IconNames.ASLEEP)
    elif ble_val == "4":
        basic.show_icon(IconNames.HEART)
    elif ble_val == "5":
        basic.show_icon(IconNames.DUCK)
    elif ble_val == "6":
        basic.show_icon(IconNames.HOUSE)
    elif ble_val == "0":
        basic.clear_screen()

def on_button_pressed_ab():
    global passwd_enter
    I2C_LCD1602.clear()
    if passwd_enter == password:
        I2C_LCD1602.show_string("correct", 0, 0)
        I2C_LCD1602.show_string("ouverture de la porte", 0, 1)
        pins.servo_write_pin(AnalogPin.P8, 180)
        passwd_enter = ""
    else:
        I2C_LCD1602.show_string("reessayer", 0, 0)
        I2C_LCD1602.show_string("erreur", 0, 1)
        passwd_enter = ""
        basic.pause(1000)
        I2C_LCD1602.clear()
        I2C_LCD1602.show_string("entrer le mot de passe", 0, 0)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global passwd_enter
    passwd_enter = "" + passwd_enter + "-"
    I2C_LCD1602.show_string(passwd_enter, 0, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

def sensor_mode():
    global temp_flag, water_flag, gas_flag, people_flag
    if ble_val == "o":
        I2C_LCD1602.clear()
        temp_flag = 1
    elif ble_val == "p":
        I2C_LCD1602.clear()
        water_flag = 1
    elif ble_val == "q":
        gas_flag = 1
    elif ble_val == "r":
        people_flag = 1
    elif ble_val == "x":
        water_flag = 0
        temp_flag = 0
        people_flag = 0
        gas_flag = 0
        I2C_LCD1602.clear()
        I2C_LCD1602.show_string("entrer le mot de passe", 0, 0)
def neopixel_mode():
    global neo_count
    if ble_val == "i":
        neo_count += 1
        if neo_count >= 9:
            neo_count = 9
    elif ble_val == "j":
        neo_count += -1
        if neo_count <= 1:
            neo_count = 1
    elif ble_val == "k":
        neo_count = 0
    if neo_count == 1:
        strip.show_color(neopixel.colors(NeoPixelColors.RED))
    elif neo_count == 2:
        strip.show_color(neopixel.colors(NeoPixelColors.ORANGE))
    elif neo_count == 3:
        strip.show_color(neopixel.colors(NeoPixelColors.YELLOW))
    elif neo_count == 4:
        strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
    elif neo_count == 5:
        strip.show_color(neopixel.colors(NeoPixelColors.BLUE))
    elif neo_count == 6:
        strip.show_color(neopixel.colors(NeoPixelColors.INDIGO))
    elif neo_count == 7:
        strip.show_color(neopixel.colors(NeoPixelColors.VIOLET))
    elif neo_count == 8:
        strip.show_color(neopixel.colors(NeoPixelColors.PURPLE))
    elif neo_count == 9:
        strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
    elif neo_count == 0:
        strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
someone_flag = 0
security_flag = 0
dangerous_flag = 0
water_val = 0
people_flag = 0
gas_flag = 0
water_flag = 0
temp_flag = 0
ble_val = ""
connect = 0
passwd_enter = ""
window_flag = 0
password = ""
neo_count = 0
strip: neopixel.Strip = None
serial.redirect(SerialPin.USB_TX, SerialPin.USB_RX, BaudRate.BAUD_RATE9600)
basic.show_icon(IconNames.HOUSE)
pins.servo_write_pin(AnalogPin.P9, 125)
I2C_LCD1602.lcd_init(39)
I2C_LCD1602.clear()
basic.pause(100)
I2C_LCD1602.show_string("entrer le mot de passe", 0, 0)
pins.digital_write_pin(DigitalPin.P16, 0)
strip = neopixel.create(DigitalPin.P14, 4, NeoPixelMode.RGB)
strip.clear()
strip.show()
neo_count = 0
password = "..--"
window_flag = 1

def on_forever():
    global water_val, dangerous_flag, security_flag, someone_flag
    water_val = pins.analog_read_pin(AnalogPin.P0)
    if water_val > 200 and window_flag == 1:
        pins.servo_write_pin(AnalogPin.P9, 0)
    elif water_val <= 200 and window_flag == 1:
        pins.servo_write_pin(AnalogPin.P9, 125)
    if temp_flag == 1:
        for index in range(1):
            I2C_LCD1602.show_string("temperature", 0, 0)
        I2C_LCD1602.show_number(input.temperature(), 0, 1)
        basic.pause(500)
    elif water_flag == 1:
        for index2 in range(1):
            I2C_LCD1602.show_string("capteur de valeur", 0, 0)
        I2C_LCD1602.show_number(pins.analog_read_pin(AnalogPin.P0), 0, 1)
        basic.pause(500)
    elif gas_flag == 1:
        if pins.digital_read_pin(DigitalPin.P1) == 0:
            if dangerous_flag == 0:
                I2C_LCD1602.clear()
                I2C_LCD1602.show_string("dangereux", 0, 0)
                basic.pause(500)
                dangerous_flag = 1
                security_flag = 0
        else:
            if security_flag == 0:
                I2C_LCD1602.clear()
                I2C_LCD1602.show_string("sécurité", 0, 0)
                basic.pause(500)
                dangerous_flag = 0
                security_flag = 1
    elif people_flag == 1:
        if pins.digital_read_pin(DigitalPin.P15) == 1:
            if someone_flag == 0:
                I2C_LCD1602.clear()
                I2C_LCD1602.show_string("présence de personne ", 0, 0)
                basic.pause(500)
                someone_flag = 1
        else:
            if someone_flag == 1:
                I2C_LCD1602.clear()
                I2C_LCD1602.show_string("RAS", 0, 0)
                basic.pause(500)
                someone_flag = 0
basic.forever(on_forever)

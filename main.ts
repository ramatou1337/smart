input.onLogoEvent(TouchButtonEvent.Touched, function () {
    pins.servoWritePin(AnalogPin.P8, 0)
    I2C_LCD1602.clear()
    I2C_LCD1602.ShowString("entrer le mot de passe", 0, 0)
    passwd_enter = ""
})
bluetooth.onBluetoothConnected(function () {
    basic.showIcon(IconNames.Happy)
    connect = 1
    while (connect == 1) {
        ble_val = bluetooth.uartReadUntil(serial.delimiters(Delimiters.Hash))
        serial.writeString("" + (ble_val))
        serial.writeLine("")
        if (ble_val == "a") {
            pins.digitalWritePin(DigitalPin.P16, 1)
        } else if (ble_val == "b") {
            pins.digitalWritePin(DigitalPin.P16, 0)
        } else if (ble_val == "c") {
            pins.servoWritePin(AnalogPin.P8, 180)
        } else if (ble_val == "d") {
            pins.servoWritePin(AnalogPin.P8, 0)
        } else if (ble_val == "e") {
            window_flag = 0
            pins.servoWritePin(AnalogPin.P9, 0)
        } else if (ble_val == "f") {
            pins.servoWritePin(AnalogPin.P9, 125)
            window_flag = 1
        } else if (ble_val == "g") {
            I2C_LCD1602.BacklightOff()
            basic.clearScreen()
            basic.pause(100)
            pins.analogWritePin(AnalogPin.P12, 1023)
            pins.analogWritePin(AnalogPin.P13, 300)
        } else if (ble_val == "h") {
            pins.analogWritePin(AnalogPin.P12, 0)
            pins.analogWritePin(AnalogPin.P13, 0)
            I2C_LCD1602.BacklightOn()
            basic.showIcon(IconNames.Happy)
        }
        neopixel_mode()
        face_mode()
        sensor_mode()
    }
})
bluetooth.onBluetoothDisconnected(function () {
    basic.showIcon(IconNames.Sad)
})
input.onButtonPressed(Button.A, function () {
    passwd_enter = "" + passwd_enter + "."
    I2C_LCD1602.ShowString(passwd_enter, 0, 1)
})
function face_mode () {
    if (ble_val == "1") {
        basic.showIcon(IconNames.Happy)
    } else if (ble_val == "2") {
        basic.showIcon(IconNames.Sad)
    } else if (ble_val == "3") {
        basic.showIcon(IconNames.Asleep)
    } else if (ble_val == "4") {
        basic.showIcon(IconNames.Heart)
    } else if (ble_val == "5") {
        basic.showIcon(IconNames.Duck)
    } else if (ble_val == "6") {
        basic.showIcon(IconNames.House)
    } else if (ble_val == "0") {
        basic.clearScreen()
    }
}
input.onButtonPressed(Button.AB, function () {
    I2C_LCD1602.clear()
    if (passwd_enter == password) {
        I2C_LCD1602.ShowString("correct", 0, 0)
        I2C_LCD1602.ShowString("ouverture de la porte", 0, 1)
        pins.servoWritePin(AnalogPin.P8, 180)
        passwd_enter = ""
    } else {
        I2C_LCD1602.ShowString("reessayer", 0, 0)
        I2C_LCD1602.ShowString("erreur", 0, 1)
        passwd_enter = ""
        basic.pause(1000)
        I2C_LCD1602.clear()
        I2C_LCD1602.ShowString("entrer le mot de passe", 0, 0)
    }
})
input.onButtonPressed(Button.B, function () {
    passwd_enter = "" + passwd_enter + "-"
    I2C_LCD1602.ShowString(passwd_enter, 0, 1)
})
function sensor_mode () {
    if (ble_val == "o") {
        I2C_LCD1602.clear()
        temp_flag = 1
    } else if (ble_val == "p") {
        I2C_LCD1602.clear()
        water_flag = 1
    } else if (ble_val == "q") {
        gas_flag = 1
    } else if (ble_val == "r") {
        people_flag = 1
    } else if (ble_val == "x") {
        water_flag = 0
        temp_flag = 0
        people_flag = 0
        gas_flag = 0
        I2C_LCD1602.clear()
        I2C_LCD1602.ShowString("entrer le mot de passe", 0, 0)
    }
}
function neopixel_mode () {
    if (ble_val == "i") {
        neo_count += 1
        if (neo_count >= 9) {
            neo_count = 9
        }
    } else if (ble_val == "j") {
        neo_count += -1
        if (neo_count <= 1) {
            neo_count = 1
        }
    } else if (ble_val == "k") {
        neo_count = 0
    }
    if (neo_count == 1) {
        strip.showColor(neopixel.colors(NeoPixelColors.Red))
    } else if (neo_count == 2) {
        strip.showColor(neopixel.colors(NeoPixelColors.Orange))
    } else if (neo_count == 3) {
        strip.showColor(neopixel.colors(NeoPixelColors.Yellow))
    } else if (neo_count == 4) {
        strip.showColor(neopixel.colors(NeoPixelColors.Green))
    } else if (neo_count == 5) {
        strip.showColor(neopixel.colors(NeoPixelColors.Blue))
    } else if (neo_count == 6) {
        strip.showColor(neopixel.colors(NeoPixelColors.Indigo))
    } else if (neo_count == 7) {
        strip.showColor(neopixel.colors(NeoPixelColors.Violet))
    } else if (neo_count == 8) {
        strip.showColor(neopixel.colors(NeoPixelColors.Purple))
    } else if (neo_count == 9) {
        strip.showColor(neopixel.colors(NeoPixelColors.White))
    } else if (neo_count == 0) {
        strip.showColor(neopixel.colors(NeoPixelColors.Black))
    }
}
let someone_flag = 0
let security_flag = 0
let dangerous_flag = 0
let water_val = 0
let people_flag = 0
let gas_flag = 0
let water_flag = 0
let temp_flag = 0
let ble_val = ""
let connect = 0
let passwd_enter = ""
let window_flag = 0
let password = ""
let neo_count = 0
let strip: neopixel.Strip = null
serial.redirect(
SerialPin.USB_TX,
SerialPin.USB_RX,
BaudRate.BaudRate9600
)
basic.showIcon(IconNames.House)
pins.servoWritePin(AnalogPin.P9, 125)
I2C_LCD1602.LcdInit(39)
I2C_LCD1602.clear()
basic.pause(100)
I2C_LCD1602.ShowString("entrer le mot de passe", 0, 0)
pins.digitalWritePin(DigitalPin.P16, 0)
strip = neopixel.create(DigitalPin.P14, 4, NeoPixelMode.RGB)
strip.clear()
strip.show()
neo_count = 0
password = "..--"
window_flag = 1
basic.forever(function () {
    water_val = pins.analogReadPin(AnalogPin.P0)
    if (water_val > 200 && window_flag == 1) {
        pins.servoWritePin(AnalogPin.P9, 0)
    } else if (water_val <= 200 && window_flag == 1) {
        pins.servoWritePin(AnalogPin.P9, 125)
    }
    if (temp_flag == 1) {
        for (let index = 0; index < 1; index++) {
            I2C_LCD1602.ShowString("temperature", 0, 0)
        }
        I2C_LCD1602.ShowNumber(input.temperature(), 0, 1)
        basic.pause(500)
    } else if (water_flag == 1) {
        for (let index = 0; index < 1; index++) {
            I2C_LCD1602.ShowString("capteur de valeur", 0, 0)
        }
        I2C_LCD1602.ShowNumber(pins.analogReadPin(AnalogPin.P0), 0, 1)
        basic.pause(500)
    } else if (gas_flag == 1) {
        if (pins.digitalReadPin(DigitalPin.P1) == 0) {
            if (dangerous_flag == 0) {
                I2C_LCD1602.clear()
                I2C_LCD1602.ShowString("dangereux", 0, 0)
                basic.pause(500)
                dangerous_flag = 1
                security_flag = 0
            }
        } else {
            if (security_flag == 0) {
                I2C_LCD1602.clear()
                I2C_LCD1602.ShowString("sécurité", 0, 0)
                basic.pause(500)
                dangerous_flag = 0
                security_flag = 1
            }
        }
    } else if (people_flag == 1) {
        if (pins.digitalReadPin(DigitalPin.P15) == 1) {
            if (someone_flag == 0) {
                I2C_LCD1602.clear()
                I2C_LCD1602.ShowString("présence de personne ", 0, 0)
                basic.pause(500)
                someone_flag = 1
            }
        } else {
            if (someone_flag == 1) {
                I2C_LCD1602.clear()
                I2C_LCD1602.ShowString("RAS", 0, 0)
                basic.pause(500)
                someone_flag = 0
            }
        }
    }
})

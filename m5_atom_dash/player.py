# Buzzer sounds player

from machine import PWM
import time
from notes import note_freq

class Player:
    
    def play_tone(frequency, duration, duty=32768):
        pwm = PWM(33)
        pwm.freq(frequency)
        pwm.duty_u16(duty)  # Duty cycle for volume control
        time.sleep(duration)
        pwm.deinit()

    def play_tune(tune, duty = 16384):
        for note in tune:
            Player.play_tone(note_freq[note[0]], note[1], duty)

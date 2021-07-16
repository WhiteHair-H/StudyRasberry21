import RPi.GPIO as GPIO
import dht11
import time

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 4
instance = dht11.DHT11(pin = 4)

while True:
    try:
        start = time.time()
        result = instance.read()
        while (time.time() - start) < 1.0:
            pass

        if result.is_valid():
            print("Temperature: %-3.1f C" % result.temperature)
            print("Humidity: %-3.1f %%" % result.humidity)
        else:
            pass

    except KeyboardInterrupt:
        GPIO.cleanup()
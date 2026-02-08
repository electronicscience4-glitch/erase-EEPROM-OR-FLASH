import os
import machine
import utime
filename = "data.txt" # ناوی فایل
led = machine.Pin(25, machine.Pin.OUT)# LEDی ناوەکی 
print("=" * 40)
print("سیستەمی سڕینەوەی فایل")
print("بۆرد: Raspberry Pi Pico")
print("=" * 40)
led.off()  
files = os.listdir() 
if filename in files:
    print(f" fail '{filename}' nadozrayawa")  
    file_size = os.stat(filename)[6] 
    print(f"Qabaray fail: {file_size} baet")
    for _ in range(3):    # لێدانەکانی ڕەشتی (یارمەتی بۆ بینین)
        led.on()
        utime.sleep(0.1)
        led.off()
        utime.sleep(0.1)
    try:     
        os.remove(filename)
        print("fail srayawa")
        led.on() 
        utime.sleep(3)
        led.off()
    except Exception as e:
        print(f" هەڵە لە سڕینەوەی فایل: {e}")
        for _ in range(10): # لێدانی خێرای LED (نیشاندانی هەڵە)
            led.on()
            utime.sleep(0.05)
            led.off()
            utime.sleep(0.05) 
else:
    print(f"فایلی '{filename}' بوونی نییە!")
    for _ in range(2):    # لێدانی 2 جار (نیشاندانی بوونی نییە)
        led.on()
        utime.sleep(0.3)
        led.off()
        utime.sleep(0.3)
print("=" * 40)
print("کۆتایی!")
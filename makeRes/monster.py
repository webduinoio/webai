import sensor,lcd,time
import KPU as kpu
from _board import webai

def showMessage(msg):
    lcd.clear()
    lcd.draw_string(int(311-len(msg)*6.9)//2,224//2,msg,lcd.WHITE)

lcd.init(freq=15000000)
lcd.clear()
showMessage("init camera")
sensor.reset(freq=20000000)
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_windowing((320, 224))
sensor.skip_frames(time = 2000)
sensor.set_vflip(1)
sensor.set_auto_gain(1)
sensor.set_auto_whitebal(1)
sensor.set_auto_exposure(1)
sensor.set_brightness(2)
sensor.run(1)

classes = ['Green', 'Red', 'Yellow','Blue']
colors = [(0, 255, 0), (255, 0, 0),(255, 255, 0),(0, 0, 255)]

# load model
showMessage("load model")
task = kpu.load(webai.res.monster())
anchor = (1.889, 2.5245, 2.9465, 3.94056, 3.99987, 5.3658, 5.155437, 6.92275, 6.718375, 9.01025)
kpu.init_yolo2(task, 0.5, 0.3, 5, anchor)
print("init yolo finish")

while True:
    try:
        img = sensor.snapshot()
        code = kpu.run_yolo2(task, img)
        if code:
            for i in code:
                mycolor = colors[i.classid()]
                img.draw_rectangle(i.rect(), color=mycolor, thickness=5, fill=False)
            lcd.display(img)
            time.sleep(0.05)
        else:
            lcd.display(img)
    except Exception as e:
        print(e)

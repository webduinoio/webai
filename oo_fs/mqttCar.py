from _board import webai
from webai import mcar
import machine , ubinascii , os , time , gc , sensor

mcar.init()
def cmd(name,msg):
    webai.cmdProcess.sub(name,msg)
    if msg == 'up':
        webai.show(img=webai.res.loadImg('mrun.jpg'))
        mcar.forward(50)
    if msg == 'down':
        webai.show(img=webai.res.loadImg('m02.jpg'))
        mcar.backward(50)
    if msg == 'left':
        webai.show(img=webai.res.loadImg('mleft.jpg'))
        mcar.left(50)
    if msg == 'right':
        webai.show(img=webai.res.loadImg('mright.jpg'))
        mcar.right(50)
    if msg == 'reset':
        webai.show(img=webai.res.loadImg('m01.jpg'))
        mcar.stop()
    if msg == '開心':
        webai.speaker.play(filename="logo.wav")

webai.show(img=webai.res.loadImg('mooncar.jpg'))
webai.mqtt.sub('PING',cmd,includeID=True)

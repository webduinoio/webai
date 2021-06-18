from webai import *
from webai_blockly import Lcd, Camera, Speaker
import random, time

random.seed(time.ticks_ms())
monster = None
view = Lcd()
camera = Camera()
sp = Speaker()

webai.asr.init(fromRes=True)
view.displayImg(img=(webai.res.loadImg('m01.jpg')))

def capture():
  global view
  global camera

  view.drawString(x=120, y=110, text=b"{var}".format(var='自拍中'), color=0xFFFF, scale=1.5, x_spacing=20, mono_space=False)
  view.clear()
  view.displayImg(img=(camera.snapshot()))

def whoAreYou():
  global webai
  global sp

  view.displayImg(img=(webai.res.loadImg('m01.jpg')))
  sp.setVolume(90)
  sp.start(fileName='intro', sample_rate=11025)


def areYouOk():
  global random
  global monster
  global sp
  global webai
  sp.setVolume(90)
  monster = random.randint(1, 4)
  if monster == 1:
    view.displayImg(img=(webai.res.loadImg('red.jpg')))
    sp.setVolume(70)
    sp.start(fileName='angry', sample_rate=11025)
  elif monster == 2:
    view.displayImg(img=(webai.res.loadImg('green.jpg')))
    sp.setVolume(70)
    sp.start(fileName='happy', sample_rate=11025)
  elif monster == 3:
    view.displayImg(img=(webai.res.loadImg('yellow.jpg')))
    sp.setVolume(60)
    sp.start(fileName='laugh', sample_rate=11025)
  else:
    view.displayImg(img=(webai.res.loadImg('blue.jpg')))
    sp.setVolume(20)
    sp.start(fileName='cry', sample_rate=11025)

webai.asr.set_dtw_threshold(dtw_threshold=350)
webai.asr.addASRListener(0, areYouOk)
webai.asr.addASRListener(1, capture)
webai.asr.addASRListener(2, whoAreYou)
webai.asr.addASRListener(3, areYouOk)
webai.asr.addASRListener(4, capture)
webai.asr.addASRListener(5, whoAreYou)
webai.asr.addASRListener(6, areYouOk)
webai.asr.addASRListener(7, capture)
webai.asr.addASRListener(8, whoAreYou)


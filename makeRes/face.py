from time import sleep
from webai_blockly import Camera
from webai import FaceDetect
from webai_blockly import Lcd
from _board import webai

snapshot = None
info = None
camera = Camera()
FaceDetect.init(webai.res.face())
view = Lcd()

while True:
  snapshot = camera.snapshot()
  info = FaceDetect.findMax(snapshot, areaLimit=100, confidenceLimit=0.65, drawRectangle=True)
  view.drawString(x=140, y=110, text=b"{var}".format(var=(''.join([str(x) for x in ['(', info['x'] if info else '', ',', info['y'] if info else '', ')']]))), color=0xFFFF, scale=1.5, x_spacing=6, img=snapshot, display=False)
  view.displayImg(img=snapshot)

  sleep(0.001)

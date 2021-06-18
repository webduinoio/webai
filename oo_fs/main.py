try:
    import gc, lcd, image, sys
    gc.collect()
    # lcd.init()
    lcd.clear()
    lcd.draw_string(0,0,'test',lcd.WHITE,lcd.BLACK)
    loading = image.Image(size=(lcd.width(), lcd.height()))
    # loading.draw_rectangle((0, 0, lcd.width(), lcd.height()), fill=True, color=(255, 0, 0))
    info = "Webduino WebAI"
    loading.draw_string(int(lcd.width()//2 - len(info) * 5)-10, (lcd.height())//2-20, info, color=(255, 255, 255), scale=2, mono_space=0)
    # v = sys.implementation.version
    # vers = 'V{}.{}.{} : webduino.io'.format(v[0],v[1],v[2])
    # loading.draw_string(int(lcd.width()//2 - len(info) * 6), (lcd.height())//3 + 20, vers, color=(255, 255, 255), scale=1, mono_space=1)
    lcd.display(loading)
    # del loading, v, info, vers
    del loading,info
    gc.collect()
finally:
    gc.collect()

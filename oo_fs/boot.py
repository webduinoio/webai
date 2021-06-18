
try:
    from board import board_info
    from _board import webai,QRCodeRunner
    from machine import Timer
    import time

    cmdData = webai.cfg.get("cmd")
    print("[boot.py] cmdData:",cmdData)
    SYSTEM_WiFiCheckCount = 5

    cfgData = webai.cfg.load()
    WIFI_SSID = "webduino.io"
    WIFI_PASW = "webduino"
    if 'wifi' in cfgData:
        WIFI_SSID = cfgData['wifi']['ssid']
        WIFI_PASW = cfgData['wifi']['pwd']    

    if cmdData == None:
        print("[boot.py] normal boot...")
        def timerCount(timer):
            global SYSTEM_WiFiCheckCount
            if SYSTEM_WiFiCheckCount<=0:
                webai.clear()
                timer.stop()
            webai.showMessage("play after "+str(SYSTEM_WiFiCheckCount)+" seconds",x=-1,y=6,center=False,clear=False)
            SYSTEM_WiFiCheckCount-=1
            print("[boot.py] timer:",SYSTEM_WiFiCheckCount)

        tim = Timer(Timer.TIMER0, Timer.CHANNEL0, mode=Timer.MODE_PERIODIC, period=1, unit=Timer.UNIT_S, callback=timerCount, arg=timerCount, start=False, priority=1, div=0)
        gc.collect()
        lcd.clear()
        webai.img = image.Image()
        webai.draw_string(47,28,"DeviceID: "+webai.deviceID,scale=2,x_spacing=4)
        webai.show(img=webai.img)
        webai.img = None
        gc.collect()
        webai.showMessage("ver:"+os.uname()[6],x=-1,y=5,center=False,clear=False)
        webai.showMessage("WiFi checking...",x=-1,y=4,center=False,clear=False)
        setWiFiFlag=True
        webai.showMessage("ssid: "+WIFI_SSID,x=-1,y=2.5,center=False,clear=False)
        err = 0
        wifiStatus=""
        ifconfig = None
        if setWiFiFlag:
            ifconfig = webai.esp8285.wlan.ifconfig()
            if ifconfig[0]=="0.0.0.0" or ifconfig[3]!=WIFI_SSID:
                while 1:
                    try:
                        webai.esp8285.wlan.connect(WIFI_SSID, WIFI_PASW)
                        ifconfig=webai.esp8285.wlan.ifconfig()
                        webai.esp8285.updateState()
                        wifiStatus="OK"
                    except Exception as e:
                        print(e)
                        err += 1
                        print("Connect AP failed, now try again")
                        wifiStatus="ERROR"
                        if err > 1:
                            print("Conenct AP fail")
                            break
                        continue
                    break
            else:
                webai.esp8285.wifiConnect = True
                wifiStatus="OK"
        del err,WIFI_SSID,WIFI_PASW,setWiFiFlag
        if wifiStatus=="OK":
            webai.mqtt.sub('PING',webai.cmdProcess.sub,includeID=True)
            webai.esp8285.ota()
            webai.showMessage(" "*40,x=-1,y=4,center=False,clear=False)
            webai.showMessage("WiFi status:OK ("+ifconfig[6]+" dBm)",x=-1,y=4,center=False,clear=False)
        else:
            webai.showMessage(" "*40,x=-1,y=4,center=False,clear=False)
            webai.showMessage("WiFi status:not OK!!!",x=-1,y=4,center=False,clear=False)
        del wifiStatus
        qrcodeMode=False
        tim.start()
        lcd.draw_string(0,224,"press L Play                press R Scan",lcd.RED,lcd.BLACK)
        while 1:
            if SYSTEM_WiFiCheckCount<0:
                break
            if webai.btnL.btn.value()==0:
                print("run main.py")
                break
            if SYSTEM_WiFiCheckCount>0 and webai.btnR.btn.value()==0:
                tim.stop()
                img = image.Image()
                img.draw_string(80,100,"init Camera...",scale=2,x_spacing=4)
                lcd.display(img)
                img = None
                gc.collect()
                webai.initCamera(True)
                QRCodeRunner.scan()
        webai.lcd.clear()
        if not webai.img == None:
            webai.img.clear()
        tim.stop()
        tim.deinit()
        del tim
    else:
        print("[boot] run command...")
        #time.sleep(1)
        webai.connect(WIFI_SSID,WIFI_PASW)
        webai.esp8285.wifiConnect = True
        webai.mqtt.sub('PING',webai.cmdProcess.sub,includeID=True)
        webai.cmdProcess.load()

except Exception as e:
    print(">>>>",e)

import rpa

def moverizquierda(labelObj,mouseX,mouseY):
    rpa.click(labelObj)
    rpa.hover(labelObj)
    rpa.mouse('down')
    rpa.hover((mouseX+500),mouseY)
    rpa.mouse('up')


rpa.init(visual_automation=True)
rpa.url('https://lingojam.com/ZalgoText')
rpa.click('//*[@id="english-text"]')
rpa.type('//*[@id="english-text"]','Esto lo escribi sin manos')
moverizquierda('//*[@id="voice_speed"]',rpa.mouse_x(),rpa.mouse_y())


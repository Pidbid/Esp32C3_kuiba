from machine import Pin,SPI
from st7735 import ST7735
import time

class LCD:
    def __init__(self,width=80,height=160,rot=0):
        # 初始化SPI
        spi=SPI(1, baudrate=20000000, polarity=0, phase=0, sck=Pin(2), mosi=Pin(3))
        # 初始化LCD  rot 是显示方向，bgr是默认显示的颜色
        self.lcd=ST7735(width, height, spi,dc=Pin(6),cs=Pin(7),rst=Pin(10),rot=rot,bgr=0)
        #执行没有报错我们就继续了，正常初始化后屏幕应该是变黑了，这是因为我们初始化时是传了bgr=0，也就是填充黑色
        #加载字体文件 如果不是发的固件，应该就是没有下面这个方法
        self.lcd.font_load('./GB2312-16.fon')
        self.width = width
        self.height = height

    def text(self,text,x,y,color):
        self.lcd.text(text,x,y,color)
        
    def fill(self,color):
        self.lcd.fill(color)
        
    def show(self):
        self.lcd.show()
    
    def add_text(self,text,x,y,size):
        self.line_list = []
        self.lines = int(self.height/size)
        self.max_width = int(self.width/size)
        if len(text) <= self.max_width:
            pass
    
if __name__ == "__main__":
    lcd = LCD()
    #lcd.text("你好",5,5,0xFFFF)
    dkey = Pin(9,Pin.IN,Pin.PULL_UP)
    lkey = Pin(13,Pin.IN,Pin.PULL_UP)
    rkey = Pin(8,Pin.IN,Pin.PULL_UP)
    ukey = Pin(5,Pin.IN,Pin.PULL_UP)
    ckey = Pin(4,Pin.IN,Pin.PULL_UP)
    #print(ckey.value(),ukey.value(),dkey.value(),lkey.value(),rkey.value())
    #lcd.show()
    while True:
        if ckey.value() == 0:
            time.sleep_ms(100)
            if ckey.value() == 0:
                lcd.text("我的小鱼你",5,5,0xFFFF)
                lcd.text("醒了，",5,21,0xFFFF)
                lcd.show()
        if ukey.value() == 0:
            time.sleep_ms(100)
            if ukey.value() == 0:
                lcd.text("还认识早晨",5,37,0xFFFF)
                lcd.text("吗？",5,53,0xFFFF)
                lcd.show()
        if dkey.value() == 0:
            time.sleep_ms(100)
            if dkey.value() == 0:
                lcd.text("昨夜你曾经",5,69,0xFFFF)
                lcd.text("说，",5,85,0xFFFF)
                lcd.show()
        if lkey.value() == 0:
            time.sleep_ms(100)
            if lkey.value() == 0:
                lcd.text("愿夜幕永不",5,101,0xFFFF)
                lcd.text("开启,",5,117,0xFFFF)
                lcd.show()
        if rkey.value() == 0:
            time.sleep_ms(100)
            if rkey.value() == 0:
                lcd.text("你的香腮边",5,133,0xFFFF)
                lcd.text("轻轻滑落的",5,149,0xFFFF)
                lcd.show()
    
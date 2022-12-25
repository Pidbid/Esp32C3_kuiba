from machine import Pin,SPI
from st7735 import ST7735
#from lcd import TFT
 
# 初始化SPI
spi=SPI(1, baudrate=20000000, polarity=0, phase=0, sck=Pin(2), mosi=Pin(3))
# 初始化LCD  rot 是显示方向，bgr是默认显示的颜色
lcd=ST7735(80, 160, spi,dc=Pin(6),cs=Pin(7),rst=Pin(10),rot=0,bgr=0)
 
#执行没有报错我们就继续了，正常初始化后屏幕应该是变黑了，这是因为我们初始化时是传了bgr=0，也就是填充黑色
#加载字体文件 如果不是发的固件，应该就是没有下面这个方法
lcd.font_load('./GB2312-16.fon')
 
# 现在我们就可以开始显示中文了，试一下吧
lcd.text("你好测试一下",30,30,0xFFFF)
# 记住一定要调用下面这个方法，不然内容是不会显示出来的哦，所以你可以把所有的内容都显示好后再调用，这样刷新没有闪一下的感觉了

 
# 其实现在主要是调用的FrameBuffer里的方法在进行显示信息，主要方法有
# 填充屏幕颜色
#lcd.fill(0)
lcd.show()

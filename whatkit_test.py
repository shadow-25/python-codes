import pywhatkit as pyw
import time
hour=int(time.strftime('%H'))
min=int(time.strftime('%M'))
pyw.sendwhatmsg('+917887647604','python sa message hai',hour,min+1)
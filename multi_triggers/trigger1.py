import handler
from threading import (Event, Thread)
import time

event = handler.event

# イベント停止のフラグ
stop = False

thread = Thread(target=handler.handler)
thread.start()
time.sleep(3)
event.set()

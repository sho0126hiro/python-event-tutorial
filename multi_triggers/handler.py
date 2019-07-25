from threading import (Event, Thread)
event = Event()
def handler():
    print("スレッド開始")
    event.wait()
    event.clear()
    print("スレッド終了")
import time
from win10toast import ToastNotifier
toaster = ToastNotifier()

while True:
    toaster.show_toast("pani pi la", "plz pani pi lo(:",  duration=20)
    time.sleep(20)
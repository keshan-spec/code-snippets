from win10toast import ToastNotifier

toaster = ToastNotifier()

def notify(msg, head):
    toaster.show_toast(head,msg ,threaded=True, icon_path=None, duration=5)

notify("Hello", "Alert")
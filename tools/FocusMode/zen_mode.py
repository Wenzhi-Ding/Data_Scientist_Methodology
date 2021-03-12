import ctypes
import os

sys = 'C:\Windows\System32\drivers\etc'

if 'hosts.zen' in os.listdir(sys):  # 说明非专注模式
    os.rename(f'{sys}\hosts', f'{sys}\hosts.bak')
    os.rename(f'{sys}\hosts.zen', f'{sys}\hosts')
    ctypes.windll.user32.SystemParametersInfoW(20, 0, "E:\OneDrive\图片\wallpaper_focus.jpg", 0)
else:
    os.rename(f'{sys}\hosts', f'{sys}\hosts.zen')
    os.rename(f'{sys}\hosts.bak', f'{sys}\hosts')
    ctypes.windll.user32.SystemParametersInfoW(20, 0, "E:\OneDrive\图片\wallpaper.jpg", 0)
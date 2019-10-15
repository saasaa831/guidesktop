import os
import sys
import time
import psutil
import platform

SERVER = 'node'
folder = os.path.join(os.path.expanduser("~"), ".wdm")

def is_running(name):
    for p in psutil.process_iter():
        try:
            if p.name() == name:
                return True
        except psutil.ZombieProcess:
            return False
    return False


def get_pid(name):
    for p in psutil.process_iter():
        try:
            if p.name() == name:
                return p.pid
        except psutil.ZombieProcess:
            return None
    return None


def run_server():
    if not is_running(SERVER):
        print('=======  WinApp have been Started  ===========')
        os.system(os.path.join(folder, 'guidriver', 'WinAppDriver.exe'))
        time.sleep(5)
        for _ in range(5):
            if is_running('node'):
                print('====== WinApp has been started =======')
                break
            time.sleep(1)
        else:
            print('======= WinApp has been stopped =======')
            sys.exit(1)
    else:
        print('======= WinApp is already running =======')


def stop_server():
    getplat=platform.architecture()
    if is_running('WinAppDriver.exe'):
        if 'Windows' not in getplat[1]:os.system('kill -9 {pid}'.format(pid=get_pid('WinAppDriver.exe')))
        else: os.system("taskkill /f /im WinAppDriver.exe")

#if __name__ == '__main__':
    #stop_server()
    #run_server()
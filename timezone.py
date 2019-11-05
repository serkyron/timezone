import ntsecuritycon
import win32security
import win32api
import sys
import os
import platform


def adjust_privilege(priv):
    flags = ntsecuritycon.TOKEN_ADJUST_PRIVILEGES | ntsecuritycon.TOKEN_QUERY
    htoken =  win32security.OpenProcessToken(win32api.GetCurrentProcess(), flags)
    id = win32security.LookupPrivilegeValue(None, priv)
    newPrivileges = [(id, ntsecuritycon.SE_PRIVILEGE_ENABLED)]
    win32security.AdjustTokenPrivileges(htoken, 0, newPrivileges)


system = platform.system()

if system != "Windows":
    raise Exception("OS type not supported")

adjust_privilege(win32security.SE_TIME_ZONE_NAME)
command = 'tzutil /s "%s"' % sys.argv[1]
os.system(command)

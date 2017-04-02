import os
from os.path import expanduser
import platform

def get_apktool_loc():
    pform = platform.system().lower()
    if pform == "darwin":
        dir_name = "darwin"
    elif pform == "windows":
        dir_name = "win"
    elif pform == "linux":
        dir_name = "linux"
    else:
        print "Unsupported Operating System"
        return
    return "lib/" + dir_name + "/apktool"

def default_workspace_loc():
    home = expanduser("~")
    workspace = home + '/RefractorWorkspace'
    if not os.path.exists(workspace):
        os.makedirs(workspace)
    return workspace

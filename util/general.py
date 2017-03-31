import os
from os.path import expanduser

def default_workspace_location():
    home = expanduser("~")
    workspace = home + '/RefractorWorkspace'
    if not os.path.exists(workspace):
        os.makedirs(workspace)
    return workspace

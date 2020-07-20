# https://stackoverflow.com/questions/2352181/how-to-use-a-dot-to-access-members-of-dictionary

from box import Box, BoxList

def Modelify(data):
    if isinstance(data, dict):
        return Box(data)
    else:
        return BoxList(data)

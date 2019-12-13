import sys
import fileinput

def getInput():
    """
    Check if the input is null. If that is the case simply listen for stdin
    Returns the input that it got eg a url, uri or domain
    """
    if len(sys.argv) == 1:
        return fileinput.input()[0]
    return sys.argv[1]
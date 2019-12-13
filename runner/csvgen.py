
import runner.config
import datetime

def getDate():
    return str(datetime.date.today())

def generateCSV(URI, score, reason):
    """
    Generate a standard csv output of the generated data
    """
    return "{}|{}|{}|{}|{}".format(URI, getDate(), runner.config.NAME, score,  reason)
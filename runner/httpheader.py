
import runner.config

class httpheader:
    """
    This is a base class each http header should inherit
    It contains all methods that need to be implemented in order to generate a final result
    """

    def __init__(self, value, headers):
        """
        Value is the payload supplied with the header
        headers is a list of tuples containing all http headers in the response
        """
        self.value = value
        self.headers = headers
    
    def score(self):
        """
        returns a float containing the score for this header (between 0.0 and 10.0)
        """
        return 10
    
    def reason(self):
        """
        Returns a string why the score is what is is
        """
        return runner.config.SCORE_IDEAL

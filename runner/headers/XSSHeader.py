import runner.headers.httpheader as generic
import runner.config

class XSSHeader(generic.httpheader):
    name="X-XSS-Protection"
    badReason = ["No protection against cross site scripting"]
    missingScore=runner.config.MISSING_SCORE_XSS # no protection is really bad

    def __init__(self, value, headers):
        super().__init__(value, headers)
    
    def score(self):
        """
        returns a float containing the score for this header (between 0.0 and 10.0)
        """
        if self.value == "0":
            return 10
        self.reason = self.badReason[0]
        return 0
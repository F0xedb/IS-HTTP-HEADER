import runner.headers.httpheader as generic
import runner.config

class CORSHeader(generic.httpheader):
    name="Access-Control-Allow-Origin"
    badReason = ["No Cross origin is safe", "Cross origin resource sharing is dangerous" "Cross origin resource sharing on all webpages is dangerous"]
    missingScore=runner.config.MISSING_SCORE_CORS# No cors is very safe
    def __init__(self, value, headers):
        super().__init__(value, headers)
    
    def score(self):
        """
        returns a float containing the score for this header (between 0.0 and 10.0)
        """
        if "*" in self.value:
            self.reason = self.badReason[2]
            return 0
        # there is a filter for the cross origin 
        self.reason = self.badReason[1]
        # CORS is dangerous but only certain websites can use the endpoint
        return 5
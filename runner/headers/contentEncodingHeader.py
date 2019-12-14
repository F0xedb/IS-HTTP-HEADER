import runner.headers.httpheader as generic
import runner.config

class ContentEncodingHeader(generic.httpheader):
    name="Content-Encoding"
    badReason = ["No compression is set", "Unknown Compression type"]
    missingScore=runner.config.MISSING_SCORE_CONTENT_ENCODING # no compression is rather bad but that can be dealt with
    def __init__(self, value, headers):
        super().__init__(value, headers)
    
    def score(self):
        """
        returns a float containing the score for this header (between 0.0 and 10.0)
        """
        if "gzip" in self.value:
            return 10
        # cannot guess the compression type
        self.reason = self.badReason[1]
        # Uncommon compression can mean bad support from the client
        return 8
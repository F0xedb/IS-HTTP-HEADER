
# MIT License
# 
# Copyright (c) 2019 Meyers Tom
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import runner.config

class httpheader:
    """
    This is a base class each http header should inherit
    It contains all methods that need to be implemented in order to generate a final result
    """
    name = "HTTP_HEADER_NAME" # this name should match the real http header name. It is used to match the class to the real header
    reason = runner.config.SCORE_IDEAL # in case no reason was found
    missingScore = 0 # score to give when the header is not found
    
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
        return self.reason

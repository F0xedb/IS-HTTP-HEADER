
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
import runner.headers.httpheader as generic
import runner.config

class CORSHeader(generic.httpheader):
    name="Access-Control-Allow-Origin"
    badReason = ["No Cross origin is safe", "Cross origin resource sharing is dangerous", "Cross origin resource sharing on all webpages is dangerous"]
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
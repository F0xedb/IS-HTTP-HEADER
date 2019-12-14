
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

class XFrameHeader(generic.httpheader):
    name="X-Frame-Options"
    badReason = ["Clickjacking is a possibility", "{} is configured incorrectly".format(name)]
    missingScore=runner.config.MISSING_SCORE_XFRAME_HEADER# No cors is very safe
    def __init__(self, value, headers):
        super().__init__(value, headers)
    
    def score(self):
        """
        returns a float containing the score for this header (between 0.0 and 10.0)
        """

        # gws is the google web server
        if "SAMEORIGIN" == self.value.upper():
            self.reason = "Setting {} to DENY is better that {}".format(self.name, self.value)
            return 9
        elif "DENY" == self.value.upper():
            return 10
        elif "allow-from" == self.value.lower():
            self.reason = "Allowing clickjacking from certain locations can be very dangerous"
            return 5
        
        # Allow all is set which is very dangerous
        self.reason = self.badReason[1]
        # Clickjacking is a posibility
        return 3
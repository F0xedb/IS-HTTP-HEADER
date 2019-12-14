
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
import datetime
from pytz import timezone

class DateHeader(generic.httpheader):
    name="Date"
    badReason = ["No date header has been set", "Message was send long ago (more that {} seconds)".format(runner.config.DATE_RESPONSE_DELAY)]
    missingScore=runner.config.MISSING_SCORE_DATE # no cookies is a good thing

    def __init__(self, value, headers):
        super().__init__(value, headers)
    
    def score(self):
        """
        returns a float containing the score for this header (between 0.0 and 10.0)
        """
        try:
            # convert to datetime object
            time = datetime.datetime.strptime(self.value, '%a, %d %b %Y %H:%M:%S %Z')
            # handle the send timezone
            time = timezone(self.value.split(" ")[-1]).fromutc(time)

            # convert our current timezone to the timezone of the server
            now = datetime.datetime.now(timezone(self.value.split(" ")[-1]))

            # compute the delay
            delay = (now-time).total_seconds()
            if delay > runner.config.DATE_RESPONSE_DELAY:
                self.reason = self.badReason[1]
                return 5
        except Exception as e:
            print(e)
            self.reason = "Date format is not defined as per RFC 7231"
            return 5
        self.reason = self.badReason[1]
        return 7
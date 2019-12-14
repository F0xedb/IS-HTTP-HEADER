
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

NAME="Qhead" # the name of our program

SCORE_IDEAL="Your score is optimal" # message in case nothing is wrong

PING_TIMEOUT=3 # timeout until connection with the URI fails

PROTOCOLS=["https", "http"] # possible protocols to test

DEFAULT_PROTOCOL=PROTOCOLS[0] # default protocol to use in case none is provided

DATE_RESPONSE_DELAY=10 # the difference between our current time and when the server send us the payload


# the scores to give when a certain header is missing

MISSING_SCORE_CONTENT_ENCODING=5 # no compression is rather bad but that can be dealt with
MISSING_SCORE_XSS=0 # no protection against cross site scripting is bad
MISSING_SCORE_CORS=10 # no cors is very safe
MISSING_SCORE_SERVER_HEADER=5 # cannot determin the type of server (if this is not present something is fishy)
MISSING_SCORE_XFRAME_HEADER=2 # No x-Frame header is supplied. Clickjacking can happen
MISSING_SCORE_COOKIE=10 # no cookies is a bonus
MISSING_SCORE_DATE=3 # no date provided means we cannot determin when it was send

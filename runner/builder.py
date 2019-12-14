
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

import runner.headers.httpheader as header
import runner.headers.contentEncodingHeader as encoding
import runner.headers.XSSHeader as xss
import runner.headers.CORSHeader as CORS

# all different headers to resolve
# they must inherit httpheader at least
headerResolver = [encoding.ContentEncodingHeader, xss.XSSHeader, CORS.CORSHeader]


def match(httpResponse, headers):
    """
    takes a tuple in the form of (str, str)
    where the first string it the http header type and the second string is the http header value
    Based on these values it will construct a http header object
    """
    key, value = httpResponse
    for resolver in headerResolver:
        if resolver.name == key:
            return resolver(httpResponse[1], headers)
    # cannot resolve the current header
    return None
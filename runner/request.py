
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

import urllib.request
import runner.config


def _normalizeURI(uri):
    """
    Look at the input uri and generate a normalized output from it.
    Eg input is www.google.com -> output is http://www.google.com
    """
    for protocol in runner.config.PROTOCOLS:
        protocolURI = "{}://".format(protocol)
        # check if the uri is correct
        if uri[0:len(protocolURI)] == protocolURI:
            return uri
    return "{}://{}".format(runner.config.DEFAULT_PROTOCOL, uri)

def resolve(domain):
    """
    Returns a list of Tuples containing the http header type and its value.
    It gets this data from performing a http get request to the server
    """
    domain = _normalizeURI(domain)
    request = urllib.request.Request(domain)
    request.add_header('Accept-encoding', 'gzip,deflate')
    response = urllib.request.urlopen(request, timeout=runner.config.PING_TIMEOUT)
    headers = response.info().raw_items()
    # convert genertor to a generic list
    list = []
    for header, value in headers:
        list.append((header, value))
    return list
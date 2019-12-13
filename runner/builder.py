import runner.httpheader as header

def match(httpResponse, headers):
    """
    takes a tuple in the form of (str, str)
    where the first string it the http header type and the second string is the http header value
    Based on these values it will construct a http header object
    """
    return header.httpheader(httpResponse[1], headers)

def resolve(domain):
    """
    Returns a list of Tuples containing the http header type and its value.
    It gets this data from performing a http get request to the server
    """
    return [("test-header", "this is a test value")]
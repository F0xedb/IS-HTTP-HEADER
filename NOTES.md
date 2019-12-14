* 13 December:
    - Thinking about the design of the script (python module)
    - Modularity of adding headers
        - HTTP scan class -> returns score of said header
        - Auto loads into the main file
    - Normalizing output is a seperate class
    - Input via stdin or argumant
    - Output over stdout or file
    - Module should only depend on the default python api (no extra dependencies)
    - Research
        - Looking into OWASP (owasp.org) for general security regarding web

Research notes:
* OWASP (Open Web Application Security Project) Interesting look to figure out what to check upon

* Scanning google http headers for www.google.com

| Headers type     | Meaning                                          |
|------------------|--------------------------------------------------|
| Date             | date when the message was send                   |
| Expires          | date and time when response is considered stale  |
| Cache-Control    | Rules for caching (in seconds)                   |
| Content-Type     | Indicates resource media type                    |
| Content-Encoding | Indicates encoding eg gzip                       |
| Server           | Information abut how the server handles requests |
| Content-Length   | Indicates the body size                          |
| X-XSS-Protection | Stops pages from loading when detecting xss      |
| X-Frame-Options  | Avoid clickjacking                               |
| Set-Cookie       | Sends cookie from server to client               |

* Start research python http standard library got gather all http headers
    - interesting read (https://bugs.python.org/issue4773)
    - documentation (https://docs.python.org/3/library/urllib.html)
    - Concrete implementation (https://docs.python.org/3/library/urllib.request.html#module-urllib.request)
* Started research on standardized http headers
    - http headers on wikipedia (https://en.wikipedia.org/wiki/List_of_HTTP_header_fields)
    - RFCs 7230, 7231, 7232, 7233, 7234, and 7235 contain standardized http headers
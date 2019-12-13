* 13 December:
    - Thinking about the design of the script (python module)
    - Modularity of adding headers
        - HTTP scan class -> returns score of said header
        - Auto loads into the main file
    - Normalizing output is a seperate class
    - Input via stdin or argumant
    - Output over stdout or file
    - Module should only depend on the default python api (no extra dependencies)
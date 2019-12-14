
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/F0xedb/IS-HTTP-HEADER">
    <img src="https://tos.pbfp.xyz/images/logo.svg" alt="Logo" width="150" height="200">
  </a>

  <h3 align="center">Header scanner framework</h3>

  <p align="center">
    Scan http and https headers to check if a webserver is configured correctly
    <br />
    <a href="https://github.com/F0xedb/IS-HTTP-HEADER"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/F0xedb/IS-HTTP-HEADER">View Demo</a>
    ·
    <a href="https://github.com/F0xedb/IS-HTTP-HEADER/issues">Report Bug</a>
    ·
    <a href="https://github.com/F0xedb/IS-HTTP-HEADER/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
  * [General](#general)
  * [Docker](#docker)
  * [Debug](#debug)
* [Extend](#Extend)
  * [Headers](#Headers)
  * [STDout](#STDout)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.
This software has been tested on RHEL 8, Arch linux and TOS linux
It should work on most Operating systems as long as they have Python3 installed with pytz (python timezone)

### Prerequisites

Make sure python is installed if not here is a quick example

Arch Linux
```sh
sudo pacman -Syu python
```

RHEL
```sh
sudo yum install python3
```

Debian, ubuntu and more
```sh
sudo apt-get install python3
```

Make sure `pytz` is installed

Arch Linux
```sh
sudo pacman -Syu python-pytz
```

PIP
```sh
sudo pip install pytz
```

### Installation
 
1. Clone the IS-HTTP-HEADER repo
```sh
git clone "https://github.com/F0xedb/IS-HTTP-HEADER.git"
# or over ssh
git clone "git@github.com:F0xedb/IS-HTTP-HEADER.git"
```
2. Check if python is installed
```sh
command -v python || command -v python3 # depends on where your python3 is symlinked
```



<!-- USAGE EXAMPLES -->
## Usage


### general
Using this tool is rather easy. Simply use the following command

```sh
python -m runner "<endpoint>"
```

For example test the utility against google

```sh
python -m runner "www.google.com"
python -m runner "google.com"
python -m runner "https://google.com"
python -m runner "http://google.com"

```
> All of the above will produces the same outout (except for the last one as that uses http)

> Endpoint in the example above can either be a ip, URL, URI or domain

### docker

You can also use this tool with `docker` or `docker-compose`.
Here is a quick and simple tutorial

Using docker:

1. build the image
```sh
docker build -t <name> .
```
2. run the image with google
```sh
docker run <name>
```
3. run the image with a custom domain
```sh
docker run -it --rm http python -m runner <domain> # where domain is the domain you want to scan
```

Alternativly you can use docker-compose to perform a scan

1. Run a scan to google.com
```sh
docker-compose up
```
2. Run a scan to a custom domain
```yml
version: "3"
services:
  python:
    build: .
    command: "python -m runner <domain>" # where domain is the domain you want to scan
```
3. run a scan to a custom domain without editing the yaml file
```sh
docker-compose run python "python"  "-m" "runner" "<domain>" # where domain is the domain you want to scan
```

### debug

You can enable debug messages in order to develop or debug you website/ application

For more information run the help menu
```sh
python -m runner -h
```

There are multiple levels of debugging each level will display more information

This debug level will print out all headers, their score and the reason why that header has been assigned their score
```sh
python -m runner -v <domain>
```

This debug level does the same as above but also prints out the header value. In case you don't know why that reason has been given
```sh
python -m runner -vv <domain>
```

_For more examples, please refer to the [Documentation](https://github.com/F0xedb/IS-HTTP-HEADER)_

<!-- Write own test -->
## Extend

This section will describe how to extend the current piece of software to include more checks or different ways of parsing.

> try to include as much information into the `runner/config.py` file as this is a centralized place for changing how to program generates output

<!-- Add more headers -->
### Headers

Before you can add headers you should understand how the project has been setup.
All different headers live in the `runner/headers` directory.
All headers should inherit the `runner/headers/httpheader.py` class
Each class is responsible for generating a score for that header and a reason why that score was given.

All you need to do to add a extra header is the following

1. Create the header file
```sh
touch runner/headers/headerName.py
```
2. create the header class inside that file
```python
import runner.headers.httpheader as generic
import runner.config

class XSSHeader(generic.httpheader):
    name="X-XSS-Protection"
    badReason = ["No protection against cross site scripting"]
    missingScore=runner.config.MISSING_SCORE_XSS # no protection is really bad

    def __init__(self, value, headers):
        super().__init__(value, headers)
    
    def score(self):
        """
        returns a float containing the score for this header (between 0.0 and 10.0)
        """
        if self.value == "0":
            return 10
        self.reason = self.badReason[0]
        return 0
```
3. Add this class to the builder in `runner/builder.py`
```python
import runner.headers.headerName as headerName
headerResolver = [..., headerName.headerName]
```

Here are a few tips for you to know if you are writing your own headers.

* The name property must match the Header type exactly as defined in RFCs 7230, 7231, 7232, 7233, 7234, and 7235.
* The badReason property must be a list containing all reason that can be generated from that header
* The first element in the badReason list must be the reason when the header is missing
* The missingScore property must be the score given if that headers is missing (between 0 and 10) where 10 is not so bad and 0 is severe
* the score method returns the score given based on the header information (between 0 and 10) where 10 is not so bad and 0 is severe
* You can override the reason method look at `runner.headers.httpheader.py` for more information
* Try to put as much hardcoded values into the `runner/config.py` file as possible

<!--  STDout-->
### STDout

Appart from testing the output you can also change the way the output is generated.
Look at the `runner/csvgen.py` for more information.
All you need to do in order to generate anything else is by copying this file over and changing the `runner/__main__.py` file.
More specifically this line
```python
print(runner.csvgen.generateCSV(domain, normalizedScore, reason))
```

into your own output generator

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/F0xedb/IS-HTTP-HEADER/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

F0xedb - tom@odex.be

Project Link: [https://github.com/F0xedb/IS-HTTP-HEADER](https://github.com/F0xedb/IS-HTTP-HEADER)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [F0xedb](https://github.com/F0xedb)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/F0xedb/IS-HTTP-HEADER.svg?style=flat-square
[contributors-url]: https://github.com/F0xedb/IS-HTTP-HEADER/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/F0xedb/IS-HTTP-HEADER.svg?style=flat-square
[forks-url]: https://github.com/F0xedb/IS-HTTP-HEADER/network/members
[stars-shield]: https://img.shields.io/github/stars/F0xedb/IS-HTTP-HEADER.svg?style=flat-square
[stars-url]: https://github.com/F0xedb/IS-HTTP-HEADER/stargazers
[issues-shield]: https://img.shields.io/github/issues/F0xedb/IS-HTTP-HEADER.svg?style=flat-square
[issues-url]: https://github.com/F0xedb/IS-HTTP-HEADER/issues
[license-shield]: https://img.shields.io/github/license/F0xedb/IS-HTTP-HEADER.svg?style=flat-square
[license-url]: https://github.com/F0xedb/IS-HTTP-HEADER/blob/master/LICENSE.txt
[product-screenshot]: https://tos.pbfp.xyz/images/logo.svg

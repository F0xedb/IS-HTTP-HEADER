
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
It should work on most Operating systems as long as they have Python3 installed

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

### Installation
 
1. Clone the IS-HTTP-HEADER repo
```sh
git clone "https://github.com/F0xedb/IS-HTTP-HEADER.git"
```
2. Check if python is installed
```sh
command -v python || command -v python3 # depends on where your python3 is symlinked
```



<!-- USAGE EXAMPLES -->
## Usage

Using this tool is rather easy. Simply use the following command

```sh
python main.py "<endpoint>"
```

> Endpoint in the example above can either be a ip, URL, URI or domain

_For more examples, please refer to the [Documentation](https://github.com/F0xedb/IS-HTTP-HEADER)_



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

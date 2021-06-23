# Rest_like_A_boss
<br />
<p align="center">
  <a href="https://github.com/Murithijoshua/Rest_like_A_boss">
<!--     <img src="<img src="http://placeskull.com/g/80/80/" alt="place ape" />" alt="Logo" width="80" height="80"> -->
  </a>

  <h3 align="center">Reddit_Clone API</h3>

  <p align="center">
    This is a Reddit_clone REST API, where one can upvote or  down vote posts.
    <br />
    <br />
    <br />
    <a href="https://github.com/Murithijoshua/Rest_like_A_boss">View Demo</a>
    ·
    <a href="https://github.com/Murithijoshua/Rest_like_A_boss/issues">Report Bug</a>
    ·
    <a href="https://github.com/Murithijoshua/Rest_like_A_boss/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


### Built With

* [Python](https://python.org)
* [Django](https://www.djangoproject.com/)
* [Django Rest framework](https://www.django-rest-framework.org/)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Check if python3 is installed 
  ```sh
  python3 --version
  
  ```
* Else download from [Python.org](https://python.org)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Murithijoshua/Rest_like_A_boss.git
   ```
2. Create virtual enviroment
   ```sh
   python3 -m venv env
   ```
3. Activate the virtual env
   ```sh
   source env/bin/activate
   ```
4. Install all the dependencies
   ```sh
   pip install -r requirements.txt
   ```
5. Run the application
   ```sh
   cd Rest_like_A_boss

   ```
* create admin account, this will enable you for authetication while doing POST via the API
    ```sh
   python manage.py createsuperuser

   ```
 * do data migrations
 
    ```sh
   python manage.py migrate 

   ```
 * now lets create a file to store all the Secret key
   ``` sh
   touch .env
   ```
 * add thid text to your key
    ```sh
    KEY = 'django-insecure-wf*i)x^#*+f7+r!al*q&qqi&jyww7vi@$*^%7u8xivhwkzv!u@'
    ```
 * now lets wakes this beast from sleep
   ```sh
   python manage.py runserver

   ```
* Run this on browser will fetch all data and POST data 
    ```sh
   127.0.0.1:8000/api/all

   ```
* You can now vote for a specific post using this. **you can only vote once**
    ```sh
   127.0.0.1:8000/api/all/<int>/vote

   ```





<!-- USAGE EXAMPLES -->
## Usage

> this is still under_development 


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/Murithijoshua/Rest_like_A_boss/issues) for a list of proposed features (and known issues).



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

<!-- Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email -->

Project Link: [https://github.com/Murithijoshua/Rest_like_A_boss](https://github.com/Murithijoshua/Rest_like_A_boss)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* []()
* []()
* []()





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Murithijoshua/repo.svg?style=for-the-badge
[contributors-url]: https://github.com/Murithijoshua/repo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Murithijoshua/repo.svg?style=for-the-badge
[forks-url]: https://github.com/Murithijoshua/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/Murithijoshua/repo.svg?style=for-the-badge
[stars-url]: https://github.com/Murithijoshua/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/Murithijoshua/repo.svg?style=for-the-badge
[issues-url]: https://github.com/Murithijoshua/repo/issues
[license-shield]: https://img.shields.io/github/license/Murithijoshua/repo.svg?style=for-the-badge
[license-url]: https://github.com/Murithijoshua/repo/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/Murithijoshua

<p align="center">
    <h1 align="center">FRIDGY-SOARIO-2024</h1>
</p>

<p align="center">
	<img src="https://img.shields.io/github/license/ved-patel226/FRIDGY-SOARIO-2024?style=flat&logo=opensourceinitiative&logoColor=white&color=f79477" alt="license">
	<img src="https://img.shields.io/github/last-commit/ved-patel226/FRIDGY-SOARIO-2024?style=flat&logo=git&logoColor=white&color=f79477" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/ved-patel226/FRIDGY-SOARIO-2024?style=flat&color=f79477" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/ved-patel226/FRIDGY-SOARIO-2024?style=flat&color=f79477" alt="repo-language-count">
</p>
<p align="center">
		<em>Built with the tools and technologies:</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=flat&logo=HTML5&logoColor=white" alt="HTML5">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
</p>

<br>


##  Overview

<code>❯ Fridgy is a tool for tracking food in your fridge! You can make google calander events, get reminded of when to shop, and more!</code>

---

##  Features

<code>❯ 1. Graph to show fridge % over time</code>

<code>❯ 2. Fridge-Empty Predictor</code>

<code>❯ 3. Finding Ideal days to shop, taking acount your events and the weather</code>

<code>❯ 4. Everything in your fridge</code>

---

##  Repository Structure

```sh
└── FRIDGY-SOARIO-2024/
    ├── LICENSE
    ├── main.py
    ├── py_tools
    │   ├── __init__.py
    │   ├── ai.py
    │   ├── calander.py
    │   ├── env_translator.py
    │   ├── json_editor.py
    │   ├── json_saver.py
    │   ├── mongo_db_editor.py
    │   ├── weather.py
    │   ├── week_refresh.py
    │   └── wtforms_upload.py
    ├── static
    │   ├── Fridge-IMGS
    │   │   └── ved-patel226
    │   ├── JSON
    │   │   └── ved-patel226
    │   ├── imgs
    │   │   ├── upload.png
    │   │   └── upload.svg
    │   ├── js
    │   │   ├── load.js
    │   │   └── scroll.js
    │   └── styles
    │       ├── bg1.png
    │       ├── home.css
    │       ├── other.css
    │       └── styles.css
    └── templates
        ├── base.html
        ├── dashboard.html
        └── index.html
```

---

##  Modules

<details closed><summary>.</summary>

| File | Summary |
| --- | --- |
| [main.py](https://github.com/ved-patel226/FRIDGY-SOARIO-2024/blob/main/main.py) | <code>❯ Flask App</code> |

</details>

<details closed><summary>templates</summary>

| File | Summary |
| --- | --- |
| [base.html](https://github.com/ved-patel226/FRIDGY-SOARIO-2024/blob/main/templates/base.html) | <code>❯ Base HTML file</code> |
| [index.html](https://github.com/ved-patel226/FRIDGY-SOARIO-2024/blob/main/templates/index.html) | <code>❯ Homepage</code> |
| [dashboard.html](https://github.com/ved-patel226/FRIDGY-SOARIO-2024/blob/main/templates/dashboard.html) | <code>❯ Dashboard with all information</code> |

</details>

<details closed><summary>py_tools</summary>

| File | Summary |
| --- | --- |
| [env_translator.py](https://github.com/ved-patel226/FRIDGY-SOARIO-2024/blob/main/py_tools/env_translator.py) | <code>❯ Translates .env secrets to strings</code> |
| [week_refresh.py](https://github.com/ved-patel226/FRIDGY-SOARIO-2024/blob/main/py_tools/week_refresh.py) | <code>❯ Deletes all user data everyweek</code> |
| [weather.py](https://github.com/ved-patel226/FRIDGY-SOARIO-2024/blob/main/py_tools/weather.py) | <code>❯ Contacts weather API</code> |
| [json_editor.py](https://github.com/ved-patel226/FRIDGY-SOARIO-2024/blob/main/py_tools/json_editor.py) | <code>❯ Converts DB data to usable data</code> |
| [ai.py](https://github.com/ved-patel226/FRIDGY-SOARIO-2024/blob/main/py_tools/ai.py) | <code>❯ Communicates with LLM</code> |
| [calander.py](https://github.com/ved-patel226/FRIDGY-SOARIO-2024/blob/main/py_tools/calander.py) | <code>❯ Contacts Google Calander API</code> |
| [wtforms_upload.py](https://github.com/ved-patel226/FRIDGY-SOARIO-2024/blob/main/py_tools/wtforms_upload.py) | <code>❯ Old prototype for file uploads</code> |
| [json_saver.py](https://github.com/ved-patel226/FRIDGY-SOARIO-2024/blob/main/py_tools/json_saver.py) | <code>❯ Old prototype for saving JSON data locally</code> |
| [mongo_db_editor.py](https://github.com/ved-patel226/FRIDGY-SOARIO-2024/blob/main/py_tools/mongo_db_editor.py) | <code>❯ Makes it easier to communicate with MONGO</code> |

</details>

---

##  Getting Started

###  Prerequisites

**Python**: `version 3.12.3`

###  Installation

Build the project from source:

1. Clone the FRIDGY-SOARIO-2024 repository:
```sh
❯ git clone https://github.com/ved-patel226/FRIDGY-SOARIO-2024
```

2. Navigate to the project directory:
```sh
❯ cd FRIDGY-SOARIO-2024
```

3. Install the required dependencies:
```sh
❯ pip install -r requirements.txt
```

4. Follow .ENV template and fill it in with your API keys
```sh
.env
```

5. Follow the JSON template and fill it with your google app JSON
```sh
credentials.json
```

###  Usage

To run the project, execute the following command:

```sh
❯ python main.py
```

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/ved-patel226/FRIDGY-SOARIO-2024/issues)**: Submit bugs found or log feature requests for the `FRIDGY-SOARIO-2024` project.
- **[Submit Pull Requests](https://github.com/ved-patel226/FRIDGY-SOARIO-2024/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/ved-patel226/FRIDGY-SOARIO-2024/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/ved-patel226/FRIDGY-SOARIO-2024
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/ved-patel226/FRIDGY-SOARIO-2024/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=ved-patel226/FRIDGY-SOARIO-2024">
   </a>
</p>
</details>

---

##  License

This project is protected under the [Apache 2.0](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

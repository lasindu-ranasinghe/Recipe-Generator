# Recipe Generator

<img src="assets/robot.png" alt="Robot Chef">

Recipe Generator is an LLM-based web app for generating recipes using your own ingredients. Recipe Generator is powered by OpenAI's GPT3.5 model, and uses a Streamlit app as its frontend.

## Setup

### Prerequisites

1. <a href="https://git-scm.com/">Git<a>
2. Python (at least 3.9.0) must be installed on your system.

After Python has been set up, install the `virtualenv` package to create and manage a virtual environment for this project. This helps you maintain the project's dependencies in a hassle-free manner, without installing any unnecessary packages globally throughout your system.

```
pip install virtualenv
```

### 1. Clone the Project

Clone this project to create a local copy of it on your system:

```shell
git clone "https://github.com/lasindu-ranasinghe/Recipe-Generator.git"
```

Then, move into the project folder:

```shell
cd Recipe-Generator
```

### 2. Create a Virtual Environment

Create a virtual environment inside the project folder to isolate its dependencies:

```shell
python -m venv env

# or

python3 -m venv env
```

Next, activate the virtual environment:

```shell
# on Windows:
.\env\Scripts\activate

# on MacOS or Linux
source env/bin/activate
```

You can deactivate this environment when you are done working with the project:

```shell
# on Windows, MacOS or Linux
deactivate
```

### 3. Install Dependencies

Set up your project with the necessary packages and libraries. After activating the virtual environment, enter the following command:

```shell
pip install -r requirements.txt
```

### 4. Start Streamlit

After you have completed the above steps, you can start the Streamlit app.

```shell
streamlit run app.py
```

Streamlit will start up in `localhost:8501`.

<hr />

This project is owned by Lasindu Ranasinghe, and is licensed under the <a href="https://github.com/lasindu-ranasinghe/Recipe-Generator/blob/main/LICENSE">Apache License</a>.
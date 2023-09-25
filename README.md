# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.8+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

To run the app (which connectes to trello), you will need to add three keys to the .env file. These are listed below

These can be obtained by signing up for an Atlassian Trello account at https://trello.com/signup

A power up will need to be created which will then allow you to access the API KEY required to fill in to the project below. To create a power up you will need to specify the power-up or integration name (arbitrary). You will need to specify a workspace (this is a drop down list and will default to your main workspace).

IFrame connector URL is unnecessary for this step. 

The remaining fields (email and author) are self explanatory. When you have clicked "Create" on the power up screen, you will be able to access your API Key. 

Next to your API Key, you will see a hyperlink indicating token creation - click this - and authorise at the next step. Copy the Token that will be generated and add it in the env file next to the var listed below.

For Board ID, you can use the following URL in POSTMAN (pasting in your key and token where indicated)

https://api.trello.com/1/members/me/boards?fields=name,url&key={your_api_key_here}&token={your_token_here}

You will then be presented with output which indicates the boards you have access to. Copy the id from the board you want to work with (indicated by the name field) and paste it into the Trello Board ID field.

TRELLO_API_KEY      `This is used to access your boards via the API`
TRELLO_TOKEN        `This is the token to allow your app access to your boards`
TRELLO_BOARD_ID     `The hex identifier of your board`

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

# Movies

This project is a refactor of the [Multi-User Movie Watch List](https://github.com/ZanClifton/basic-python-projects/tree/main/26-multi-user-movie-watch-list) created in the Mini Python Projects repo. Very little is different, except that instead of writing to a local database, it now writes to PostgreSQL a database at [ElephantSQL](https://www.elephantsql.com/).

#

## Creating A Local Copy

### ✔️ 1. CLONE THE REPO

![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white) ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white) ![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)

Terminal Commands:

```
$ git clone https://github.com/ZanClifton/movies.git
$ cd movies
```

### ✔️ 2. ELEPHANTSQL AND DOTENV

<img height=25 width=60 src="https://github.com/ZanClifton/shrelly-mail-api/blob/main/env.png">

It is recommended that you sign up with [ElephantSQL](https://www.elephantsql.com/) and create your own instance. You don't need to do any complicated configuration to make it work, just sign up and create a free instance (named anything you like) on the [Tiny Turtle](https://www.elephantsql.com/plans.html) plan. Once you have created this, go to the details page and copy the URL.

To be able to run this project locally you'll need to create a file in the main directory:

```
.env
```

You can rename the `.env.example` file to `.env` if you like.

Your `.env` file should already contain the following:

```
DATABASE_URL=
```

Paste your url directly after the `=` sign. You will not need to add anything else.

In the terminal at the root of the project folder run the following command:

```
$ pip install python-dotenv
```

Your local copy should now be set up and ready to use.

### ✔️ 3. USAGE

![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white) ![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)

You don't need an IDE to run the project locally as it runs in the terminal; however, if you wish to make changes to the code or inspect it locally, you will. I recommend VS Code or PyCharm, both of which can be installed for free.

From the root folder of the project, run the script in the terminal:

```
$ python3 main.py
```

#

### Python 3.8

This project was created using Python 3.8 and requires it to run. Please ensure you have updated Python to the latest available version.

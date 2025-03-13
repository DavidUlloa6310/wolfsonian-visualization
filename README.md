# Wolfsonian Visualization

The Wolfsonian Visualization project is focused on helping visitors to FIU's [The Wolfosnian](https://wolfsonian.org/), a museum, art exhibit, and research center understand the experience through data.

## Installation

In order to run the project, you must install [Python](https://www.python.org/) and [Git](https://git-scm.com/) on your local machine. After you've installed both, follow these steps:

1. **Clone the Repository:** To clone the repository, simply run the command `git clone https://github.com/DavidUlloa6310/wolfsonian-visualization.git`. If there's an issue involving authentication, you will need to install the [GitHub CLI tool](https://cli.github.com/) and run `gh auth` before trying again. By running the `git clone` command in your terminal, the repository will be coped to a folder called `wolfsonian_vis` in the same directory your terminal (of which you ran the command) was in.
2. **Create a Virtual Environment & Install Packages:** After copying the repository, you'll need to create a [Python virtual environment](https://docs.python.org/3/library/venv.html). Run the command `python -m venv venv` (or potentially `python3 -m venv venv` if your Python installation's is configured as python3) inside the `wolfsonian_vis` directory. After creating the environment, you'll need to activate it, which means your Python installation will use the installed packages in your `venv` environment. For Mac users, run `source venv/bin/activate`. For Windows users, run `venv\Scripts\activate.bat`. The final step is to install the packages important to the project using the `requirements.txt` file, so run `pip install -r requirements.txt`.
3. **Run Flask Application:** If you've activated your environment your correctly and installed the packages, you'll be able to run `python main.py`, which should start up the Flask application. You'll need to re-activate your virtual environment (but not re-install the packages) everytime you close your terminal. You should see a URL printed to the terminal after running main.py for the link to your site, i.e. http://127.0.0.1:5000.

You should now be able to open that URL and see the Wolfsonian Visualization project! If you make any changes to the codebase while the server is running, all you'll need to do is re-fresh the website to see them.

# ai-agent

boot.dev project that uses the gemini google ai agent.

SETUP

    Create a new directory and Git repository for this project somewhere on your computer.
    Create a virtual environment at the top level of your project directory:

python3 -m venv venv

Always add the venv directory to your .gitignore file.

    Activate the virtual environment:

source venv/bin/activate

You should see (venv) at the beginning of your terminal prompt, for example, mine is:

(venv) wagslane@MacBook-Pro-2 aiagent %

Always make sure that your virtual environment is activated when running the code or using the Boot.dev CLI.

    Create a file called requirements.txt in the top level of your project directory with the following contents:

google-genai==1.12.1
python-dotenv==1.1.0

This tells Python that this project requires google-genai version 1.12.1 and the python-dotenv version 1.1.0.

    Install the requirements:

pip install -r requirements.txt

Run and submit the CLI tests while in your virtual environment.

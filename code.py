#!/usr/local/bin/python3.12

# Import the os module to interact with the operating system
import os

# Import the dotenv module to load environment variables from a .env file
import dotenv

# Import the shutil module for file operations like copying
import shutil

# Import the subprocess module to run external commands
import subprocess

# Import the logging module to log messages
import logging

# Import the argparse module to parse command-line arguments
import argparse


class Code:
    """
    A class to handle environment setup and running code2prompt with specified templates and directories.
    """

    def __init__(self):
        """
        Initializes the Code class with default values and setups environment variables and logging.
        """
        self.display_log: int = 0
        # Initialize display_log attribute to control logging visibility

        self.api_key: str = ''
        # Initialize api_key attribute to store the API key

        self.model: str = ''
        # Initialize model attribute to store the model identifier

        self.script_path: str = os.path.dirname(os.path.realpath(__file__))
        # Determine and store the script's directory path

        self.excluded_folders: str = ''
        # Initialize excluded_folders attribute to store folders to exclude

        self.load_env_variables()
        # Call the method to load environment variables

        self.setup_logging()
        # Call the method to setup logging

    def setup_logging(self):
        """
        Set up logging for this script based on DISPLAY_LOG environment variable.
        """
        self.display_log = os.environ.get('DISPLAY_LOG')
        # Retrieve the DISPLAY_LOG value from environment variables

        if self.display_log == 'True' or self.display_log == '1':
            # Check if logging should be enabled

            logging.basicConfig(
                level=logging.INFO,
                format='%(asctime)s - %(levelname)s: %(message)s',
                datefmt='%Y-%m-%d %H:%M')
            # Configure logging format and level

    def load_env_variables(self):
        """
        Load environment variables from .env file. If .env does not exist, copy from .env.example.
        """
        env_path = f"{self.script_path}/.env"
        # Define the path to the .env file

        env_example_path = f"{self.script_path}/.env.example"
        # Define the path to the .env.example file

        if not os.path.isfile(env_path):
            # Check if the .env file does not exist

            if not os.path.isfile(env_example_path):
                # Check if the .env.example file does not exist

                logging.error(f"{env_example_path} could not be found.")
                # Log an error message

                exit(1)
                # Exit the program with an error code

            shutil.copyfile(env_example_path, env_path)
            # Copy the .env.example file to .env

        dotenv.load_dotenv()
        # Load environment variables from the .env file

        self.model = os.getenv('GROQ_MODEL')
        # Retrieve the GROQ_MODEL value from environment variables

        self.api_key = os.getenv('GROQ_API_KEY')
        # Retrieve the GROQ_API_KEY value from environment variables

        if not (self.model and self.api_key):
            # Check if either the model or api_key is missing

            logging.error("Required environment variables GROQ_MODEL or GROQ_API_KEY are missing.")
            # Log an error message

            exit(2)
            # Exit the program with an error code

    def run_code2prompt(self, template, directory, exclude_folders=None):
        """
        Run code2prompt command with specified template and directory.
        """
        if exclude_folders is None:
            # Check if exclude_folders parameter was not provided

            exclude_folders = "node_modules,build,dist,venv"
            # Set default folders to exclude

        try:
            subprocess.run([
                'code2prompt',
                f'--exclude-folders={exclude_folders}',
                '-t', f"{self.script_path}/templates/{template}.hbs",
                directory,
            ], check=True)
            # Run the code2prompt command with specified parameters

            directory_realpath = os.path.realpath(directory)
            # Get the real path of the directory

            logging.info(f"Successfully ran code2prompt with template \"{template}\" on {directory_realpath}")
            # Log a success message

        except subprocess.CalledProcessError as e:
            # Catch subprocess errors

            logging.error(f"Subprocess failed with message: {e}")
            # Log the error message

            exit(3)
            # Exit the program with an error code

    def list_templates(self):
        """
        List available templates in the templates directory.
        """

        # Define the path to the templates directory using a formatted string that includes script_path
        templates_dir = f"{self.script_path}/templates"

        # Create a list of template names by iterating over files in templates_dir, stripping '.hbs' from their
        # names, and including only those that end with '.hbs'
        templates = [t.replace('.hbs', '') for t in os.listdir(templates_dir) if t.endswith('.hbs')]

        # Print all template names, each on a new line
        print('\n'.join(templates))

        # Exit the program with status 0 (normal termination)
        exit(0)

    def main(self):
        """
        Main method to parse command-line arguments and execute corresponding actions.
        """

        # Initialize an argument parser object with a description of what it does
        parser = argparse.ArgumentParser(
            description="Wrapper around code2prompt tool"
        )

        # Add optional positional argument 'template' for specifying template name
        parser.add_argument(
            'template',
            nargs='?',
            help="Template name"
        )

        # Add optional positional argument 'directory' for specifying target directory where operations will be
        # performed
        parser.add_argument(
            'directory',
            nargs='?',
            help="Target Directory"
        )

        # Add optional flag '--list-templates' to enable listing of available templates when set true
        parser.add_argument(
            '--list-templates',
            action='store_true',
            help="List available templates"
        )

        # Parse command-line arguments and store them in args variable
        args = parser.parse_args()

        # Check if '--list-templates' flag is used; if yes, call list_templates method
        if args.list_templates:
            self.list_templates()

        elif not args.template or not args.directory:
            # If either 'template' or 'directory' is missing, show error message and usage instruction
            parser.error("Not enough parameters. Usage: code <template> <directory>")

        else:
            # If both 'template' and 'directory' are provided, execute run_code2prompt method with these parameters
            self.run_code2prompt(args.template, args.directory)


if __name__ == "__main__":
    Code().main()

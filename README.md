# AI Code Assist

![Python Version](https://img.shields.io/badge/python-3.12-blue) ![License](https://img.shields.io/badge/license-MIT-green) ![Coverage Status](https://img.shields.io/codecov/c/github/thaikolja/ai-code-assist)

## Description

**AI Code Assist** is a Python-based tool that acts as a convenient and easy-to-use wrapper around the [`code2prompt`](https://github.com/mufeedvh/code2prompt) utility, facilitating streamlined template generation and directory management.

## Features

- **Environment Setup**: Automatically loads environment variables from `.env` files.
- **Logging**: Configurable logging based on environment variables.
- **Template Management**: Dynamically lists and utilizes templates for various tasks.
- **Command-line Interface**: Easy-to-use CLI for running commands with specified templates and directories.

## Installation Instructions

1. Clone the repository:

```bash
git clone https://github.com/thaikolja/ai-code-assist.git
cd ai-code-assist
```

2. Ensure you have [Python 3.12 or later](https://www.python.org/downloads/release/python-3120/) installed.

3. Install required dependencies (if any):

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root or ensure an existing 
`.env.example` is present to be copied:

```bash
cp .env.example .env
```

## Usage Examples

To run the tool with a specified template and directory:

```bash
python code.py <template> <directory>
```

For example:

```bash
python code.py pr /path/to/project/
```

To list available templates:

```bash
python code.py --list-templates
```

Explore more about `code2prompt` [here](https://github.com/mufeedvh/code2prompt).

## Configuration

The following environment variables are used:

- `GROQ_MODEL`: The model identifier.
- `GROQ_API_KEY`: The API key for authentication.
- `DISPLAY_LOG`: Set to 'True' or '1' to enable logging.

Ensure these are set in your `.env` file:

```ini
GROQ_MODEL = your_model_id_here
GROQ_API_KEY = your_api_key_here
DISPLAY_LOG = True  # Enable logging; set to False or remove this line to disable logging.
```

Learn more about setting up environment variables in Python [here](https://pypi.org/project/python-dotenv/).

## Contribution

1. Fork the repository on GitHub by clicking [here](https://github.com/thaikolja/ai-code-assist/fork).
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Create a new Pull Request on GitHub via [this link](https://github.com/thaikolja/ai-code-assist/pulls).

Please ensure your contributions adhere to our coding standards and include relevant tests where applicable.

Read our full contribution guidelines [here](CONTRIBUTING.md).

## Testing

This project uses `unittest`. To run tests, execute the following command:

```bash
python -m unittest discover -s tests/
```

Make sure all tests pass before submitting any pull requests.

Learn more about unit testing in Python from this comprehensive
guide [here](https://docs.python.org/3/library/unittest.html).

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details. Find out more about the MIT License [here](https://opensource.org/license/MIT).

## Acknowledgements

### Credits

* **Kolja Nolte** <[kolja.nolte@gmail.com](mailto:kolja.nolte@gmail.com)>

### Thanks

I want to give special thanks to the people behind the original [**code2prompt** CLI](https://github.com/mufeedvh/code2prompt). Check it out and give them a star!

---

Happy coding! 🚀

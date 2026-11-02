# Python with AI & Machine Learning Course Chatbot

A small command-line chatbot that answers questions about a Python with Artificial Intelligence and Machine Learning course. It provides a course overview, a 12-module syllabus, module-by-module topics, the tools covered, and key course features.

This is a beginner-friendly Python project that demonstrates dictionaries, functions, string normalization, conditional logic, and a simple interactive input loop. It is rule-based: it does not use a machine-learning model, an AI service, or an external API.

## Features

- Displays an overview of the course and its 12 learning modules.
- Shows details for each module, from Python fundamentals through a final project.
- Describes course tools and technologies, including Python, Jupyter Notebook, VS Code, NumPy, Pandas, Matplotlib, Scikit-learn, Git, and GitHub.
- Lists course highlights such as practical training, assignments, interview preparation, and portfolio support.
- Recognizes a small set of greetings and provides help for unsupported module requests.
- Runs interactively in a terminal and exits when you enter `bye`.
- Uses only the Python standard library; no package installation or internet connection is required.

## Requirements

- Python 3
- A terminal or command prompt

No third-party packages are needed.

## Run the chatbot

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Run the program with Python 3:

   **Windows**

   ```powershell
   py -3 chatbot.py
   ```

   **macOS / Linux**

   ```bash
   python3 chatbot.py
   ```

If `python3` is the command for Python 3 on your system, you can also use `python3 chatbot.py` on Windows. The program prints a welcome message and then waits for input.

## Commands

| Input | Response |
| --- | --- |
| `hello`, `hi`, `hey` | Greeting |
| `good morning`, `good evening` | Greeting |
| `overview` | Course title, tagline, and summary |
| `modules` | Names of all 12 modules |
| `module 1` through `module 12` | Topics in the selected module |
| `tools` | Course tools and technologies |
| `features` | Course highlights |
| `help` | List of available commands |
| `bye` | End the conversation |

Input is trimmed and converted to lowercase, so capitalization and leading or trailing spaces do not affect recognized commands. For example, `  MODULES ` is treated as `modules`.

### Example session

```text
PyBot: Hello! Welcome to Python with AI & Machine Learning Course Advisor.
PyBot: Type 'overview' to see course summary or 'help' for example commands.
PyBot: Type 'bye' to end the chat.
You: module 9
PyBot: Module 9: MACHINE LEARNING
- Introduction to ML & Types of Machine Learning
- Data Preprocessing & Train-Test Split
- Linear Regression & Logistic Regression
- Decision Tree, Random Forest & KNN
- Model Evaluation (Accuracy, Precision & Recall)
You: bye
PyBot: Goodbye! Have a great learning journey.
```

## How it works

`get_response(message)` normalizes each message and looks it up in a dictionary of supported responses. A few greetings and messages containing `module` have additional rule-based handling; other unrecognized input receives a prompt to try `help`. The main loop reads one message at a time, prints the response, and ends when the user enters `bye`.

## Project structure

```text
Basic-Chatbot/
|-- chatbot.py   # Chatbot responses and interactive command-line loop
|-- README.md    # Project overview and usage instructions
```

## Scope and limitations

This project is an educational, fixed-response course guide. It does not interpret free-form questions, retain conversation history, or connect to a real AI model. Use the exact commands listed above; asking about a module with an unsupported format may return a request to specify a module number from 1 to 12.

## Contributing

Suggestions and improvements are welcome. Keep changes focused, preserve the simple setup, and test the command-line flow with representative commands such as `help`, `overview`, `module 1`, and `bye`.

## License

No license has been specified yet. Unless a license is added, reuse and redistribution are subject to the project's applicable copyright rules.

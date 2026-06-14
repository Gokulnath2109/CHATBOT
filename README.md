# DecoBot - Rule-Based AI Chatbot

## Project Overview

DecoBot is a simple rule-based chatbot developed using Python. It responds to predefined user inputs with randomized replies, simulating a basic conversational experience. This project demonstrates fundamental Python programming concepts such as dictionaries, lists, functions, loops, conditional statements, and user input handling.

## Features

* Interactive command-line chatbot
* Multiple predefined conversation topics
* Randomized responses for natural interaction
* Handles greetings, AI-related questions, jokes, facts, and more
* Supports exit commands (exit, quit, stop)
* Input validation for empty messages

## Technologies Used

* Python 3
* Random Module

## Project Structure

```text
project-folder/
│
├── chatbot.py
├── README.md
```

## How It Works

1. The chatbot waits for user input.
2. User input is converted to lowercase and cleaned.
3. The chatbot searches for a matching predefined response category.
4. A random response is selected and displayed.
5. The conversation continues until the user enters an exit command.

## Installation

1. Install Python 3 on your system.
2. Download or clone this repository.
3. Open a terminal in the project directory.

## Running the Project

```bash
python chatbot.py
```

## Sample Interaction

```text
You: hello
DecoBot: Hi! Welcome to DecoBot!

You: what is ai
DecoBot: AI stands for Artificial Intelligence — machines simulating human thinking.

You: bye
DecoBot: Goodbye! Keep building great things!
```

## Learning Outcomes

* Understanding rule-based chatbot design
* Using Python dictionaries for intent matching
* Working with functions and loops
* Handling user input and program flow
* Generating randomized responses

## Future Improvements

* Partial keyword matching
* More conversation topics
* Chat history storage
* GUI version using Tkinter
* Integration with machine learning models

## Author

Developed as part of the DecodeLabs AI Internship Program.

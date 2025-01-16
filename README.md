# Git Repository to all-in-one Text file Converter
This is a script that generates an all-in-one text file containing your repository's structure and code content, making it easier to analyze or feed into Large Language Models (LLMs) for project understanding.

## Features
- Generates repository tree structure
- Extracts code content from all relevant files
- Ignores common system files, build artifacts, and configuration files
- Supports UTF-8 encoding
- Handles both absolute and relative paths
- Works with any git repository

## Usage
No additional dependencies required - uses only Python standard library!

Clone the git repository to local.
```
git clone git-repository-url
```
Under the path you want to save this text file, run the script:
```
python repo_to_txt.py
```
When prompted "Enter the path to your git repository: ", you can enter the path to the local git repository

## Output
The script will generate a file named ```{repository_name}_repository_content.txt``` containing:

1. A tree view of your repository structure
2. The content of each source file
3. Clear separators between files for easy navigation

#### Example Text File Output
```
Repository Structure:
└── src
  └── main.py
  └── utils
    └── helper.py
└── tests
  └── test_main.py

================================================================================
File: src/main.py
================================================================================
def main():
    print("Hello World")
...

================================================================================
```

## Configuration
The script automatically ignores common files and directories including:

- Build directories (build/, dist/, target/, etc.)
- IDE files (.idea/, .vscode/, etc.)
- Configuration files (.env, .gitignore, etc.)
- System files (.DS_Store, Thumbs.db, etc.)
- Binary and compiled files (.class, .pyc, etc.)
  
To customize ignored patterns, modify the ignore_patterns set in the should_ignore_file() function.

## Use Cases

LLM Training: Generate a comprehensive view of your project for LLMs to understand your codebase

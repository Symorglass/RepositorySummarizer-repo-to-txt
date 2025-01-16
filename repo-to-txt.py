import os
import pathlib
from typing import List, Set

def should_ignore_file(file_path: str) -> bool:
    """
    Check if a file should be ignored based on common patterns.
    """
    ignore_patterns = {
        # Build and cache directories
        '.gradle', 'build', 'dist', 'target', 'out',
        'node_modules', '__pycache__', '.cache', 'bin',
        
        # IDE and editor directories
        '.idea', '.vscode', '.eclipse', '.settings',
        
        # Version control
        '.git',
        
        # Configuration files
        '.gitignore', '.env', '.editorconfig', '.prettierrc',
        'package-lock.json', 'yarn.lock', 'pom.xml',
        'gradle.properties', 'gradlew', 'gradlew.bat',
        'settings.gradle', 'build.gradle',
        
        # Compiled files
        '.class', '.pyc', '.pyo', '.pyd', '.so', '.dll', '.dylib',
        
        # System files
        '.DS_Store', 'Thumbs.db',
        
        # Temporary files
        '*.log', '*.tmp', '*.temp', '*.swp',
        
        # Binary and media files
        '*.pdf', '*.jpg', '*.png', '*.gif', '*.ico',
        '*.zip', '*.tar', '*.gz', '*.rar',
        
        # Database files
        '*.sqlite', '*.sqlite3'
    }
    
    # Check if file matches any ignore pattern
    return any(
        pattern in file_path
        for pattern in ignore_patterns
    )

def get_repository_tree(repo_path: str, indent: str = "  ") -> str:
    """
    Generate a tree structure of the repository.
    """
    tree = ["Repository Structure:", ""]
    
    def add_to_tree(directory: str, level: int = 0):
        entries = sorted(os.scandir(directory), key=lambda e: (e.is_file(), e.name))
        
        for entry in entries:
            if should_ignore_file(entry.path):
                continue
                
            tree.append(f"{indent * level}{'└── ' if level > 0 else ''}{entry.name}")
            
            if entry.is_dir():
                add_to_tree(entry.path, level + 1)
    
    add_to_tree(repo_path)
    return "\n".join(tree)

def get_file_content(file_path: str) -> str:
    """
    Read and return the content of a file.
    Returns empty string if file can't be read.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Warning: Could not read {file_path}: {str(e)}")
        return ""

def process_repository(repo_path: str) -> str:
    """
    Process the entire repository and generate formatted output.
    """
    output_parts = []
    
    # Add repository tree
    output_parts.append(get_repository_tree(repo_path))
    output_parts.append("\n" + "="*80 + "\n")  # Separator
    
    # Process all files
    for root, _, files in os.walk(repo_path):
        for file in sorted(files):
            file_path = os.path.join(root, file)
            
            # Skip ignored files
            if should_ignore_file(file_path):
                continue
            
            # Get relative path from repository root
            rel_path = os.path.relpath(file_path, repo_path)
            
            # Read file content
            content = get_file_content(file_path)
            if content:
                output_parts.extend([
                    f"File: {rel_path}",
                    "="*80,
                    content,
                    "="*80 + "\n"
                ])
    
    return "\n".join(output_parts)

def main():
    # Get repository path from user input
    repo_path = input("Enter the path to your git repository: ").strip()
    
    # Validate path
    if not os.path.exists(repo_path):
        print(f"Error: Path {repo_path} does not exist")
        return
    
    # Process repository
    output = process_repository(repo_path)
    
    # Generate output file name
    repo_name = os.path.basename(os.path.abspath(repo_path))
    output_file = f"{repo_name}_repository_content.txt"
    
    # Write output to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output)
    
    print(f"\nRepository content has been written to {output_file}")

if __name__ == "__main__":
    main()
    
    

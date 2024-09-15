# CLI File Organizer

A command-line tool to organize files in a directory by their type, with options for dry runs and undo functionality.

## Features
- Sort files into folders by type (documents, images, videos, music, etc.)
- Customizable rules for file types
- Dry run mode to simulate the organization
- Undo the last organization operation

## Installation
Clone the repository and set up a virtual environment:
```bash
git clone git@github.com:4xyy/CLI-File-Organizer.git
cd CLI-File-Organizer
python3 -m venv .venv
source .venv/bin/activate

Usage
python organize.py /path/to/directory
Dry Run:
python organize.py /path/to/directory --dry-run
Undo Organization:
python organize.py /path/to/directory --undo

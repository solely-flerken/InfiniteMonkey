import os
import random
import shutil
import string
import subprocess
import time
from datetime import datetime

# Configurable parameters
FILE_PATH = "monkey-attempt.py"
SUCCESS_DIR = "success"
BRANCH_NAME = "main"
MIN_DELAY = 3600  #  1 hour
MAX_DELAY = 43200 # 12 hours
CODE_LENGTH = 50

def generate_random_code():
    """Generate a random string resembling programming code."""
    # Randomly choose characters that are common in Python code (letters, digits, and symbols)
    possible_characters = string.ascii_letters + string.digits + string.punctuation + ' \n'
    random_code = ''.join(random.choice(possible_characters) for _ in range(CODE_LENGTH))
    return random_code

def save_successful_file(file_path):
    """Move the successfully tested file to the success directory with a timestamp."""
    if not os.path.exists(SUCCESS_DIR):
        os.makedirs(SUCCESS_DIR)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    new_filename = f"monkey_success_{timestamp}.py"
    new_path = os.path.join(SUCCESS_DIR, new_filename)

    shutil.move(file_path, new_path)
    print(f"File moved to '{new_path}'")

def test_file(file_path):
    """Test if the Python file executes without errors."""
    try:
        result = subprocess.run(['python', file_path], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"The Monkey finally did it. File '{file_path}' ran successfully.")
            print("Output:", result.stdout)
            return True
        else:
            print(f"The monkey failed: '{file_path}': {result.stderr}")
    except Exception as e:
        print(f"Exception occurred while testing the file: {e}")

    return False

def make_git_changes():
    """Modify the file."""
    random_code = generate_random_code()
    modify_file(FILE_PATH, random_code)

def modify_file(file_path, new_content):
    """Modify the specified file with new content."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)
    print(f"Modified {file_path}")

def git_commit_and_push(commit_message: str):
    """Commit and push changes to GitHub."""
    commands = [
        f"git add -A",
        f'git commit -m "{commit_message}"',
        f"git push origin {BRANCH_NAME}"
    ]

    for cmd in commands:
        process = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        if process.returncode != 0:
            print(f"Error executing command: {cmd}")
            print("Error:", process.stderr)
        else:
            print(f"Command succeeded: {cmd}")
            print(process.stdout)

def schedule_updates():
    """Schedule updates at random intervals."""
    while True:
        delay = random.randint(MIN_DELAY, MAX_DELAY)
        print(f"Waiting for {delay} seconds before the next update...")
        time.sleep(delay)

        make_git_changes()

        if test_file(FILE_PATH):
            commit_message = f"🐵 The monkey actually coded something at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            save_successful_file(FILE_PATH)
        else:
            commit_message = f"🙈 The monkey smashed on the keyboard at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

        git_commit_and_push(commit_message)

if __name__ == '__main__':
    schedule_updates()

import os

# Folder structure
folders = [
    "backend",
    "frontend",
    "frontend/screens",
    "prompts",
    "data",
    "data/teachers",
    "notebooks",
    "scripts"
]

# Files to create (placeholders)
files = [
    "README.md",
    "requirements.txt",
    "backend/app_stub.py",
    "backend/quiz_engine.py",
    "backend/timetable.py",
    "frontend/main.py",
    "frontend/screens/login.kv",
    "frontend/screens/lesson.kv",
    "frontend/screens/quiz.kv",
    "frontend/screens/timetable.kv",
    "prompts/tutor_baseline.txt",
    "data/sample_transcripts.json",
    "data/sample_quiz.json",
    "notebooks/experiment_api_calls.ipynb",
    "scripts/demo_flow.py"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"Created folder: {folder}")

# Create files
for file in files:
    if not os.path.exists(file):
        open(file, 'w').close()
        print(f"Created file: {file}")
    else:
        print(f"File already exists: {file}")

print("\n Lumina skeleton setup complete in the current directory!")
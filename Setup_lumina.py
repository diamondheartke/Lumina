#!/usr/bin/env python3
"""
setup_lumina.py
Create Lumina project skeleton in the current working directory.
Safe to run.
"""

from pathlib import Path
import json
import sys

BASE = Path.cwd()

FOLDERS = [
    "backend",
    "frontend",
    "frontend/screens",
    "prompts",
    "data",
    "notebooks",
    "scripts",
]

FILES_WITH_CONTENT = {
    "README.md": (
        "# Lumina\n\n"
        "Lumina - an AI powered platform with a virtual tutor and timetable generator"    ),
    "requirements.txt": "flask\nrequests\npython-dotenv\n# kivy\n# kivymd\n",
    ".gitignore": "__pycache__/\n.env\n*.pyc\n.DS_Store\n",
    "prompts/tutor_baseline.txt": (
        "You are Lumina, a concise tutor. Use only the provided lesson transcript to answer.\n"
        "If the transcript lacks enough info, respond: \"I don't know - ask a teacher.\""
    ),
    "data/sample_transcripts.json": json.dumps(
        [
            {"id": 1, "title": "Intro to Algebra", "transcript": "Basic algebra concepts..."},
            {"id": 2, "title": "Photosynthesis", "transcript": "Plants convert light into energy..."}
        ],
        indent=2,
    ),
    "data/sample_quiz.json": json.dumps(
        {
            "lesson_id": 1,
            "questions": [
                {"q": "What is x in 2x=4?", "type": "mcq", "choices": ["1","2","3","4"], "answer": "2"},
                {"q": "Name the product of photosynthesis.", "type": "short", "answer": "Glucose"}
            ]
        },
        indent=2,
    ),
    "notebooks/experiment_api_calls.ipynb": "",  # placeholder
    "scripts/demo_flow.py": (
        "# Demo flow script placeholder\n"
        "print('Demo flow placeholder: load data, call handlers, print outputs')\n"
    ),
    "backend/app_stub.py": (
        "from flask import Flask, jsonify, request\n\n"
        "app = Flask(__name__)\n\n"
        "@app.route('/health')\n"
        "def health():\n"
        "    return jsonify({'status': 'ok'})\n\n"
        "if __name__ == '__main__':\n"
        "    app.run(host='0.0.0.0', port=8000)\n"
    ),
    "backend/quiz_engine.py": (
        "def grade_mcq(submitted, answer):\n"
        "    return submitted == answer\n"
    ),
    "backend/timetable.py": (
        "class Timetable:\n"
        "    def __init__(self, days=5, lessons_per_day=10):\n"
        "        self.days = days\n"
        "        self.lessons_per_day = lessons_per_day\n        " 
        "        self.matrix = [[None]*lessons_per_day for _ in range(days)]\n"
        "    def print_table(self):\n"
        "        for d, row in enumerate(self.matrix, 1):\n"
        "            print(f'Day {d}:', row)\n"
    ),
    "frontend/main.py": (
        "# KivyMD frontend placeholder\n"
        "print('Frontend placeholder - KivyMD files will go here')\n"
    ),
    "frontend/screens/login.kv": "<!-- login.kv placeholder -->\n",
    "frontend/screens/lesson.kv": "<!-- lesson.kv placeholder -->\n",
    "frontend/screens/quiz.kv": "<!-- quiz.kv placeholder -->\n",
    "frontend/screens/timetable.kv": "<!-- timetable.kv placeholder -->\n",
    ".env.example": "OPENAI_API_KEY=\nGEMINI_API_KEY=\n",
}

def create_folders():
    for folder in FOLDERS:
        path = BASE / folder
        path.mkdir(parents=True, exist_ok=True)
        print(f"Created folder: {path.relative_to(BASE)}")

def create_files():
    for rel_path, content in FILES_WITH_CONTENT.items():
        path = BASE / rel_path
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            # For large/complex binary placeholders keep empty
            mode = "w"
            path.write_text(content, encoding="utf-8")
            print(f"Created file: {path.relative_to(BASE)}")
        else:
            print(f"File exists: {path.relative_to(BASE)}")

def main():
    print(f"Bootstrapping Lumina skeleton in: {BASE}")
    create_folders()
    create_files()
    print("Done! all files and folders created.")
if __name__ == "__main__":
    main()

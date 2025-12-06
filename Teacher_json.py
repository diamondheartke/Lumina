from JSON import MyJSON
import os
import re

JS = MyJSON()
PATH = "data/teachers"
os.makedirs(PATH, exist_ok=True)

class Teacher:
    def __init__(self, name, *subjects):
        self.ID = self.generate_ID(PATH)
        self.name = name
        self.subjects = list(subjects) 
        self.availability = {
            "Monday": [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10],
            "Tuesday": [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10],
            "Wednesday": [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10],
            "Thursday": [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10],
            "Friday": [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10]
            }

    @staticmethod        
    def list_ids(path: str):
        try:
            files = os.listdir(path)
        except FileNotFoundError:
            return []
        ids = []
        for filename in files:
            if not filename.lower().endswith('.json'):
                continue
            filepath = os.path.join(path, filename)
            try:
                teacher = JS.load_json(filepath)
                if isinstance(teacher, dict) and 'ID' in teacher:
                    ids.append(teacher['ID'])
            except Exception:
                continue
        return ids

    @staticmethod
    def generate_ID(path: str) -> int:
        ids = list_ids(path)
        if not ids:
            return 1
        try:
            max_id = max(int(i) for i in ids)
        except Exception:
            max_id = max(ids)
        return max_id + 1
                                                        
    def send_to_json(self) -> dict:
        data = {
        "ID": self.ID,
        "name": self.name,
        "subjects": self.subjects,
        "availability": self.availability
        }
        return data 

    def safe_filename(self, name) -> str: 
        name = re.sub(r'[^\w\s\-]', '', name).strip().replace(" ", "_")
        name = name.strip('_-. ')
        if not name:
             print("Name cannot be empty! using default")
             name = "Teacher"
        return name 

if __name__ == "__main__":
        
    while True:
        name = input("Enter name: ").strip()
        if name.lower() in ("exit", "quit"):
            break
        subjects_input = input("Enter subjects: ").strip()
        subjects = subjects_input.split() if subjects_input else []
        
        Tr = Teacher(name, *subjects)
        
        safe_name = Tr.safe_filename(name)  
        filename = f"{Tr.ID:02d}_{safe_name}.json" 
        
        filepath = os.path.join(PATH, filename)
        
        JS.create_json(filepath, Tr.send_to_json())
        print(f"JSON created successfully: {filename}")
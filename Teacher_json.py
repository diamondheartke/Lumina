from JSON import MyJSON
import os

JS = MyJSON()
PATH = "data/teachers"

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
            
    def list_tr(self, path):
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

    def generate_ID(self, path):
        ids = self.list_tr(path)
        if not ids:
            return 1
        try:
            max_id = max(int(i) for i in ids)
        except Exception:
            max_id = max(ids)
        return max_id + 1
                                                        
    def send_to_json(self):
        data = {
        "ID": self.ID,
        "name": self.name,
        "subjects": self.subjects,
        "availability": self.availability
        }
        return data 
        
if __name__ == "__main__":
        
        while True:
                   name = input("Enter name: ")
                   if "quit" in name or "exit" in name:
                       break
                   subjects = input("Enter subjects: ").split()
                   Tr = Teacher(name, *subjects)
                   JS.create_json(os.path.join(PATH, f"{str(Tr.ID)}_{Tr.name}.json"), Tr.send_to_json())   
                   #print("JSON created successfully", Tr.name)  
                   
                       

import os
import json
from typing import Dict, List

class FileStructureAnalyzer:
    def __init__(self, root_dir: str):
        self.root_dir = root_dir
        self.structure: Dict[str, List[str]] = {}

    def analyze(self) -> None:
        for dirpath, dirnames, filenames in os.walk(self.root_dir):
            relative_path = os.path.relpath(dirpath, self.root_dir)
            self.structure[relative_path] = filenames

    def get_structure(self) -> Dict[str, List[str]]:
        return self.structure

    def save_structure(self, filename: str) -> None:
        with open(filename, 'w') as f:
            json.dump(self.structure, f, indent=2)

    @staticmethod
    def load_structure(filename: str) -> Dict[str, List[str]]:
        with open(filename, 'r') as f:
            return json.load(f)

# Usage
if __name__ == "__main__":
    analyzer = FileStructureAnalyzer("/path/to/your/codebase")
    analyzer.analyze()
    analyzer.save_structure("file_structure.json")
    
    # Later, you can load the structure
    loaded_structure = FileStructureAnalyzer.load_structure("file_structure.json")
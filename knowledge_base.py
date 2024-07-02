import json
from typing import Dict, Any
from file_structure_analyzer import FileStructureAnalyzer
from code_parser import CodeParser

class KnowledgeBase:
    def __init__(self):
        self.file_structure: Dict[str, Any] = {}
        self.code_summaries: Dict[str, Any] = {}

    def add_file_structure(self, structure: Dict[str, Any]) -> None:
        self.file_structure = structure

    def add_code_summary(self, file_path: str, summary: Dict[str, Any]) -> None:
        self.code_summaries[file_path] = summary

    def get_file_structure(self) -> Dict[str, Any]:
        return self.file_structure

    def get_code_summary(self, file_path: str) -> Dict[str, Any]:
        return self.code_summaries.get(file_path, {})

    def save(self, filename: str) -> None:
        data = {
            'file_structure': self.file_structure,
            'code_summaries': self.code_summaries
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

    @staticmethod
    def load(filename: str) -> 'KnowledgeBase':
        with open(filename, 'r') as f:
            data = json.load(f)
        kb = KnowledgeBase()
        kb.file_structure = data['file_structure']
        kb.code_summaries = data['code_summaries']
        return kb

# Usage
if __name__ == "__main__":
    kb = KnowledgeBase()
    kb.add_file_structure(FileStructureAnalyzer.load_structure("file_structure.json"))
    
    parser = CodeParser("/path/to/your/file.py")
    parser.parse()
    parser.analyze()
    kb.add_code_summary("/path/to/your/file.py", parser.get_summary())
    
    kb.save("knowledge_base.json")
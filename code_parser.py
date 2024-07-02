import ast
from typing import Dict, Any

class CodeParser:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.ast_tree: Any = None
        self.summary: Dict[str, Any] = {}

    def parse(self) -> None:
        with open(self.file_path, 'r') as file:
            source = file.read()
            self.ast_tree = ast.parse(source)

    def analyze(self) -> None:
        self.summary['functions'] = [node.name for node in ast.walk(self.ast_tree) if isinstance(node, ast.FunctionDef)]
        self.summary['classes'] = [node.name for node in ast.walk(self.ast_tree) if isinstance(node, ast.ClassDef)]
        self.summary['imports'] = [node.names[0].name for node in ast.walk(self.ast_tree) if isinstance(node, ast.Import)]

    def get_summary(self) -> Dict[str, Any]:
        return self.summary

# Usage
if __name__ == "__main__":
    parser = CodeParser("/path/to/your/file.py")
    parser.parse()
    parser.analyze()
    print(parser.get_summary())
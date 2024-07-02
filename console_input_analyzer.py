import re
from typing import Dict, Any

class ConsoleInputAnalyzer:
    def __init__(self):
        self.error_patterns = {
            'python': r'^Traceback \(most recent call last\):\n(.*?)^\w+Error: (.*)$',
            'javascript': r'^(\w+Error): (.*)$',
            # Add more patterns for other languages
        }

    def analyze(self, console_output: str, language: str) -> Dict[str, Any]:
        pattern = self.error_patterns.get(language)
        if not pattern:
            return {'error': 'Unsupported language'}

        match = re.search(pattern, console_output, re.DOTALL | re.MULTILINE)
        if match:
            if language == 'python':
                return {
                    'type': 'error',
                    'traceback': match.group(1).strip(),
                    'error_message': match.group(2).strip()
                }
            elif language == 'javascript':
                return {
                    'type': 'error',
                    'error_type': match.group(1),
                    'error_message': match.group(2)
                }
        
        return {'type': 'unknown'}

# Usage
if __name__ == "__main__":
    analyzer = ConsoleInputAnalyzer()
    python_output = """
Traceback (most recent call last):
  File "example.py", line 10, in <module>
    result = 10 / 0
ZeroDivisionError: division by zero
"""
    result = analyzer.analyze(python_output, 'python')
    print(result)
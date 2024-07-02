from typing import Dict, Any
import openai

class AIDebuggingEngine:
    def __init__(self, api_key: str):
        self.api_key = api_key
        openai.api_key = self.api_key

    def generate_debug_suggestion(self, error_info: Dict[str, Any], code_context: str) -> str:
        prompt = f"""
        Error information:
        {error_info}
        
        Code context:
        {code_context}
        
        Based on the error information and code context provided, suggest a solution to debug this issue:
        """
        
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=150
        )
        
        return response.choices[0].text.strip()

    def generate_code_fix(self, error_info: Dict[str, Any], code_context: str) -> str:
        prompt = f"""
        Error information:
        {error_info}
        
        Code context:
        {code_context}
        
        Based on the error information and code context provided, generate a code fix to resolve this issue:
        """
        
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=200
        )
        
        return response.choices[0].text.strip()

# Usage
if __name__ == "__main__":
    engine = AIDebuggingEngine("your-openai-api-key")
    error_info = {
        'type': 'error',
        'error_type': 'ZeroDivisionError',
        'error_message': 'division by zero'
    }
    code_context = """
    def divide(a, b):
        return a / b
    
    result = divide(10, 0)
    print(result)
    """
    suggestion = engine.generate_debug_suggestion(error_info, code_context)
    code_fix = engine.generate_code_fix(error_info, code_context)
    print("Suggestion:", suggestion)
    print("Code Fix:", code_fix)
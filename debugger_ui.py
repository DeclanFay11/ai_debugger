import tkinter as tk
from tkinter import filedialog, scrolledtext
from file_structure_analyzer import FileStructureAnalyzer
from code_parser import CodeParser
from knowledge_base import KnowledgeBase
from console_input_analyzer import ConsoleInputAnalyzer
from ai_debugging_engine import AIDebuggingEngine

class DebuggerUI:
    def __init__(self, master):
        self.master = master
        master.title("AI-Powered Debugger")

        self.kb = KnowledgeBase()
        self.console_analyzer = ConsoleInputAnalyzer()
        self.ai_engine = AIDebuggingEngine("your-openai-api-key")

        self.create_widgets()

    def create_widgets(self):
        # File selection
        self.file_btn = tk.Button(self.master, text="Select File", command=self.select_file)
        self.file_btn.pack()

        # Console input
        self.console_label = tk.Label(self.master, text="Console Output:")
        self.console_label.pack()
        self.console_input = scrolledtext.ScrolledText(self.master, height=10)
        self.console_input.pack()

        # Debug button
        self.debug_btn = tk.Button(self.master, text="Debug", command=self.debug)
        self.debug_btn.pack()

        # Results
        self.results_label = tk.Label(self.master, text="Debug Results:")
        self.results_label.pack()
        self.results_output = scrolledtext.ScrolledText(self.master, height=10)
        self.results_output.pack()

    def select_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            parser = CodeParser(file_path)
            parser.parse()
            parser.analyze()
            self.kb.add_code_summary(file_path, parser.get_summary())

    def debug(self):
        console_output = self.console_input.get("1.0", tk.END)
        error_info = self.console_analyzer.analyze(console_output, 'python')  # Assuming Python for now
        
        if 'error' in error_info:
            file_path = list(self.kb.code_summaries.keys())[0]  # Just use the first file for this example
            code_context = open(file_path, 'r').read()  # In a real app, you'd want to be more selective
            
            suggestion = self.ai_engine.generate_debug_suggestion(error_info, code_context)
            code_fix = self.ai_engine.generate_code_fix(error_info, code_context)
            
            self.results_output.delete("1.0", tk.END)
            self.results_output.insert(tk.END, f"Suggestion: {suggestion}\n\nCode Fix: {code_fix}")
        else:
            self.results_output.delete("1.0", tk.END)
            self.results_output.insert(tk.END, "No error detected in console output.")

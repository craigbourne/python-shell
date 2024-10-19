import os
import shlex
import re

class SecureSimpleShell:
    def __init__(self):
        self.running = True
        self.commands = {
            "list": "List the contents of the current directory",
            "add": "Add two numbers (Usage: ADD <number1> <number2>)",
            "help": "Show this help message",
            "exit": "Exit the shell"
        }

    def run(self):
        print("Welcome to SecureSimpleShell! Type 'help' for a list of commands.")
        while self.running:
            user_input = input("SecureSimpleShell> ").strip()
            if user_input.lower() == "exit":
                self.running = False
            else:
                self.execute_command(user_input)

    def execute_command(self, command):
        # Sanitise input to prevent command injection
        sanitised_command = self.sanitise_input(command)
        parts = shlex.split(sanitised_command)
        
        if not parts:
            return
        
        cmd = parts[0].lower()
        if cmd == "list":
            self.list_directory()
        elif cmd == "add":
            if len(parts) == 3 and self.validate_numbers(parts[1], parts[2]):
                self.add_numbers(parts[1], parts[2])
            else:
                print("Usage: ADD <number1> <number2>")
        elif cmd == "help":
            self.show_help()
        else:
            print(f"Unknown command: {cmd}")

    def sanitise_input(self, input_string):
        # Remove any potentially dangerous characters
        return re.sub(r'[;&|]', '', input_string)

    def validate_numbers(self, num1, num2):
        # Ensure inputs are valid numbers
        return re.match(r'^-?\d+(\.\d+)?$', num1) and re.match(r'^-?\d+(\.\d+)?$', num2)

    def list_directory(self):
        """List the contents of the current directory."""
        try:
            items = os.listdir()
            for item in items:
                # Sanitise output to prevent potential XSS if output is ever displayed in a web context
                print(self.sanitise_output(item))
        except Exception as e:
            print(f"Error listing directory: {str(e)}")

    def add_numbers(self, num1, num2):
        """Add two numbers and print the result."""
        try:
            result = float(num1) + float(num2)
            print(f"Result: {result}")
        except ValueError:
            print("Error: Please enter valid numbers.")

    def show_help(self):
        """Display the list of available commands."""
        print("Available commands:")
        for cmd, description in self.commands.items():
            print(f"  {cmd.upper()}: {description}")

    def sanitise_output(self, output):
        # Implement output sanitisation (e.g., HTML escaping) if needed
        return re.sub(r'[<>&]', '', output)  # Basic sanitisation for demonstration

if __name__ == "__main__":
    shell = SecureSimpleShell()
    shell.run()
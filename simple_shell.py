import os

class SimpleShell:
    def __init__(self):
        self.running = True

    def run(self):
        while self.running:
            user_input = input("SimpleShell> ").strip()
            if user_input.lower() == "exit":
                self.running = False
            else:
                self.execute_command(user_input)

    def execute_command(self, command):
        parts = command.split()
        if parts[0].lower() == "list":
            self.list_directory()
        elif parts[0].lower() == "add":
            if len(parts) == 3:
                self.add_numbers(parts[1], parts[2])
            else:
                print("Usage: ADD <number1> <number2>")
        else:
            print(f"Unknown command: {command}")

    def list_directory(self):
        """List the contents of the current directory."""
        try:
            items = os.listdir()
            for item in items:
                print(item)
        except Exception as e:
            print(f"Error listing directory: {e}")

    def add_numbers(self, num1, num2):
        """Add two numbers and print the result."""
        try:
            result = float(num1) + float(num2)
            print(f"Result: {result}")
        except ValueError:
            print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    shell = SimpleShell()
    shell.run()
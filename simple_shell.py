import os
import subprocess

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
        if command.lower() == "list":
            self.list_directory()
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

if __name__ == "__main__":
    shell = SimpleShell()
    shell.run()
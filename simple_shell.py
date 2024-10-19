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
        # This will handle different commands
        pass

if __name__ == "__main__":
    shell = SimpleShell()
    shell.run()
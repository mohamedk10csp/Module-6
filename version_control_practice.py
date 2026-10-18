"""Module 6: Individual Git and GitHub Practice.

Run this starter program, complete the TODO tasks, and commit your changes.
No outside packages are required.
"""


def show_project_info():
    """Display basic information about this version-control exercise."""
    project_name = "Khalid's Git Practice Project"
    version = "2.0"
    print(f"Project: {project_name}")
    print(f"Version: {version}")
    print("Git helps track changes in a software project.")


def show_git_workflow():
    """Print the basic sequence used in this exercise."""
    steps = [
        "1. Edit and save your Python file.",
        "2. Stage your changes with git add.",
        "3. Record a local commit with git commit.",
        "4. Upload your commit to GitHub with git push.",
    ]
    for step in steps:
        print(step)


def main():
    show_project_info()
    print()
    show_git_workflow()
    print()

    # TODO 1: Change the project_name and version values above to your own.
    # TODO 2: Add a print() statement below that explains, in your own words,
    #         why it is useful to save your code changes with Git.
    # TODO 3: Add another print() statement describing one difference
    #         between git commit and git push.
    print("Git is useful because it saves the history of code changes and helps recover older versions.")
    print("Git commit saves changes locally, while git push uploads committed changes to GitHub.")

if __name__ == "__main__":
    main() 
   

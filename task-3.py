"""
Display a directory tree with colored directory and file names.
Used with a directory path as a command-line argument or defaults to the "picture" directory.
"""

# sys for command-line arguments, pathlib for path manipulations, and colorama for colored output.
import sys
from pathlib import Path

from colorama import Fore, Style, init


# Define colors for directories and files
DIRECTORY_COLOR = Fore.BLUE
FILE_COLOR = Fore.GREEN


def print_tree(path: Path, prefix: str = "") -> None:
    """Print ``path`` and all its descendants as a colored tree."""
    try:
        # Keep files and directories together in alphabetical order.
        entries = sorted(
            # Use iterdir() to get all entries in the directory
            path.iterdir(),
            # Sort entries by name in a case-insensitive manner
            key=lambda entry: entry.name.lower(),
        )
    # Handle errors if the directory cannot be read (e.g., due to permissions)
    except OSError as error:
        # Print an error message in red indicating the directory cannot be read
        print(f"{prefix}{Fore.RED}[cannot read: {error}]")
        # return from the function to avoid further processing of this directory
        return

    # Loop through each entry in the sorted list of directory entries
    for entry in entries:
        # Determine the color based on whether the entry is a directory or a file
        entry_color = DIRECTORY_COLOR if entry.is_dir() else FILE_COLOR
        # Add a suffix of "/" for directories to visually indicate they are directories
        suffix = "/" if entry.is_dir() else ""
        # Print the entry name with the appropriate color and prefix, followed by the suffix ("/" for directories)
        # STYLE.RESET_ALL resets the color back to default after printing the entry name
        print(f"{prefix}{entry_color}{entry.name}{suffix}{Style.RESET_ALL}")

        # If the entry is a directory and not a symbolic link, recursively call print_tree to print its contents
        if entry.is_dir() and not entry.is_symlink():
            # prefix is a string that is prepended to each line of output to create a visual indentation for nested directories
            print_tree(entry, prefix + "    ")


def main() -> int:
    """Validate the command-line argument and display the directory tree."""
    # Check if more than one argument is provided (the script name is always the first argument)
    # sys.argv is a list of command-line arguments passed to the script, where sys.argv[0] is the script name and sys.argv[1:] are the additional arguments
    if len(sys.argv) > 2:
        # Print an error message to stderr indicating the correct usage of the script
        # file=sys.stderr used to direct the output to the standard error stream instead of the standard output stream
        print(f"Usage: python {Path(sys.argv[0]).name} [directory]", file=sys.stderr)
        # return 1 to indicate an error occurred due to incorrect usage
        return 1

    # Determine the directory to display, defaulting to "picture" if no argument is provided
    directory = Path(sys.argv[1] if len(sys.argv) == 2 else "picture").expanduser()
    if not directory.exists():
        print(f"Error: directory does not exist: {directory}", file=sys.stderr)
        return 1
    if not directory.is_dir():
        print(f"Error: path is not a directory: {directory}", file=sys.stderr)
        return 1

    # Initialize colorama to enable colored output in the terminal
    # autoreset=False means that the color settings will not automatically reset after each print statement, allowing for more control over when colors are reset
    init(autoreset=False)
    # Print the root directory name in blue, followed by a "/" to indicate it's a directory
    print(f"{DIRECTORY_COLOR}{directory.name or directory}{Style.RESET_ALL}/")
    # Call print_tree to recursively print the directory tree starting from the specified directory, with an initial indentation of four spaces
    print_tree(directory, "    ")
    # Return 0 to indicate successful execution of the script
    # 0 or 1 is used to indicate success or failure of the script execution, respectively. 0 means success, while 1 indicates an error occurred.
    return 0


# If the script is being run directly (not imported as a module), call the main function and exit with its return code.
if __name__ == "__main__":
    sys.exit(main())

# Context Printer Script

This script prints the contents of files from a specified directory or a list of files for context in a query.

## Features

- Handles both directories and individual files.
- Supports recursive directory traversal with a flag.
- Limits file reading to a maximum size of 1MB.
- Outputs the content in a structured format.

## Requirements

- Python 3.x

## Usage

## Bash Alias

```
alias context_printer='python /path/to/context_printer.py'
```

### Running the Script

1. **For a directory** (optionally recursive):
    ```sh
    context_printer --directory /path/to/directory --recursive
    ```

2. **For specific files**:
    ```sh
    context_printer --files /path/to/file1 /path/to/file2
    ```

3. **Copy output directly to clipboard**
    ```sh
    context_printer --files /path/to/file1 /path/to/file2 | pbcopy
    ```
    
### Command Line Arguments

- `--directory`: Path to the directory containing files.
- `--files`: List of individual file paths.
- `--recursive`: (Optional) Recursively include files from subdirectories when a directory is specified.

### Example Outputs

```
Below are the files for the context of the query, files are separated by ====
====
Filename: relative/path/to/file1
Contents: (contents of file1)
====
Filename: relative/path/to/file2
Contents: (contents of file2)
====
```

## Notes

- The script will skip files larger than 1MB.
- Ensure the script has the necessary permissions to read the files and directories specified.


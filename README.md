# Context Printer Script

This script prints the contents of files from a specified directory or a list of files for context in a query.

## Features

- Handles both directories and individual files.
- Supports recursive directory traversal with a flag.
- Limits file reading to a maximum size of 1MB.
- Outputs the content in a structured format.
- Can split large text into chunks for easier handling.

## Requirements

- Python 3.x

## Usage

### Bash Alias

```
alias context_printer='python /path/to/context_printer.py'
alias prompt_chunker='python /path/to/prompt_chunker.py'
```

### Running the Script

1. **For a directory** (optionally recursive):
    ```sh
    context_printer --directory /path/to/directory --recursive
    ```

2. **Ignore a subdirectory**
    ```sh
    context_printer --directory /path/to/project --recursive --ignore ".terraform" ".git"
    ```

3. **For specific files**:
    ```sh
    context_printer --files /path/to/file1 /path/to/file2
    ```

4. **Copy output directly to clipboard**
    ```sh
    context_printer --files /path/to/file1 /path/to/file2 | pbcopy
    ```

### Splitting Output into Chunks

If you need to split the output into chunks for easier handling, you can use the `prompt_chunker` script.

1. **Pipe the output of `context_printer` into `prompt_chunker`**:
    ```sh
    context_printer --directory /path/to/directory --recursive | prompt_chunker 500 -out ./output_chunks
    ```

2. **Explanation of parameters**:
    - `500`: The length of each chunk.
    - `-out ./output_chunks`: The directory where chunk files will be saved.

3. **Initial Instruction for Chunk Handling**:
    ```sh
    Please copy the following initial instruction followed by each of the chunk files.

    ----------
    The total length of the content that I want to send you is too large to send in only one piece.

    For sending you that content, I will follow this rule:

    [START PART 1/10]
    this is the content of the part 1 out of 10 in total
    [END PART 1/10]

    Then you just answer: "Received part 1/10"

    And when I tell you "ALL PARTS SENT", then you can continue processing the data and answering my requests.
    ----------
    ```

4. **For each chunk file**:
    ```sh
    Chunk saved to output_chunks/20240730160915-chunk-1.txt. To copy run the following command and paste into ChatGPT
    cat output_chunks/20240730160915-chunk-1.txt | pbcopy
    ```

### Command Line Arguments

- `--directory`: Path to the directory containing files.
- `--files`: List of individual file paths.
- `--recursive`: (Optional) Recursively include files from subdirectories when a directory is specified.
- `--ignore`: (Optional) Ignore files or directories matching this pattern.
- `split_length`: Length of each chunk when using `prompt_chunker`.
- `-out`: Output directory for chunk files when using `prompt_chunker`.

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

This updated README includes all the necessary details on how to use both the context printer script and the chunker script.
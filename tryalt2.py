import os

# Path to the "names" folder (update this to the correct path on your system)
names_folder_path = "names"

def get_first_non_text_files_from_folders(root_directory, max_folders=5):
    """
    Get the first non-text file (not a .txt file) from the first `max_folders` folders in the root directory.
    The folders are sorted alphabetically by their names (e.g., "firstname lastname").
    
    :param root_directory: Path to the root directory to search in.
    :param max_folders: Number of folders to process.
    :return: List of tuples containing folder name, file name, and the count of non-text files.
    """
    folder_count = 0
    first_files = []

    # Get all folder paths in the root directory and sort them alphabetically
    folder_paths = [os.path.join(root_directory, folder) for folder in os.listdir(root_directory) 
                    if os.path.isdir(os.path.join(root_directory, folder))]
    folder_paths.sort()  # Sort folders alphabetically

    # Total number of folders
    total_folders = len(folder_paths)

    # Iterate through the sorted folder paths
    for folder_path in folder_paths:
        # Stop if we've reached the max_folders limit
        if folder_count >= max_folders:
            break

        # Get the filenames in the folder, but exclude text files (not ending with .txt)
        non_text_files = sorted([f for f in os.listdir(folder_path) if not f.endswith(".txt")])

        if non_text_files:
            # Add the folder name, first non-text file, and count of non-text files
            first_files.append((os.path.basename(folder_path), non_text_files[0], len(non_text_files)))
            folder_count += 1

    return first_files, total_folders

def find_step_file_in_folder(folder_path):
    """
    Looks for a step.txt file within a folder and returns its content if found.
    
    :param folder_path: The path to the folder to search in.
    :return: Content of the step.txt file, or None if not found.
    """
    step_file_path = os.path.join(folder_path, "step.txt")
    if os.path.isfile(step_file_path):
        with open(step_file_path, 'r') as file:
            return file.read().strip()  # Return the text found in step.txt
    return None

def process_step_file(step_text):
    """
    Process the step text to determine the next file or folder to look for.
    This is where the logic for step-by-step processing would go.

    :param step_text: Text found in the step.txt file to guide the search.
    :return: None
    """
    # Example: If the step text is the name of the next file or folder to search for
    print(f"Processing step with text: {step_text}")
    # The actual logic for using the `step_text` can be added here
    return step_text  # You can customize this as needed.

def get_non_text_files_and_process_step(root_directory, max_folders=5):
    """
    Search for the first non-text file in each folder, then look for step.txt.
    If found, process the step and repeat the process as needed.
    
    :param root_directory: Path to the root directory to search in.
    :param max_folders: Number of folders to process.
    """
    first_files, total_folders = get_first_non_text_files_from_folders(root_directory, max_folders)

    # Output the first non-text files found and count of non-text files in each folder
    print("First non-text files from the first 5 folders:")
    for folder_name, file_name, file_count in first_files:
        print(f"Folder: {folder_name}, First Non-Text File: {file_name}, Non-Text File Count: {file_count}")

        # Now look for a step.txt file in the folder and process its content if found
        step_text = find_step_file_in_folder(os.path.join(root_directory, folder_name))
        if step_text:
            print(f"Found step.txt with content: {step_text}")
            process_step_file(step_text)
        else:
            print("No step.txt found in this folder.")

    # Display the total number of folders investigated
    print(f"\nTotal number of folders investigated: {total_folders}")

# Start the process
get_non_text_files_and_process_step(names_folder_path, max_folders=5)

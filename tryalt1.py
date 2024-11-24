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

def search_file_in_directory(root_directory, file_name):
    """
    Search for a specific file within a directory and its subdirectories.

    :param root_directory: Path to the root directory to search in.
    :param file_name: Name of the file to search for.
    :return: Full path of the file if found, None otherwise.
    """
    for dirpath, dirnames, filenames in os.walk(root_directory):
        if file_name in filenames:
            return os.path.join(dirpath, file_name)
    return None

# Get the first non-text files from the first five folders
first_files, total_folders = get_first_non_text_files_from_folders(names_folder_path, max_folders=5)

# Output the first non-text files found and count of non-text files in each folder
print("First non-text files from the first 5 folders:")
for folder_name, file_name, file_count in first_files:
    print(f"Folder: {folder_name}, First Non-Text File: {file_name}, Non-Text File Count: {file_count}")

# Display the total number of folders investigated
print(f"\nTotal number of folders investigated: {total_folders}")

# Example of a non-text file to search for
target_file = "example_image.jpg"  # Change this to the file you are looking for

# Search for the target file
result = search_file_in_directory(names_folder_path, target_file)

# Output the result of the search
if result:
    print(f"File found: {result}")
else:
    print(f"The file '{target_file}' was not found in the '{names_folder_path}' folder.")

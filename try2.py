import os

# Path to the "names" folder (update this to the correct path on your system)
names_folder_path = "names"

# Target file to search for
target_file = "f081ced9-2c7b-4505-973a-630979eb8100.txt"

def get_first_files_from_folders(root_directory, max_folders=5):
    """
    Get the first text file from the first `max_folders` folders in the root directory.
    The folders are sorted alphabetically by their names (e.g., "firstname lastname").
    
    :param root_directory: Path to the root directory to search in.
    :param max_folders: Number of folders to process.
    :return: List of tuples containing folder name, file name, and the count of text files.
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

        # Get the filenames in the folder and sort them alphabetically
        text_files = sorted([f for f in os.listdir(folder_path) if f.endswith(".txt")])

        if text_files:
            # Add the folder name, first text file, and count of text files
            first_files.append((os.path.basename(folder_path), text_files[0], len(text_files)))
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

# Get the first text files from the first five folders
first_files, total_folders = get_first_files_from_folders(names_folder_path, max_folders=5)

# Output the first text files found and count of text files in each folder
print("First text files from the first 5 folders:")
for folder_name, file_name, file_count in first_files:
    print(f"Folder: {folder_name}, First File: {file_name}, Text File Count: {file_count}")

# Display the total number of folders investigated
print(f"\nTotal number of folders investigated: {total_folders}")

# Search for the target file
result = search_file_in_directory(names_folder_path, target_file)

# Output the result of the search
if result:
    print(f"File found: {result}")
else:
    print(f"The file '{target_file}' was not found in the '{names_folder_path}' folder.")

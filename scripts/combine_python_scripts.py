import os

script_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(script_directory)
app_directory = os.path.join(parent_directory, "app")

blacklist_folders = ["__pycache__", "alembic"]
blacklist_files = ["__init__.py"]
whitelist_extensions = [".py"]


def print_all_files(folder_path):
    for root, dirs, files in os.walk(folder_path):
        dirs[:] = [d for d in dirs if d not in blacklist_folders]

        for file in files:
            if file in blacklist_files:
                continue

            if not any(file.endswith(ext) for ext in whitelist_extensions):
                continue

            print(os.path.join(root, file))


print_all_files(app_directory)

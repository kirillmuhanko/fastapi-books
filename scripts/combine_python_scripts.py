import os

script_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(script_directory)
app_directory = os.path.join(parent_directory, "app")

blacklist_folders = ["__pycache__", "alembic"]
blacklist_files = ["__init__.py"]
whitelist_extensions = [".py"]
output_file = os.path.join(app_directory, "__pycache__", "combined_scripts.txt")


def combine_python_scripts_into_txt(folder_path, output_file):
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as outfile:
        for root, dirs, files in os.walk(folder_path):
            dirs[:] = [d for d in dirs if d not in blacklist_folders]

            for file in files:
                if file in blacklist_files:
                    continue

                if not any(file.endswith(ext) for ext in whitelist_extensions):
                    continue

                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, parent_directory)
                outfile.write(f"# File: {relative_path}\n")
                outfile.write(f"# {'-'*len(relative_path)}\n")

                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                outfile.write(content)
                outfile.write("\n\n")

    print(f"All Python script content has been saved to {output_file}")


combine_python_scripts_into_txt(app_directory, output_file)

import os


def get_files_info(working_directory, directory="."):
    abs_working_dir = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(abs_working_dir, directory))

    if not full_path.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory\n'

    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory\n'

    final_response = ""
    contents = os.listdir(full_path)
    for content in contents:
        content_path = os.path.join(full_path, content)
        content_size = os.path.getsize(content_path)
        is_dir = os.path.isdir(content_path)
        final_response += f"- {content}: file_size={content_size}, is_dir={is_dir}\n"
    return final_response

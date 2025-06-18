import os.path

def get_files_info(working_directory, directory=None):
    cwd_abs_path = os.path.abspath(working_directory)
    dir_abs_path = cwd_abs_path
    if directory:
        dir_abs_path = os.path.abspath(os.path.join(cwd_abs_path, directory))
    if not dir_abs_path.startswith(cwd_abs_path):
        return f'Error: Cannot list "{directory}" as it is outside of the permitted working directory'

    is_dir = os.path.isdir(dir_abs_path)
    if not is_dir:
        return f'Error: "{directory}" is not a directory'

    # print(f"is_dir={is_dir}")
    if is_dir:
        dir_listing = []
        for f in os.listdir(dir_abs_path):
            filepath = os.path.join(dir_abs_path, f)
            filesize = os.path.getsize(filepath)
            file_is_dir = os.path.isdir(filepath)
            dir_listing.append(f"- {f}: file_size={filesize} bytes, is_dir={file_is_dir} ")
            # print(f"- {f}: file_size={filesize} bytes, is_dir={file_is_dir} ")
        return "\n".join(dir_listing)


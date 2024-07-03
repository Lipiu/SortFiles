import os
import shutil

def make_name(name, dest_list):
    base_name, ext = os.path.splitext(name)
    counter = 1
    while name in dest_list:
        name = f"{base_name}{counter}{ext}"
        counter += 1
    return name

def organize_files(src, dest_dict):
    for file_name in os.listdir(src):
        for file_type, dest_path in dest_dict.items():
            if file_name.endswith(file_type):
                if not os.path.exists(dest_path):
                    os.makedirs(dest_path)
                new_name = make_name(file_name, os.listdir(dest_path))
                os.rename(os.path.join(src, file_name), os.path.join(src, new_name))
                shutil.move(os.path.join(src, new_name), dest_path)

src = '.'
destinations = {
    '.doc': './Word Files',
    '.docx': './Word Files',
    '.xlsx': './Excel Files',
    '.accdb': './Access Files',
    '.ppt': './PPT Files',
    '.pptx': './PPT Files',
    '.pdf': './PDF Files',
    '.zip': './ZIP Files',
    '.rar': './ZIP Files',
    '.txt': './TXT Files'
}

organize_files(src, destinations)

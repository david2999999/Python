import time
import os

mod_time = os.path.getmtime("C:\\Users\\david2999999\\Desktop\\Python\\PDF\\File_And_Directory")
print(time.ctime(mod_time))

def print_dir_info(dir_path):
    for name in os.listdir(dir_path):
        full_path = os.path.join(dir_path, name)
        file_size = os.path.getsize(full_path)
        mod_time = time.ctime(os.path.getmtime(full_path))
        print("-%32s: %8d bytes, modified %s" % (name, file_size, mod_time))

print_dir_info("C:\\Users\\david2999999\\Desktop\\Python\\PDF\\File_And_Directory")
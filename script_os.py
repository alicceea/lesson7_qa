import os.path

current_file = os.path.abspath(__file__)

current_dir = os.path.dirname(current_file)

tmp_dir = os.path.join(current_dir, "tmp")
print(tmp_dir)
import os

funsearch_path = "funsearch-tsp/"
folder_path = os.path.join(funsearch_path, "TSPLIB_Dataset")
tsp_dict = {}

# Get the absolute path of the TSP dataset folder
absolute_folder_path = os.path.abspath(folder_path)

# Get a list of all the files in the folder
file_list = os.listdir(absolute_folder_path)

# Filter the list to only include files with the ".tsp" extension
tsp_files = [file for file in file_list if file.endswith(".tsp")]

# Iterate through the tsp files and read their contents
for tsp_file in tsp_files:
    file_path = os.path.join(absolute_folder_path, tsp_file)
    with open(file_path, 'r') as file:
        file_contents = file.read()
    
    # Store the file contents as key-value pairs in the tsp_dict dictionary
    tsp_dict[tsp_file[:-4]] = file_contents

# Update the TSP_utils.py file with the dictionary contents
TSP_utils_path = os.path.join(funsearch_path, "TSP_utils.py")
with open(TSP_utils_path, 'a') as utils_file:
    utils_file.write("datasets['TSPLIB'] = {\n")
    for key, value in tsp_dict.items():
        utils_file.write(f"'{key}':\"\"\"{value}\"\"\",\n")
    utils_file.write("}")

print("The TSP datasets are preprocess in the file 'TSP_utils.py'.")
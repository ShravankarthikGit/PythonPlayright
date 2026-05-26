import fileoperations as fo

# Example usage
file_path = "C:\\AADDrive\\Mystuff\\PlayWrightPython\\Automation\\automationFiles\\myfile.txt"

# Write to file
fo.write_to_file(file_path, "Welcome to Python \n File Handling")

# Append to file
fo.append_to_file(file_path, "\nThis line is appended.")

# Read file
print(fo.read_file(file_path, "all"))

# Rename file
fo.rename_file(file_path, "C:\\AADDrive\\Mystuff\\PlayWrightPython\\Automation\\automationFiles\\myfile2.txt")

# Delete file
fo.delete_file("C:\\AADDrive\\Mystuff\\PlayWrightPython\\Automation\\automationFiles\\myfile.txt")

# Directory operations
dir_path = "C:\\AADDrive\\Mystuff\\PlayWrightPython\\Automation\\automationFiles\\test"
fo.create_directory(dir_path)
print("Directory exists:", fo.check_directory_exists(dir_path))
fo.rename_directory(dir_path, "C:\\AADDrive\\Mystuff\\PlayWrightPython\\Automation\\automationFiles\\test2")
fo.remove_directory("C:\\AADDrive\\Mystuff\\PlayWrightPython\\Automation\\automationFiles\\test2", force=False)

# Current working directory
print("CWD:", fo.get_current_working_directory())

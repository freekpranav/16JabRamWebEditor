import os
import subprocess

def run_nuclei_command(template_path, output_path):
    command = ["nuclei", "-l", output_path, "-t", template_path]
    subprocess.run(command)

def run_nuclei_for_folders(nuclei_temp_directory, output_file):
    for folder_name in os.listdir(nuclei_temp_directory):
        template_path = os.path.join(nuclei_temp_directory, folder_name)
        if os.path.isdir(template_path):
            print(f"Running nuclei command for template in folder: {folder_name}")
            run_nuclei_command(template_path, output_file)
            print(f"Finished running nuclei for template in folder: {folder_name}\n")

if __name__ == "__main__":
    nuclei_temp_directory = '/workspaces/16JabRamWebEditor/Tools/nuclei_temp'
    
    # Ask the user to input the desired output file path
    output_file = input("Enter the path for the output file: ")

    run_nuclei_for_folders(nuclei_temp_directory, output_file)

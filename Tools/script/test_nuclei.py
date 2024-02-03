import os
import subprocess

def run_nuclei_command(template_path, domain_list_file, output_directory):
    with open(domain_list_file, 'r') as domain_file:
        for domain in domain_file:
            domain = domain.strip()
            if domain:
                output_file = os.path.join(output_directory, f"{domain}_{os.path.basename(template_path)}_output.txt")
                command = ["nuclei", "-l", output_file, "-t", template_path, "-target", domain]
                subprocess.run(command, check=True)
                print(f"Finished running nuclei for template {os.path.basename(template_path)} on domain: {domain}. Output saved to: {output_file}\n")

def run_nuclei_for_templates(nuclei_temp_directory, domain_list_file, output_directory):
    for template_name in os.listdir(nuclei_temp_directory):
        template_path = os.path.join(nuclei_temp_directory, template_name)
        if os.path.isfile(template_path):
            print(f"Running nuclei command for template: {template_name}")
            run_nuclei_command(template_path, domain_list_file, output_directory)
            print(f"Finished running nuclei for template: {template_name}\n")

if __name__ == "__main__":
    nuclei_temp_directory = '/workspaces/16JabRamWebEditor/Tools/nuclei_temp'

    # Ask the user to input the domain list file and output directory
    domain_list_file = input("Enter the path for the domain list file: ")
    output_directory = input("Enter the path for the output directory: ")

    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    run_nuclei_for_templates(nuclei_temp_directory, domain_list_file, output_directory)

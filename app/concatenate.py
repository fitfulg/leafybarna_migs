import os

def concatenate_files(output_file):
    """Concatenate all .py files in the 'app' directory into one file, except this script."""
    directory_path = os.path.dirname(os.path.abspath(__file__))  # Get the current script directory
    output_path = os.path.join(directory_path, output_file)

    ignore_files = ['concatenate.py, py_built.py']  # List of files to ignore (including itself)

    with open(output_path, 'w', encoding='utf-8') as outfile:
        for filename in os.listdir(directory_path):
            if filename.endswith('.py') and filename not in ignore_files:
                outfile.write(f'# ===== Start of {filename} =====\n\n')
                
                with open(os.path.join(directory_path, filename), 'r', encoding='utf-8') as infile:
                    outfile.write(infile.read())
                    outfile.write('\n\n')

        outfile.write('# ===== End of concatenated files =====\n')

if __name__ == '__main__':
    output_file = 'py_built.py'
    concatenate_files(output_file)
    print(f'All .py files from the app folder have been concatenated into {output_file}')

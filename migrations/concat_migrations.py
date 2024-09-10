import os

def concatenate_migration_files(output_file):
    """Concatenate all .py files in the migrations folder into one file."""
    current_directory = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(current_directory, output_file)

    ignore_files = ['concat_migrations.py', 'py_built_migrations.py']

    with open(output_path, 'w', encoding='utf-8') as outfile:
        for filename in os.listdir(current_directory):
            if filename.endswith('.py') and filename not in ignore_files:
                outfile.write(f'# ===== Start of {filename} =====\n\n')
                
                with open(os.path.join(current_directory, filename), 'r', encoding='utf-8') as infile:
                    outfile.write(infile.read())
                    outfile.write('\n\n')

        outfile.write('# ===== End of concatenated files =====\n')

if __name__ == '__main__':
    output_file = 'py_built_migrations.py'  # Output file name
    concatenate_migration_files(output_file)
    print(f'All .py files in the migrations folder have been concatenated into {output_file}')

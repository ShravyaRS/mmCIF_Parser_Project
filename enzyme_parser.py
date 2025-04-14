"""
enzyme_parser.py

This script uses BioPython's MMCIF2Dict to extract structural and experimental
details from mmCIF files for enzymes like TPH1 and PAH. It summarizes key
metadata (title, resolution, method, etc.) and saves the results to text files.

Enzyme files:
- TPH1 (6OB0.cif)
- PAH  (1PAH.cif)
"""

from Bio.PDB.MMCIF2Dict import MMCIF2Dict
import os

# Folder where mmCIF files are stored
data_folder = "real_data"

# List of enzyme files to parse
enzyme_files = ["6OB0.cif", "1PAH.cif"]

# Output folder to save summary text files
output_folder = "summaries"
os.makedirs(output_folder, exist_ok=True)

# Function to parse and extract key info
def parse_mmcif_file(file_path):
    data = MMCIF2Dict(file_path)

    # Extract metadata safely
    description = data.get('_entity.pdbx_description', ['N/A'])[0]
    struct_title = data.get('_struct.title', 'N/A')
    resolution = data.get('_refine.ls_d_res_high', ['N/A'])[0]
    exp_method = data.get('_exptl.method', ['N/A'])[0]
    deposition_date = data.get('_pdbx_database_status.recvd_initial_deposition_date', 'N/A')

    # Return the extracted summary
    return {
        "Description": description,
        "Title": struct_title,
        "Resolution (Å)": resolution,
        "Method": exp_method,
        "Deposition Date": deposition_date
    }

# Process each enzyme file
for file_name in enzyme_files:
    file_path = os.path.join(data_folder, file_name)
    summary = parse_mmcif_file(file_path)

    # Save the output in .txt format
    output_file = os.path.join(output_folder, file_name.replace(".cif", "_summary.txt"))
    with open(output_file, "w") as f:
        for key, value in summary.items():
            f.write(f"{key}: {value}\n")
    
    print(f"✅ Parsed and saved summary for {file_name}")

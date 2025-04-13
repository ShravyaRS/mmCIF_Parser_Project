from mmcif_parser import parse_mmcif

def main():
    file_path = "example.cif"
    structure = parse_mmcif(file_path)
    
    print(f"Structure ID: {structure.id_code}")
    print("Chain Summary:")
    summary = structure.get_chain_summary()
    
    for chain_id, residue_count in summary.items():
        print(f"  Chain {chain_id}: {residue_count} residues")

if __name__ == "__main__":
    main()

from data_structures import Atom, ProteinStructure

def parse_mmcif(file_path):
    structure = None
    loop_started = False
    atom_headers = []
    atom_data_started = False

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()

            if line.startswith("data_"):
                structure = ProteinStructure(line[5:])
            elif line.startswith("loop_"):
                loop_started = True
                atom_headers = []
                atom_data_started = False
            elif loop_started and line.startswith("_atom_site."):
                atom_headers.append(line)
            elif loop_started and line:
                if not atom_data_started:
                    atom_data_started = True
                fields = line.split()
                if len(fields) < 11:
                    continue
                atom = Atom(
                    serial=fields[1],
                    name=fields[2],
                    res_name=fields[3],
                    chain_id=fields[4],
                    res_seq=fields[5],
                    x=fields[6],
                    y=fields[7],
                    z=fields[8],
                    element=fields[10],
                )
                structure.add_atom(atom)

    return structure

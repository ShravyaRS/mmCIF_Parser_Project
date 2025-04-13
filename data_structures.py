class Atom:
    def __init__(self, serial, name, res_name, chain_id, res_seq, x, y, z, element):
        self.serial = int(serial)
        self.name = name
        self.res_name = res_name
        self.chain_id = chain_id
        self.res_seq = int(res_seq)
        self.coord = (float(x), float(y), float(z))
        self.element = element

    def __repr__(self):
        return f"{self.name} ({self.element}) at {self.coord}"

class Chain:
    def __init__(self, chain_id):
        self.chain_id = chain_id
        self.atoms = []

    def add_atom(self, atom):
        self.atoms.append(atom)

    def residue_count(self):
        return len(set((a.res_name, a.res_seq) for a in self.atoms))

class ProteinStructure:
    def __init__(self, id_code):
        self.id_code = id_code
        self.atoms = []
        self.chains = {}

    def add_atom(self, atom):
        self.atoms.append(atom)
        if atom.chain_id not in self.chains:
            self.chains[atom.chain_id] = Chain(atom.chain_id)
        self.chains[atom.chain_id].add_atom(atom)

    def get_chain_summary(self):
        return {chain_id: chain.residue_count() for chain_id, chain in self.chains.items()}

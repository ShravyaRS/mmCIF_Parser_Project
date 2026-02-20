# mmCIF Parser in Python

A lightweight mmCIF (Macromolecular Crystallographic Information File) parser built from scratch in Python, with no external dependencies. Designed as both an educational resource and a practical tool for structural bioinformatics.

See [Features.md](Features.md) for a detailed feature list.

---

## Features

- No external dependencies (no Biopython required)
- Clean, object-oriented Python code
- Extracts atomic-level information from CIF files
- Supports .cif files from RCSB PDB
- Useful for understanding how structural biology file formats work internally

---

## Theoretical Binary Data Structure Model

### Objective

Define a low-level binary data structure for storing mmCIF entries and sections efficiently in memory, simulating a compiled or serialized format.

### Data Record Structure

Each mmCIF data item (atom site, loop header, value) is represented in the following binary format:

| Segment | Description | Example |
|---------|-------------|---------|
| RECORD_TYPE (1B) | 0x01 = header, 0x02 = loop, 0x03 = data value | `0x02` |
| RECORD_ID (2B) | Unique ID for the entry (short int) | `0x00FA` |
| FIELD_NAME_LENGTH (1B) | Length of the field name | `0x07` |
| FIELD_NAME | UTF-8 string of field name | `_atom_site` |
| VALUE_LENGTH (1B) | Length of the value | `0x05` |
| VALUE | UTF-8 string of the value | `C1'` |

### Block Structure

Each mmCIF block is a binary sequence of multiple record units. A block header can optionally store metadata such as loop count, atom count, etc.

### Why This Model

- Enables serialization and memory-efficient storage
- Fast search and indexing for compiled applications
- Suitable for integration with compiled languages (C, Rust)
- Can be exported as `.bin` for direct loading into visualization tools or bioinformatics engines

---

## File Structure
```
mmCIF_Parser_Project/
├── main.py                # Run this to see the parser in action
├── mmcif_parser.py        # Core parsing logic
├── data_structures.py     # Binary data structure model
├── enzyme_parser.py       # Enzyme-specific parsing utilities
├── example.cif            # Sample mmCIF file
├── data/                  # Additional CIF files
└── README.md
```

## Usage
```bash
python main.py data/example.cif
```

## Tests
```bash
python test_mmcif_parser.py
```

---

## Extended Analyses

Additional analyses demonstrating real-world applications of mmCIF parsing:

- [Enzyme Comparison: TPH1 vs PAH](./enzyme_comparison.md)
- [TPH1 vs PAH Overview](./TPH1_vs_PAH_Overview.md)

---

## License

See [LICENSE](LICENSE) for details.

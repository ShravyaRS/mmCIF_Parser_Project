# 🧬 mmCIF Parser in Python (No Biopython)

This project demonstrates how to parse mmCIF (Macromolecular Crystallographic Information File) formats **from scratch using Python**. It serves as both an educational resource and a practical tool for molecular biology and structural bioinformatics.

---

## 🚀 Features

- ✅ No external dependencies (not even Biopython!)
- 🧠 Clean object-oriented Python code
- 📊 Extracts atomic-level information from CIF files
- 📁 Supports .cif files from RCSB PDB
- 💡 Perfect for learning how file formats work internally

---

## 🧮 Theoretical Binary Data Structure Model

To enhance the efficiency and compactness of atomic-level data parsing from mmCIF files, we propose a theoretical binary data structure to represent each atom's information. This model can be used for low-level optimization or future file compression.

### 🧱 Binary Layout (Example for One Atom Entry)

| Field            | Bits | Description                          |
|------------------|------|--------------------------------------|
| Atom ID          | 16   | Unique identifier for the atom       |
| Atom Name        | 32   | Encoded string (ASCII binary)        |
| Residue Name     | 32   | 3-letter residue code                |
| Chain ID         | 8    | Single character chain identifier    |
| Residue Number   | 16   | Residue sequence number              |
| X Coordinate     | 32   | IEEE 754 floating-point format       |
| Y Coordinate     | 32   | IEEE 754 floating-point format       |
| Z Coordinate     | 32   | IEEE 754 floating-point format       |
| Element Symbol   | 16   | 1 or 2-letter element encoded        |
| Occupancy        | 16   | Float encoded                        |
| B-factor         | 16   | Float encoded                        |

Total = **256 bits (32 bytes)** per atom

### 🧬 Purpose

- Enables future binary-based CIF formats or compression
- Demonstrates theoretical understanding of memory-efficient storage
- Adds novelty to the project from both a CS and bioinformatics angle


## 📂 File Structure

```bash
mmCIF_Parser_Project/
├── main.py              # Run this to see the parser in action
├── mmcif_parser.py      # Core parsing logic
├── example.cif          # Sample mmCIF file
└── README.md            # This file
## 📌 Usage

To run the parser on the provided example file:

```bash
python main.py data/example.cif

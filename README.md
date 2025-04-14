# 🧬 mmCIF Parser in Python (No Biopython)

This project demonstrates how to parse mmCIF (Macromolecular Crystallographic Information File) formats **from scratch using Python**. It serves as both an educational resource and a practical tool for molecular biology and structural bioinformatics.

---
👉 Check out the [Features](Features.md) of this project.

## 🚀 Features

- ✅ No external dependencies (not even Biopython!)
- 🧠 Clean object-oriented Python code
- 📊 Extracts atomic-level information from CIF files
- 📁 Supports .cif files from RCSB PDB
- 💡 Perfect for learning how file formats work internally

---

# 📘 Theoretical Binary Data Structure Model for mmCIF Parser

## 🧠 Objective
To define a theoretical low-level binary data structure for storing mmCIF entries and sections efficiently in memory, mimicking a compiled or serialized format.

---

## 1️⃣ Data Record Structure

Each mmCIF data item (e.g. atom site, loop header, values) is internally represented in the following binary format:


| Segment            | Description                                   | Example                    |
|--------------------|-----------------------------------------------|----------------------------|
| RECORD_TYPE (1B)   | 0x01 = header, 0x02 = loop, 0x03 = data value | `0x02`                     |
| RECORD_ID (2B)     | Unique ID for the entry (short int)           | `0x00FA`                   |
| FIELD_NAME_LENGTH  | Length of the field name (1B)                 | `0x07`                     |
| FIELD_NAME         | UTF-8 string of field name                    | `_atom_site`               |
| VALUE_LENGTH       | Length of the value (1B)                      | `0x05`                     |
| VALUE              | UTF-8 string of the value                     | `C1'`                      |

---

## 2️⃣ Example: `_atom_site.label_atom_id  C1'`

In binary (hex representation):


---

## 3️⃣ Block Structure

Each mmCIF block is a binary sequence of multiple `RECORD` units. Parsing follows this logic:


Optional: A BLOCK_HEADER could store metadata like number of loops, atom count, etc.

---

## 4️⃣ Why Use This Model?

- 🧠 Enables serialization and memory-efficient storage
- ⚡️ Fast search and indexing in future compiled applications
- 🔬 Suitable for integration with compiled languages (C, Rust)
- 💾 Can be exported as `.bin` for direct loading into visualization tools or bioinformatics engines

---

## 📦 Future Possibility

We may build a compiler that translates standard mmCIF into this binary form for fast parsing in high-performance environments like protein modeling pipelines.

---



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
### Theoretical Binary Flowchart

![Theoretical Binary Flowchart](A_flowchart_diagram_depicts_a_theoretical_binary_d.png)

## 📂 Theoretical Model

📄 [Theoretical Binary Representation](./theoretical_model.md)  
A structured binary representation of mmCIF elements in memory.



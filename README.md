# 🧬 mmCIF Parser Project

This project implements a clean and modular mmCIF file parser in Python, built from scratch using custom data structures.  
It reads protein structure files in `.cif` format and organizes the atomic data into meaningful Python classes.

---

## 📁 Folder Structure


---

## ⚙️ How It Works

- **`data_structures.py`**: Defines core objects: `Atom`, `Chain`, `ProteinStructure`
- **`mmcif_parser.py`**: Parses mmCIF file and fills the data structure with atoms
- **`main.py`**: Loads the `.cif` file, uses parser, and prints residues per chain

---

## ▶️ How to Run

1. Open your terminal or command prompt  
2. Navigate to your project folder:

   ```bash
   cd path/to/mmCIF_Parser_Project

python main.py

## 💡 Why This Project?

This project shows how bioinformatics and computer science intersect.  
Instead of using Biopython, we build everything from scratch — ideal for learning and academic use.

- 📚 Great for understanding PDB/mmCIF format  
- 🧠 Demonstrates class design & object-oriented Python  
- 🧪 Useful for molecular structure analysis  

---

## 📢 Author

Shravya R S  
Bioinformatics Enthusiast | Python Developer  
*(This project is a part of a class assignment and intended for potential publication.)*

## 🔬 Academic Note
This parser was written entirely from scratch without using external libraries like Biopython. 
It was developed for educational purposes and academic demonstration — particularly to highlight core principles of object-oriented design in Python and low-level understanding of the mmCIF format.


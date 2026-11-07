# Huffman Coding — Lossless Text Compression

A Python implementation of the **Huffman coding algorithm**, a classic lossless compression technique that assigns shorter binary codes to frequent characters and longer codes to rare ones.

The project reads a text file, builds the Huffman tree step by step, generates the coding table, compresses the text into a bit string, and reports the compression rate. The tree can also be displayed graphically. The implementation works with any set of characters, not only a small alphabet.

## Features

- Character frequency analysis
- Step-by-step Huffman tree construction (sorting, merging the two lowest-weight nodes, repeating until a single root remains)
- Coding table generation (`1` for a left edge, `0` for a right edge)
- Compression of the text into a binary string
- Decompression using the coding table, with an automatic check that the original text is recovered
- Compression rate computation (compared with 8-bit ASCII encoding)
- Graphical visualization of the Huffman tree with `matplotlib`
- Clean separation between the compression logic and the display code

## Project Structure

```
.
├── huffman.py          # Compression logic (Node, tree building, codes, compress, decompress, rate)
├── affichage.py        # Display: console output and graphical tree
├── main.py             # Entry point: connects the logic and the display
└── texte.txt           # Input text file
```

## How It Works

1. **Frequency count** — each character of the text is counted.
2. **Tree construction** — every character becomes a leaf `Node(name, weight)`. At each iteration, the nodes are sorted by weight, the two lightest are merged into a parent node whose weight is the sum of its children, and the parent replaces them in the list. The process stops when only one node (the root) is left.
3. **Code generation** — the tree is traversed recursively from the root. Going left appends `1` to the code, going right appends `0`. The code of a character is the path leading to its leaf.
4. **Compression** — each character is replaced by its code and all codes are concatenated.
5. **Decompression** — the coding table is inverted (`code -> character`) and the bits are read one by one until the accumulated bits match a code. Huffman codes are *prefix-free* (no code is the beginning of another), so the first match is always the correct one.
6. **Compression rate** — `(1 - compressed_size / original_size) * 100`, where the original size is `8 bits × number of characters`.

### Example

For the text `aaabbc`:

| Character | Frequency | Code |
|-----------|-----------|------|
| a         | 3         | `1`  |
| c         | 1         | `01` |
| b         | 2         | `00` |

- Compressed string: `111000001` (9 bits instead of 48)
- Compression rate: **81.25 %**

## Requirements

- Python 3.8 or higher
- `matplotlib` (only needed for the tree visualization)

```bash
pip install matplotlib
```

## Usage

Place your input in a file named `texte.txt` (or generate a sample), then run:

```bash

# Run the compression
python main.py

# Or use your own file
python main.py my_file.txt
```

The program prints the character frequencies, each step of the tree construction, the coding table, the compressed string, and the compression rate. It then verifies the decompression and opens a window displaying the tree.

## Notes

- Line breaks are ignored when reading the input file.
- If the text contains a single distinct character, it is encoded with the code `0` so that the compressed output is never empty.
- Larger and more uneven character distributions generally lead to higher compression rates.
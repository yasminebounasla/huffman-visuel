import sys

from huffman import (count_frequencies, build_tree, generate_codes,
                     compress, decompress, compression_rate)
from display import (show_frequencies, show_steps, show_codes,
                       show_compressed, show_rate, show_check, show_tree)


def main():
    # the file name can be given in the terminal, otherwise we use texte.txt
    filename = sys.argv[1] if len(sys.argv) > 1 else "texte.txt"

    try:
        with open(filename, encoding="utf-8") as f:
            text = f.read().replace("\n", "")   # we ignore the line breaks
    except FileNotFoundError:
        print(f"Fichier '{filename}' introuvable.")
        return

    # 1. count the occurrences of each character
    frequencies = count_frequencies(text)
    show_frequencies(frequencies)

    # 2. build the tree (steps are kept for the display)
    root, steps = build_tree(frequencies)
    show_steps(steps)

    # 3. coding table
    codes = generate_codes(root)
    show_codes(codes)

    # 4. compressed string
    bits = compress(text, codes)
    show_compressed(bits)

    # 5. compression rate
    original, compressed, rate = compression_rate(text, bits)
    show_rate(original, compressed, rate)

    # 6. check that the decompression gives back the original text
    show_check(decompress(bits, codes) == text)

    # 7. graph of the tree (matplotlib window)
    show_tree(root)


if __name__ == "__main__":
    main()
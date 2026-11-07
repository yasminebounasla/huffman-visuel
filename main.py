import sys

from huffman import (count_frequencies, build_tree, generate_codes,compress, decompress, compression_rate)
from display import (show_frequencies, show_steps, show_codes,show_compressed, show_rate, show_check)


def main():
    filename = sys.argv[1] if len(sys.argv) > 1 else "texte.txt"

    try:
        with open(filename, encoding="utf-8") as f:
            text = f.read().replace("\n", "")   # we remove line breaks for simplicity
    except FileNotFoundError:
        print(f"Fichier '{filename}' introuvable. Lance d'abord : python generer_texte.py")
        return

    frequencies = count_frequencies(text)
    show_frequencies(frequencies)

    root, steps = build_tree(frequencies)
    show_steps(steps)

    codes = generate_codes(root)
    show_codes(codes)

    bits = compress(text, codes)
    show_compressed(bits)

    original, compressed, rate = compression_rate(text, bits)
    show_rate(original, compressed, rate)

    show_check(decompress(bits, codes) == text)


if __name__ == "__main__":
    main()
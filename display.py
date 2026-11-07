# All the display of the project (no compression logic here)


def show_frequencies(frequencies):
    print("=== Nombre d'occurrences ===")
    for c, f in sorted(frequencies.items()):
        print(f"  '{c}' : {f}")


def show_steps(steps):
    print("\n=== Construction de l'arbre ===")
    for i, s in enumerate(steps, 1):
        print(f"\nÉtape {i}")
        print("  Liste triée :", s["list"])
        print(f"  Deux plus faibles : '{s['left'].name}' ({s['left'].weight}) "
              f"et '{s['right'].name}' ({s['right'].weight})")
        print(f"  Nouveau noeud : '{s['parent'].name}' ({s['parent'].weight})")


def show_codes(codes):
    print("\n=== Table de codage (1 = gauche, 0 = droite) ===")
    for c, code in sorted(codes.items()):
        print(f"  '{c}' -> {code}")


def show_compressed(bits, max_len=200):
    print("\n=== Chaîne compressée ===")
    if len(bits) > max_len:                 # a long string is cut to keep the console readable
        print(bits[:max_len] + f"... ({len(bits)} bits au total)")
    else:
        print(bits)


def show_rate(original, compressed, rate):
    print("\n=== Taux de compression ===")
    print(f"  Taille originale  : {original} bits")
    print(f"  Taille compressée : {compressed} bits")
    print(f"  Taux de compression : {rate:.2f} %")


def show_check(ok):
    print("\nVérification (décompression == texte original) :", "OK" if ok else "ERREUR")


# ---------- Graphical display of the tree ----------

def compute_positions(node, depth, positions, next_x):
    # give each node a position (x, y) for the drawing
    if node.is_leaf():
        positions[node] = (next_x[0], -depth)   # leaves are placed from left to right
        next_x[0] += 1
    else:
        compute_positions(node.left, depth + 1, positions, next_x)
        compute_positions(node.right, depth + 1, positions, next_x)
        # the parent is placed in the middle of its two children
        x = (positions[node.left][0] + positions[node.right][0]) / 2
        positions[node] = (x, -depth)


def draw_node(node, positions, ax):
    # draw the node, then its two children (with 1 on the left and 0 on the right)
    x, y = positions[node]

    if not node.is_leaf():
        for child, bit in ((node.left, "1"), (node.right, "0")):
            cx, cy = positions[child]
            ax.plot([x, cx], [y, cy], color="black", zorder=1)      # the edge
            ax.text((x + cx) / 2, (y + cy) / 2, bit, color="red",   # the bit written on the edge
                    fontsize=12, fontweight="bold", ha="center", va="center",
                    bbox=dict(facecolor="white", edgecolor="none", pad=1), zorder=2)
            draw_node(child, positions, ax)

    # leaf : character + weight / internal node : weight only
    label = f"{node.name}\n{node.weight}" if node.is_leaf() else str(node.weight)
    color = "lightgreen" if node.is_leaf() else "lightblue"
    ax.text(x, y, label, ha="center", va="center", fontsize=11, zorder=3,
            bbox=dict(boxstyle="circle", facecolor=color, edgecolor="black"))


def show_tree(root):
    import matplotlib.pyplot as plt

    positions = {}
    compute_positions(root, 0, positions, [0])

    fig, ax = plt.subplots(figsize=(10, 6))
    draw_node(root, positions, ax)
    ax.set_title("Arbre de Huffman (1 = gauche, 0 = droite)")
    ax.axis("off")
    ax.margins(0.1)
    plt.show()
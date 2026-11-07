

def show_frequencies(frequencies):
    print("=== Number of occurrences ===")
    for c, f in sorted(frequencies.items()):
        print(f"  '{c}' : {f}")


def show_steps(steps):
    print("\n=== Construction of the tree ===")
    for i, s in enumerate(steps, 1):
        print(f"\nStep {i}")
        print("  Sorted list :", s["list"])
        print(f"  Two weakest : '{s['left'].name}' ({s['left'].weight}) "
              f"et '{s['right'].name}' ({s['right'].weight})")
        print(f"  New node : '{s['parent'].name}' ({s['parent'].weight})")


def show_codes(codes):
    print("\n=== Coding Table (1 = left, 0 = right) ===")
    for c, code in sorted(codes.items()):
        print(f"  '{c}' -> {code}")


def show_compressed(bits, max_len=200):
    print("\n=== Compressed String ===")
    if len(bits) > max_len:
        print(bits[:max_len] + f"... ({len(bits)} bits au total)")
    else:
        print(bits)


def show_rate(original, compressed, rate):
    print("\n=== Compression Rate ===")
    print(f"  Original size  : {original} bits")
    print(f"  Compressed size : {compressed} bits")
    print(f"  Compression rate : {rate:.2f} %")


def show_check(ok):
    print("\nVerification (decompression == original text) :", "OK" if ok else "ERROR")
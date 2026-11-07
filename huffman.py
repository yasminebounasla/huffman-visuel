from collections import Counter


class Node:
    def __init__(self, name, weight, left=None, right=None):
        self.name = name        # the character
        self.weight = weight    # the frequency of the character
        self.left = left
        self.right = right

    def is_leaf(self):          # True if the node is a character 
        return self.left is None and self.right is None


def count_frequencies(text):
    return dict(Counter(text))  # return : {character: number of occurrences}


def get_weight(n):
    return n.weight


def build_tree(frequencies):
    if not frequencies:
        raise ValueError("Empty text: nothing to compress.")

    nodes = [Node(c, f) for c, f in frequencies.items()]
    steps = []  # we keep each step for visualization

    while len(nodes) > 1:
        nodes.sort(key=get_weight)                          # sort
        sorted_list = [(n.name, n.weight) for n in nodes]   # save the sorted list for visualization

        left, right = nodes[0], nodes[1]                    # the two weakest
        parent = Node(left.name + right.name, left.weight + right.weight, left, right)

        nodes = nodes[2:] + [parent]                        # the parent replaces its two children
        steps.append({"list": sorted_list, "left": left, "right": right, "parent": parent})

    return nodes[0], steps



def generate_codes(node, code=""):
    if node.is_leaf():
        return {node.name: code or "0"}     # "0" if the text has only one character

    codes = {}
    codes.update(generate_codes(node.left, code + "1"))
    codes.update(generate_codes(node.right, code + "0"))

    return codes    # return : {character1: code1, character2: code2, ...}


def compress(text, codes):
    return "".join(codes[c] for c in text)  # replace each character by its code and concatenate all codes into a single string


def decompress(bits, codes):
    # Inverse the dictionary : {"a": "1"} becomes {"1": "a"}
    reverse = {}
    for char in codes:
        code = codes[char]
        reverse[code] = char

    # read the bits one by one and decode them using the reverse dictionary
    result = ""
    current = ""
    for bit in bits:
        current = current + bit   # read the next bit
        if current in reverse:  
            result = result + reverse[current]   #if current substring is a code , we add the corresponding character to the result
            current = ""

    return result


def compression_rate(text, bits):
    original = len(text) * 8        # original size in bits (1 character = 8 bits)
    compressed = len(bits)
    return original, compressed, (1 - compressed / original) * 100
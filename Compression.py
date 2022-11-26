from Huffman_Nodes import HuffmanNode


def preorder_coding(obj):
    if obj is None:
        return
    if obj.left is not None:
        lft = obj.left
        code = obj.code + '0'
        lft.setcode(code)

    if obj.right is not None:
        rit = obj.right
        code = obj.code + '1'
        rit.setcode(code)

    preorder_coding(obj.left)
    preorder_coding(obj.right)


codes_dict = dict()
codes = []
compressed_string = ''


def printing(obj):
    if obj is None:
        return
    if obj.right is None and obj.left is None:
        codes_dict[obj.symbol] = obj.code
        codes.append(f"{obj.symbol}={obj.code}")

    printing(obj.left)
    printing(obj.right)


with open("Input.txt", "r") as file:
    huffman_input = file.read()
    nodes = []
    symbols = set()

    for i in huffman_input:
        symbols.add(i)

    for i in symbols:
        probability = huffman_input.count(i) / len(huffman_input)
        node = HuffmanNode(probability, i, None, None, '')
        nodes.append(node)

    nodes.sort(key=lambda x: x.value)
    while len(nodes) > 1:
        node = nodes[0] + nodes[1]
        nodes.pop(0)
        nodes.pop(0)
        nodes.append(node)
        nodes.sort(key=lambda x: x.value)
    preorder_coding(nodes[0])
    printing(nodes[0])
    for i in huffman_input:
        compressed_string += codes_dict[i]

print(codes)
print(compressed_string)

with open("Output.txt", "w") as file:
    for i in codes:
        file.write(i)
        file.write('\n')
    file.write(compressed_string)

with open("Output.txt", "r") as test:
    out = test.read().splitlines()
    print(type(out))
    print(out)

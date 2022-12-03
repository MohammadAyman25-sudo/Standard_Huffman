from Huffman_Nodes import HuffmanNode
import os


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


class HuffmanCompression:
    def __init__(self, fileName="Input.txt", string=''):
        self.filename = fileName
        self.text = string
        self.compressed = compressed_string
        self.code = codes
        self.code_dict = codes_dict

    def compress(self):
        if self.filename == 'Input.txt':
            with open(self.filename, 'w') as file:
                file.write(self.text)
        elif self.filename != 'Input.txt':
            path = str(os.getcwd())
            path = f'{path}\\{self.filename}'
            if not os.path.isfile(path):
                return None
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
                self.compressed += codes_dict[i]

        with open("Huffman/Short Code.txt", "w") as file:
            for i in self.code:
                file.write(i)
                file.write('\n')

        with open("Huffman/Compressed Stream.txt", "w") as file:
            file.write(self.compressed)

        return self.compressed

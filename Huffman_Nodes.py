class HuffmanNode:
    def __init__(self, val=0.0, symbl='', left=None, right=None, code=''):
        self.value = val
        self.symbol = symbl
        self.left = left
        self.right = right
        self.code = code

    def __repr__(self):
        return f"{self.symbol}: {self.code}"

    def __add__(self, obj):
        x = obj.value + self.value
        symbl = f'{self.symbol}+{obj.symbol}'
        tem = HuffmanNode(x, symbl, self, obj, '')
        return tem

    def setcode(self, code):
        self.code = code

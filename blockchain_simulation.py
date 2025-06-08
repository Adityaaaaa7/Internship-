import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.ctime()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        content = str(self.index) + self.timestamp + str(self.data) + self.previous_hash
        return hashlib.sha256(content.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_chain()

    def create_chain(self):
        origin = Block(0, "Origin Block", "0")
        self.chain.append(origin)
        block1 = Block(1, "Block 1 Data", origin.hash)
        self.chain.append(block1)
        block2 = Block(2, "Block 2 Data", block1.hash)
        self.chain.append(block2)

    def display_chain(self):
        for block in self.chain:
            print(f"\nBlock {block.index}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Data: {block.data}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Hash: {block.hash}")
            
# Main
bc = Blockchain()
# Original Blockchain
bc.display_chain()

# Change Block 1's data
bc.chain[1].data = "Malicious Data"
bc.chain[1].hash = bc.chain[1].calculate_hash()

# After Changes in Block 1
bc.display_chain()

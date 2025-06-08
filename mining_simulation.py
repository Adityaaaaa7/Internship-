import hashlib
import time

class Block:
    def __init__(self, index, data, hash):
        self.index = index
        self.data = data
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        content = str(self.index) + self.data + str(self.nonce)
        return hashlib.sha256(content.encode()).hexdigest()

    def mine_block(self, difficulty):
        target = "0" * difficulty  # 0000
        start = time.time()

        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

        end = time.time()
        print(f"Block mined with hash: {self.hash}")
        print(f"Nonce attempts: {self.nonce}")
        print(f"Time taken: {round(end - start, 4)} seconds")

# Main
difficulty = 4
block1 = Block(1, "Block 1 Data", "0")
block1.mine_block(difficulty)

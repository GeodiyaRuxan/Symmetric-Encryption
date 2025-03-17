import hashlib
import time

# Block class
class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash_value):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash_value = hash_value

# Blockchain class
class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    # Create the first block (genesis block)
    def create_genesis_block(self):
        genesis_block = Block(0, "0", int(time.time()), "Genesis Block", self.calculate_hash(0, "0", int(time.time()), "Genesis Block"))
        self.chain.append(genesis_block)

    # Add a block to the chain
    def add_block(self, data):
        previous_block = self.chain[-1]
        new_index = previous_block.index + 1
        new_timestamp = int(time.time())
        new_hash_value = self.calculate_hash(new_index, previous_block.hash_value, new_timestamp, data)
        
        new_block = Block(new_index, previous_block.hash_value, new_timestamp, data, new_hash_value)
        self.chain.append(new_block)

    # Calculate hash of a block
    def calculate_hash(self, index, previous_hash, timestamp, data):
        value = str(index) + str(previous_hash) + str(timestamp) + str(data)
        return hashlib.sha256(value.encode('utf-8')).hexdigest()

    # Display the blockchain
    def display_chain(self):
        for block in self.chain:
            print(f"Block #{block.index}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Data: {block.data}")
            print(f"Hash: {block.hash_value}")
            print(f"Previous Hash: {block.previous_hash}\n")

# Example Usage
if __name__ == "__main__":
    blockchain = Blockchain()
    
    # Add blocks to the blockchain
    blockchain.add_block("First transaction data")
    blockchain.add_block("Second transaction data")
    
    # Display the blockchain
    blockchain.display_chain()

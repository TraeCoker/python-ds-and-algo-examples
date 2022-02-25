'''
PyCoin (PC)

t1: Anna sends Bob 2 PC
t2: Bob sends Daniel 4.3 PC
t3: Mark sends Charlie 3.2 PC

SHA 256 

B1 ("Start", t1, t2, t3) -> 76fd89, B2 ("76fd89", t4, t5, t6) -> 8923ff, B3 ("8923ff", t7, t8, t9)

'''
import hashlib

class PyCoinBlock:
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = " - ".join(transaction_list) + " - " + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


t1 = "Anna sends 2 PC to Mike"
t2 = "Bob sends 4.1 PC to Mike"
t3 = "Mike sends 3.2 PC to Anna"
t4 = "Daniel sends 0.3 PC to Bob"
t5 = "Todd sends 1 PC to Steve"
t6 = "Steve sends 5.4 PC to Mike"

initial_block = PyCoinBlock("Genesis Block", [t1, t2])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block = PyCoinBlock(initial_block.block_hash, [t3, t4])

print(second_block.block_data)
print(second_block.block_hash)

third_block = PyCoinBlock(second_block.block_hash, [t5, t6])

print(third_block.block_data)
print(third_block.block_hash)
import hashlib as hasher
import datetime as date

#블록 정의
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index #번호
        self.timestamp = timestamp #시간
        self.data = data #날짜
        self.previous_hash = previous_hash #전에 있던 블록
        self.hash = self.hash_block()
        
    def hash_block(self):
        sha = hasher.sha256()
        sha.update(str(self.index).encode('utf-8') + str(self.timestamp).encode('utf-8') + str(self.data).encode(
            'utf-8') + str(self.previous_hash).encode('utf-8'))

        return sha.hexdigest()


#맨 처음 블록 생성
def create_genesis_block():
    return Block(0, date.datetime.now(), "Genesis Block", "0")

#다음 블록 생성
def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Hey! I'm block " + str(this_index)
    this_hash = last_block.hash
    
    return Block(this_index, this_timestamp, this_data, this_hash)


#맨 처음 블록 생성 후 체인으로 블록 묶기
blockchain = [create_genesis_block()]
previous_block = blockchain[0] #맨 처음 블록은 0번

#20개의 블록 생성
num_of_blocks_to_add = 20


#체인으로 묶기
for i in range(0, num_of_blocks_to_add):
    block_to_add = next_block(previous_block) #next_block사용하여 블록 생성
    blockchain.append(block_to_add) #맨 처음 붙인 블록에 위에 만든 블록 붙임(리스트임)
    previous_block = block_to_add #전의 블록은 위에 생성된 블록으로 바꿈

    print("Block #{} has been added to the blockchain!".format(block_to_add.index))
    print("Hash: {}\n".format(block_to_add.hash))


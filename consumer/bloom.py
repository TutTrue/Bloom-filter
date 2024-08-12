import hashlib


class BloomFilter:
    # 335477044 for 10 million items 0.0000001 (1 in 9994083) false positive rate
    def __init__(self, size=1000, bit_array=0):
        self.bit_array = bit_array
        self.size = size


    def _hashes(self, item):
        hashes = []
        item_encoded = item.encode()

        for i in range(23):
            hash_func = hashlib.md5 if i % 2 == 0 else hashlib.sha1
            hasher = hash_func()
            hasher.update(item_encoded)
            hasher.update(str(i).encode())
            hash_value = int(hasher.hexdigest(), 16)
            hashes.append(hash_value)

        return hashes


    def add(self, item):
        for hash in self._hashes(item):
            index = hash % self.size
            self.bit_array |= 1 << index


    def contains(self, item):
        for hash in self._hashes(item):
            index = hash % self.size
            if self.bit_array & (1 << index) == 0:
                return False
        return True


    def __contains__(self, item):
        return self.contains(item)


    def __len__(self):
        return bin(self.bit_array).count('1')

    
    def __repr__(self):
        return f'BloomFilter({self.hash_funcs}, {self.size}, {self.bit_array})'


    def __str__(self):
        return bin(self.bit_array)

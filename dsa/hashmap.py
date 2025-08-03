class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.map = [[] for _ in range(size)]  # list of buckets (chaining)

    def _hash(self, key):
        return hash(key) % self.size  # built-in hash, mod size to fit in map

    def put(self, key, value):
        index = self._hash(key)
        bucket = self.map[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # update value
                return
        bucket.append((key, value))  # insert new key-value pair

    def get(self, key):
        index = self._hash(key)
        bucket = self.map[index]

        for k, v in bucket:
            if k == key:
                return v
        return None  # key not found

    def remove(self, key):
        index = self._hash(key)
        bucket = self.map[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False

    def display(self):
        for i, bucket in enumerate(self.map):
            if bucket:
                print(f"Bucket {i}: {bucket}")

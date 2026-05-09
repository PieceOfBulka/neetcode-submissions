class TimeMap:

    def __init__(self):
        self.dictionary = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dictionary:
            self.dictionary[key] = []
        self.dictionary[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dictionary:
            return ''
        l,r=0,len(self.dictionary[key])-1
        while l<=r:
            mid=l+(r-l)//2
            if self.dictionary[key][mid][0] == timestamp:
                return self.dictionary[key][mid][1]
            elif self.dictionary[key][mid][0] > timestamp:
                r = mid-1
            else:
                l = mid+1
        return self.dictionary[key][r][1] if self.dictionary[key][r][0]<=timestamp else ''
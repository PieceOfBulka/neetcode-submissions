class Solution:

    def encode(self, strs: List[str]) -> str:
        return 'ё'.join(['']+strs)

    def decode(self, s: str) -> List[str]:
        return s.split('ё')[1:]

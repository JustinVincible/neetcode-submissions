class Solution:

    def encode(self, strs: List[str]) -> str:
        lens = [len(x) for x in strs]
        header = str(len(lens)) + ";" + ";".join(map(str, lens)) + ";#"
        payload = "".join(strs)
        message = header+payload
        return message

    def decode(self, s: str) -> List[str]:
        header, payload = s.split("#", maxsplit=1)
        header = header.split(";")
        res = []
        header.insert(0, 0)
        pos = 0
        for i in range(int(header[1])):
            res.append(payload[pos:pos+int(header[i+2])])
            pos += int(header[i+2])
        return res
# Problem Description
# In this problem, we need to develop a method to encode and decode lists of strings so that they can be sent correctly over a network. The main challenge is to create a format for the encoded string that allows us to uniquely decipher each string in the list upon decoding without any ambiguity or loss of information. The encoded string must carry enough information to restore the original list of strings exactly.

# we assume to create a size of 4 len prefix string based on the len of the string 

class Codec:
    def encode(self, strs):
        encoded_string = []

        for string in strs:
            len_prefix = '{:4}'.format(len(string))
            print(len_prefix)
            encoded_string.append(len_prefix+string)

        return ''.join(encoded_string)
    def decode(self, strs):
        output = []
        i = 0 
        while i < len(strs):
            len_str = int(strs[i:i+4])
            i += 4 
            output.append(strs[i:i+len_str])
            i += len_str
        return output


c = Codec()

encoded_string = c.encode(["hello", "world", "leetcode", "example"])

print(encoded_string)

print(c.decode(encoded_string))
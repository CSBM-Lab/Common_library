# DNA Transcription to RNA converter
def Complement_R(s):
        s = s.replace('A', 'U')
        s = s.replace('T', 'A')
        s = s.replace('G', 'c')
        s = s.replace('C', 'G')
        s = s.replace('c', 'C')
        return s

# test Sequence
Seq = 'ACTGGGCTABDJEETTGGCACGT'
NewSeq = Complement_R(Seq)
print(NewSeq)
print('UGACCCGAUBDJEEAACCGUGCA') # the correct output comparison
# DNA Complement strand converter
def Complement_D(s):
        s = s.replace('A', 't')
        s = s.replace('T', 'A')
        s = s.replace('G', 'c')
        s = s.replace('C', 'G')
        s = s.replace('t', 'T')
        s = s.replace('c', 'C')
        return s

# test Sequence
Seq = 'ACTGGGCTABDJEETTGGCACGT'
NewSeq = Complement_D(Seq)
print(NewSeq)
print('TGACCCGATBDJEEAACCGTGCA') # the correct output comparison
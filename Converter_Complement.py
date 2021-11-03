# DNA Complement strand converter
def complement(s):
        s = s.replace('A', 't')
        s = s.replace('T', 'A')
        s = s.replace('G', 'c')
        s = s.replace('C', 'G')
        s = s.replace('t', 'T')
        s = s.replace('c', 'C')
        return s
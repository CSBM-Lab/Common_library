# Convert codon to amino acid, from a list to a new list
def Convert_codon_aa_l(s):
    def Codon_aa_l(c):
        if   c[i] == 'GTT' or c[i] == 'GTC' or c[i] == 'GTA' or c[i] == 'GTG' or c[i] == 'GUU' or (
                          c[i] == 'GUC' or c[i] == 'GUA' or c[i] == 'GUG'):
            c[i] = 'V' # Val
        elif c[i] == 'GCT' or c[i] == 'GCC' or c[i] == 'GCA' or c[i] == 'GCG' or c[i] == 'GCU':
            c[i] = 'A' # Ala
        elif c[i] == 'GAT' or c[i] == 'GAC' or c[i] == 'GAU':
            c[i] = 'D' # Asp
        elif c[i] == 'GAA' or c[i] == 'GAG':
            c[i] = 'E' # Glu
        elif c[i] == 'GGT' or c[i] == 'GGC' or c[i] == 'GGA' or c[i] == 'GGG' or c[i] == 'GGU':
            c[i] = 'G' # Gly
        elif c[i] == 'TTT' or c[i] == 'TTC' or c[i] == 'UUU' or c[i] == 'UUC':
            c[i] = 'F' # Phe
        elif c[i] == 'TTA' or c[i] == 'TTG' or c[i] == 'UUA' or c[i] == 'UUG' or c[i] == 'CTT' or (
                           c[i] == 'CTC' or c[i] == 'CTA' or c[i] == 'CTG' or c[i] == 'CUU' or 
                           c[i] == 'CUC' or c[i] == 'CUA' or c[i] == 'CUG'):
            c[i] = 'L' # Leu
        elif c[i] == 'TCT' or c[i] == 'TCC' or c[i] == 'TCA' or c[i] == 'TCG' or c[i] == 'UCU' or (
                           c[i] == 'UCC' or c[i] == 'UCA' or c[i] == 'UCG' or c[i] == 'AGT' or 
                           c[i] == 'AGC' or c[i] == 'AGU'):
            c[i] = 'S' # Ser
        elif c[i] == 'TAT' or c[i] == 'TAC' or c[i] == 'UAU' or c[i] == 'UAC':
            c[i] = 'Y' # Tyr
        elif c[i] == 'TGT' or c[i] == 'TGC' or c[i] == 'UGU' or c[i] == 'UGC':
            c[i] = 'C' # Cys
        elif c[i] == 'TGG' or c[i] == 'UGG':
            c[i] = 'W' # Trp
        elif c[i] == 'CCT' or c[i] == 'CCC' or c[i] == 'CCA' or c[i] == 'CCG' or c[i] == 'CCU':
            c[i] = 'P' # Pro
        elif c[i] == 'CAT' or c[i] == 'CAC' or c[i] == 'CAU':
            c[i] = 'H' # His
        elif c[i] == 'CAA' or c[i] == 'CAG':
            c[i] = 'Q' # Gln
        elif c[i] == 'CGT' or c[i] == 'CGC' or c[i] == 'CGA' or c[i] == 'CGG' or (
                           c[i] == 'CGU' or c[i] == 'AGA' or c[i] == 'AGG'):
            c[i] = 'R' # Arg
        elif c[i] == 'ATT' or c[i] == 'ATC' or c[i] == 'ATA' or (
                           c[i] == 'AUU' or c[i] == 'AUC' or c[i] == 'AUA'):
            c[i] = 'I' # Ile
        elif c[i] == 'ATG' or c[i] == 'AUG':
            c[i] = 'M' # Met (Starting codon)
        elif c[i] == 'ACT' or c[i] == 'ACC' or c[i] == 'ACA' or c[i] == 'ACG' or c[i] == 'ACU':
            c[i] = 'T' # Thr
        elif c[i] == 'AAT' or c[i] == 'AAC' or c[i] == 'AAU':
            c[i] = 'N' # Asn
        elif c[i] == 'AAA' or c[i] == 'AAG':
            c[i] = 'K' # Lys
        elif c[i] == 'TAA' or c[i] == 'TAG' or c[i] == 'UAA' or (
                           c[i] == 'UAG' or c[i] == 'TGA' or c[i] == 'UGA'):
            c[i] = '*' # STOP
    for i in range(len(s)):
        Codon_aa_l(s)
    return s

# test all codon to aa
codon = ['UUU', 'UUC', 'UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG', 'AUU', 'AUC', 'AUA', 
    'AUG', 'GUU', 'GUC', 'GUA', 'GUG', 'UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC', 'CCU', 
    'CCC', 'CCA', 'CCG', 'ACU', 'ACC', 'ACA', 'ACG', 'GCU', 'GCC', 'GCA', 'GCG', 'UAU', 
    'UAC', 'UAA', 'UAG', 'UGA', 'CAU', 'CAC', 'CAA', 'CAG', 'AAU', 'AAC', 'AAA', 'AAG', 
    'GAU', 'GAC', 'GAA', 'GAG', 'UGU', 'UGC', 'UGG', 'CGU', 'CGC', 'CGA', 'CGG', 'AGA', 
    'AGG', 'GGU', 'GGC', 'GGA', 'GGG']
codon_aa = Convert_codon_aa_l(codon)
print(codon_aa)
# correct output count
print('F2-L6-I3-M1-V4-S6-P4-T4-A4-Y2-(*3)-H2-Q2-N2-K2-D2-E2-C2-W1-R6-G4')


# Convert codon to amino acid from string
def Codon_aa(c):
    if   c == 'GTT' or c == 'GTC' or c == 'GTA' or c == 'GTG' or c == 'GUU' or (
                   c == 'GUC' or c == 'GUA' or c == 'GUG'):
        c = 'V' # Val
    elif c == 'GCT' or c == 'GCC' or c == 'GCA' or c == 'GCG' or c == 'GCU':
        c = 'A' # Ala
    elif c == 'GAT' or c == 'GAC' or c == 'GAU':
        c = 'D' # Asp
    elif c == 'GAA' or c == 'GAG':
        c = 'E' # Glu
    elif c == 'GGT' or c == 'GGC' or c == 'GGA' or c == 'GGG' or c == 'GGU':
        c = 'G' # Gly
    elif c == 'TTT' or c == 'TTC' or c == 'UUU' or c == 'UUC':
        c = 'F' # Phe
    elif c == 'TTA' or c == 'TTG' or c == 'UUA' or c == 'UUG' or c == 'CTT' or (
                    c == 'CTC' or c == 'CTA' or c == 'CTG' or c == 'CUU' or 
                    c == 'CUC' or c == 'CUA' or c == 'CUG'):
        c = 'L' # Leu
    elif c == 'TCT' or c == 'TCC' or c == 'TCA' or c == 'TCG' or c == 'UCU' or (
                    c == 'UCC' or c == 'UCA' or c == 'UCG' or c == 'AGT' or 
                    c == 'AGC' or c == 'AGU'):
        c = 'S' # Ser
    elif c == 'TAT' or c == 'TAC' or c == 'UAU' or c == 'UAC':
        c = 'Y' # Tyr
    elif c == 'TGT' or c == 'TGC' or c == 'UGU' or c == 'UGC':
        c = 'C' # Cys
    elif c == 'TGG' or c == 'UGG':
        c = 'W' # Trp
    elif c == 'CCT' or c == 'CCC' or c == 'CCA' or c == 'CCG' or c == 'CCU':
        c = 'P' # Pro
    elif c == 'CAT' or c == 'CAC' or c == 'CAU':
        c = 'H' # His
    elif c == 'CAA' or c == 'CAG':
        c = 'Q' # Gln
    elif c == 'CGT' or c == 'CGC' or c == 'CGA' or c == 'CGG' or (
                    c == 'CGU' or c == 'AGA' or c == 'AGG'):
        c = 'R' # Arg
    elif c == 'ATT' or c == 'ATC' or c == 'ATA' or (
                    c == 'AUU' or c == 'AUC' or c == 'AUA'):
        c = 'I' # Ile
    elif c == 'ATG' or c == 'AUG':
        c = 'M' # Met (Starting codon)
    elif c == 'ACT' or c == 'ACC' or c == 'ACA' or c == 'ACG' or c == 'ACU':
        c = 'T' # Thr
    elif c == 'AAT' or c == 'AAC' or c == 'AAU':
        c = 'N' # Asn
    elif c == 'AAA' or c == 'AAG':
        c = 'K' # Lys
    elif c == 'TAA' or c == 'TAG' or c == 'UAA' or (
                    c == 'UAG' or c == 'TGA' or c == 'UGA'):
        c = '*' # STOP   
    return c

# Print the strand's converted aa with sequence shift
def Seq_aa(s):
    Seq_count = len(s)
    Codon_count = (Seq_count - Seq_shift) // 3 
    aa = ''
    loc1 = 0 + Seq_shift
    loc2 = 3 + Seq_shift
    for i in range(Codon_count):
        codon = s[loc1:loc2]
        aa += Codon_aa(codon)
        loc1 += 3
        loc2 += 3
    return aa

# test all codon to aa from string
Seq_shift = 0
codon = 'TTTTTCTTATTGCTTCTCCTACTGATTATCATAATGGTTGTCGTAGTGTCTTCCTCATCGAGTA' + (
        'GCCCTCCCCCACCGACTACCACAACGGCTGCCGCAGCGTATTACTAATAGTGACATCACCAACA' +
        'GAATAACAAAAAGGATGACGAAGAGTGTTGCTGGCGTCGCCGACGGAGAAGGGGTGGCGGAGGG')
codon_aa = Seq_aa(codon)
print(codon_aa)
# correct output comparison
print('FFLLLLLLIIIMVVVVSSSSSSPPPPTTTTAAAAYY(*)HHQQNNKKDDEECCWRRRRRRGGGG')
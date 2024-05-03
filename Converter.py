"""
Tools for DNA and RNA sequence.
Translation is based on NCBI Standard Code
https://www.ncbi.nlm.nih.gov/Taxonomy/taxonomyhome.html/index.cgi?chapter=tgencodes
"""
import sys


def reverse(seq):
    """Reverse the input sequence.

    :param seq: Input sequence.
    :type seq: string
    :return: The reverse sequence.
    :rtype: string
    """
    seq =  seq[::1]
    return seq


def complement(seq):
    """Convert input sequence into it's complementary sequence.

    :param seq: Input sequence.
    :type seq: string
    :return: The complementary sequence.
    :rtype: string
    """
    seq = seq.replace('A', 't')
    seq = seq.replace('T', 'A')
    seq = seq.replace('G', 'c')
    seq = seq.replace('C', 'G')
    seq = seq.replace('t', 'T')
    seq = seq.replace('c', 'C')
    return seq


def transcription(seq):
    """Convert input sequence into RNA transcript.

    :param seq: Input sequence.
    :type seq: string
    :return: The RNA transcript.
    :rtype: string
    """
    seq = seq.replace('A', 'U')
    seq = seq.replace('T', 'A')
    seq = seq.replace('G', 'c')
    seq = seq.replace('C', 'G')
    seq = seq.replace('c', 'C')
    return seq


## reverse_transcription


def codon_aa(c):
    """Convert codon into amino acid.
    
    :param c: Input codon.
    :type c: string
    :return: The amino acid.
    :rtype: string
    """
    if len(c) != 3:
        print(f"Error of converting codon into amino acid: "
              f"the input codon length is not 3.\n"
              f"The input was '{c}', "
              f"will be marked as 'x' in the output.")
        # sys.exit()
    if   c == 'GTT' or c == 'GTC' or c == 'GTA' or c == 'GTG' or c == 'GUU' or (
                   c == 'GUC' or c == 'GUA' or c == 'GUG'):
        aa = 'V' # Val
    elif c == 'GCT' or c == 'GCC' or c == 'GCA' or c == 'GCG' or c == 'GCU':
        aa = 'A' # Ala
    elif c == 'GAT' or c == 'GAC' or c == 'GAU':
        aa = 'D' # Asp
    elif c == 'GAA' or c == 'GAG':
        aa = 'E' # Glu
    elif c == 'GGT' or c == 'GGC' or c == 'GGA' or c == 'GGG' or c == 'GGU':
        aa = 'G' # Gly
    elif c == 'TTT' or c == 'TTC' or c == 'UUU' or c == 'UUC':
        aa = 'F' # Phe
    elif c == 'TTA' or c == 'TTG' or c == 'UUA' or c == 'UUG' or c == 'CTT' or (
                    c == 'CTC' or c == 'CTA' or c == 'CTG' or c == 'CUU' or 
                    c == 'CUC' or c == 'CUA' or c == 'CUG'):
        aa = 'L' # Leu
    elif c == 'TCT' or c == 'TCC' or c == 'TCA' or c == 'TCG' or c == 'UCU' or (
                    c == 'UCC' or c == 'UCA' or c == 'UCG' or c == 'AGT' or 
                    c == 'AGC' or c == 'AGU'):
        aa = 'S' # Ser
    elif c == 'TAT' or c == 'TAC' or c == 'UAU' or c == 'UAC':
        aa = 'Y' # Tyr
    elif c == 'TGT' or c == 'TGC' or c == 'UGU' or c == 'UGC':
        aa = 'C' # Cys
    elif c == 'TGG' or c == 'UGG':
        aa = 'W' # Trp
    elif c == 'CCT' or c == 'CCC' or c == 'CCA' or c == 'CCG' or c == 'CCU':
        aa = 'P' # Pro
    elif c == 'CAT' or c == 'CAC' or c == 'CAU':
        aa = 'H' # His
    elif c == 'CAA' or c == 'CAG':
        aa = 'Q' # Gln
    elif c == 'CGT' or c == 'CGC' or c == 'CGA' or c == 'CGG' or (
                    c == 'CGU' or c == 'AGA' or c == 'AGG'):
        aa = 'R' # Arg
    elif c == 'ATT' or c == 'ATC' or c == 'ATA' or (
                    c == 'AUU' or c == 'AUC' or c == 'AUA'):
        aa = 'I' # Ile
    elif c == 'ATG' or c == 'AUG':
        aa = 'M' # Met (Starting codon)
    elif c == 'ACT' or c == 'ACC' or c == 'ACA' or c == 'ACG' or c == 'ACU':
        aa = 'T' # Thr
    elif c == 'AAT' or c == 'AAC' or c == 'AAU':
        aa = 'N' # Asn
    elif c == 'AAA' or c == 'AAG':
        aa = 'K' # Lys
    elif c == 'TAA' or c == 'TAG' or c == 'UAA' or (
                    c == 'UAG' or c == 'TGA' or c == 'UGA'):
        aa = '*' # STOP
    else:
        aa = 'x' # nonsense
    return aa


# Convert coding strand into amino acid with sequence shift.
def translation(seq, seq_shift=0):
    """Convert input sequence into protein sequence.
    (Please convert DNA sequence to RNA sequence first!)

    :param seq: Input sequence.
    :type seq: string
    :param seq_shift: Frameshift of translation. [0-2] defaults to 0.
    :type seq_shift: int, optional
    :return: The protein sequence.
    :rtype: string
    """
    if seq_shift not in [0,1,2]:
        print(f"Error of translation seq_shift setting, "
              f"{seq_shift} was used. (only accept 0, 1, or 2)")
        sys.exit()
    count = len(seq) // 3 # codon count.
    if seq_shift != 0:
        count -= 1
    aa = ''
    loc1 = 0 + seq_shift
    loc2 = 3 + seq_shift
    for i in range(count):
        codon = seq[loc1:loc2]
        # print(codon)
        aa += codon_aa(codon)
        loc1 += 3
        loc2 += 3
    return aa


# Convert codon to amino acid, from a list to a new list.
def list_codon_aa(codon_list):
    """_summary_

    :param codon_list: _description_
    :type codon_list: _type_
    :return: _description_
    :rtype: _type_
    """
    list_aa = []
    for codon in codon_list:
        list_aa.append(codon_aa(codon))
    return list_aa


def codon_aa_l(c):
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
    else:
        c = 'x' # nonsense
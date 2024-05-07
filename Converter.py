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
    seq =  seq[::-1]
    return seq


def complement(seq):
    """Convert the input sequence into it's complementary sequence.

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
    """Convert the input sequence into RNA transcript.

    :param seq: Input sequence.
    :type seq: string
    :return: The RNA transcript.
    :rtype: string
    """
    seq = seq.replace('T', 'U')
    return seq


def transcription_rev(seq):
    """Reverse transcribe into DNA sequence.

    :param seq: Input sequence.
    :type seq: string
    :return: The DNA sequence.
    :rtype: string
    """
    seq = seq.replace('U', 'T')
    return seq


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


def translation(seq, seq_shift=0):
    """Convert the input sequence into protein sequence.
    (Works on both DNA or RNA sequences!)

    :param seq: Input sequence.
    :type seq: string
    :param seq_shift: Sequence shift of translation. [0,1,2,-1] defaults to 0.
    :type seq_shift: int, optional
    :return: The protein sequence.
    :rtype: string
    """
    if seq_shift not in [0,1,2,-1]:
        print(f"Error of translation seq_shift setting, "
              f"'{seq_shift}' was used. (only accept 0, 1, 2 or -1)")
        sys.exit()
    count = len(seq) // 3 # codon count.
    if seq_shift != 0:
        count -= 1
        if seq_shift == -1:
            seq_shift = 2
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
    """Convert list of codons to list of amino acids.

    :param codon_list: Input codons.
    :type codon_list: list
    :return: The amino acids.
    :rtype: list
    """
    list_aa = []
    for codon in codon_list:
        list_aa.append(codon_aa(codon))
    return list_aa
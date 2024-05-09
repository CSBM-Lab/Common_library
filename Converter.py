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
    if c in ['GTT', 'GTC', 'GTA', 'GTG', 'GUU', 'GUC', 'GUA', 'GUG']:
        aa = 'V' # Val
    elif c in ['GCT', 'GCC', 'GCA', 'GCG', 'GCU']:
        aa = 'A' # Ala
    elif c in ['GAT', 'GAC', 'GAU']:
        aa = 'D' # Asp
    elif c in ['GAA', 'GAG']:
        aa = 'E' # Glu
    elif c in ['GGT', 'GGC', 'GGA', 'GGG', 'GGU']:
        aa = 'G' # Gly
    elif c in ['TTT', 'TTC', 'UUU', 'UUC']:
        aa = 'F' # Phe
    elif c in ['TTA', 'TTG', 'UUA', 'UUG', 'CTT', 'CTC', 'CTA', 'CTG', 'CUU', 'CUC', 'CUA', 'CUG']:
        aa = 'L' # Leu
    elif c in ['TCT', 'TCC', 'TCA', 'TCG', 'UCU', 'UCC', 'UCA', 'UCG', 'AGT', 'AGC', 'AGU']:
        aa = 'S' # Ser
    elif c in ['TAT', 'TAC', 'UAU', 'UAC']:
        aa = 'Y' # Tyr
    elif c in ['TGT', 'TGC', 'UGU', 'UGC']:
        aa = 'C' # Cys
    elif c in ['TGG', 'UGG']:
        aa = 'W' # Trp
    elif c in ['CCT', 'CCC', 'CCA', 'CCG', 'CCU']:
        aa = 'P' # Pro
    elif c in ['CAT', 'CAC', 'CAU']:
        aa = 'H' # His
    elif c in ['CAA', 'CAG']:
        aa = 'Q' # Gln
    elif c in ['CGT', 'CGC', 'CGA', 'CGG', 'CGU', 'AGA', 'AGG']:
        aa = 'R' # Arg
    elif c in ['ATT', 'ATC', 'ATA', 'AUU', 'AUC', 'AUA']:
        aa = 'I' # Ile
    elif c in ['ATG', 'AUG']:
        aa = 'M' # Met (Starting codon)
    elif c in ['ACT', 'ACC', 'ACA', 'ACG', 'ACU']:
        aa = 'T' # Thr
    elif c in ['AAT', 'AAC', 'AAU']:
        aa = 'N' # Asn
    elif c in ['AAA', 'AAG']:
        aa = 'K' # Lys
    elif c in ['TAA', 'TAG', 'UAA', 'UAG', 'TGA', 'UGA']:
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
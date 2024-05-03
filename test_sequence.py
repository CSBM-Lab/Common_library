from Converter import *

test_sequence = 'AUGUACGACUGUCGACAGGUCCAAUAG'
test_list = ['AUG', 'UAC', 'GAC', 'UGU', 'CGA', 'CAG', 'GUC', 'CAA', 'UAG']

# print(codon_aa('AUG'))

# result_translation = translation(test_sequence)
# print(result_translation)
# result_trans_list = list_codon_aa(test_list)
# print(result_trans_list)



all_codon = 'TTTTTCTTATTGCTTCTCCTACTG\
            ATTATCATAATGGTTGTCGTAGTG\
            TCTTCCTCATCGCCTCCCCCACCG\
            ACTACCACAACGGCTGCCGCAGCG\
            TATTACTAATAGCATCACCAACAG\
            AATAACAAAAAGGATGACGAAGAG\
            TGTTGCTGATGGCGTCGCCGACGG\
            AGTAGCAGAAGGGGTGGCGGAGGG'
print(len(all_codon))

codon = ['TTT', 'TTC', 'TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG',
         'ATT', 'ATC', 'ATA', 'ATG', 'GTT', 'GTC', 'GTA', 'GTG',
         'TCT', 'TCC', 'TCA', 'TCG', 'CCT', 'CCC', 'CCA', 'CCG',
         'ACT', 'ACC', 'ACA', 'ACG', 'GCT', 'GCC', 'GCA', 'GCG',
         'TAT', 'TAC', 'TAA', 'TAG', 'CAT', 'CAC', 'CAA', 'CAG',
         'AAT', 'AAC', 'AAA', 'AAG', 'GAT', 'GAC', 'GAA', 'GAG',
         'TGT', 'TGC', 'TGA', 'TGG', 'CGT', 'CGC', 'CGA', 'CGG',
         'AGT', 'AGC', 'AGA', 'AGG', 'GGT', 'GGC', 'GGA', 'GGG']
print(len(codon))

correct_protein = 'FFLLLLLLIIIMVVVV\
                   SSSSPPPPTTTTAAAA\
                   YY***HHQQNNKKDDEE\
                   CC*WRRRRSSRRGGGG'
print(correct_protein)

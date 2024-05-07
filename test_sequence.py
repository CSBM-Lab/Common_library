from Converter import *


### Testing sequence.
codon_all = 'TTTTTCTTATTGCTTCTCCTACTG' + \
            'ATTATCATAATGGTTGTCGTAGTG' + \
            'TCTTCCTCATCGCCTCCCCCACCG' + \
            'ACTACCACAACGGCTGCCGCAGCG' + \
            'TATTACTAATAGCATCACCAACAG' + \
            'AATAACAAAAAGGATGACGAAGAG' + \
            'TGTTGCTGATGGCGTCGCCGACGG' + \
            'AGTAGCAGAAGGGGTGGCGGAGGG'
print(f'{"Original sequence:" : <20} {codon_all}')

codon_list_dna = ['TTT', 'TTC', 'TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG',
                  'ATT', 'ATC', 'ATA', 'ATG', 'GTT', 'GTC', 'GTA', 'GTG',
                  'TCT', 'TCC', 'TCA', 'TCG', 'CCT', 'CCC', 'CCA', 'CCG',
                  'ACT', 'ACC', 'ACA', 'ACG', 'GCT', 'GCC', 'GCA', 'GCG',
                  'TAT', 'TAC', 'TAA', 'TAG', 'CAT', 'CAC', 'CAA', 'CAG',
                  'AAT', 'AAC', 'AAA', 'AAG', 'GAT', 'GAC', 'GAA', 'GAG',
                  'TGT', 'TGC', 'TGA', 'TGG', 'CGT', 'CGC', 'CGA', 'CGG',
                  'AGT', 'AGC', 'AGA', 'AGG', 'GGT', 'GGC', 'GGA', 'GGG']
print(f'{"list of DNA codons:" : <20} {codon_list_dna}')

codon_list_rna = ['UUU', 'TTC', 'TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG',
                  'ATT', 'ATC', 'ATA', 'ATG', 'GTT', 'GTC', 'GTA', 'GTG',
                  'TCT', 'TCC', 'TCA', 'TCG', 'CCT', 'CCC', 'CCA', 'CCG',
                  'ACT', 'ACC', 'ACA', 'ACG', 'GCT', 'GCC', 'GCA', 'GCG',
                  'TAT', 'TAC', 'TAA', 'TAG', 'CAT', 'CAC', 'CAA', 'CAG',
                  'AAT', 'AAC', 'AAA', 'AAG', 'GAT', 'GAC', 'GAA', 'GAG',
                  'TGT', 'TGC', 'TGA', 'TGG', 'CGT', 'CGC', 'CGA', 'CGG',
                  'AGT', 'AGC', 'AGA', 'AGG', 'GGT', 'GGC', 'GGA', 'GGG']
print(f'{"list of RNA codons:" : <20} {codon_list_rna}')

translation_ref = 'FFLLLLLLIIIMVVVV' + \
                  'SSSSPPPPTTTTAAAA' + \
                  'YY**HHQQNNKKDDEE' + \
                  'CC*WRRRRSSRRGGGG'
print(f'{"Protein reference:" : <20} {translation_ref}')


### Examples.
# 1. Reverse
result = reverse(codon_all)
print(f'{"Reverse sequence:" : <20} {result}')

# 2. Complement
result = complement(codon_all)
print(f'{"Complement sequence:" : <20} {result}')

# 3. Transcription
rna = transcription(codon_all)
print(f'{"Transcription:" : <20} {rna}')

# 4. Reverse transcription
dna = transcription_rev(rna)
print(f'{"Reverse transcribed:" : <20} {dna}')

# 5. Translation
# Note: Works on both DNA and RNA sequences.
protein_dna = translation(dna)
protein = translation(rna)
print(f'{"Protein reference:" : <20} {translation_ref}')
print(f'{"Translation RNA:" : <20} {protein}')
print(f'{"Translation DNA:" : <20} {protein_dna}')

# 6. Translation from list of codons.
aa_list_dna = list_codon_aa(codon_list_dna)
aa_list_rna = list_codon_aa(codon_list_rna)
aa_string_dna = ''.join(aa_list_dna)
aa_string_rna = ''.join(aa_list_rna)
print(f'{"From DNA list:" : <20} {aa_string_dna}')
print(f'{"From RNA list:" : <20} {aa_string_rna}')
print(f'{"Translated DNA list:" : <20} {aa_list_dna}')
print(f'{"Translated RNA list:" : <20} {aa_list_rna}')

# 7. Translation with sequence shift.
# Note: seq_shift only accepts 0, 1, 2 or -1 as input.
protein_shift_1 = translation(dna, 1)
protein_shift_2 = translation(dna, 2)
protein_shift_11 = translation(dna, -1)
print(f'{"Translation shift 1:" : <21} {protein_shift_1}')
print(f'{"Translation shift 2:" : <21} {protein_shift_2}')
print(f'{"Translation shift -1:" : <21} {protein_shift_11}')
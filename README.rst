Common_library
--------------

This is for storing the commonly used scripts to make our life easier.
Please name the script based on the main goal of the code, and also remember to add comments which can help other memebers to understand and modify the script.
The scripts are the following:

Converter.py
^^^^^^^^^^^^
Converter for gene sequence

**complement**
::
    - Description:
        Convert the original strand into the complementary strand.

    - Usage:   
        complement(strand)

    - Arguments:    
        strand    the original strand. Type: string

**transcription**
::
    - Description:
        Convert the original strand into the RNA transcript.

    - Usage:
        transcription(strand)

    - Arguments:
        strand    the original strand. Type: string

**codon_aa**
::
    - Description:
        Convert codon into amino acid.
    
    - Usage:
        codon_aa(codon)
    
    - Arguments:
        codon    the coding strand, can be either DNA or RNA. Type: string

**Seq_aa**
::
    - Description:
        Convert coding strand into amino acid with sequence shift.

    - Usage:
        Seq_shift = 0
        Seq_aa(codon)

    - Arguments:
        Seq_shift    the number of phase or sequence shift. Type: interger
        codon    the coding strand, can be either DNA or RNA. Type: string
    
**codon_aa_ls**
::
    - Description:
        Convert codon into amino acid. (list type)
    
    - Usage:
        codon_aa_ls(strand)

    - Arguments:
        strand    the coding strand, can be either DNA or RNA. Type: list


**Author(s)**
Johnathan Lin




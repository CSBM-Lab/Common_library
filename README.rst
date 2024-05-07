Common_library
--------------

This is for storing the commonly used scripts to make our life easier.
Please name the script based on the main goal of the code, and also remember to add comments which can help other memebers to understand and modify the script.
The scripts are the following:

Converter.py
^^^^^^^^^^^^
Converter for gene sequence

**reverse**
::
    - Description:
        Reverse the input sequence.

    - Usage:
        reverse(seq)

    - Arguments:
        seq     the input sequence. Type: string

**complement**
::
    - Description:
        Convert the input sequence into it's complementary sequence.

    - Usage:   
        complement(seq)

    - Arguments:    
        seq    the input sequence. Type: string

**transcription**
::
    - Description:
        Convert the input sequence into RNA transcript.

    - Usage:
        transcription(seq)

    - Arguments:
        seq    the input sequence. Type: string

**transcription_rev**
::
    - Description:
        Reverse transcribe into DNA sequence.

    - Usage:
        transcription(seq)

    - Arguments:
        seq    the input sequence. Type: string

**codon_aa**
::
    - Description:
        Convert codon into amino acid.
    
    - Usage:
        codon_aa(codon)
    
    - Arguments:
        codon    a single codon, can be either DNA or RNA. Type: string

**translation**
::
    - Description:
        Convert the input sequence into protein sequence.

    - Usage:
        translation(seq, seq_shift)

    - Arguments:
        seq    the input sequence, can be either DNA or RNA. Type: string
        seq_shift    the number of phase or sequence shift. [0,1,2,-1] defaults to 0. Type: interger
    
**list_codon_aa**
::
    - Description:
        Convert list of codons to list of amino acids.
    
    - Usage:
        list_codon_aa(codon_list)

    - Arguments:
        codon_list    the input codons, can be either DNA or RNA. Type: list


**Author(s)**
    Johnathan Lin




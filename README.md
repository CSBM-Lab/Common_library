# Common_library

This is for storing the commonly used scripts to make our life easier.
Please name the script based on the main goal of the code, and also remember to add comments which can help other memebers to understand and modify the script.
The scripts are the following:

<h3>gff_parser.gff</h3>

For parsing Gff file

::

    usage: annogesic [-h] [--version]
                     {create,get_input_files,update_genome_fasta,annotation_transfer,
                      tss_ps,optimize_tss_ps,terminator,transcript,utr,srna,sorf,
                      promoter,operon,circrna,go_term,srna_target,snp,ppi_network,
                      localization,riboswitch_thermometer,crispr,merge_features,
                      screenshot,colorize_screenshot_tracks}
                     ...
    
    positional arguments:
      {create,get_input_files,update_genome_fasta,annotation_transfer,tss_ps,
       optimize_tss_ps,terminator,transcript,utr,srna,sorf,promoter,operon,circrna,
       go_term,srna_target,snp,ppi_network,localization,riboswitch_thermometer,
       crispr,merge_features,screenshot,colorize_screenshot_tracks}
                            commands
        create              Create a project
        get_input_files     Get required files. (i.e. annotation files, fasta
                            files)
        update_genome_fasta
                            Get fasta files of query genomes if the query
                            sequences do not exist.
        annotation_transfer
                            Transfer the annotations from a closely related
                            species genome to a target genome.
        tss_ps              Detect TSSs or processing sites.
        optimize_tss_ps     Optimize TSSs or processing sites based on manual
                            detected ones.
        terminator          Detect rho-independent terminators.
        transcript          Detect transcripts based on coverage file.
        utr                 Detect 5'UTRs and 3'UTRs.
        srna                Detect intergenic, antisense and UTR-derived sRNAs.
        sorf                Detect expressed sORFs.
        promoter            Discover promoter motifs.
        operon              Detect operons and sub-operons.
        circrna             Detect circular RNAs.
        go_term             Extract GO terms from Uniprot.
        srna_target         Detect sRNA-mRNA interactions.
        snp                 Detect SNP/mutation and generate fasta file if
                            mutations were found.
        ppi_network         Detect protein-protein interactions suported by
                            literature.
        localization        Predict subcellular localization of proteins.
        riboswitch_thermometer
                            Predict riboswitches and RNA thermometers.
        crispr              Predict CRISPR related RNAs.
        merge_features      Merge all features to one gff file.
        screenshot          Generate screenshots for selected features using IGV.
        colorize_screenshot_tracks
                            Add color information to screenshots (e.g. useful for
                            dRNA-Seq based TSS and PS detection. It only works
                            after running "screenshot" (after running batch
                            script).
    
    optional arguments:
      -h, --help            show this help message and exit
      --version, -v         show version

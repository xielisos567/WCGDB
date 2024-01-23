##Step 1 Download the assembled genomes and the biosample files on NCBI

##Step 2 Standardization of the biosample files:
python Bio_info_exact_new2.py

##Step 3 Filter data based on the first column:
python3 temp3.py

##Statics between ARGs and the collection date，host and continent:
python3 args_stat.py all_info.txt matching_CC_ARG.txt output

###all_info.txt is the file that contains biosample information and genomes.
###matching_CC_ARG.txt is the file that contains annotation of ARGs.
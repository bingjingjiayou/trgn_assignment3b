# trgn_assignment3b
##extract_phonenum.py
Usage:
You can input "python3 extract_phonenum.py mytextfile.txt" in command line.
Description:
Run "python3 extract_phonenum. py" in the terminal to output the phone number in file "mytextfile.txt" as required.
Known issues
This script can only print out the phone number at the terminal and cannot be output to a specified.

##file.ensg2hugo.py
Usage:
First, use "wget http://ftp.ensembl.org/pub/release-75/gtf/homo_sapiens/Homo_sapiens.GRCh37.75.gtf.gz" to download this gtf file, then use comman gunzip this file. Input the command "python3 ensg2hugo.py [-f][2] [file]", the number following '-f' means the order of the colume contains gene id in a specific file including gene information.
Description:
This program can replace gene_id with the hugo name of the gene in a specific file.
Known issues:
A reasonable output is not effectively returned if the only argument entered by the user is a filename.

##histogram.py
Usage:
This program produces png picture of histograms of specified columns in a file.
Description:
Input "histogram.py -f0 laboratory_data.csv" in terminal
Known issues:
I edited this program based on csv file, this may not be work if a the input document is other types of file.

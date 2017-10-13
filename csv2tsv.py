# here is example of running python script in bash


import sys
import csv
 
tabin = csv.reader(sys.stdin, dialect=csv.excel_tab)
commaout = csv.writer(sys.stdout, dialect=csv.excel)
for row in tabin:
    commaout.writerow(row)



Here is a simple wrapper Bash script to run the conversion in batch:
for file in *.tsv
do
    python tsv2csv.py < $file > ${file%.*}.csv
done

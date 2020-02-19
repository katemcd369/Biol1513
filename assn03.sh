#!/bin/bash
assn03
# assn03-1
$for a in $(seq 808 8008); do echo TR-$a;done 

# assn03-2
c = ls -al
h = history

# assn03-3
in gene_trees/
$ls -1 *.fasta | wc -l
#15085

# assn03-4
in gene_trees/
$ls -1 *.tre | wc -l
#14640

# assn03-5
in gene_trees/
$ls -1 *.sched | wc -l
#15262

# assn03-6
in gene_trees/
#!/bin/bash
#if then code to find fasta files with no tree

for i in *.fasta
do
if [[ -e ${i%.fasta}_raxml.tre]]
then
continue
else
echo no match $i
fi
done
# saved ad File_Compare.sh

$ ./File_Compare.sh | wc -l
#445

# assn03-7
in gene_trees/
$grep "Program Return Code:*" *.sched > Return_Code
$echo Successful; grep ': 0' Return_Code | uniq | wc -l; echo Unsuccessful; grep -v ': 0' Return_Code | uniq | wc -l 
#successful 15217
#unsuccessful 44

# assn03-8
in gene_trees/

#!/bin/bash
#python script code

for i in *.fasta
do
if [[ -e ${i%.fasta}_raxml.tre]]
then
continue
else
echo 'write_raxml_job_script $i > ${i%.fasta}.pbs
fi
done
#saved as Python_tree.sh

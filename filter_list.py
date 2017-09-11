# Script used to compare the datasets in two files and print out difference

list_processed = [line.rstrip('\n') for line in open('datasets-gensim-20170731.txt')]
list_all       = [line.rstrip('\n') for line in open('datasets-gensim-20170731-all.txt')]
list_filtered  = [x for x in list_all if x not in list_processed]

print list_filtered[:10]

f = open('datasets-gensim-20170731-filtered.txt', 'w')
for x in list_filtered:
    f.write(x+'\n')
f.close()

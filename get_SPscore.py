# ECE 208
# This is function to automatacally run the FastSP to acquire the alignment error.


import os
import subprocess

def read_FASTA(stream):
    '''
    This function reads a FASTA file from a given stream and returns a dictionary mapping identifiers to sequences
    '''
    seqs = {}; name = None; seq = ''
    for line in stream:
       
        l = line.strip()
        if len(l) == 0:
            continue
        if l[0] == '>':
            if name is not None:
                assert len(seq) != 0, "Malformed FASTA"
                seqs[name] = seq
            name = l[1:]
            assert name not in seqs, "Duplicate sequence ID: %s" % name
            seq = ''
        else:
            seq += l
    assert name is not None and len(seq) != 0, "Malformed FASTA"
    seqs[name] = seq
    return seqs
    
    



#os.system(bashCommand)

group = '0'
p = '0.50'
ere = '34'
B = 'def'
head = ['group', 'p', 'ere', 'Backbone', 'SP_Score', 'SPFN', 'SPFP']
result = {}
for group in ['0', '1', '2', '3', '4']:
    for p in ['0.50', '0.75', '0.875']:
        ref_file = './actualSeq/' + group + '_' + p + '_true.fasta'
        for ere in range(34, 85, 5):
            for B in ['def', '1000', '2000', '4000']:
                est_file = './alignment/'+group+'_'+p+'_500_'
                if B =='def':
                    est_file += str(ere)+'.fasta'
                else:
                    est_file += str(ere)+'_B' + B+'.fasta'
                    #print(est_file)
                if os.path.isfile(est_file):
                    bashCommand = 'java -jar FastSP.jar -r '+ ref_file + ' -e '+est_file
                    prog = os.popen(bashCommand)
                    x =prog.read().split()
                    prefix = est_file[12:-6]
                    result[prefix] = [group, p, str(ere), B, x[1], x[5], x[7]]
                #print(prefix)

with open('result.csv', 'w') as f:
    f.write(','.join(head))
    f.write('\n')
    for k in result.keys():
        f.write(','.join(result[k]))
        f.write('\n')


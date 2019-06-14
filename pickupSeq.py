# ECE 208 
# This is function to pick up the sequence appeared in alignment result. Then, the pickup sequences are saved as reference.

import os


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
    
    
def rewriteSeq(group, p, key):
    trueSeq_file = './'+group+'/'+p+'/500/model/true.fasta'
    with open(trueSeq_file) as t:
        trueSeq = read_FASTA(t)
        
    pick_file = './actualSeq/'+group+'_'+p+'_true.fasta'
    with open(pick_file,'w') as outfile:
        for pair in trueSeq.items():
            if pair[0] in key:
                outfile.write('>%s\n%s\n' % pair)
            #if pair[0] == 'SBA':
            #    print(pair)
def getKey(group, p):
    alignmentSeq_file = './alignment/'+group+'_'+p+'_500_84'+'.fasta'
    with open(alignmentSeq_file) as f:
        alignmentSeq = read_FASTA(f)
    return(alignmentSeq.keys())
   
   
for group in ['0', '1', '2', '3', '4']:
    for p in ['0.50', '0.75', '0.875']:
        k = getKey(group, p)
        rewriteSeq(group, p, k)
print(k)

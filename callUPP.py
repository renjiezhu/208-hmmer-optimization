# ECE 208
# This is a function that automatically change the ere value in job.py. Then, it runs run_upp.py periodically.

import os

ere_list = ['0.64', '0.69', '0.74', '0.79','0.84']
curr_ere = '0.84'
filename = "./sepp/jobs.py"

for ere in ere_list:
    # replacement
    with open(filename, 'r') as file :
      filedata = file.read()
    # Replace the target string
    filedata = filedata.replace(curr_ere, ere)
    curr_ere = ere
    # Write the file out again
    with open(filename, 'w') as file:
      file.write(filedata)
    
    with open(filename, 'r') as file :
      for i,line in enumerate(file):
        if i == 267:
            print(line)
    
    os.system("mkdir "+curr_ere)
    group = "4"
    p_list = ["0.50", "0.75", "0.875"]
    #p_list = ["0.75", "0.875"]
    L = "500"

    for p in p_list:
        outpath = curr_ere+"/"+group+'_'+p+'_'+L
        
        md = "mkdir "+ outpath
        #os.system(md)

        bashCommand = "python run_upp.py -s ./1000M2/4/"+p+"/500/model/query.fas -x 4 -d ./"+outpath + " -p "+outpath
        os.system(bashCommand)

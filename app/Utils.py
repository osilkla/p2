def initCSV(csvUrl, header):
     with open(csvUrl,"w") as outf:
        outf.write(header)

def addItemToCSV(csvUrl, props):
   with open(csvUrl,"a") as outf:
        outf.write(props)
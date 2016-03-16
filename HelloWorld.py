import rpy2.robjects as robjects
read_delim = robjects.r('read.delim')
seq_data = read_delim('sequence.index', header=True, stringsAsFactors=False)
#In R:
# seq.data <- read.delim('sequence.index', header=TRUE,
# stringsAsFactors=FALSE)
print('This dataframe has %d columns and %d rows' %
(seq_data.ncol, seq_data.nrow))
print(seq_data.colnames)
#In R:
# print(colnames(seq.data))
# print(nrow(seq.data))
# print(ncol(seq.data))
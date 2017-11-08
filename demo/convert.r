
input.fname <- "riskg_group3.tsv";
output.fname <- "surv_group3_riskg.mtx";

x <- read.csv(input.fname, sep="\t");
y <- t(x);

write.tsv(y, output.fname, col.names=FALSE, row.names=TRUE);


input.fname <- "riskg_group4.tsv";
output.fname <- "surv_group4_riskg.mtx";

x <- read.csv(input.fname, sep="\t");
y <- t(x);

write.tsv(y, output.fname, col.names=FALSE, row.names=TRUE);


input.fname <- "riskg_shh.tsv";
output.fname <- "surv_shh_riskg.mtx";

x <- read.csv(input.fname, sep="\t");
y <- t(x);

write.tsv(y, output.fname, col.names=FALSE, row.names=TRUE);


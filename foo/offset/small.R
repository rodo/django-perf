library(ggplot2)
png('small.png', width=300, height=300)
# header = TRUE ignores the first line, check.names = FALSE allows '+' in 'C++'
benchmark <- read.table("small.dat", header = TRUE, row.names = "Title", check.names = FALSE)

# 't()' is matrix tranposition, 'beside = TRUE' separates the benchmarks, 'heat' provides nice colors
barplot(t(as.matrix(benchmark)), beside = TRUE, col = heat.colors(2))

# 'cex' stands for 'character expansion', 'bty' for 'box type' (we don't want borders)
legend("topright", names(benchmark), cex = 0.9, bty = "n", fill = heat.colors(2))
#


#!/usr/bin/gnuplot
# each 10 seconds
set terminal png
set xlabel "time"
set xdata time
set timefmt "%d-%m %H:%M:%S"
set format x "%M:%S"
set title "IO requests"
set ylabel "requests"
set output "io-requests.png"
set datafile separator ","
plot "dstat.dat" every ::8 using 1:2  title "io read" with lines, \
 "dstat.dat" every ::8 using 1:3  title "io write" with lines

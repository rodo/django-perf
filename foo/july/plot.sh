#!/usr/bin/gnuplot
# each 10 seconds
set terminal png
set xlabel "time"
set xdata time
set timefmt "%d-%m %H:%M:%S"
set yrange [0:500]
set y2range [0:100]
set title "IO requests"
set ylabel "requests"
set y2label "cpu iowait"
set xtics font "Verdana,8"
set ytics font "Verdana,8"
set datafile separator ","
set output "io-requests4.png"
plot "dstat4.dat" every ::7 using 1:2 axes x1y1 title "io read" with lines, \
    "dstat4.dat" every ::7 using 1:9 axes x1y2 title "io wait" with lines

#!/usr/bin/gnuplot
# each 10 seconds
set terminal png
set xlabel "time"
set xdata time
set timefmt "%d-%m %H:%M:%S"
set ylabel "kB/sec"
set y2label "%"
set y2range [0:50]
set xtics font "Verdana,8"
set ytics font "Verdana,8"
set y2tics font "Verdana,8"
set datafile separator ","
set title "Disk IO - test 4"
set output "io-requests4.png"
plot "dstat4.dat" every ::5 using 1:($4/1024) axes x1y1 title "disk read" with lines linetype rgb "blue", \
    "dstat4.dat" every ::5 using 1:9 axes x1y2 title "iowait" with lines

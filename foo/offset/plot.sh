#!/usr/bin/gnuplot
# each 10 seconds

set terminal pngcairo  transparent enhanced font "arial,10" fontscale 1.0 size 500, 350 
set output 'histograms.2.png'
set auto x
set boxwidth 0.9 absolute
set style data histograms
set xtics  norangelimit font ",8"
set title "Utilisation de Paginator" 
splot y
plot 'offset.dat' using 1 title 'offset', 2 title 'keyset'

set terminal tikz standalone

set xlabel "x"
set ylabel "D(x)"
set xrange [0:9]
set yrange [0:1]
set grid
set sample 100
set key spacing 3 box

set output "dist_funcs.tex"

f(x) = 1/(1+x)
g(x) = exp(-x)
h(x) = exp(-x/2)

plot f(x) lw 2 lc rgb '#FF0000' title '$\frac{1}{1+x}$',\
     g(x) lw 2 lc rgb '#00DD00' title '$e^{-x}$',\
     h(x) lw 2 lc rgb '#0000DD' title '$e^{-\frac{1}{2}x}$'

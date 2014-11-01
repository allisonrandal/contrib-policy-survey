set terminal pngcairo enhanced font "DroidSans,10" size 640, 200
set output "signed.png"
set datafile separator ","

set title "Percentage of developers who have contributed in the past"
set size ratio 0.25
set offsets 0.1, 0.1, 1, 1

set style line 1 lc rgb "#2166ac" lt 1 linewidth 1.3
set style line 11 lc rgb "#000000" lt 1
set border 3 linestyle 11
set tics nomirror

set format y "%g %%" 
set key outside enhanced autotitles nobox
plot "signed.dat" \
		using (column(0)):4:xtic(1) \
		notitle \
		with lines \
		linestyle 1, \

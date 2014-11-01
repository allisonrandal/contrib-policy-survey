set terminal pngcairo enhanced font "DroidSans,10" size 640, 200
set output "future.png"
set datafile separator ","

set title "Percentage of developers willing to contribute under an agreement in the future"
set size ratio 0.25
set offsets 0.1, 0.1, 1, 1

set style line 1 lc rgb "#2166ac" lt 1 linewidth 1.3
set style line 2 lc rgb "#999999" lt 1 linewidth 1.3
set style line 3 lc rgb "#b2182b" lt 1 linewidth 1.3
set style line 11 lc rgb "#000000" lt 1
set border 3 linestyle 11
set tics nomirror

set format y "%g %%" 
set key outside enhanced autotitles nobox
plot "future.dat" \
		using (column(0)):2:xtic(1) \
		title "Willing" \
		with lines \
		linestyle 1, \
     "future.dat" \
		using (column(0)):3:xtic(1) \
		title "Neutral" \
		with lines \
		linestyle 2, \
     "future.dat" \
		using (column(0)):4:xtic(1) \
		title "Unwilling" \
		with lines \
		linestyle 3 \

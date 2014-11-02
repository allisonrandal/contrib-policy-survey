set terminal pngcairo enhanced font "DroidSans,10" size 640, 640
set output "experience.png"
set datafile separator ","

set style line 1 lc rgb "#2166ac" pt 7
 
set xlabel "Years of FLOSS development experience"
set ylabel "Years of development experience"

plot "experience.dat" \
		using 1:2 \
		with points \
		notitle \
		linestyle 1

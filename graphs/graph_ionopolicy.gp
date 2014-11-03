set terminal pngcairo enhanced font "DroidSans,10" size 640, 640
set output "ionopolicy.png"
set datafile separator ","

set style histogram columns
set style fill solid 1
unset key
set boxwidth 0.8
set title "Correlation between selection of inbound=outbound and No policy"
set xtics ("inbound=outbound" 0, "Both" 1, "No policy" 2)

plot "ionopolicy.dat" \
		using 1 \
		with histograms \
		lc rgb "#a6cee3", \
     "ionopolicy.dat" \
		using 2 \
		with histograms \
		lc rgb "#1f78b4", \
     "ionopolicy.dat" \
		using 3 \
		with histograms \
		lc rgb "#b2df8a"

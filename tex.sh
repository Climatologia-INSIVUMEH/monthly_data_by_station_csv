#!/bin/bash

# Directorio de entrada donde se encuentran los archivos .tex
input_dir="/home/charmeleon/Documents/INSIVUMEH/git/monthly_data_by_station_csv/outputtex"

# Directorio de salida donde se guardarán los archivos generados
output_dir="/home/charmeleon/Documents/INSIVUMEH/git/monthly_data_by_station_csv/outputtex"

# Compila cada archivo .tex en el directorio de entrada
for file in $input_dir/*.tex
do
  echo "Compilando archivo $file"
  pdflatex -output-directory="$output_dir" "$file"
done

# Mueve los archivos generados al directorio de salida
#mv $output_dir/*.pdf $output_dir/*.log $output_dir/*.aux $output_dir/*.out $output_dir/*.toc $output_dir/*.gz $output_dir/*.snm $output_dir/*.nav $output_dir/*.fdb_latexmk $output_dir/*.fls $output_dir/*.synctex.gz $output_dir/*.synctex.gz\(busy\) $output_dir/*.xdv $output_dir/*.run.xml $output_dir/*.bcf $output_dir/*.blg $output_dir/*.bbl $output_dir/*.lot $output_dir/*.lof $output_dir/*.tdo $output_dir/*.snm $output_dir/*.nav $output_dir/*.vrb $output_dir/*.toc ./backup

echo "Compilación completada."


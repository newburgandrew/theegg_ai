#!/bin/bash
# rr
echo "dame un nombre"
read NEW_DIR
ORIG_DIR=$(pwd)

[[ -d $NEW_DIR ]] && echo $NEW_DIR already exist, aborting && exit

THE_DIR=/mnt/c/users/tutoretza3/almacen_de_escritorio/$NEW_DIR'_'$(date +%B)$(date +%Y)
echo $NEW_DIR
mkdir $THE_DIR
cd $THE_DIR
pwd
# mv /mnt/c/users/tutoretza3/desktop/pseudoescritorio/*.pdf  $THE_DIR
cp  -R /mnt/c/users/tutoretza3/desktop/pseudoescritorio/. $THE_DIR

for n in 9 8 7 6 5 4 3 2 1 0
do
touch file$n
done
ls file?
for names in file?
do
echo This file is namen > $names > $names
done
rm /mnt/c/users/tutoretza3/desktop/pseudoescritorio/*
cat file?
cd $ORIG_DIR
rm -rf $NEW_DIR
echo "Good byee"
echo mesess = $(date +%B)
echo $cadena

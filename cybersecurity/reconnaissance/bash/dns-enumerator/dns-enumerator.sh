#!/bin/bash


for palavra in $( cat dns_wordlist.txt )
do
echo ""
echo "FERRAMENTA 'HOST'"
echo ""
host $palavra.bancocn.com

echo ""
echo "FERRAMENTA 'DIG'"
echo ""
dig $palavra

echo ""
echo "FERRAMENTA 'DNSENUM' (WORDLIST PADRÃO)"
echo ""
dnsenum $palavra
done

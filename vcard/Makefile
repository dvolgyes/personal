#!/usr/bin/make
default:
	@make -C code
	echo "https://raw.githubusercontent.com/dvolgyes/personal/master/vcard/ntnu.vcf" | qr >ntnu_qr.png
	echo "https://raw.githubusercontent.com/dvolgyes/personal/master/vcard/ntnu.vcf" |qr --factory=svg-path --error-correction=L --optimize=2 >ntnu_qr.svg
	@inkscape ntnu_qr.svg -E ntnu_qr.eps --export-ignore-filters --export-ps-level=3


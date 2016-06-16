#!/usr/bin/make
default:
	@make -C code
	qr <ntnu_simplified.vcf --error-correction=L --optimize=2 >ntnu_qr.png
	qr <ntnu_simplified.vcf --factory=svg-path --error-correction=L --optimize=2 >ntnu_qr.svg
	@inkscape ntnu_qr.svg -E ntnu_qr.eps --export-ignore-filters --export-ps-level=3


#!/usr/bin/make

default: pdf

qr:
	@make -C code
	@qr <ntnu_simplified.vcf --error-correction=L --optimize=2 >ntnu_simplified.png
	@optipng ntnu_simplified.png -o9 -clobber

optimize: qr
	@qr <ntnu_simplified.vcf --factory=svg-path --error-correction=L --optimize=2 >ntnu_simplified.svg
	@inkscape ntnu_simplified.svg -E ntnu_simplified.eps --export-ignore-filters --export-ps-level=3

pdf: optimize
	@pdflatex vcard.tex
	@pdflatex vcard.tex
#cleanup
	@rm -f vcard.log
	@rm -f vcard.aux

clean:
	@rm -f ntnu_simplified.eps
	@rm -f ntnu_simplified.png
	@rm -f ntnu_simplified.svg
	@rm -f ntnu_simplified.vcf
	@rm -f ntnu.vcf
	@rm -f vcard.pdf

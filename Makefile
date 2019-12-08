all: repro

deps:
	exec/python
	Rscript packrat/init.R --bootstrap-packrat

data:
	exec/retrieve
	exec/crawl

map:
	exec/mapini
	exec/mapfin

prep:
	exec/extract

repro: deps
	data
	map

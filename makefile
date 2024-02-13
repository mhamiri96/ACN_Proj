MAKEFLAGS+="-j -l $(shell grep -c ^processor /proc/cpuinfo) "

target: run_source1 run_source2 run_source3 

run_source1:
	python source.py 0 0.5 100 100
run_source2:
	python source.py 1 1 100 100
run_source3:
	python source.py 2 0.4 100 100
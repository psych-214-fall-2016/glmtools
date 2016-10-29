# This is a Makefile for the "make" utility.
#
# It automates a set of common steps that I (your kindly instructor) run on
# the files in this repo.
#
# You will probably find yourself using "make" and Makefiles, but this is not
# part of the exercises for class, it is for me to automate building the
# exercises.
PYTHON ?= python3

LAB_TOOLS = .tools
PROC_SOLUTIONS = $(LAB_TOOLS)/proc_solutions.py

write-check-solutions:
	$(PYTHON) $(PROC_SOLUTIONS) write-solutions
	$(PYTHON) -m pytest glmtools
	$(PYTHON) $(PROC_SOLUTIONS) write

check:
	$(PYTHON) $(PROC_SOLUTIONS) check

write:
	$(PYTHON) $(PROC_SOLUTIONS) write

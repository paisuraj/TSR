# How to use
Copy and paste coverage_reduce.py and reduce.py to the top level of a project directory.

In Powershell, run:
> py coverage_reduce.py

Results of running this script will create a workspace folder with this structure at the top level of the project directory:

workspace
	COVERAGE
		coverage-test_file.json
		...
	RESULTS
		results_ge.txt
		results_gre.txt
		results_greedy.txt
		results_hgs.txt
		results_random.txt
	DATA-FILE.txt
	ORIG-FILE.txt
	STATS.txt
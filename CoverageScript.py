
#with open('Projects/') as file_obj:

import os
install_reqs = 'pipreqs'
os.system(install_reqs)
run_reqs = 'pip install -r requirements.txt'
os.system(run_reqs)
run_coverage = 'coverage run - m pytest'
os.system(run_coverage)
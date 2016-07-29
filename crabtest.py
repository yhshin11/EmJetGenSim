import subprocess
crabcommand = './crab_wrapper.sh --skip-estimates --dryrun jobs/mass_X_d_400_mass_pi_d_1_tau_pi_d_0p001/crabConfig.py'
print crabcommand
print 'Executing crabcommand'
p = subprocess.call(crabcommand, shell=True)

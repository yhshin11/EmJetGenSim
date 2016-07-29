from string import Template
from collections import OrderedDict
import os
import subprocess
import sys

cmssw_base = os.environ['CMSSW_BASE']
genfraglinkdir = os.path.join(cmssw_base, 'src/Configuration/GenProduction/python/EmJet/')
print 'genfraglinkdir: ' , genfraglinkdir
if not os.path.exists(genfraglinkdir):
    os.makedirs(genfraglinkdir)

def getjobname(mass_X_d, mass_pi_d, tag_tau_pi_d):
    jobname = 'mass_X_d_%d_mass_pi_d_%d_tau_pi_d_%s' % (mass_X_d, mass_pi_d, tag_tau_pi_d)
    return jobname

def execute(args):
    """Wrapper function to execute arbitrary shell commands"""
    print 'args: ', args
    p = subprocess.Popen(args, shell=True)
    p.wait()
    return p


jobdirname = 'jobs'
crabconfigname = 'crabConfig.py'
# Specify values for keyword values
values = {}
testing = True
if testing:
    values['mass_X_d']   = [400]
    values['tau_pi_d']   = [0.001]
    values['mass_pi_d']  = [1]
else:
    values['mass_X_d']   = [400, 600, 800, 1000, 1500, 2000]
    values['tau_pi_d']   = [0.001, 0.1, 1., 5., 150., 300.]
    values['mass_pi_d']  = [1, 2, 5, 10]
    # String representation for values of tau_pi_
tags_tau_pi_d = {0.001 : '0p001', 0.1 : '0p1', 1. : '1', 5. : '5', 150. : '150', 300. : '300'}



for mass_X_d in values['mass_X_d']:
    for tau_pi_d in values['tau_pi_d']:
        for mass_pi_d in values['mass_pi_d']:
            tag_tau_pi_d = tags_tau_pi_d[tau_pi_d]
            jobname = getjobname(mass_X_d, mass_pi_d, tag_tau_pi_d)
            ########################################
            # Submit CRAB tasks
            ########################################
            print os.getcwd()
            crabconfigpath = os.path.join(jobdirname, jobname, crabconfigname)
            crabcommand =  './crab_wrapper.sh %s %s %s' % ('--skip-estimates', '--dryrun', crabconfigpath)
            crabcommand2 = './crab_wrapper.sh --skip-estimates --dryrun jobs/mass_X_d_400_mass_pi_d_1_tau_pi_d_0p001/crabConfig.py'
            print 'crabcommand==crabcommand2', crabcommand==crabcommand2
            print 'crabcommand: ', crabcommand
            print 'crabcommand2: ', crabcommand2
            print 'Executing crabcommand'
            p=subprocess.Popen(crabcommand, shell=True)
            p.wait()

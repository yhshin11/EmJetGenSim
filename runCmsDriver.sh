#!/bin/bash
genfragment=$1
configfile=$2
source ~/.bashrc
echo 'CMSSW_BASE:'
echo $CMSSW_BASE
cd $CMSSW_BASE/src
eval `scramv1 runtime -sh`
# cmsenv
scram b

# echo "printenv:"
# printenv

echo "cmsDriver.py ${genfragment} \
--fileout file:output.root \
--step GEN,SIM --mc \
--eventcontent RAWSIM \
--datatier GEN-SIM \
--conditions MCRUN2_71_V1::All \
--customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring \
--beamspot NominalCollision2015 \
--magField 38T_PostLS1 \
--python_filename ${configfile} \
--no_exec -n 43"

cmsDriver.py ${genfragment} \
--fileout file:output.root \
--step GEN,SIM --mc \
--eventcontent RAWSIM \
--datatier GEN-SIM \
--conditions MCRUN2_71_V1::All \
--customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring \
--beamspot NominalCollision2015 \
--magField 38T_PostLS1 \
--python_filename ${configfile} \
--no_exec -n 43

# #!/usr/bin/env bash

genfragment=$1
configfile=$2
cd $CMSSW_BASE/src

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

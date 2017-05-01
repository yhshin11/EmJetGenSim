#!/bin/sh
echo "##############################"
echo "Running cmsRun wrapper script"
echo "##############################"
echo "Current working directory is $PWD"
echo "Outputting directory structure:"
echo "find ."
find .

echo "##############################"
echo "Setting environment variables" 
echo "##############################"
echo "Before setting:"
echo "PYTHIA8DATA      : $PYTHIA8DATA"
echo "LD_LIBRARY_PATH  : $LD_LIBRARY_PATH"
export PYTHIA8DATA=$PWD/src/EmJetGenSim/PythiaData/data/Pythia8
export LD_LIBRARY_PATH=$PWD/lib/$SCRAM_ARCH:$LD_LIBRARY_PATH
echo "After setting:"
echo "PYTHIA8DATA      : $PYTHIA8DATA"
echo "LD_LIBRARY_PATH  : $LD_LIBRARY_PATH"


echo "##############################"
echo "Executing cmsRun"
echo "##############################"

cmsRun -j FrameworkJobReport.xml -p PSet.py

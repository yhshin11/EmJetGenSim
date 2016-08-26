# Command to test
```
mkdir EmJetMCProd
cd EmJetMCProd
cmsrel CMSSW_7_1_18
cd CMSSW_7_1_18/src
cmsenv

git cms-init
mkdir -p Configuration
cd Configuration
git clone git@github.com:cms-sw/genproductions.git GenProduction
cd ..

```

# Edit $CMSSW_BASE/config/toolbox/$SCRAM_ARCH/tools/selected/pythia8.xml by adding path to patched version of Pythia8 and commenting out the original definition

```
<tool name="pythia8" version="205-mod">
  <lib name="pythia8"/>
  <client>
                <environment name="PYTHIA8_BASE" default="/afs/cern.ch/user/y/yoshin/pythia8205"/>
    <environment name="LIBDIR" default="$PYTHIA8_BASE/lib"/>
    <environment name="INCLUDE" default="$PYTHIA8_BASE/include"/>
  </client>
  <runtime name="PYTHIA8DATA" value="$PYTHIA8_BASE/share/Pythia8/xmldoc"/>
  <use name="hepmc"/>
  <use name="lhapdf"/>
</tool>
```

# Symlink pythia8 libraries to $CMSSW_BASE/lib/$SCRAM_ARCH/

```
scram setup pythia8
scram b ToolUpdated pythia8
cmsenv
```

# Checkout code
```
git clone file:///afs/cern.ch/work/y/yoshin/public/emjet_generate EmJetGen
cd EmJetGen

# Symlink $PYTHIA8DATA to $CMSSW_BASE/src/EmJetGen/PythiaData/data/Pythia8
mkdir -p $CMSSW_BASE/src/EmJetGen/PythiaData/data/Pythia8
ln -s $PYTHIA8DATA/* $CMSSW_BASE/src/EmJetGen/PythiaData/data/Pythia8/
```

```
source /cvmfs/cms.cern.ch/crab3/crab.sh
voms-proxy-init
python runJobs.py
```


```bash
mkdir EmJetMCProd
cd EmJetMCProd
cmsrel CMSSW_7_1_18
cd CMSSW_7_1_18/src
cmsenv

git cms-init
mkdir -p Configuration
cd Configuration
git clone git@github.com:cms-sw/genproductions.git GenProduction
cd ..

# Checkout code
git clone file:///afs/cern.ch/work/y/yoshin/public/emjet_generate EmJetGen
# mkdir emjet_generate
# cd emjet_generate
# rsync -av ~/work/public/emjet_generate/ .

# git pull file:///afs/cern.ch/work/y/yoshin/public/emjet_generate
```

Testing instructions for calling cmsDriver from python
```
# Produce date time string
dt=$(date '+%d%m%Y-%H%M%S');

mkdir tmp_$dt
cd tmp_$dt
cmsrel CMSSW_7_1_18
cd CMSSW_7_1_18/src
cmsenv

git cms-init
mkdir -p Configuration
cd Configuration
git clone git@github.com:cms-sw/genproductions.git GenProduction
cd ..

mkdir EmJetGen
cd EmJetGen
rsync -av ~/work/public/emjet_generate/ .

mkdir -p $CMSSW_BASE/src/Configuration/GenProduction/python/EmJet/
cp mass_X_d_400_mass_pi_d_1_tau_pi_d_0p001_cfi.py $CMSSW_BASE/src/Configuration/GenProduction/python/EmJet/

python cmsDriver_test.py


```




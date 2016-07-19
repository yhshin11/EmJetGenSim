from WMCore.Configuration import Configuration
import time

config = Configuration()

config.section_("General")
config.General.requestName = 'EmJetSignalMC' + time.strftime("-%Y%m%d-%H%M%S")
config.General.workArea = 'crabTasks/' + config.General.requestName
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName  = 'PrivateMC'
# Name of the CMSSW configuration file
config.JobType.psetName    = 'jobs/mass_X_d_400_mass_pi_d_1_tau_pi_d_0p001/mass_X_d_400_mass_pi_d_1_tau_pi_d_0p001_cfi.py'
# config.JobType.pyCfgParams = ['crab=1']
config.JobType.scriptExe   = 'cmsRunWrapper.sh'
# config.JobType.scriptArgs  = ''

config.section_("Data")
config.Data.outputPrimaryDataset = 'EmergingJets_mass_X_d_400_mass_pi_d_1_tau_pi_d_0p001_TuneCUETP8M1_13TeV_pythia8Mod'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 100
config.Data.totalUnits = 100
config.Data.publication = True
config.Data.outLFNDirBase = '/store/user/mamouzeg/EmJet/'

# This string is used to construct the output dataset name
config.Data.outputDatasetTag = 'mass_X_d_400_mass_pi_d_1_tau_pi_d_0p001'

config.section_("Site")
# Where the output files will be transmitted to
config.Site.storageSite = 'T3_US_UMD'


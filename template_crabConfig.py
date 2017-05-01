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
config.JobType.psetName    = '${configpath}'
# config.JobType.pyCfgParams = ['crab=1']
config.JobType.scriptExe   = 'cmsRunWrapper.sh'
# config.JobType.scriptArgs  = ''
config.JobType.priority   = 1

config.section_("Data")
config.Data.outputPrimaryDataset = '${datasetname}'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = ${eventsperjob}
config.Data.totalUnits = ${totalevents}
config.Data.publication = True
config.Data.outLFNDirBase = '${lfndirbase}'

# This string is used to construct the output dataset name
config.Data.outputDatasetTag = '${jobname}'

config.section_("Site")
# Where the output files will be transmitted to
config.Site.storageSite = '${storagesite}'


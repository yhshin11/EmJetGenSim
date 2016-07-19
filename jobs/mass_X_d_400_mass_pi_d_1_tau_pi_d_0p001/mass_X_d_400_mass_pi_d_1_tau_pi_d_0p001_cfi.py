import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
	comEnergy = cms.double(13000.0),
	crossSection = cms.untracked.double(1.333),
	filterEfficiency = cms.untracked.double(1),
	maxEventsToPrint = cms.untracked.int32(0),
	pythiaHepMCVerbosity = cms.untracked.bool(False),
	pythiaPylistVerbosity = cms.untracked.int32(1),
	PythiaParameters = cms.PSet(
	        pythia8CommonSettingsBlock,
		pythia8CUEP8M1SettingsBlock,
		processParameters = cms.vstring(
			'ParticleDecays:limitTau0 = off',             # Override option in pythia8CommonSettings

			'PartonLevel:MPI = on',                       # from DarkQCD_Scan.cc
			'PartonLevel:ISR = on',                       # from DarkQCD_Scan.cc
			'HiddenValley:FSR = on',                      # from DarkQCD_Scan.cc
			'HiddenValley:fragment = on',                 # from DarkQCD_Scan.cc

			'HiddenValley:gg2DvDvbar = on',               # gg fusion
			'HiddenValley:qqbar2DvDvbar = on',            # qqbar fusion
			'HiddenValley:alphaHVrun = on',               # Let it run
			'HiddenValley:Ngauge = 3',                    # Number of dark QCD colours
			'HiddenValley:nfl = 7',                       # flavours used for the running
			'HiddenValley:spinFv = 0',                    # Spin of bi-fundamental res.
			'4900001:m0 = 400',                   # Mass of bi-fundamental resonance
			'4900001:mWidth = 10',                        # Width of bi-fundamental resonance
			'4900001:isResonance = on',
			'4900001:mayDecay = on',
			'4900001:0:bRatio = 1',
			'4900001:0:meMode = 102',
			'HiddenValley:LambdaHV=10.',
			'HiddenValley:pTminFSR = 11.',
			'4900101:m0 = 2',                   # dark quark mass = LambdaHV
			'4900111:m0 = 1',                  # dark scalar (pion) mass
			'4900111:tau0 = 0.001',                 # dark scalar (pion) lifetime (in mm)
			'4900113:m0 = 4',                 # dark vector (rho) mass
			'4900111:0:all on 1.0 102 1 -1',              # dark pion decay to down quarks
			'4900113:0:all on 0.999 102 4900111 4900111', # dark vector to dark pions 99.9%
			'4900113:addchannel on 0.001 102 1 -1',       # dark vector to down quarks 0.1%
		),
		parameterSets = cms.vstring('pythia8CommonSettings',
		                            'pythia8CUEP8M1Settings',
		                            'processParameters')
	)
)

ProductionFilterSequence = cms.Sequence(generator)

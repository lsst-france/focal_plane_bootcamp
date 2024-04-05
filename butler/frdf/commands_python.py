import lsst.daf.butler as dafButler
import lsst.afw.display as afwDisplay
from uuid import UUID

#repo = '/sps/lsst/groups/training/2024_03_lapp_workshop/postgresql/butler/main/'
repo = '/sps/lsst/groups/FocalPlane/SLAC/run6/butler/main/'

butler = dafButler.Butler(repo)
registry = butler.registry

###General
print('=======Collections')
for c in sorted(registry.queryCollections()):
       print(c)

        


# in  repo = '/sps/lsst/groups/FocalPlane/SLAC/run6/butler/main/'  
# LATISS/calib/DM-43022                                                         CHAINED    
#  LATISS/calib/DM-43022/refactorCalibs/bias.20240229a                         CALIBRATION
#  LATISS/calib/DM-43022/refactorCalibs/dark.20240229a                         CALIBRATION
#  LATISS/calib/DM-43022/refactorCalibs/defects.20240229a                      CALIBRATION
#  LATISS/calib/DM-43022/refactorCalibs/flat-g.20240229a                       CALIBRATION
#  LATISS/calib/DM-43022/refactorCalibs/flat-r.20240229a                       CALIBRATION
#  LATISS/calib/DM-43022/refactorCalibs/flat-i.20240229a                       CALIBRATION
#  LATISS/calib/DM-43022/refactorCalibs/flat-z.20240229a                       CALIBRATION
#  LATISS/calib/DM-43022/refactorCalibs/flat-y.20240229a                       CALIBRATION
#  LATISS/calib/DM-43022/refactorCalibs/flat-white.20240229a                   CALIBRATION
#LATISS/calib/DM-43022/refactorCalibs/bias.20240229a                           CALIBRATION
#LATISS/calib/DM-43022/refactorCalibs/biasGen.20240227b/20240227T231645Z       RUN        
#LATISS/calib/DM-43022/refactorCalibs/dark.20240229a                           CALIBRATION
#LATISS/calib/DM-43022/refactorCalibs/darkGen.20240227b/20240227T234127Z       RUN        
#LATISS/calib/DM-43022/refactorCalibs/defectGen.20240227b/20240227T233918Z     RUN        
#LATISS/calib/DM-43022/refactorCalibs/defects.20240229a                        CALIBRATION
#LATISS/calib/DM-43022/refactorCalibs/flat-g.20240229a                         CALIBRATION
#LATISS/calib/DM-43022/refactorCalibs/flat-i.20240229a                         CALIBRATION
#LATISS/calib/DM-43022/refactorCalibs/flat-r.20240229a                         CALIBRATION
#LATISS/calib/DM-43022/refactorCalibs/flat-white.20240229a                     CALIBRATION
#LATISS/calib/DM-43022/refactorCalibs/flat-y.20240229a                         CALIBRATION
#LATISS/calib/DM-43022/refactorCalibs/flat-z.20240229a                         CALIBRATION

#LATISS/calib/DM-43022/refactorCalibs/flatGen.g.20240227b/20240227T235022Z     RUN        
#LATISS/calib/DM-43022/refactorCalibs/flatGen.i.20240227b/20240228T000517Z     RUN        
#LATISS/calib/DM-43022/refactorCalibs/flatGen.r.20240227b/20240227T235647Z     RUN        
#LATISS/calib/DM-43022/refactorCalibs/flatGen.white.20240227b/20240228T005251Z RUN        
#LATISS/calib/DM-43022/refactorCalibs/flatGen.y.20240227b/20240228T004114Z     RUN        
#LATISS/calib/DM-43022/refactorCalibs/flatGen.z.20240227b/20240228T003239Z     RUN         
        
        
#exit(0)      
        
#print('=======Datasets')
#for x in sorted(registry.queryDatasetTypes()):
#       print(x)

# ##Exposures
# list the dimensions of exposures
# print(registry.dimensions["exposure"].RecordClass.fields)

# query on exposures
# for i, ref in enumerate(registry.queryDimensionRecords('exposure')):
#    if(ref.observation_type=='flat'):
#        print(str(ref.id) + ' | observation_type = ' + str(ref.observation_type) + ' | exposure_time = ' + str(ref.exposure_time))

# access an exposure
# exp = butler.get("raw", instrument="LSSTCam", day_obs=20230621, seq_num=393, full_name="R13_S12", collections="LSSTCam/raw/all")
# print(exp.getImage().getArray())

# access the metadata of an exposure
# expMetadata = butler.get("raw.metadata", instrument="LSSTCam", day_obs=20230621, seq_num=393, full_name="R13_S12", collections="LSSTCam/raw/all")
# print(expMetadata)

# ##Calibrations
# get a dark
# calib = butler.get ('dark', instrument='LATISS', detector=0,collections='LATISS/calib/DM-43022/refactorCalibs/darkGen.20240227b/20240227T234127Z')
# print(calib.getImage().getArray())

#get a flat (need to add the physical filter)
#calib = butler.get ('flat', instrument='LATISS', physical_filter ='SDSSg_65mm~empty', detector=0, collections='LATISS/calib/DM-43022/refactorCalibs/flatGen.g.20240227b/20240227T235022Z')

#calib = butler.get ('flat', instrument='LATISS', physical_filter ='SDSSg_65mm~empty', detector=0, collections='LATISS/calib/DM-43022/refactorCalibs/flatGen.g.20240227b/20240227T235022Z')

calib = butler.get ('flat', instrument='LATISS', physical_filter ='SDSSg_65mm~empty', detector=0, collections='LATISS/calib/DM-43022/refactorCalibs/flatGen.g.20240227b/20240227T235022Z')

#calib = butler.get ('flat', instrument='LATISS', physical_filter ='SDSSg_65mm~empty', detector=0, collections='LATISS/calib/DM-40904')
print(calib.getImage().getArray())

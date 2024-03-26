import pandas as pd
# LSST Science Pipelines (Stack) packages
import lsst.daf.butler as dafButler
import lsst.afw.display as afwDisplay
from uuid import UUID

repo = '/sps/lsst/groups/training/2024_03_lapp_workshop/butler/main/'
butler = dafButler.Butler(repo)
registry = butler.registry

###General
#print('=======Collections')
#for c in sorted(registry.queryCollections()):
#       print(c)
#print('=======Datasets')
#for x in sorted(registry.queryDatasetTypes()):
#       print(x)

###Exposures
#3023062100284
#list the dimensions of exposures
#print(registry.dimensions["exposure"].RecordClass.fields)
#query on exposures
for i, ref in enumerate(registry.queryDimensionRecords('exposure')):
    if(ref.observation_type=='flat'):
        print(str(ref.id) + ' | observation_type = ' + str(ref.observation_type) + ' | exposure_time = ' + str(ref.exposure_time))

###Calibrations

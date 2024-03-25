## Instructions to run ISR tasks at FrDF

### LSST-stack setup
```
mkdir workarea_w_2024_09
source /cvmfs/sw.lsst.eu/linux-x86_64/lsst_distrib/w_2024_09/loadLSST.bash
setup lsst_distrib
```

### Run an official ISR task
#define the butler path
```
export REPO=/sps/lsst/groups/training/2024_03_lapp_workshop/butler/main/
```

#AuxTel example<br />
#run the task
```
EXPOSURES='2024030800199'
pipetask --log-level DEBUG --long-log run -b $REPO -p isr_example.yaml \
    -j 8 \
    -i LATISS/raw/all,LATISS/calib/DM-43022 -o u/tguillem/lapp_workshop/test_20240318a \
    -c myIsr:doDefect=True -c myIsr:doOverscan=True -c myIsr:overscan.doParallelOverscan=False -c myIsr:overscan.fitType='MEDIAN_PER_ROW' \
    -d "instrument='LATISS' AND exposure IN ($EXPOSURES)" \
    --register-dataset-types
```

The output products will be stored in a user part of the butler as defined by the path given to the \-o option (here u/tguillem/lapp_workshop/test_20240318a).

#Focal plane example<br />
#run the task for one CCD
```
EXPOSURES='3023062100284'
pipetask --log-level DEBUG --long-log run -b $REPO -p isr_example.yaml \
    -j 8 \
    -i LSSTCam/raw/all,LSSTCam/calib/DM-NNNNN/unbounded -o u/tguillem/lapp_workshop/test_fp_20240325a \
    -c myIsr:doDefect=False -c myIsr:doOverscan=True -c myIsr:overscan.doParallelOverscan=False -c myIsr:overscan.fitType='MEDIAN_PER_ROW' \
    -d "instrument='LSSTCam' AND exposure IN ($EXPOSURES) AND detector.full_name='R13_S11'" \
    --register-dataset-types
```

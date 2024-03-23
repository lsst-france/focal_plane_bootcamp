## Instructions to run cp_pipe tasks at FrDF

### LSST-stack setup
```
mkdir workarea_w_2024_09
source /cvmfs/sw.lsst.eu/linux-x86_64/lsst_distrib/w_2024_09/loadLSST.bash
setup lsst_distrib
```

### Run an official cp_pipe task
#define the butler path
```
export REPO=/sps/lsst/groups/training/2024_03_lapp_workshop/butler/main
```

#run the task
```


EXPOSURES='2024030800199'
pipetask --log-level DEBUG --long-log run -b $REPO -p isr_example.yaml \
    -j 8 \
    -i LATISS/raw/all,LATISS/calib/DM-43022,LATISS/calib/DM-NNNNN/unbounded -o u/tguillem/lapp_workshop/test_20240318a \
    -c myIsr:doDefect=True -c myIsr:doOverscan=True -c myIsr:overscan.doParallelOverscan=False -c myIsr:overscan.fitType='MEDIAN_PER_ROW' \
    -d "instrument='LATISS' AND exposure IN ($EXPOSURES)" \
    --register-dataset-types
```

The output products will be stored in a user part of the butler as defined by the path given to the \-o option (here u/tguillem/lapp_workshop/test_20240318a).

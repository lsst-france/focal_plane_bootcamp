## Instructions to run cp_pipe tasks at FrDF

### LSST-stack setup
```
mkdir workarea_w_2024_09
source /cvmfs/sw.lsst.eu/linux-x86_64/lsst_distrib/w_2024_09/loadLSST.bash
setup lsst_distrib
```

### Run an official cp_pipe task
Define the butler path
```
export REPO=/sps/lsst/groups/training/2024_03_lapp_workshop/postgresql/butler/main
```
Run a combined bias task for a set of 5 exposures
```
EXPOSURES='3023062100272, 3023062100273, 3023062100274, 3023062100275, 3023062100276'
pipetask --long-log run -b $REPO -p ${CP_PIPE_DIR}/pipelines/LsstCam/cpBias.yaml \
    -i LSSTCam/raw/all,LSSTCam/calib/DM-NNNNN/unbounded -o u/tguillem/lapp_workshop/test_mb_20240325a \
    -c biasIsr:doDefect=False -c biasIsr:doOverscan=True -c biasIsr:overscan.doParallelOverscan=False -c biasIsr:overscan.fitType='MEDIAN' \
    -d "instrument='LSSTCam' AND exposure.science_program='13391' AND exposure.observation_type='bias' AND exposure IN ($EXPOSURES) AND detector.full_name='R13_S11'" \
    --register-dataset-types
```
The output products will be stored in a user part of the butler as defined by the path given to the \-o option (here u/tguillem/lapp_workshop/test_mb_20240325a).

## Exercices
- Access your output collection<br />
- Change the pipetask options from the command line<br />
- Run a local version of cp_pipe and modify cpBias.yaml: check in the log that your change is really applied<br />
- Apply your combined bias on another bias exposure: check the image and check in the image metadata that your combined bias has been used

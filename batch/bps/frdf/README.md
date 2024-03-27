### Environment setup

All commands given below must be executed from an CC-IN2P3 interactive node (`cca.in2p3.fr`).

Setup your PostgreSQL credentials for the database `postgresql://ccpglsstdev.in2p3.fr:6553/tguillem`, namespace "workshop_butler_repo", 
as described in https://doc.lsst.eu/tutorial/butler.html#using-a-postgresql-registry-database

This can be done by adding the following content in your file `~/.lsst/db-auth.yaml`:
```
- url: "postgresql://ccpglsstdev.in2p3.fr:6553/tguillem"
  namespace: "workshop_butler_repo"
  username: "your_login"
  password: your_password
```

Create the following directories that will be used to store all files related to the bps execution:
```
mkdir -p /sps/lsst/users/${USER}/bps/bps_parsl_logs
mkdir -p /sps/lsst/users/${USER}/bps/submit
```

cd in your bps directory and clone the project:
```
cd /sps/lsst/users/${USER}/bps
git clone https://github.com/lsst-france/focal_plane_bootcamp
```

Source the environment
```
source /pbs/throng/lsst/software/bps-parsl/prod/setup.sh 
```

### Local execution of ISR on a single detector using BPS

The first step is to process locally a single detector with the ISR task. Instead of using `pipetask`, this can be done using BPS:
```
bps_submit.sh --interactive --release w_2024_09 focal_plane_bootcamp/batch/bps/frdf/LSSTCam_isr.yaml
```

The run should complete in a few minutes.

Check the BPS logs in the `bps_parsl_logs` directory, and the task logs in the `submit` directory.
You can also check that your output data have been written in the Butler repository by setting
```
export REPO=/sps/lsst/groups/training/2024_03_lapp_workshop/postgresql/butler/main
```
and looking into `$REPO/u/${USER}`.

Collections can be displayed with:
```
butler query-collections $REPO u/${USER}/isr_run/LSSTCam_isr
```
Datasets can be listed with:
```
butler query-datasets $REPO --collections u/${USER}/isr_run/LSSTCam_isr
```



### Batch execution of ISR on a full exposure using BPS

The next step is to process a full exposure. In the file `focal_plane_bootcamp/batch/bps/frdf/LSSTCam_isr.yaml`, edit the last line to modify the `dataQuery` by removing the detector constraint:
```
dataQuery: "instrument='LSSTCam' AND exposure IN (3023062100284)"
```

Because the processing requires more computing power, we can make use of ther capability of BPS to submit the processing tasks on the Slurm computing farm using Parsl. To do so, the second line must be edited to use `ccin2p3` instead of `local` for the `computeSite`:
```
computeSite: ccin2p3
```

The run can then be submitted as previously:
```
bps_submit.sh --interactive --release w_2024_09 focal_plane_bootcamp/batch/bps/frdf/LSSTCam_isr.yaml
```

You can check with `squeue` that one job per detector will be submitted. Jobs will complete in about one minute, and the full run should take several minutes.

### Gathering task executions using the BPS clustering feature

Because the ISR tasks are short, one might want to execute them together within the same job, especially when we have multiple exposures to process. This can be done using the clustering feature of BPS.

To enable it, add the following lines in the file `focal_plane_bootcamp/batch/bps/frdf/LSSTCam_isr.yaml`:
```
includeConfigs:
  - clustering.yaml
```
The run can then be submitted as previously:
```
bps_submit.sh --interactive --release w_2024_09 focal_plane_bootcamp/batch/bps/frdf/LSSTCam_isr.yaml
```

As expected only one job will be submitted this time, and its execution time will be much longer (30 minutes).
You can see in the task logs (`submit` directory) that a single log file includes the task logs for all  detectors.



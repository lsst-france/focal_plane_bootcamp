### Environment setup

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

### Batch execution of ISR on a full exposure using BPS

The next step is to process a full exposure. In the file `focal_plane_bootcamp/batch/bps/frdf/LSSTCam_isr.yaml`, edit the last line to modify toe `dataQuery` by removing the detector constraint:
```
dataQuery: "instrument='LSSTCam' AND exposure IN (3023062100284)"
```


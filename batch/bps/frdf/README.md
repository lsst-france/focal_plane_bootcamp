### Environment setup

Create the following directories:
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

```
bps_submit.sh --interactive --release w_2024_09 focal_plane_bootcamp/batch/bps/frdf/LSSTCam_isr.yaml
```


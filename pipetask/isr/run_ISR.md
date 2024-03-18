## Instructions to run ISR tasks at CC-IN2P3

This is a written follow-up to a presentation given at a LSST-France commissioning meeting:
https://drive.google.com/file/d/1fH5InUBy0612vr06tOR3rs0NZswOH_UG/view?usp=sharing  
The overall goal of this work was to gain expertise with the ISR tools in the stack. The more concrete goal was to try to define and test new overscan correction methods in the stack.  
The examples access BOT focal plane data using a butler gen3 (sqlite3 way) at CC-IN2P3.

### LSST-stack setup
```
cd workarea_w_2022_34
source /cvmfs/sw.lsst.eu/linux-x86_64/lsst_distrib/w_2022_34/loadLSST.zsh 
setup lsst_distrib
```
### Get and use local DM packages
```
git clone https://github.com/lsst/cp_pipe.git
cd cp_pipe
git checkout w.2022.34
setup -k -r .
scons -j 4
eups declare -r . -t tguillem
setup cp_pipe -t tguillem
```
From there, any call to cp_pipe will use your local package.  
N.B: by default, you will not be authorized to push to the Git repository (DM property), so it is recommended to fork the repository and do your commits there.

### Run a cp_pipe task
This is an example script using the local version of cp_pipe.
```
#define the butler path
export REPO=/sps/lsst/groups/FocalPlane/SLAC/run5/butler/gen3/all_runs/13159/
#run the task
pipetask --long-log run -b $REPO -p cp_pipe/pipelines/cpBias.yaml \
-i LSSTCam/raw/all,LSSTCam/calib -o u/tguillem/DM-30001/biasGen.full.20220829 -c isr:doDefect=False \
-d "instrument='LSSTCam' AND exposure.observation_type='bias' AND exposure.obs_id='MC_C_20211212_000086' AND detector.full_name='R14_S22'" \
--register-dataset-types
```

The output products will be stored in a user part of the butler as defined by the path given to the –o option (here u/tguillem/DM-30001/biasGen.full.20220829).  
You can test that modifying cp_pipe/pipelines/cpBias.yaml produces the expected change (checking the output log).  
Many changes can be actually done just by passing options to pipetask, but for more significant changes, a local version of the package will be necessary. In my case, I had to modify a class in the ip_isr package: so I did a fork, cloned it locally, defined it as my stack version and then I could use this version and commit my changes in Git.  
See: https://github.com/tguillemLSST/ip_isr/blob/main/python/lsst/ip/isr/overscan.py#L49

The reference page for calibration tasks in the stack is: https://pipelines.lsst.io/v/daily/modules/lsst.cp.pipe/constructing-calibrations.html


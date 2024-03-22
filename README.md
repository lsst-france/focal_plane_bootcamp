## Package description
This package was created for the LSST-France focal plane workshop at LAPP in March 2024.<br />
Website of the workshop: https://indico.in2p3.fr/event/32125/.<br />
Associated slack channel: in2p3-focal-plane<br />

## Content
This package was created to store:<br />
- basic examples for the hands-on sessions of the workshop<br />
- more advanced examples relevant for the commissioning work, in order to share expertise.<br />
Table of content:<br />
1) Butler usage<br /> 
2) Pipetasks (e.g. ISR) <br /> 
3) Job submission with BPS<br /> 
4) Calibration collections<br />
5) Science Validation and Verification tools<br />

## Ressources
- LSST-France User Guide: https://doc.lsst.eu/<br />
- DM Pipelines Bootcamp 2022: https://confluence.lsstcorp.org/display/DM/DM+Pipelines+Bootcamp+2022<br />
- Commissioning Science Validation Bootcamp 2023: https://confluence.lsstcorp.org/display/DM/May+2023+Commissioning+Science+Validation+Bootcamp<br />
- USDF account: https://developer.lsst.io/usdf/onboarding.html
- Slides of Pierre Antilogus from the 2019 LSST-France commissioning meeting: https://drive.google.com/file/d/1rfrEjrljPZIE0LekLj6Ko1swUX_RS7sI/view?usp=drive_link<br />

## Basic setup
LSST-stack setup
```
mkdir workarea_w_2024_09
source /cvmfs/sw.lsst.eu/linux-x86_64/lsst_distrib/w_2024_09/loadLSST.bash
setup lsst_distrib
```
workshop butler
```
export REPO=/sps/lsst/groups/training/2024_03_lapp_workshop/butler/main/
```
Run 6 butler (to test your postgresql account)
```
export REPO=/sps/lsst/groups/FocalPlane/SLAC/run6/butler/main/
```

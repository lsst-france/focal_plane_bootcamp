export REPO=/sps/lsst/groups/training/2024_03_lapp_workshop/postgresql/butler/main

#list all collections
butler query-collections $REPO --chains=TREE

#list some collections
#butler query-collections $REPO LATISS/calib/*
#butler query-collections $REPO LSSTCam/raw/all

#list all datasets
#butler query-datasets $REPO
#list some datasets
#butler query-datasets $REPO raw --where "instrument='LSSTCam' and exposure = 3023062100284" 
#to get the paths of the files
#butler query-datasets $REPO raw --where "instrument='LSSTCam' and exposure = 3023062100284" --show-uri

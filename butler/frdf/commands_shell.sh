export REPO=/sps/lsst/groups/training/2024_03_lapp_workshop/postgresql/butler/main

echo "list all collections"
cmd="butler query-collections $REPO --chains=TREE"
echo $cmd
eval "$cmd"
sleep 5

echo "list some collections"
cmd="butler query-collections $REPO LATISS/calib/*"
echo $cmd
eval "$cmd"
sleep 5


cmd="butler query-collections $REPO LSSTCam/raw/all"
echo $cmd
eval "$cmd"
sleep 5

echo "list all datasets"
cmd="butler query-datasets $REPO"
echo $cmd
eval "$cmd"

echo "list some datasets"

cmd="butler query-datasets $REPO raw --where \"instrument='LSSTCam' and exposure = 3023062100284\""
echo $cmd
eval "$cmd"

echo "to get the paths of the files"

cmd="butler query-datasets $REPO raw --where \"instrument='LSSTCam' and exposure = 3023062100284\" --show-uri"
echo $cmd
eval "$cmd"

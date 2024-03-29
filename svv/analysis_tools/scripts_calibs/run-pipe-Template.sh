#!/bin/sh

# choose your butler
export REPO="/sps/lsst/groups/training/2024_03_lapp_workshop/postgresql/butler/main"
#export REPO="/sps/lsst/groups/FocalPlane/SLAC/run6/butler/main" # get error here
# Choose your template
# 1) see https://tigress-web.princeton.edu/%7Elkelvin/pipelines/w_2024_12/analysis_tools/amplifierQualityCore/pipeline_analysis_tools_amplifierQualityCore.pdf
export TEMPL="amplifierQualityCore" # "Dataset type(s) ['verifyBiasCorrelations'] are not registered
# 2) see https://tigress-web.princeton.edu/%7Elkelvin/pipelines/w_2024_12/analysis_tools/exposureCore/pipeline_analysis_tools_exposureCore.pdf
# 3) see https://tigress-web.princeton.edu/%7Elkelvin/pipelines/w_2024_12/analysis_tools/cpPtcMetrics/pipeline_analysis_tools_cpPtcMetrics.pdf
#export TEMPL="exposureCore" # "Dataset type(s) ['verifyBiasCorrelations'] are not registered
#export TEMPL="cpPtcMetrics" 
echo $TEMPL
pipetask run -p $ANALYSIS_TOOLS_DIR/pipelines/${TEMPL}.yaml -b ${REPO} \
-i LSSTCam/raw/all,LATISS/calib/DM-43022,LSSTCam/raw/all,LSSTCam/calib/DM-NNNNN/unbounded \
-o u/${USER}/analysis_tools_test/Plots_${TEMPL} \
-d "instrument='LSSTCam'" --register-dataset-types 
#--prune-replaced=purge --replace-run

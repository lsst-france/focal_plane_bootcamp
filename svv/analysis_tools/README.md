# Analysis tools


## The analysis_tools pipelines


The ``analysis_tools`` are organised in set of tasks that can be run in independant pipelines as shown on:

- the [list of the analysis_tools pipelines](https://tigress-web.princeton.edu/~lkelvin/pipelines/w_2024_12/analysis_tools/):


<img src="./Figs/AnalysisToolsPipelines.png" width="400"> 





### calibration analysis_tools pipelines

- [amplifierQualityCore](https://tigress-web.princeton.edu/%7Elkelvin/pipelines/w_2024_12/analysis_tools/amplifierQualityCore/pipeline_analysis_tools_amplifierQualityCore.pdf) : analysis tool linked to bias

- [exposureCore](https://tigress-web.princeton.edu/%7Elkelvin/pipelines/w_2024_12/analysis_tools/exposureCore/pipeline_analysis_tools_exposureCore.pdf) : analysis tool of bias and darks

- [cpPtcMetrics](https://tigress-web.princeton.edu/%7Elkelvin/pipelines/w_2024_12/analysis_tools/cpPtcMetrics/pipeline_analysis_tools_cpPtcMetrics.pdf) : analysis of PTC

 

### Visit analysis_tools pipelines

- [visitQualityCore](https://tigress-web.princeton.edu/%7Elkelvin/pipelines/w_2024_12/analysis_tools/visitQualityCore/pipeline_analysis_tools_visitQualityCore.pdf) : Nothing inside

- [visitQualityExtended](https://tigress-web.princeton.edu/%7Elkelvin/pipelines/w_2024_12/analysis_tools/visitQualityExtended/pipeline_analysis_tools_visitQualityExtended.pdf) : photometric calibration

- [matchedVisitQualityCore](https://tigress-web.princeton.edu/%7Elkelvin/pipelines/w_2024_12/analysis_tools/matchedVisitQualityCore/pipeline_analysis_tools_matchedVisitQualityCore.pdf) : **photometric calibration repeatability**
 
- [visitColumnValidate](https://tigress-web.princeton.edu/%7Elkelvin/pipelines/w_2024_12/analysis_tools/visitColumnValidate/pipeline_analysis_tools_visitColumnValidate.pdf) : Simple task

	 
### Coadds object analysis_tools pipelines
	 
 
- [coaddQualityCore](https://tigress-web.princeton.edu/%7Elkelvin/pipelines/w_2024_12/analysis_tools/coaddQualityCore/pipeline_analysis_tools_coaddQualityCore.pdf) : Nothing inside	 
- [coaddQualityExtended](https://tigress-web.princeton.edu/%7Elkelvin/pipelines/w_2024_12/analysis_tools/coaddQualityExtended/pipeline_analysis_tools_coaddQualityExtended.pdf) : **Some work inside**


- [coaddDiffMatchedQualityExtended]	 (https://tigress-web.princeton.edu/%7Elkelvin/pipelines/w_2024_12/analysis_tools/coaddDiffMatchedQualityExtended/pipeline_analysis_tools_coaddDiffMatchedQualityExtended.pdf) : some work inside	

- [coaddColumnValidate](https://tigress-web.princeton.edu/%7Elkelvin/pipelines/w_2024_12/analysis_tools/coaddColumnValidate/pipeline_analysis_tools_coaddColumnValidate.pdf) : Simple task
 	 
 
### DIA analysis_tools pipelines

- [diaObjectAssociatedSources](https://tigress-web.princeton.edu/%7Elkelvin/pipelines/w_2024_12/analysis_tools/diaObjectAssociatedSources/pipeline_analysis_tools_diaObjectAssociatedSources.pdf) : Nothing inside
- [diaTractQualityCore](https://tigress-web.princeton.edu/%7Elkelvin/pipelines/w_2024_12/analysis_tools/diaTractQualityCore/pipeline_analysis_tools_diaTractQualityCore.pdf) : Some analysis inside	

### AP analysis_tool pipelines


- [apDetectorVisitQualityCore](https://tigress-web.princeton.edu/%7Elkelvin/pipelines/w_2024_12/analysis_tools/apDetectorVisitQualityCore/pipeline_analysis_tools_apDetectorVisitQualityCore.pdf) : Some analysis inside





## Running these pipelines

Here is an example for running the pipeline.

```bash
pipetask run -p $ANALYSIS_TOOLS_DIR/pipelines/matchedVisitQualityCore.yaml \
-b /sdf/group/rubin/repo/oga \
-i LATISS/runs/AUXTEL_DRP_IMAGING_20230509_20240201/w_2024_05/PREOPS-4871 \
-o u/dagoret/analysis_tools_test/Plots_matchedVisitQualityCore \
-d "instrument='LATISS' AND (band='g' or band='r' or band='i' or band='z' or band='y') AND skymap='latiss_v1' \
AND tract=3864 AND (patch=236 or patch=237)" \
--register-dataset-types --prune-replaced=purge --replace-run
```



## Accessing to the output of analysis tools

- A demo dating from [bootcamp2023](https://confluence.lsstcorp.org/display/DM/May+2023+Commissioning+Science+Validation+Bootcamp) can be installed from github [analysis_tools_examples](https://github.com/lsst-dm/analysis_tools_examples).


- The Official documentation on ``analysis_tools`` in the [pipelines documentation](https://pipelines.lsst.io/v/daily/modules/lsst.analysis.tools/index.html).


- The web-page : [plot-navigator](https://usdf-rsp.slac.stanford.edu/plot-navigator/dashboard_gen3) 

- notebooks



## Design of a tool





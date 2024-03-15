################################################################################
Three years of atmospheric parameters above Rubin-LSST site from MERRA2 database
################################################################################

.. abstract::

   While the Auxtel auxiliary telescope of the Rubin LSST observatory observes the sky 
   in spectroscopic mode to determine atmospheric parameters, 
   we report in this note the parameters recorded in the MERRA2 GMAO 
   database in a region of the El Pachon site. 
   Although these data may not correspond to those valid for telescope observations, 
   they can nevertheless provide valuable indications of annual or seasonal variational 
   trends and fluctuations, and present correlations with local measurements.



Introduction
============

The auxiliary telescope has been observing the sky in spectroscopic mode since early 2021, 
measuring atmospheric transparency to characterize the contribution 
of atmospheric transmission to the spectral shape of the Rubin-LSST 
main telescope's color filter passbands.

The shape of the spectral transmission curve of the atmosphere in the optical range covered
by LSST is determined both by the mass thickness of the atmosphere and by 
the molecular composition of certain atmospheric components.
While the relative composition of Nitrogen and Oxygen molecules is stable, 
precipitable water and Ozone molecules are variable, 
leading to variations in atmospheric transmission in certain wavelength ranges.  

In addition, small particles of atmospheric matter known as aerosols, 
which vary in nature and size and in altitude distribution, 
attenuate atmospheric transmission.



Atmospheric parameters time series 
===================================




Precipitable water vapor
------------------------

.. image:: Figs/Merra2_PWVHistRecord.png
   :height: 500
   :width: 1400
   :scale: 50
   :alt: Precipitable water vapor in mm


Ozone
-----

.. image:: Figs/Merra2_OzoneHistRecord.png
   :height: 500
   :width: 1400
   :scale: 50
   :alt: Ozone in Dobson Unit

Aerosols
--------

Vertical aerosol depth
^^^^^^^^^^^^^^^^^^^^^^

.. image:: Figs/Merra2_AerExtinctHistRecord.png
   :height: 500
   :width: 1400
   :scale: 50
   :alt: Aerosol VAOD


Aerosol exponent
^^^^^^^^^^^^^^^^

.. image:: Figs/Merra2_AerAngstromHistRecord.png
   :height: 500
   :width: 1400
   :scale: 50
   :alt: Aerosol Angstrom parameter
 


Summary and Conclusion
======================


References
==========

- MERRA2:

.. _a link: https://gmao.gsfc.nasa.gov/reanalysis/MERRA-2/



See the `Documenteer documentation <https://documenteer.lsst.io/technotes/index.html>`_ for tips on how to write and configure your new technote.

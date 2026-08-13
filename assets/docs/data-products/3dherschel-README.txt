3D-HERSCHEL UV-TO-FIR PHOTOMETRIC CATALOGS
===========================================
RELEASE: V1.1
DATE: June 15, 2026

AUTHORS
-------
McNulty et al. 2026

DESCRIPTION
-----------
This release provides UV-to-far-infrared (UV-FIR) photometric catalogs
for galaxies in four CANDELS/3D-HST extragalactic fields: COSMOS,
GOODS-South, GOODS-North, and UDS. These catalogs extend the UV-to-MIR
3D-HST photometric catalogs (Skelton et al. 2014) with Spitzer/MIPS
24 um photometry and Herschel/PACS+SPIRE far-infrared photometry
(70-350 um). Also included are stellar population parameters derived
from an emulator trained to reproduce Prospector SED modeling results,
fit to both the full UV-FIR photometry and to catalogs limited to
UV-24 um.

Herschel band coverage by field:
  COSMOS:     100, 160, 250, 350um
  GOODS-S:     70, 100, 160, 250, 350um
  GOODS-N:    100, 160, 250, 350um
  UDS:        100, 160, 250, 350um

If you use these catalogs, please cite:
  McNulty et al. 2026, ApJ (submitted), arXiv:2602.22384
  Whitaker et al. 2014, ApJ, 795, 104
  Skelton et al. 2014, ApJS, 214, 24

DOWNLOAD CONTENTS
-----------------
This release contains one tar archive per field, plus this README.

  README.txt                            This file
  cosmos_3dherschel.v1.1.cats.tar       COSMOS catalogs
  goodss_3dherschel.v1.1.cats.tar       GOODS-South catalogs
  goodsn_3dherschel.v1.1.cats.tar       GOODS-North catalogs
  uds_3dherschel.v1.1.cats.tar          UDS catalogs

Each tar archive unpacks into a directory with the following structure:

  [field]_3dherschel.v1.1.cats/
  ├── README_[field].txt
  ├── Photometry/
  │   ├── [field]_3dherschel.v1.1.cat          Photometric catalog (ASCII)
  │   └── [field]_3dherschel.v1.1.cat.FITS     Photometric catalog (FITS)
  └── Prospector/
      ├── [field]_3dherschel_sps.v1.1.cat      SPS catalog with Herschel (ASCII)
      ├── [field]_3dherschel_sps.v1.1.cat.FITS SPS catalog with Herschel (FITS)
      └── Prospector_without_Herschel/
          ├── [field]_24um_sps.v1.1.cat        SPS catalog without Herschel (ASCII)
          └── [field]_24um_sps.v1.1.cat.FITS   SPS catalog without Herschel (FITS)

CATALOG DESCRIPTIONS
--------------------
Photometric Catalog:
  Contains UV-to-FIR photometry supplementing the 3D-HST UV-MIR
  photometry (Skelton et al. 2014) with Spitzer/MIPS 24um (Whitaker
  et al. 2014) and Herschel/PACS+SPIRE far-infrared fluxes.

SPS Catalog (with Herschel):
  Stellar population parameters derived from Prospector SED modeling
  emulator fits to the full UV-FIR photometry. Parameters include 
  stellar mass, SFR, dust attenuation, etc.

SPS Catalog (without Herschel):
  Stellar population parameters derived from Prospector SED modeling
  emulator fits to photometry limited to UV-24 um.

DATA FORMAT
-----------
Catalogs are provided in both ASCII and FITS formats. Column
descriptions and units are provided in the field-level READMEs
contained within each tar archive.

VERSION HISTORY
---------------
V1.1  June 15, 2026  Initial public release

CONTACT
-------
For questions regarding this data release, please contact:
Seamusjmcn@gmail.com


ACKNOWLEDGEMENTS
----------

This work is based on observations taken by the 3D-HST Treasury 
Program (GO 12177 and 12328) with the NASA/ESA HST, which is operated 
by the Association of Universities for Research in Astronomy, Inc., 
under NASA contract NAS5-26555. This work makes use of the 3D-HST 
photometric and grism spectroscopic catalogs (Skelton et al. 2014; 
Momcheva et al. 2016; Brammer et al. 2012), which are publicly 
available from the Mikulski Archive for Space Telescopes (MAST) at 
https://archive.stsci.edu/prepds/3d-hst/. This work is based in part 
on observations made with the Spitzer Space Telescope, which was 
operated by the Jet Propulsion Laboratory, California Institute of 
Technology, under a contract with NASA. Herschel is an ESA space 
observatory with science instruments provided by European-led Principal 
Investigator consortia and with important participation from NASA. The 
Herschel data used in this work were obtained as part of the 
GOODS-Herschel (PI: D. Elbaz), CANDELS-Herschel (PI: M. Dickinson), 
PACS Evolutionary Probe (PEP), and HerMES programs.

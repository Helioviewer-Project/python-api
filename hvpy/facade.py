from typing import Any, Dict, List, Union, Optional
from datetime import datetime

from hvpy.core import execute_api_call
from hvpy.parameters import *
from hvpy.utils import add_shared_docstring

__all__ = ["getJP2Image", "getJP2Header", "getJPXClosestToMidPoint", "getJPX", "getStatus"]


@add_shared_docstring(getJP2ImageInputParameters)
def getJP2Image(
    date: datetime,
    sourceId: int,
    jpip: bool = False,
    json: bool = False,
) -> Union[bytes, str, Dict[str, Any]]:
    """
    Retrieve a JP2000 image from the helioviewer.org API.

    {Insert}
    Examples
    --------
    >>> from hvpy import getJP2Image
    >>> getJP2Image(date=datetime(2019,1,1), sourceId=1, jpip=True)
    'jpip://helioviewer.org:8090/EIT/2013/08/07/195/2013_08_07__01_13_50_146__SOHO_EIT_EIT_195.jp2'
    """
    params = getJP2ImageInputParameters(date=date, sourceId=sourceId, jpip=jpip, json=json)
    return execute_api_call(input_parameters=params)


@add_shared_docstring(getJP2HeaderInputParameters)
def getJP2Header(
    id: int,
    callback: Optional[str] = None,
) -> Union[bytes, str, Dict[str, Any]]:
    """
    Get the XML header embedded in a JPEG2000 image. Includes the FITS header
    as well as a section of Helioviewer-specific metadata.

    {Insert}
    Examples
    --------
    >>> from hvpy import getJP2Header
    >>> getJP2Header(id=9838343,callback="xml_header")
    'xml_header(\'<?xml version="1.0" encoding="utf-8"?><meta><fits><SIMPLE>1</SIMPLE><BITPIX>16</BITPIX><NAXIS>2</NAXIS><NAXIS1>4096</NAXIS1><NAXIS2>4096</NAXIS2><EXTEND>1</EXTEND><DATE_OBS>2013-02-16T12:36:47.34</DATE_OBS><ORIGIN>SDO</ORIGIN><DATE>2013-02-16T12:48:18</DATE><TELESCOP>SDO</TELESCOP><INSTRUME>AIA_3</INSTRUME><DATE-OBS>2013-02-16T12:36:47.34</DATE-OBS><T_OBS>2013-02-16T12:36:48.34Z</T_OBS><TOBSSTEP>1.0000000</TOBSSTEP><TOBSEPOC>1977.01.01_00:00:00_TAI</TOBSEPOC><CAMERA>3</CAMERA><IMG_TYPE>LIGHT</IMG_TYPE><EXPTIME>1.9996010</EXPTIME><EXPSDEV>0.00015900000</EXPSDEV><INT_TIME>2.2734380</INT_TIME><WAVELNTH>171</WAVELNTH><WAVEUNIT>angstrom</WAVEUNIT><WAVE_STR>171_THIN</WAVE_STR><FSN>62714680</FSN><FID>0</FID><LVL_NUM>1.5000000</LVL_NUM><QUALLEV0>0</QUALLEV0><QUALITY>1073741824</QUALITY><TOTVALS>16777216</TOTVALS><DATAVALS>16777216</DATAVALS><MISSVALS>0</MISSVALS><PERCENTD>100.000</PERCENTD><DATAMIN>0</DATAMIN><DATAMAX>6948</DATAMAX><DATAMEDN>133</DATAMEDN><DATAMEAN>195.780</DATAMEAN><DATARMS>284.180</DATARMS><DATASKEW>5.25000</DATASKEW><DATAKURT>-20.5000</DATAKURT><OSCNMEAN>nan</OSCNMEAN><OSCNRMS>nan</OSCNRMS><FLAT_REC>aia.flatfield[:#135]</FLAT_REC><CTYPE1>HPLN-TAN</CTYPE1><CUNIT1>arcsec</CUNIT1><CRVAL1>0.0000000</CRVAL1><CDELT1>0.60000000</CDELT1><CRPIX1>2048.5000</CRPIX1><CTYPE2>HPLT-TAN</CTYPE2><CUNIT2>arcsec</CUNIT2><CRVAL2>0.0000000</CRVAL2><CDELT2>0.60000000</CDELT2><CRPIX2>2048.5000</CRPIX2><CROTA2>0.0000000</CROTA2><R_SUN>1620.0072</R_SUN><MPO_REC>sdo.master_pointing[:#541]</MPO_REC><INST_ROT>0.019327000</INST_ROT><IMSCL_MP>0.59948900</IMSCL_MP><X0_MP>2053.5300</X0_MP><Y0_MP>2045.7100</Y0_MP><RSUN_LF>nan</RSUN_LF><X0_LF>nan</X0_LF><Y0_LF>nan</Y0_LF><ASD_REC>sdo.lev0_asd_0004[:#24069122]</ASD_REC><SAT_Y0>-8.8067430</SAT_Y0><SAT_Z0>13.073612</SAT_Z0><SAT_ROT>1.0000000e-05</SAT_ROT><ACS_MODE>SCIENCE</ACS_MODE><ACS_ECLP>NO</ACS_ECLP><ACS_SUNP>YES</ACS_SUNP><ACS_SAFE>NO</ACS_SAFE><ACS_CGT>GT3</ACS_CGT><ORB_REC>sdo.fds_orbit_vectors[2013.02.16_12:36:00_UTC]</ORB_REC><DSUN_REF>1.4959787e+11</DSUN_REF><DSUN_OBS>1.4782158e+11</DSUN_OBS><RSUN_REF>6.9600000e+08</RSUN_REF><RSUN_OBS>971.17644</RSUN_OBS><GCIEC_X>nan</GCIEC_X><GCIEC_Y>nan</GCIEC_Y><GCIEC_Z>nan</GCIEC_Z><HCIEC_X>nan</HCIEC_X><HCIEC_Y>nan</HCIEC_Y><HCIEC_Z>nan</HCIEC_Z><OBS_VR>-2460.4310</OBS_VR><OBS_VW>29920.374</OBS_VW><OBS_VN>59.733235</OBS_VN><CRLN_OBS>74.451271</CRLN_OBS><CRLT_OBS>-6.8863820</CRLT_OBS><CAR_ROT>2133</CAR_ROT><ROI_NWIN>-2147483648</ROI_NWIN><ROI_SUM>-2147483648</ROI_SUM><ROI_NAX1>-2147483648</ROI_NAX1><ROI_NAY1>-2147483648</ROI_NAY1><ROI_LLX1>-2147483648</ROI_LLX1><ROI_LLY1>-2147483648</ROI_LLY1><ROI_NAX2>-2147483648</ROI_NAX2><ROI_NAY2>-2147483648</ROI_NAY2><ROI_LLX2>-2147483648</ROI_LLX2><ROI_LLY2>-2147483648</ROI_LLY2><ISPSNAME>aia.lev0_isp_0011</ISPSNAME><ISPPKTIM>2013-02-16T12:36:44.50Z</ISPPKTIM><ISPPKTVN>001.197</ISPPKTVN><AIVNMST>453</AIVNMST><AIMGOTS>1739709443</AIMGOTS><ASQHDR>2.2101983e+09</ASQHDR><ASQTNUM>2</ASQTNUM><ASQFSN>62714680</ASQFSN><AIAHFSN>62714672</AIAHFSN><AECDELAY>1539</AECDELAY><AIAECTI>0</AIAECTI><AIASEN>0</AIASEN><AIFDBID>241</AIFDBID><AIMGOTSS>5158</AIMGOTSS><AIFCPS>10</AIFCPS><AIFTSWTH>0</AIFTSWTH><AIFRMLID>3120</AIFRMLID><AIFTSID>40960</AIFTSID><AIHISMXB>7</AIHISMXB><AIHIS192>0</AIHIS192><AIHIS348>2539275</AIHIS348><AIHIS604>7478310</AIHIS604><AIHIS860>8388608</AIHIS860><AIFWEN>204</AIFWEN><AIMGSHCE>2000</AIMGSHCE><AECTYPE>0</AECTYPE><AECMODE>ON</AECMODE><AISTATE>CLOSED</AISTATE><AIAECENF>1</AIAECENF><AIFILTYP>0</AIFILTYP><AIMSHOBC>41.080002</AIMSHOBC><AIMSHOBE>26.068001</AIMSHOBE><AIMSHOTC>55.287998</AIMSHOTC><AIMSHOTE>69.264000</AIMSHOTE><AIMSHCBC>2040.7720</AIMSHCBC><AIMSHCBE>2025.8600</AIMSHCBE><AIMSHCTC>2054.8401</AIMSHCTC><AIMSHCTE>2068.6321</AIMSHCTE><AICFGDL1>0</AICFGDL1><AICFGDL2>137</AICFGDL2><AICFGDL3>201</AICFGDL3><AICFGDL4>236</AICFGDL4><AIFOENFL>1</AIFOENFL><AIMGFSN>5</AIMGFSN><AIMGTYP>0</AIMGTYP><AIAWVLEN>7</AIAWVLEN><AIAGP1>0</AIAGP1><AIAGP2>0</AIAGP2><AIAGP3>0</AIAGP3><AIAGP4>0</AIAGP4><AIAGP5>0</AIAGP5><AIAGP6>0</AIAGP6><AIAGP7>0</AIAGP7><AIAGP8>393</AIAGP8><AIAGP9>457</AIAGP9><AIAGP10>748</AIAGP10><AGT1SVY>-8</AGT1SVY><AGT1SVZ>-3</AGT1SVZ><AGT2SVY>-5</AGT2SVY><AGT2SVZ>-9</AGT2SVZ><AGT3SVY>0</AGT3SVY><AGT3SVZ>1</AGT3SVZ><AGT4SVY>7</AGT4SVY><AGT4SVZ>-44</AGT4SVZ><AIMGSHEN>4</AIMGSHEN><RECNUM>56693877</RECNUM><BLANK>-32768</BLANK><CHECKSUM>VG4SXD2RVD2RVD2R</CHECKSUM><DATASUM>903067050</DATASUM><XCEN>0.00000</XCEN><YCEN>0.00000</YCEN><history>FITSHEAD2STRUCT run at: Sat Feb 16 05:06:33 2013</history><comment>FITS (Flexible Image Transport System) format is defined in \\\'Astronomyand Astrophysics\\\', volume 376, page 359; bibcode: 2001A&amp;A...376..359HFITSHEAD2STRUCT</comment></fits><helioviewer><HV_ROTATION>0.00000</HV_ROTATION><HV_JP2GEN_VERSION>0.8</HV_JP2GEN_VERSION><HV_JP2GEN_BRANCH_REVISION>No valid revision number found. Bazaar not installed? Using HV_WRITTENBY manually included revision number: 84 [2011/01/10, https://launchpad.net/jp2gen] : % SPAWN: Error managing child process.:  No such file or directory</HV_JP2GEN_BRANCH_REVISION><HV_HVS_DETAILS_FILENAME>hvs_version5.pro</HV_HVS_DETAILS_FILENAME><HV_HVS_DETAILS_FILENAME_VERSION>5.0</HV_HVS_DETAILS_FILENAME_VERSION><HV_COMMENT>JP2 file created locally at Lockheed LMSAL using hv_aia_list2jp2_gs2 at Sat Feb 16 05:06:34 2013.Contact Helioviewer LMSAL Franchise (slater@lmsal.com) for more details/questions/comments regarding this JP2 file.HVS (Helioviewer setup) file used to create this JP2 file: hvs_version5.pro (version 5.0).FITS to JP2 source code provided by ESA/NASA Helioviewer Project [contact the Helioviewer Project at webmaster@helioviewer.org][NASA-GSFC] and is available for download at https://launchpad.net/jp2gen.Please contact the source code providers if you suspect an error in the source code.Full source code for the entire Helioviewer Project can be found at https://launchpad.net/helioviewer.</HV_COMMENT><HV_SUPPORTED>TRUE</HV_SUPPORTED></helioviewer></meta>\')'
    """
    params = getJP2HeaderInputParameters(id=id, callback=callback)
    return execute_api_call(input_parameters=params)


@add_shared_docstring(getJPXClosestToMidPointInputParameters)
def getJPXClosestToMidPoint(
    startTimes: List[datetime],
    endTimes: List[datetime],
    sourceId: int,
    linked: bool = True,
    verbose: bool = False,
    jpip: bool = False,
) -> Union[bytes, str, Dict[str, Any]]:
    """
    Generate and (optionally) download a custom JPX movie of the specified
    datasource with one frame per pair of startTimes/endTimes parameters.

    {Insert}
    Examples
    --------
    >>> from hvpy import getJPXClosestToMidPoint
    >>> from datetime import datetime
    >>> getJPXClosestToMidPoint(startTimes=[datetime(2014, 1, 1, 0, 0, 0), datetime(2014, 1, 1, 2, 3, 3), datetime(2014, 1, 1, 4, 5, 5)], endTimes=[datetime(2014, 1, 1, 0, 45, 0), datetime(2014, 1, 1, 2, 33, 3), datetime(2014, 1, 1, 4, 54, 5)], sourceId=14, linked=False, verbose=False, jpip=True)
    'jpip://helioviewer.org:8090/movies/SDO_AIA_335_F2013-12-31T18.30.00Z_T2013-12-31T23.24.05ZCMP.jpxmid'
    """
    params = getJPXClosestToMidPointInputParameters(
        startTimes=startTimes,
        endTimes=endTimes,
        sourceId=sourceId,
        linked=linked,
        verbose=verbose,
        jpip=jpip,
    )
    return execute_api_call(input_parameters=params)


@add_shared_docstring(getJPXInputParameters)
def getJPX(
    startTime: List[datetime],
    endTime: List[datetime],
    sourceId: int,
    linked: bool = True,
    verbose: bool = False,
    jpip: bool = False,
    cadence: Optional[int] = None,
) -> Union[bytes, str, Dict[str, Any]]:
    """
    Generate and (optionally) download a custom JPX movie of the specified
    datasource from the helioviewer.org API.

    {Insert}
    Examples
    --------
    >>> from hvpy import getJPX
    >>> from datetime import datetime
    >>> getJPX(startTime=datetime(2014, 1, 1, 0, 0, 0),endTime=datetime(2014, 1, 1, 0, 45, 0),sourceId=14,linked=True,verbose=False,jpip=True,cadence=None)
    'jpip://helioviewer.org:8090/movies/SDO_AIA_335_F2014-01-01T00.00.00Z_T2014-01-01T00.45.00ZL.jpx'
    """
    params = getJPXInputParameters(
        startTime=startTime,
        endTime=endTime,
        sourceId=sourceId,
        linked=linked,
        verbose=verbose,
        jpip=jpip,
        cadence=cadence,
    )
    return execute_api_call(input_parameters=params)


@add_shared_docstring(getStatusInputParameters)
def getStatus() -> Union[bytes, str, Dict[str, Any]]:
    """
    Returns information about how far behind the latest available JPEG2000
    images.

    {Insert}
    Examples
    --------
    >>> from hvpy import getStatus
    >>> getStatus()
    {'AIA': {'time': '2022-07-11T08:01:35Z', 'level': 1, 'secondsBehind': 1801, 'measurement': 'AIA 94'}, 'COSMO': {'time': '2022-07-05T00:46:07Z', 'level': 4, 'secondsBehind': 546329, 'measurement': 'COSMO KCor'}, 'EIT': {'time': '2013-08-07T13:06:09Z', 'level': 5, 'secondsBehind': 281647527, 'measurement': 'EIT 284'}, 'HMI': {'time': '2022-07-11T06:00:39Z', 'level': 1, 'secondsBehind': 9057, 'measurement': 'HMI Mag'}, 'LASCO': {'time': '2022-07-11T06:30:07Z', 'level': 1, 'secondsBehind': 7289, 'measurement': 'LASCO C3'}, 'MDI': {'time': '2011-01-11T22:39:00Z', 'level': 5, 'secondsBehind': 362742756, 'measurement': 'MDI Int'}, 'SECCHI': {'time': '2022-07-08T23:57:30Z', 'level': 1, 'secondsBehind': 203646, 'measurement': 'EUVI-A 195'}, 'SWAP': {'time': '2022-07-11T06:17:19Z', 'level': 1, 'secondsBehind': 8057, 'measurement': 'SWAP 174'}, 'SXT': {'time': '2001-12-14T21:06:33Z', 'level': 5, 'secondsBehind': 649164303, 'measurement': 'SXT AlMgMn'}, 'XRT': {'time': '2022-06-24T23:56:45Z', 'level': 5, 'secondsBehind': 1413291, 'measurement': 'XRT Any/Any'}}
    """
    params = getStatusInputParameters()
    return execute_api_call(input_parameters=params)

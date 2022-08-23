from enum import Enum

__all__ = ["DataSource"]


class DataSource(Enum):
    """
    Enum for datasources hosted by the Helioviewer Project.
    """

    EIT_171 = 0
    """
    SOHO instrument EIT, measurement 171.
    """

    EIT_195 = 1
    """
    SOHO instrument EIT, measurement 195.
    """

    EIT_284 = 2
    """
    SOHO instrument EIT, measurement 284.
    """

    EIT_304 = 3
    """
    SOHO instrument EIT, measurement 304.
    """

    LASCO_C2 = 4
    """
    SOHO instrument LASCO, measurement C2.
    """

    LASCO_C3 = 5
    """
    SOHO instrument LASCO, measurement C3.
    """

    MDI_MAG = 6
    """
    SOHO instrument MDI, measurement magnetogram.
    """

    MDI_INT = 7
    """
    SOHO instrument MDI, measurement continuum.
    """

    AIA_94 = 8
    """
    SDO instrument AIA, measurement 94.
    """

    AIA_131 = 9
    """
    SDO instrument AIA, measurement 131.
    """

    AIA_171 = 10
    """
    SDO instrument AIA, measurement 171.
    """

    AIA_193 = 11
    """
    SDO instrument AIA, measurement 193.
    """

    AIA_211 = 12
    """
    SDO instrument AIA, measurement 211.
    """

    AIA_304 = 13
    """
    SDO instrument AIA, measurement 304.
    """

    AIA_335 = 14
    """
    SDO instrument AIA, measurement 335.
    """

    AIA_1600 = 15
    """
    SDO instrument AIA, measurement 1600.
    """

    AIA_1700 = 16
    """
    SDO instrument AIA, measurement 1700.
    """

    AIA_4500 = 17
    """
    SDO instrument AIA, measurement 4500.
    """

    HMI_INT = 18
    """
    SDO instrument HMI, measurement continuum.
    """

    HMI_MAG = 19
    """
    SDO instrument HMI, measurement magnetogram.
    """

    EUVI_A_171 = 20
    """
    STEREO_A instrument SECCHI, detector EUVI, measurement 171.
    """

    EUVI_A_195 = 21
    """
    STEREO_A instrument SECCHI, detector EUVI, measurement 195.
    """

    EUVI_A_284 = 22
    """
    STEREO_A instrument SECCHI, detector EUVI, measurement 284.
    """

    EUVI_A_304 = 23
    """
    STEREO_A instrument SECCHI, detector EUVI, measurement 304.
    """

    EUVI_B_171 = 24
    """
    STEREO_B instrument SECCHI, detector EUVI, measurement 171.
    """

    EUVI_B_195 = 25
    """
    STEREO_B instrument SECCHI, detector EUVI, measurement 195.
    """

    EUVI_B_284 = 26
    """
    STEREO_B instrument SECCHI, detector EUVI, measurement 284.
    """

    EUVI_B_304 = 27
    """
    STEREO_B instrument SECCHI, detector EUVI, measurement 304.
    """

    COR1_A = 28
    """
    STEREO_A instrument SECCHI, detector COR1, measurement white-light.
    """

    COR2_A = 29
    """
    STEREO_A instrument SECCHI, detector COR2, measurement white-light.
    """

    COR1_B = 30
    """
    STEREO_B instrument SECCHI, detector COR1, measurement white-light.
    """

    COR2_B = 31
    """
    STEREO_B instrument SECCHI, detector COR2, measurement white-light.
    """

    SWAP_174 = 32
    """
    PROBA2 instrument SWAP, measurement 174.
    """

    SXT_ALMGMN = 33
    """
    Yohkoh instrument SXT, measurement AlMgMn.
    """

    SXT_THIN_AL = 34
    """
    Yohkoh instrument SXT, measurement thin-Al.
    """

    SXT_WHITE_LIGHT = 35
    """
    Yohkoh instrument SXT, measurement white-light.
    """

    XRT_AL_MED_AL_MESH = 38
    """
    Hinode instrument XRT Al-med/Al-mesh.
    """

    XRT_AL_MED_AL_THICK = 39
    """
    Hinode instrument XRT Al_med/Al_thick.
    """

    XRT_AL_MED_BE_THICK = 40
    """
    Hinode instrument XRT Al_med/Be_thick.
    """

    XRT_AL_MED_GBAND = 41
    """
    Hinode instrument XRT Al_med/GBand.
    """

    XRT_AL_MED_OPEN = 42
    """
    Hinode instrument XRT Al_med/Open.
    """

    XRT_AL_MED_TI_POLY = 43
    """
    Hinode instrument XRT Al_med/Ti_poly.
    """

    XRT_AL_POLY_AL_mesh = 44
    """
    Hinode instrument XRT Al_poly/Al_mesh.
    """

    XRT_AL_POLY_AL_THICK = 45
    """
    Hinode instrument XRT Al_poly/Al_thick.
    """

    XRT_AL_POLY_BE_THICK = 46
    """
    Hinode instrument XRT Al_poly/Be_thick.
    """

    XRT_AL_POLY_GBAND = 47
    """
    Hinode instrument XRT Al_poly/GBand.
    """

    XRT_AL_POLY_OPEN = 48
    """
    Hinode instrument XRT Al_poly/Open.
    """

    XRT_AL_POLY_TI_POLY = 49
    """
    Hinode instrument XRT Al_poly/Ti_poly.
    """

    XRT_BE_MED_AL_MESH = 50
    """
    Hinode instrument XRT Be_med/Al_mesh.
    """

    XRT_BE_MED_AL_THICK = 51
    """
    Hinode instrument XRT Be_med/Al_thick.
    """

    XRT_BE_MED_BE_THICK = 52
    """
    Hinode instrument XRT Be_med/Be_thick.
    """

    XRT_BE_MED_GBAND = 53
    """
    Hinode instrument XRT Be_med/GBand.
    """

    XRT_BE_MED_OPEN = 54
    """
    Hinode instrument XRT Be_med/Open.
    """

    XRT_BE_MED_TI_POLY = 55
    """
    Hinode instrument XRT Be_med/Ti_poly.
    """

    XRT_BE_THIN_AL_MESH = 56
    """
    Hinode instrument XRT Be_thin/Al_mesh.
    """

    XRT_BE_THIN_AL_THICK = 57
    """
    Hinode instrument XRT Be_thin/Al_thick.
    """

    XRT_BE_THIN_BE_THICK = 58
    """
    Hinode instrument XRT Be_thin/Be_thick.
    """

    XRT_BE_THIN_GBAND = 59
    """
    Hinode instrument XRT Be_thin/GBand.
    """

    XRT_BE_THIN_OPEN = 60
    """
    Hinode instrument XRT Be_thin/Open.
    """

    XRT_BE_THIN_TI_POLY = 61
    """
    Hinode instrument XRT Be_thin/Ti_poly.
    """

    XRT_C_POLY_AL_MESH = 62
    """
    Hinode instrument XRT C_poly/Al_mesh.
    """

    XRT_C_POLY_AL_THICK = 63
    """
    Hinode instrument XRT C_poly/Al_thick.
    """

    XRT_C_POLY_BE_THICK = 64
    """
    Hinode instrument XRT C_poly/Be_thick.
    """

    XRT_C_POLY_GBAND = 65
    """
    Hinode instrument XRT C_poly/GBand.
    """

    XRT_C_POLY_OPEN = 66
    """
    Hinode instrument XRT C_poly/Open.
    """

    XRT_C_POLY_TI_POLY = 67
    """
    Hinode instrument XRT C_poly/Ti_poly.
    """

    XRT_MISPOSITIONED_MISPOSITIONED = 68
    """
    Hinode instrument XRT Mispositioned/Mispositioned.
    """

    XRT_OPEN_AL_MESH = 69
    """
    Hinode instrument XRT Open/Al_mesh.
    """

    XRT_OPEN_AL_THICK = 70
    """
    Hinode instrument XRT Open/Al_thick.
    """

    XRT_OPEN_BE_THICK = 71
    """
    Hinode instrument XRT Open/Be_thick.
    """

    XRT_OPEN_GBAND = 72
    """
    Hinode instrument XRT Open/GBand.
    """

    XRT_OPEN_OPEN = 73
    """
    Hinode instrument XRT Open/Open.
    """

    XRT_OPEN_TI_POLY = 74
    """
    Hinode instrument XRT Open/Ti_poly.
    """

    TRACE_171 = 75
    """
    TRACE measurement 171.
    """

    TRACE_195 = 76
    """
    TRACE measurement 195.
    """

    TRACE_284 = 77
    """
    TRACE measurement 284.
    """

    TRACE_1216 = 78
    """
    TRACE measurement 1216.
    """

    TRACE_1550 = 79
    """
    TRACE measurement 1550.
    """

    TRACE_1600 = 80
    """
    TRACE measurement 1600.
    """

    TRACE_1700 = 81
    """
    TRACE measurement 1700.
    """

    TRACE_WHITE_LIGHT = 82
    """
    TRACE measurement white-light.
    """

    COSMO_KCOR = 83
    """
    MLSO instrument COSMO, detector KCor, measurement 735.
    """

    EUI_FSI_174 = 84
    """
    Solar Orbiter instrument FSI, measurement 174.
    """

    EUI_FSI_304 = 85
    """
    Solar Orbiter instrument FSI, measurement 304.
    """

    EUI_HRI_174 = 86
    """
    Solar Orbiter instrument HRI, measurement 174.
    """

    EUI_HRI_1216 = 87
    """
    Solar Orbiter instrument HRI, measurement 1216.
    """

    SUVI_94 = 88
    """
    GOES-R instrument SUVI, measurement 94.
    """

    SUVI_131 = 89
    """
    GOES-R instrument SUVI, measurement 131.
    """

    SUVI_171 = 90
    """
    GOES-R instrument SUVI, measurement 171.
    """

    SUVI_195 = 91
    """
    GOES-R instrument SUVI, measurement 195.
    """

    SUVI_284 = 92
    """
    GOES-R instrument SUVI, measurement 284.
    """

    SUVI_304 = 93
    """
    GOES-R instrument SUVI, measurement 304.
    """

    XRT_ANY_ANY = 10001
    """
    Hinode instrument XRT any/any.
    """

    XRT_ANY_AL_MESH = 10002
    """
    Hinode instrument XRT any/Al_mesh.
    """

    XRT_ANY_AL_THICK = 10003
    """
    Hinode instrument XRT any/Al_thick.
    """

    XRT_ANY_BE_THICK = 10004
    """
    Hinode instrument XRT any/Be_thick.
    """

    XRT_ANY_GBAND = 10005
    """
    Hinode instrument XRT any/GBand.
    """

    XRT_ANY_OPEN = 10006
    """
    Hinode instrument XRT any/Open.
    """

    XRT_ANY_TI_POLY = 10007
    """
    Hinode instrument XRT any/Ti_poly.
    """

    XRT_AL_MED_ANY = 10008
    """
    Hinode instrument XRT Al_med/any.
    """

    XRT_AL_POLY_ANY = 10009
    """
    Hinode instrument XRT Al_poly/any.
    """

    XRT_BE_MED_ANY = 10010
    """
    Hinode instrument XRT Be_med/any.
    """

    XRT_BE_THIN_ANY = 10011
    """
    Hinode instrument XRT Be_thin/any.
    """

    XRT_C_POLY_ANY = 10012
    """
    Hinode instrument XRT C_poly/any.
    """

    XRT_OPEN_ANY = 10013
    """
    Hinode instrument XRT Open/any.
    """

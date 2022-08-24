from enum import Enum

__all__ = ["EventType"]


class EventType(Enum):
    """
    Enum for the event types supported by Helioviewer.
    """

    ACTIVE_REGION = "AR"
    CORONAL_CAVITY = "CC"
    CORONAL_DIMMING = "CD"
    CORONAL_HOLE = "CH"
    CORONAL_JET = "CJ"
    CORONAL_MASS_EJECTION = "CE"
    CORONAL_RAIN = "CR"
    CORONAL_WAVE = "CW"
    EMERGING_FLUX = "EF"
    ERUPTION = "ER"
    FILAMENT = "FI"
    FILAMENT_ACTIVATION = "FA"
    FILAMENT_ERUPTION = "FE"
    FLARE = "FL"
    LOOP = "LP"
    OSCILLATION = "OS"
    PLAGE = "PG"
    SIGMOD = "SG"
    SPRAY_SURGE = "SP"
    SUNSPOT = "SS"

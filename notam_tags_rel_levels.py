notam_general_relevance = {
    "RWY CLSD": {
        "color": "Red",
        "relevance": "Critical",
        "description": "A NOTAM indicating a runway closure, no matter for how long and no matter the reasons.",
    },
    "RWY RESTR": {
        "color": "Yellow",
        "relevance": "Medium",
        "description": "A NOTAM indicating partial limitations and changes into a runway operativity. These will involve the runway itself or its adjacent terrain.",
    },
    "TWY CLSD": {
        "color": "Yellow",
        "relevance": "Medium",
        "description": "A NOTAM indicating that one (or more than one) regular taxiway are closed, no matter for how long and no matter the reasons. Such a NOTAM will not include apron taxiways.",
    },
    "TWY RESTR": {
        "color": "Green",
        "relevance": "Low",
        "description": "A NOTAM reporting different kinds of limitations, events or conditions that are affecting the operational activities in a taxiway. Such a NOTAM will not include apron taxiways.",
    },
    "ATC NOT AVLB": {
        "color": "Red",
        "relevance": "Critical",
        "description": "A NOTAM reporting that Air Traffic Control primary and most needed services for IFR are unavailable.",
    },
    "APPR NOT AVLB": {
        "color": "Red",
        "relevance": "Critical",
        "description": "A NOTAM that indicates urgent or temporary limitations/unavailability of published approach procedures. These may require the attention of the crew when planning flight activities.",
    },
    "AIRPORT RESTRICTIONS": {
        "color": "Red",
        "relevance": "Critical",
        "description": "A NOTAM indicating operational and administrative restrictions affecting airport accessibility for landing. Also includes access restrictions based on aircraft type.",
    },
    "ILS": {
        "color": "Yellow",
        "relevance": "Medium",
        "description": "A NOTAM reporting all communications, issues and updates regarding the ILS (Instrumental Landing System) apparatus of the specific aerodrome.",
    },
    "APPROACH PROCEDURES": {
        "color": "Orange",
        "relevance": "High",
        "description": "A NOTAM reporting modifications, restrictions, or temporary unavailability of published instrument or visual approach procedures (might include changes to minima, navigation aid availability, missed approach instructions, charted waypoints, or required equipment).",
    },
    "AIRSPACE": {
        "color": "Orange",
        "relevance": "High",
        "description": "A NOTAM that describes the structure or status of the surrounding airspace itself, such as with activation/withdrawal of restricted, prohibited or segregated areas, or changes in control zones. Also includes modification of the availability and geometry of an airspace.",
    },
    "FLIGHT PROCEDURES": {
        "color": "Yellow",
        "relevance": "Medium",
        "description": "A NOTAM that covers how flights are managed within existing airspace. Might include changes to routings, altitude restrictions, handoff procedures, slot/flow management.",
    },
    "WEATHER WARNING": {
        "color": "Red",
        "relevance": "Critical",
        "description": "A NOTAM reporting both adverse meteorological conditions or the absence of required minimum weather parameters/apparatus an airport should normally have. Includes also so-called SNOWTAMS (describing surface conditions like snow, ice and slush on airport movements areas) and ASHTAMs (providing information on changes in volcanic ash or other dust contamination that affects airport operations).",
    },
    "COMMUNICATIONS": {
        "color": "Yellow",
        "relevance": "Medium",
        "description": "A NOTAM reporting degradation, frequency changes, frequency deletion, or whatever information that regards the overall radio communication system from air to ground.",
    },
    "AIP CHANGE": {
        "color": "Green",
        "relevance": "Low",
        "description": "A NOTAM that reports permanent or temporary changes published via AIP that are deemed to be operationally significant (even if not immediately). Trigger NOTAMs are included into this category. ",
    },
    "NAVAIDS": {
        "color": "Yellow",
        "relevance": "Medium",
    "description": "A NOTAM indicating outages, degradations, or limitations of ground-based navigation aids such as VOR, DME, NDB. Might report complete unavailability, reduced accuracy, false indications, restricted operating hours, or interference.",
    },
    "OBSTACLES": {
        "color": "Yellow",
        "relevance": "Medium",
        "description": "Physical, fixed or temporary structures protruding into standard flight profiles near the aerodrome. Typically includes cranes, antennas, buildings, or uncharted tall objects. Primarily impacts departure and arrival procedures. Must include the nature of the obstacle, the position of the obstacle written as a latitude and longitude, as well as its elevation."
    },
    "AERODROME OPERATIONS AND MAINTENANCE": {
        "color": "Yellow",
        "relevance": "Medium",
        "description": " A NOTAM that reports operational changes or maintenance activities at the aerodrome. It may include closures of aprons, stands, maintenance work on airport facilities and secondary infrastructure (e.g., lighting), changes in the availability of ground handling or fueling services, or the temporary relocation of services.",
    },
    "EMERGENCY SERVICES": {
        "color": "Yellow",
        "relevance": "Medium",
        "description": "A NOTAM in this category will report the operational status of airport rescue and firefighting services (ARFF). A typical message might include downgrading of fire fighting category, temporary unavailability of rescue services or changes in ARFF operating hours.",
    },
    "ADMINISTRATIVE": {
        "color": "Green",
        "relevance": "Low",
        "description": "A NOTAM that regards information outside the operational framework such as updated contact details, hours of service (not for the airport), slot procedures, airport minor services.",
    },
    "RADAR SERVICES": {
        "color": "Yellow",
        "relevance": "Medium",
        "description": "A NOTAM with precise information and updates regarding the radar services of an aerodrome, both primary and secondary surveillance radars.",
    },
    "HAZARDS": {
        "color": "Orange",
        "relevance": "High",
        "description": "A NOTAM of this category will describe dynamic, mobile, or uncontrolled activities posing a risk to the aircraft. Might include drones (UAS), laser interference, aerobatic flights, bird activity, and parachute drops.",
    },
    "MILITARY": {
        "color": "Green",
        "relevance": "Low",
        "description": "Includes NOTAMs starting with [US DOD PROCEDURAL NOTAM] as well as other specific information that only military crews should know.",
    },
}

import math

# Default fallback hospitals dataset centered around sample coordinates
DEFAULT_HOSPITALS = [
    {
        "id": "hosp_1",
        "name": "Apex Super Specialty Hospital",
        "lat": 23.5204,
        "lng": 87.3119,
        "phone": "+91 343 2540001",
        "emergencyBeds": 18,
        "ambulanceAvailable": True,
        "services": ["ICU", "Trauma", "Cardiology", "24/7 Pharmacy"],
        "address": "City Centre, Durgapur, West Bengal"
    },
    {
        "id": "hosp_2",
        "name": "Sanjiban Emergency Care Hospital",
        "lat": 23.5280,
        "lng": 87.3190,
        "phone": "+91 343 2540002",
        "emergencyBeds": 8,
        "ambulanceAvailable": True,
        "services": ["Emergency", "General Medicine", "Pediatrics"],
        "address": "Benachity, Durgapur, West Bengal"
    },
    {
        "id": "hosp_3",
        "name": "Mission Hospital & Trauma Centre",
        "lat": 23.5350,
        "lng": 87.2980,
        "phone": "+91 343 2540003",
        "emergencyBeds": 25,
        "ambulanceAvailable": True,
        "services": ["Neurology", "Burn Unit", "Blood Bank", "Trauma ICU"],
        "address": "Imli Chatti, Durgapur, West Bengal"
    },
    {
        "id": "hosp_4",
        "name": "LifeLine Heart & Medical Institute",
        "lat": 23.5100,
        "lng": 87.3250,
        "phone": "+91 343 2540004",
        "emergencyBeds": 12,
        "ambulanceAvailable": False,
        "services": ["Cardiology", "Diagnostics", "Outpatient"],
        "address": "Bidhannagar, Durgapur, West Bengal"
    }
]

def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Calculates the great circle distance between two points in kilometers.
    """
    R = 6371.0 # Earth radius in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) ** 2 +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return round(R * c, 2)

def get_nearby_hospitals(user_lat: float, user_lng: float, radius_km: float = 25.0):
    """
    Returns hospital list sorted by distance to specified user coordinates.
    """
    result = []
    for hosp in DEFAULT_HOSPITALS:
        dist = haversine_distance(user_lat, user_lng, hosp["lat"], hosp["lng"])
        if dist <= radius_km:
            hosp_copy = hosp.copy()
            hosp_copy["distanceKm"] = dist
            result.append(hosp_copy)
            
    # Sort by nearest distance first
    result.sort(key=lambda x: x["distanceKm"])
    return result

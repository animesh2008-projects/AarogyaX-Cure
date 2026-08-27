from flask import Blueprint, request, jsonify
import math

labs_bp = Blueprint("labs", __name__)

MOCK_LABS = [
    {
        "id": "lab_1",
        "name": "Dr. Lal PathLabs & Diagnostics",
        "category": "Pathology & Blood Testing",
        "lat": 23.5220,
        "lng": 87.3140,
        "address": "City Centre Commercial Plaza, Durgapur, WB",
        "phone": "+91 343 2548888",
        "timing": "7:00 AM - 9:00 PM",
        "homeCollection": True,
        "popularTests": ["Complete Blood Count (CBC)", "Lipid Profile", "Thyroid Profile (T3/T4/TSH)", "HbA1c Diabetes Test"],
        "rating": 4.8
    },
    {
        "id": "lab_2",
        "name": "SRL Diagnostics & Imaging Centre",
        "category": "Radiology & Pathology",
        "lat": 23.5290,
        "lng": 87.3210,
        "address": "Benachity Main Road, Durgapur, WB",
        "phone": "+91 343 2549999",
        "timing": "6:30 AM - 10:00 PM",
        "homeCollection": True,
        "popularTests": ["Blood Glucose", "Liver Function Test (LFT)", "Kidney Function Test (KFT)", "Chest X-Ray"],
        "rating": 4.7
    },
    {
        "id": "lab_3",
        "name": "Apollo Diagnostics & Health Hub",
        "category": "Full Diagnostic Care",
        "lat": 23.5380,
        "lng": 87.3010,
        "address": "Steel Township, Durgapur, WB",
        "phone": "+91 343 2547777",
        "timing": "7:00 AM - 8:30 PM",
        "homeCollection": True,
        "popularTests": ["Full Body Checkup", "Vitamin D3 & B12", "ECG", "Urine Routine"],
        "rating": 4.9
    }
]

def haversine_dist(lat1, lon1, lat2, lon2):
    R = 6371.0
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) ** 2 +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return round(R * c, 1)

@labs_bp.route("/nearby", methods=["GET"])
def get_nearby_labs():
    try:
        user_lat = float(request.args.get("lat", 23.5204))
        user_lng = float(request.args.get("lng", 87.3119))
    except (ValueError, TypeError):
        user_lat, user_lng = 23.5204, 87.3119

    test_type = request.args.get("testType", "").strip().lower()

    results = []
    for lab in MOCK_LABS:
        dist = haversine_dist(user_lat, user_lng, lab["lat"], lab["lng"])
        
        if test_type:
            matches_test = any(test_type in t.lower() for t in lab["popularTests"])
            if not matches_test:
                continue

        lab_copy = lab.copy()
        lab_copy["distanceKm"] = dist
        results.append(lab_copy)

    results.sort(key=lambda x: x["distanceKm"])

    return jsonify({
        "status": "success",
        "count": len(results),
        "userLocation": {"lat": user_lat, "lng": user_lng},
        "labs": results
    })

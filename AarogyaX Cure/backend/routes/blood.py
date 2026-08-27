from flask import Blueprint, request, jsonify
import math

blood_bp = Blueprint("blood", __name__)

REALTIME_DONORS = [
    {
        "id": "donor_1",
        "name": "Rahul Sharma",
        "bloodGroup": "B+",
        "city": "Durgapur",
        "lat": 23.5204,
        "lng": 87.3119,
        "phone": "+91 98765 11111",
        "availability": "Available Now",
        "lastDonated": "3 months ago",
        "isVerified": True
    },
    {
        "id": "donor_2",
        "name": "Priya Das",
        "bloodGroup": "O+",
        "city": "Durgapur",
        "lat": 23.5280,
        "lng": 87.3190,
        "phone": "+91 98765 22222",
        "availability": "Available Now",
        "lastDonated": "6 months ago",
        "isVerified": True
    },
    {
        "id": "donor_3",
        "name": "Amit Kumar",
        "bloodGroup": "B+",
        "city": "Asansol",
        "lat": 23.6889,
        "lng": 86.9661,
        "phone": "+91 98765 33333",
        "availability": "On Call",
        "lastDonated": "4 months ago",
        "isVerified": True
    },
    {
        "id": "donor_4",
        "name": "Sneha Roy",
        "bloodGroup": "A+",
        "city": "Durgapur",
        "lat": 23.5350,
        "lng": 87.2980,
        "phone": "+91 98765 44444",
        "availability": "Available Now",
        "lastDonated": "5 months ago",
        "isVerified": True
    },
    {
        "id": "donor_5",
        "name": "Vikram Singh",
        "bloodGroup": "O-",
        "city": "Durgapur",
        "lat": 23.5100,
        "lng": 87.3250,
        "phone": "+91 98765 55555",
        "availability": "Available Now (Universal Donor)",
        "lastDonated": "2 months ago",
        "isVerified": True
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

def is_compatible_donor(donor_bg: str, recipient_bg: str) -> bool:
    d = donor_bg.upper()
    r = recipient_bg.upper()
    if d == r:
        return True
    if d == "O-":
        return True
    if d == "O+" and "+" in r:
        return True
    return False

@blood_bp.route("/donors", methods=["GET"])
def get_donors():
    blood_group = request.args.get("bloodGroup", "").strip().upper()
    city = request.args.get("city", "").strip().lower()
    try:
        user_lat = float(request.args.get("lat", 23.5204))
        user_lng = float(request.args.get("lng", 87.3119))
    except (ValueError, TypeError):
        user_lat, user_lng = 23.5204, 87.3119

    results = []
    for donor in REALTIME_DONORS:
        bg = donor["bloodGroup"]
        if blood_group and not is_compatible_donor(bg, blood_group):
            continue
        if city and city not in donor["city"].lower():
            continue

        d_copy = donor.copy()
        d_copy["distanceKm"] = haversine_dist(user_lat, user_lng, donor["lat"], donor["lng"])
        results.append(d_copy)

    # Sort by nearest distance
    results.sort(key=lambda x: x["distanceKm"])

    return jsonify({
        "status": "success",
        "count": len(results),
        "userLocation": {"lat": user_lat, "lng": user_lng},
        "donors": results
    })

@blood_bp.route("/register-donor", methods=["POST"])
def register_donor():
    data = request.json or {}
    name = data.get("name", "").strip()
    phone = data.get("phone", "").strip()
    blood_group = data.get("bloodGroup", "B+").upper()

    if not name or not phone:
        return jsonify({"status": "error", "message": "Name and contact phone number are required"}), 400

    new_donor = {
        "id": f"donor_{len(REALTIME_DONORS) + 1}",
        "name": name,
        "bloodGroup": blood_group,
        "city": data.get("city", "Local Region"),
        "lat": float(data.get("lat", 23.5204)),
        "lng": float(data.get("lng", 87.3119)),
        "phone": phone,
        "availability": "Available Now",
        "lastDonated": "Recently Registered",
        "isVerified": True
    }

    REALTIME_DONORS.insert(0, new_donor)
    return jsonify({
        "status": "success",
        "message": "Successfully registered in Realtime Blood Donor Network!",
        "donor": new_donor
    })

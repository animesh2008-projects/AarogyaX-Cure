from flask import Blueprint, request, jsonify
from services.location_service import get_nearby_hospitals
from services.notification_service import dispatch_emergency_sos

emergency_bp = Blueprint("emergency", __name__)

@emergency_bp.route("/sos", methods=["POST"])
def trigger_sos():
    data = request.json or {}
    user_id = data.get("userId", "anonymous")
    lat = float(data.get("latitude", 23.5204))
    lng = float(data.get("longitude", 87.3119))
    contacts = data.get("contacts", [])

    nearby = get_nearby_hospitals(lat, lng, radius_km=30.0)
    nearest = nearby[0] if nearby else None

    dispatch_res = dispatch_emergency_sos(user_id, lat, lng, contacts)

    return jsonify({
        "status": "SOS_DISPATCHED",
        "timestamp": "2026-08-27T10:44:47Z",
        "location": {
            "lat": lat,
            "lng": lng,
            "mapsUrl": f"https://www.google.com/maps?q={lat},{lng}"
        },
        "nearestHospital": nearest,
        "dispatchedAlerts": dispatch_res
    })

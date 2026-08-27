from flask import Blueprint, request, jsonify
from services.location_service import get_nearby_hospitals

hospitals_bp = Blueprint("hospitals", __name__)

@hospitals_bp.route("/nearby", methods=["GET"])
def list_nearby_hospitals():
    try:
        lat = float(request.args.get("lat", 23.5204))
        lng = float(request.args.get("lng", 87.3119))
        radius = float(request.args.get("radius", 30.0))
    except (ValueError, TypeError):
        lat, lng, radius = 23.5204, 87.3119, 30.0

    hospitals = get_nearby_hospitals(lat, lng, radius)
    return jsonify({
        "status": "success",
        "userLocation": {"lat": lat, "lng": lng},
        "count": len(hospitals),
        "hospitals": hospitals
    })

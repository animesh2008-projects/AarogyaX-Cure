from flask import Blueprint, request, jsonify
from services.gemini_service import generate_health_guidance

assistant_bp = Blueprint("assistant", __name__)

@assistant_bp.route("/chat", methods=["POST"])
def assistant_chat():
    data = request.json or {}
    message = data.get("message", "").strip()
    user_context = data.get("context", "")

    if not message:
        return jsonify({"status": "error", "message": "Message content cannot be empty"}), 400

    guidance = generate_health_guidance(message, context=user_context)
    return jsonify({
        "status": "success",
        "message": message,
        "guidance": guidance,
        "disclaimer": "Guidance provided is for educational purposes only and does not replace medical advice."
    })

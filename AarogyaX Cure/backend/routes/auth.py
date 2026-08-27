from flask import Blueprint, request, jsonify

auth_bp = Blueprint("auth", __name__)

USERS_DB = {
    "animesh@aarogyax.org": {
        "uid": "usr_animesh_2026",
        "role": "patient",
        "name": "Animesh Karmakar",
        "email": "animesh@aarogyax.org",
        "phone": "+91 98765 43210",
        "bloodGroup": "B+",
        "emergencyContacts": [
          { "name": "Mom", "relation": "Parent", "phone": "+91 91234 56789" },
          { "name": "Dad", "relation": "Parent", "phone": "+91 91234 56788" }
        ],
        "allergies": "Dust, Penicillin",
        "medications": "Paracetamol 500mg"
    },
    "doctor@aarogyax.org": {
        "uid": "doc_sk_roy_2026",
        "role": "doctor",
        "name": "Dr. S. K. Roy, MD",
        "specialty": "Senior Cardiologist & Internal Medicine",
        "hospitalName": "Apex Super Specialty Hospital",
        "licenseNo": "MCI-2018-94821",
        "email": "doctor@aarogyax.org",
        "phone": "+91 98765 77777",
        "activePatients": 12,
        "consultationsToday": 5
    },
    "hospital@aarogyax.org": {
        "uid": "hosp_apex_2026",
        "role": "hospital",
        "name": "Apex Hospital Administration",
        "hospitalName": "Apex Super Specialty Hospital",
        "email": "hospital@aarogyax.org",
        "phone": "+91 343 2540001",
        "emergencyBeds": 18,
        "totalBeds": 150,
        "ambulancesAvailable": 4,
        "address": "City Centre, Durgapur, WB"
    }
}

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json or {}
    email = data.get("email", "").strip().lower()
    password = data.get("password", "")
    role = data.get("role", "patient")

    if not email or not password:
        return jsonify({"status": "error", "message": "Email and password required"}), 400

    user = USERS_DB.get(email)
    if user:
        return jsonify({
            "status": "success",
            "message": f"{role.capitalize()} login successful",
            "token": f"token_{user['uid']}",
            "role": user.get("role", role),
            "user": user
        })
    else:
        new_user = {
            "uid": f"usr_{len(USERS_DB) + 1}",
            "role": role,
            "name": email.split("@")[0].capitalize(),
            "email": email,
            "phone": "+91 98765 00000",
            "bloodGroup": "O+"
        }
        USERS_DB[email] = new_user
        return jsonify({
            "status": "success",
            "message": "Account created and logged in",
            "token": f"token_{new_user['uid']}",
            "role": role,
            "user": new_user
        })

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json or {}
    role = data.get("role", "patient").lower()
    email = data.get("email", "").strip().lower()
    name = data.get("name", "").strip()
    phone = data.get("phone", "").strip()

    if not email or not name:
        return jsonify({"status": "error", "message": "Name and email are required."}), 400

    new_id = f"{role[:3]}_{len(USERS_DB) + 1}_{Date.now() if 'Date' in globals() else 100}"
    
    new_account = {
        "uid": new_id,
        "role": role,
        "name": name,
        "email": email,
        "phone": phone
    }

    if role == "doctor":
        new_account.update({
            "specialty": data.get("specialty", "General Medicine"),
            "licenseNo": data.get("licenseNo", "MCI-2026-REG"),
            "hospitalName": data.get("hospitalName", "Regional Hospital")
        })
    elif role == "hospital":
        new_account.update({
            "hospitalName": name,
            "emergencyBeds": int(data.get("emergencyBeds", 10)),
            "totalBeds": int(data.get("totalBeds", 100)),
            "ambulancesAvailable": int(data.get("ambulancesAvailable", 2)),
            "address": data.get("address", "Local City")
        })
    else:
        new_account.update({
            "bloodGroup": data.get("bloodGroup", "B+"),
            "emergencyContacts": data.get("emergencyContacts", [])
        })

    USERS_DB[email] = new_account

    return jsonify({
        "status": "success",
        "message": f"Successfully registered new {role.capitalize()} profile!",
        "token": f"token_{new_id}",
        "role": role,
        "user": new_account
    })

@auth_bp.route("/demo-login", methods=["POST"])
def demo_login():
    data = request.json or {}
    role = data.get("role", "patient")

    if role == "doctor":
        user = USERS_DB["doctor@aarogyax.org"]
    elif role == "hospital":
        user = USERS_DB["hospital@aarogyax.org"]
    else:
        user = USERS_DB["animesh@aarogyax.org"]

    return jsonify({
        "status": "success",
        "message": f"Demo {role} session activated",
        "token": f"demo_{role}_token_2026",
        "role": role,
        "user": user
    })

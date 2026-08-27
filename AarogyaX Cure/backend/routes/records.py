from flask import Blueprint, request, jsonify

records_bp = Blueprint("records", __name__)

MOCK_RECORDS = [
    {
        "id": "rec_1",
        "title": "Complete Blood Count (CBC) Report",
        "category": "Blood Test",
        "date": "2026-08-15",
        "description": "Hemoglobin: 14.2 g/dL, Platelets: 250,000 /uL. All markers within normal reference range.",
        "doctor": "Dr. S. K. Roy",
        "fileUrl": "#"
    },
    {
        "id": "rec_2",
        "title": "General Health Prescription",
        "category": "Prescription",
        "date": "2026-07-20",
        "description": "Rx: Paracetamol 500mg BD x 3 days, Vitamin C 500mg OD x 10 days.",
        "doctor": "Dr. A. Banerjee",
        "fileUrl": "#"
    },
    {
        "id": "rec_3",
        "title": "COVID-19 Vaccination Certificate",
        "category": "Vaccination",
        "date": "2024-05-10",
        "description": "Precaution Dose (Covaxin) administered successfully.",
        "doctor": "City Health Department",
        "fileUrl": "#"
    }
]

@records_bp.route("/", methods=["GET"])
def get_records():
    category = request.args.get("category", "").strip().lower()
    filtered = MOCK_RECORDS
    if category and category != "all":
        filtered = [r for r in filtered if category in r["category"].lower()]
    
    return jsonify({
        "status": "success",
        "count": len(filtered),
        "records": filtered
    })

@records_bp.route("/add", methods=["POST"])
def add_record():
    data = request.json or {}
    new_rec = {
        "id": f"rec_{len(MOCK_RECORDS) + 1}",
        "title": data.get("title", "Medical Report"),
        "category": data.get("category", "General"),
        "date": data.get("date", "2026-08-27"),
        "description": data.get("description", "No additional notes."),
        "doctor": data.get("doctor", "Consultant Physician"),
        "fileUrl": "#"
    }
    MOCK_RECORDS.append(new_rec)
    return jsonify({
        "status": "success",
        "message": "Health record added successfully",
        "record": new_rec
    })

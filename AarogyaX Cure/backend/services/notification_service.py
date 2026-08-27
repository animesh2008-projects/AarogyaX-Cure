import logging

logger = logging.getLogger(__name__)

def dispatch_emergency_sos(user_id: str, lat: float, lng: float, contacts: list) -> dict:
    """
    Simulates sending instant SMS/Push notification alerts to user emergency contacts.
    """
    location_url = f"https://www.google.com/maps?q={lat},{lng}"
    dispatched_count = 0
    details = []

    for contact in contacts:
        contact_name = contact.get("name", "Emergency Contact")
        phone = contact.get("phone", "")
        message = f"🚨 EMERGENCY ALERT from AarogyaX User! Current GPS Location: {location_url}"
        
        logger.info(f"Simulating SOS Dispatch -> {contact_name} ({phone}): {message}")
        dispatched_count += 1
        details.append({
            "contactName": contact_name,
            "phone": phone,
            "status": "SENT_SIMULATED",
            "message": message
        })

    return {
        "userId": user_id,
        "dispatchedCount": dispatched_count,
        "locationUrl": location_url,
        "details": details
    }

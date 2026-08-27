import os
import logging
from google import genai
from google.genai import types

logger = logging.getLogger(__name__)

SYSTEM_MEDICAL_DISCLAIMER = (
    "You are the AarogyaX Health Assistant, an empathetic, highly knowledgeable AI first-aid and health guidance system. "
    "Your goal is to provide clear, practical educational information, general health advice, and first-aid steps. "
    "IMPORTANT SAFETY RULES: "
    "1. NEVER state that you are a doctor or provide formal medical diagnoses. "
    "2. Always emphasize that this information is educational guidance. "
    "3. Structure your response with clear headings, bullet points, and practical first-aid / lifestyle steps. "
    "4. End with a bold safety reminder: 'Disclaimer: This guidance is for educational purposes only. Always consult a qualified physician or healthcare provider for medical emergencies or formal diagnosis.'"
)

def generate_health_guidance(prompt: str, context: str = "") -> str:
    """
    Generates health guidance using Google GenAI SDK with Gemini 3.7 Flash model.
    Falls back gracefully if API key is missing or fails.
    """
    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    if not api_key:
        logger.warning("GEMINI_API_KEY not found in environment. Returning structured fallback guidance.")
        return format_fallback_guidance(prompt)

    try:
        client = genai.Client(api_key=api_key)
        full_content = prompt
        if context:
            full_content = f"User Profile Context: {context}\n\nUser Question: {prompt}"

        response = client.models.generate_content(
            model="gemini-3.7-flash",
            contents=full_content,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_MEDICAL_DISCLAIMER,
                temperature=0.3,
                max_output_tokens=1024
            )
        )
        if response and response.text:
            return response.text
        return format_fallback_guidance(prompt)

    except Exception as e:
        logger.error(f"Gemini API invocation failed: {e}")
        return format_fallback_guidance(prompt)

def format_fallback_guidance(prompt: str) -> str:
    """
    Simulated AI response when Gemini API is offline or unconfigured.
    """
    prompt_lower = prompt.lower()
    
    if "headache" in prompt_lower or "fever" in prompt_lower:
        return (
            "### First-Aid & General Health Guidance\n"
            "• **Rest & Environment**: Move to a quiet, dimly lit room and avoid screen exposure.\n"
            "• **Hydration**: Drink plenty of water or electrolyte fluids to avoid dehydration-induced headaches.\n"
            "• **Cool Compress**: Place a cold, damp cloth over your forehead or temple for 10-15 minutes.\n"
            "• **Monitoring**: Keep track of your body temperature and symptom duration.\n\n"
            "**Disclaimer**: This guidance is for educational purposes only. Always consult a qualified physician or call emergency services if symptoms worsen severely."
        )
    elif "sprain" in prompt_lower or "injury" in prompt_lower or "pain" in prompt_lower:
        return (
            "### Acute Injury Guidance (R.I.C.E Protocol)\n"
            "• **Rest**: Protect the injured area and avoid putting weight on it.\n"
            "• **Ice**: Apply an ice pack wrapped in a cloth for 15-20 minutes every 2 hours.\n"
            "• **Compress**: Lightly wrap with an elastic bandage to minimize swelling.\n"
            "• **Elevate**: Keep the injured limb elevated above heart level when resting.\n\n"
            "**Disclaimer**: This guidance is for educational purposes only. If you experience severe swelling, visible deformity, or immediate inability to move the limb, seek urgent emergency medical evaluation."
        )
    else:
        return (
            "### General Health & Wellness Advice\n"
            "• **Hydration & Nutrition**: Maintain adequate fluid intake and balanced meals.\n"
            "• **Rest**: Ensure 7-8 hours of uninterrupted sleep for physiological recovery.\n"
            "• **Symptom Log**: Note when symptoms started and any triggering factors.\n\n"
            "**Disclaimer**: This guidance is for educational purposes only. Consult a healthcare professional for customized medical advice."
        )

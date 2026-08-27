"""
==========================================================================
AAROGYAX CURE - BACKEND API UNIT & INTEGRATION TEST SUITE
==========================================================================
"""

import unittest
import json
import os
import sys

# Add backend directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from app import app

class AarogyaXCureTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_01_health_check(self):
        """Test health check endpoint"""
        response = self.client.get('/api/health')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data.get('status'), 'healthy')
        self.assertEqual(data.get('service'), 'AarogyaX Cure Backend')

    def test_02_patient_login(self):
        """Test Patient multi-role login"""
        payload = {
            "email": "animesh@aarogyax.org",
            "password": "demo12345",
            "role": "patient"
        }
        response = self.client.post('/api/auth/login', json=payload)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data.get('status'), 'success')
        self.assertEqual(data.get('role'), 'patient')

    def test_03_doctor_login(self):
        """Test Doctor multi-role login"""
        payload = {
            "email": "doctor@aarogyax.org",
            "password": "demo12345",
            "role": "doctor"
        }
        response = self.client.post('/api/auth/login', json=payload)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data.get('status'), 'success')
        self.assertEqual(data.get('role'), 'doctor')
        self.assertIn('Dr.', data.get('user', {}).get('name', ''))

    def test_04_hospital_login(self):
        """Test Hospital Admin multi-role login"""
        payload = {
            "email": "hospital@aarogyax.org",
            "password": "demo12345",
            "role": "hospital"
        }
        response = self.client.post('/api/auth/login', json=payload)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data.get('status'), 'success')
        self.assertEqual(data.get('role'), 'hospital')

    def test_05_doctor_registration(self):
        """Test creating a new Doctor account"""
        payload = {
            "role": "doctor",
            "name": "Dr. A. Banerjee",
            "email": "banerjee@aarogyax.org",
            "phone": "+91 98765 88888",
            "specialty": "Neurology",
            "licenseNo": "MCI-2026-TEST"
        }
        response = self.client.post('/api/auth/register', json=payload)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data.get('status'), 'success')
        self.assertEqual(data.get('role'), 'doctor')

    def test_06_nearby_hospitals(self):
        """Test nearby hospital lookup"""
        response = self.client.get('/api/hospitals/nearby?lat=23.5204&lng=87.3119')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data.get('status'), 'success')
        self.assertGreater(len(data.get('hospitals', [])), 0)

    def test_07_blood_donors_and_registration(self):
        """Test blood donor lookup and new donor registration"""
        # Fetch donors
        response = self.client.get('/api/blood/donors?bloodGroup=B+&lat=23.5204&lng=87.3119')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data.get('status'), 'success')

        # Register donor
        donor_payload = {
            "name": "Test Donor",
            "phone": "+91 99999 88888",
            "bloodGroup": "O-",
            "city": "Durgapur",
            "lat": 23.5204,
            "lng": 87.3119
        }
        reg_resp = self.client.post('/api/blood/register-donor', json=donor_payload)
        self.assertEqual(reg_resp.status_code, 200)
        reg_data = json.loads(reg_resp.data)
        self.assertEqual(reg_data.get('status'), 'success')

    def test_08_diagnostic_labs(self):
        """Test nearby diagnostic laboratories lookup"""
        response = self.client.get('/api/labs/nearby?lat=23.5204&lng=87.3119')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data.get('status'), 'success')
        self.assertGreater(len(data.get('labs', [])), 0)

    def test_09_emergency_sos_dispatch(self):
        """Test Emergency SOS alert broadcast"""
        payload = {
            "userId": "usr_test_123",
            "latitude": 23.5204,
            "longitude": 87.3119,
            "contacts": [{"name": "Mom", "phone": "+91 91234 56789"}]
        }
        response = self.client.post('/api/emergency/sos', json=payload)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn(data.get('status'), ['success', 'SOS_DISPATCHED'])

    def test_10_ai_assistant_chat(self):
        """Test Gemini AI Assistant chat route"""
        payload = {
            "message": "What is first-aid for a mild fever?"
        }
        response = self.client.post('/api/assistant/chat', json=payload)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data.get('status'), 'success')
        self.assertTrue('guidance' in data or 'reply' in data)

if __name__ == '__main__':
    print("\n--- Running AarogyaX Cure Backend Test Suite ---")
    unittest.main()

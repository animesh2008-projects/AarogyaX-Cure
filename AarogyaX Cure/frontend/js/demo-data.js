/* ==========================================================================
   AAROGYAX CURE - DEMO DATA & OFFLINE PERSISTENCE ENGINE (UP TO 5 CONTACTS)
   ========================================================================== */

window.DemoEngine = {
  isDemoMode: true,
  
  currentUser: {
    uid: "usr_animesh_2026",
    name: "Animesh Karmakar",
    email: "animesh@aarogyax.org",
    phone: "+91 98765 43210",
    bloodGroup: "B+",
    emergencyContacts: [
      { name: "Mom", relation: "Parent", phone: "+91 91234 56789" },
      { name: "Dad", relation: "Parent", phone: "+91 91234 56788" },
      { name: "Rahul Sharma", relation: "Friend", phone: "+91 98765 11111" }
    ],
    allergies: "Dust, Penicillin",
    medications: "Paracetamol 500mg, Vitamin C"
  },

  hospitals: [
    {
      id: "hosp_1",
      name: "Apex Super Specialty Hospital",
      lat: 23.5204,
      lng: 87.3119,
      phone: "+91 343 2540001",
      emergencyBeds: 18,
      ambulanceAvailable: true,
      services: ["ICU", "Trauma", "Cardiology", "24/7 Pharmacy"],
      address: "City Centre, Durgapur, WB",
      distanceKm: 1.2
    },
    {
      id: "hosp_2",
      name: "Sanjiban Emergency Care Hospital",
      lat: 23.5280,
      lng: 87.3190,
      phone: "+91 343 2540002",
      emergencyBeds: 8,
      ambulanceAvailable: true,
      services: ["Emergency", "General Medicine", "Pediatrics"],
      address: "Benachity, Durgapur, WB",
      distanceKm: 2.4
    },
    {
      id: "hosp_3",
      name: "Mission Hospital & Trauma Centre",
      lat: 23.5350,
      lng: 87.2980,
      phone: "+91 343 2540003",
      emergencyBeds: 25,
      ambulanceAvailable: true,
      services: ["Neurology", "Burn Unit", "Blood Bank", "Trauma ICU"],
      address: "Imli Chatti, Durgapur, WB",
      distanceKm: 3.8
    }
  ],

  donors: [
    {
      id: "donor_1",
      name: "Rahul Sharma",
      bloodGroup: "B+",
      city: "Durgapur",
      phone: "+91 98765 11111",
      availability: "Available Now",
      lastDonated: "3 months ago"
    },
    {
      id: "donor_2",
      name: "Priya Das",
      bloodGroup: "O+",
      city: "Durgapur",
      phone: "+91 98765 22222",
      availability: "Available Now",
      lastDonated: "6 months ago"
    },
    {
      id: "donor_3",
      name: "Amit Kumar",
      bloodGroup: "B+",
      city: "Asansol",
      phone: "+91 98765 33333",
      availability: "On Call",
      lastDonated: "4 months ago"
    },
    {
      id: "donor_4",
      name: "Sneha Roy",
      bloodGroup: "A+",
      city: "Durgapur",
      phone: "+91 98765 44444",
      availability: "Available Now",
      lastDonated: "5 months ago"
    }
  ],

  getStoredUser() {
    const saved = localStorage.getItem("aarogyax_user");
    if (saved) {
      try { return JSON.parse(saved); } catch(e) {}
    }
    return this.currentUser;
  },

  saveUser(userObj) {
    // Enforce max 5 emergency contacts limit
    if (userObj.emergencyContacts && userObj.emergencyContacts.length > 5) {
      userObj.emergencyContacts = userObj.emergencyContacts.slice(0, 5);
    }
    this.currentUser = { ...this.currentUser, ...userObj };
    localStorage.setItem("aarogyax_user", JSON.stringify(this.currentUser));
  },

  getStoredRecords() {
    const saved = localStorage.getItem("aarogyax_records");
    if (saved) {
      try { return JSON.parse(saved); } catch(e) {}
    }
    return [
      {
        id: "rec_1",
        title: "Complete Blood Count (CBC) Report",
        category: "Blood Test",
        date: "2026-08-15",
        description: "Hemoglobin: 14.2 g/dL, Platelets: 250,000 /uL. All markers within normal reference range.",
        doctor: "Dr. S. K. Roy",
        fileUrl: "#"
      },
      {
        id: "rec_2",
        title: "General Health Prescription",
        category: "Prescription",
        date: "2026-07-20",
        description: "Rx: Paracetamol 500mg BD x 3 days, Vitamin C 500mg OD x 10 days.",
        doctor: "Dr. A. Banerjee",
        fileUrl: "#"
      }
    ];
  },

  saveRecords(recordsArray) {
    localStorage.setItem("aarogyax_records", JSON.stringify(recordsArray));
  },

  getStoredReminders() {
    const saved = localStorage.getItem("aarogyax_reminders");
    if (saved) {
      try { return JSON.parse(saved); } catch(e) {}
    }
    return [
      {
        id: "rem_1",
        medicine: "Paracetamol",
        dosage: "500mg",
        time: "20:00",
        frequency: "Daily",
        status: "Pending"
      },
      {
        id: "rem_2",
        medicine: "Vitamin C",
        dosage: "500mg",
        time: "09:00",
        frequency: "Daily",
        status: "Taken"
      }
    ];
  },

  saveReminders(remindersArray) {
    localStorage.setItem("aarogyax_reminders", JSON.stringify(remindersArray));
  }
};

/* ==========================================================================
   DIGITAL HEALTH CARD CONTROLLER (UP TO 5 CONTACTS SUPPORT)
   ========================================================================== */

document.addEventListener("DOMContentLoaded", () => {
  const user = window.DemoEngine ? window.DemoEngine.getStoredUser() : null;

  if (user) {
    const cardName = document.getElementById("cardName");
    const cardBlood = document.getElementById("cardBlood");
    const cardEmergencyContactsList = document.getElementById("cardEmergencyContactsList");
    const cardAllergies = document.getElementById("cardAllergies");
    const qrCodeImg = document.getElementById("qrCodeImg");

    if (cardName) cardName.textContent = user.name;
    if (cardBlood) cardBlood.textContent = user.bloodGroup || "B+";
    if (cardAllergies) cardAllergies.textContent = user.allergies || "None reported";

    const contacts = user.emergencyContacts || [];
    if (cardEmergencyContactsList) {
      if (contacts.length === 0) {
        cardEmergencyContactsList.innerHTML = `<span style="color:var(--text-muted);">No contacts configured</span>`;
      } else {
        cardEmergencyContactsList.innerHTML = contacts.slice(0, 5).map((c, idx) => `
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <span><strong>${idx + 1}. ${c.name}</strong> (${c.relation || 'Contact'}):</span>
            <span style="color:var(--brand-emerald); font-weight:600;">${c.phone}</span>
          </div>
        `).join('');
      }
    }

    if (qrCodeImg) {
      const contactsStr = contacts.slice(0, 5).map(c => `${c.name}:${c.phone}`).join(', ');
      const qrData = encodeURIComponent(`AarogyaX Card: ${user.name} | Blood: ${user.bloodGroup} | Emergency Contacts: ${contactsStr}`);
      qrCodeImg.src = `https://api.qrserver.com/v1/create-qr-code/?size=90x90&data=${qrData}`;
    }
  }
});

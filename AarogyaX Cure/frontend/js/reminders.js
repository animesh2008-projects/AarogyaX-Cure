/* ==========================================================================
   MEDICINE REMINDERS CONTROLLER
   ========================================================================== */

document.addEventListener("DOMContentLoaded", () => {
  const addMedBtn = document.getElementById("addMedBtn");
  const addMedCard = document.getElementById("addMedCard");
  const medForm = document.getElementById("medForm");
  const remindersGrid = document.getElementById("remindersGrid");

  let currentReminders = window.DemoEngine ? window.DemoEngine.getStoredReminders() : [];

  // Request Web Notifications permission
  if ("Notification" in window && Notification.permission !== "granted" && Notification.permission !== "denied") {
    Notification.requestPermission();
  }

  function renderReminders(list) {
    if (!remindersGrid) return;
    if (list.length === 0) {
      remindersGrid.innerHTML = `
        <div style="grid-column: 1 / -1; text-align: center; padding: 3rem; background: white; border-radius: var(--radius-lg);">
          <h3>No medicine reminders scheduled</h3>
          <p style="color: var(--text-muted);">Click '+ Add New Reminder' to schedule your daily dosage.</p>
        </div>
      `;
      return;
    }

    remindersGrid.innerHTML = list.map(r => `
      <div class="feature-card">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.75rem;">
          <div class="card-icon" style="background: rgba(13, 148, 136, 0.1); color: var(--brand-teal);">💊</div>
          <span class="status-badge ${r.status === 'Taken' ? 'live' : 'demo'}">
            ${r.status === 'Taken' ? '✓ Taken' : '⏰ Scheduled'}
          </span>
        </div>
        <h3 class="card-title">${r.medicine} (${r.dosage})</h3>
        <p class="card-desc">Scheduled Time: <strong>${r.time}</strong> &bull; Frequency: ${r.frequency}</p>
        <button class="btn ${r.status === 'Taken' ? 'btn-outline' : 'btn-primary'}" onclick="toggleTaken('${r.id}')" style="width: 100%;">
          ${r.status === 'Taken' ? 'Mark as Pending' : '✓ Mark as Taken'}
        </button>
      </div>
    `).join('');
  }

  window.toggleTaken = function(id) {
    const item = currentReminders.find(r => r.id === id);
    if (item) {
      item.status = item.status === 'Taken' ? 'Pending' : 'Taken';
      if (window.DemoEngine) window.DemoEngine.saveReminders(currentReminders);
      renderReminders(currentReminders);

      if (item.status === 'Taken' && "Notification" in window && Notification.permission === "granted") {
        new Notification("Medication Tracked!", {
          body: `Great job! You logged ${item.medicine} (${item.dosage}) as taken.`,
          icon: "https://img.icons8.com/emoji/96/pill-emoji.png"
        });
      }
    }
  };

  renderReminders(currentReminders);

  if (addMedBtn && addMedCard) {
    addMedBtn.addEventListener("click", () => {
      addMedCard.style.display = addMedCard.style.display === "none" ? "block" : "none";
    });
  }

  if (medForm) {
    medForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const medicine = document.getElementById("medName").value.trim();
      const dosage = document.getElementById("medDosage").value.trim();
      const time = document.getElementById("medTime").value;
      const frequency = document.getElementById("medFreq").value;

      const newRem = {
        id: "rem_" + Date.now(),
        medicine,
        dosage,
        time,
        frequency,
        status: "Pending"
      };

      currentReminders.unshift(newRem);
      if (window.DemoEngine) window.DemoEngine.saveReminders(currentReminders);
      renderReminders(currentReminders);
      
      medForm.reset();
      addMedCard.style.display = "none";
      alert("Medication reminder added successfully!");
    });
  }
});

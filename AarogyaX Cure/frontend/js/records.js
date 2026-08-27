/* ==========================================================================
   HEALTH RECORDS CONTROLLER
   ========================================================================== */

document.addEventListener("DOMContentLoaded", () => {
  const addRecordBtn = document.getElementById("addRecordBtn");
  const addRecordCard = document.getElementById("addRecordCard");
  const recordForm = document.getElementById("recordForm");
  const recordsGrid = document.getElementById("recordsGrid");

  let currentRecords = window.DemoEngine ? window.DemoEngine.getStoredRecords() : [];

  function renderRecords(records) {
    if (!recordsGrid) return;
    if (records.length === 0) {
      recordsGrid.innerHTML = `
        <div style="grid-column: 1 / -1; text-align: center; padding: 3rem; background: white; border-radius: var(--radius-lg);">
          <h3>No health records found</h3>
          <p style="color: var(--text-muted);">Click '+ Add New Health Record' to log prescriptions or lab reports.</p>
        </div>
      `;
      return;
    }

    recordsGrid.innerHTML = records.map(r => `
      <div class="feature-card">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.75rem;">
          <div class="card-icon" style="background: rgba(13, 148, 136, 0.1); color: var(--brand-teal);">📄</div>
          <span class="status-badge" style="background: #f1f5f9; color: var(--primary-dark); font-weight: 700;">
            ${r.category}
          </span>
        </div>
        <h3 class="card-title">${r.title}</h3>
        <p class="card-desc">${r.description}</p>
        <div style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 1rem;">
          Date: <strong>${r.date}</strong> &bull; Physician: <strong>${r.doctor || 'Dr. Consult'}</strong>
        </div>
        <button class="btn btn-outline" onclick="alert('Viewing encrypted report document details...')" style="width: 100%; border-color: var(--brand-emerald); color: var(--brand-emerald);">
          👁️ View Encrypted Document
        </button>
      </div>
    `).join('');
  }

  renderRecords(currentRecords);

  if (addRecordBtn && addRecordCard) {
    addRecordBtn.addEventListener("click", () => {
      addRecordCard.style.display = addRecordCard.style.display === "none" ? "block" : "none";
    });
  }

  if (recordForm) {
    recordForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const title = document.getElementById("recTitle").value.trim();
      const category = document.getElementById("recCategory").value;
      const description = document.getElementById("recDesc").value.trim();

      const newRec = {
        id: "rec_" + Date.now(),
        title,
        category,
        date: new Date().toISOString().split("T")[0],
        description: description || "No notes provided.",
        doctor: "Dr. Self Logged",
        fileUrl: "#"
      };

      currentRecords.unshift(newRec);
      if (window.DemoEngine) window.DemoEngine.saveRecords(currentRecords);
      renderRecords(currentRecords);
      
      recordForm.reset();
      addRecordCard.style.display = "none";
      alert("Medical Record saved to your profile!");
    });
  }
});

/* ==========================================================================
   FIREBASE CONFIGURATION & INITIALIZATION (Project: data-d3a3e)
   ========================================================================== */

const firebaseConfig = {
  apiKey: "AIzaSyAJkK1MQHDJ7Jf3mmwJ5vn-etKqmQmaTpw",
  authDomain: "data-d3a3e.firebaseapp.com",
  projectId: "data-d3a3e",
  storageBucket: "data-d3a3e.firebasestorage.app",
  messagingSenderId: "214468155859",
  appId: "1:214468155859:web:43a59e9006ba11c91d7726",
  measurementId: "G-XDNNX6Q0LQ"
};

// Initialize Firebase if Compat SDK loaded
if (typeof firebase !== 'undefined') {
  if (!firebase.apps.length) {
    firebase.initializeApp(firebaseConfig);
    console.log("🔥 Firebase project 'data-d3a3e' initialized successfully!");
  }
}

// Global Auth & Firestore instances
window.getFirebaseAuth = function() {
  if (typeof firebase !== 'undefined' && firebase.auth) {
    return firebase.auth();
  }
  return null;
};

window.getFirebaseFirestore = function() {
  if (typeof firebase !== 'undefined' && firebase.firestore) {
    return firebase.firestore();
  }
  return null;
};

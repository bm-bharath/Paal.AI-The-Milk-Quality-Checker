import { initializeApp } from "firebase/app";
import { getDatabase, ref, onValue } from "firebase/database";

const firebaseConfig = {
  apiKey: "AIzaSyD_WfCyrrRTzQhFCA01fOED2N1GzJoexIU",
  authDomain: "milk-quality-monitoring.firebaseapp.com",
  databaseURL: "https://milk-quality-monitoring-default-rtdb.firebaseio.com",
  projectId: "milk-quality-monitoring",
  storageBucket: "milk-quality-monitoring.firebasestorage.app",
  messagingSenderId: "459049288615",
  appId: "1:459049288615:web:ede888e96e2edfaa786c82",
  measurementId: "G-JYTJTER15N"
};

const app = initializeApp(firebaseConfig);
const database = getDatabase(app);
export { database, ref, onValue };


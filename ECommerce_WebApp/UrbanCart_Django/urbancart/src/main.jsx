// src/main.jsx
import React from "react";
import ReactDOM from "react-dom/client";
import "./input.css";   // This imports Tailwind

// Mount any React component into a Django template element
// Example: if your template has <div id="react-root"></div>
const rootEl = document.getElementById("react-root");
if (rootEl) {
  ReactDOM.createRoot(rootEl).render(
    <React.StrictMode>
      <div className="text-primary-container font-heading">
        React is working!
      </div>
    </React.StrictMode>
  );
}
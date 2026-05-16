// vite.config.js
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import path from "path";

export default defineConfig({
  plugins: [react()],
  root: "src",                        // Vite looks inside src/
  build: {
    outDir: path.resolve(__dirname, "static/dist"),  // output → static/dist/
    emptyOutDir: true,
    rollupOptions: {
      input: {
        main: path.resolve(__dirname, "src/main.jsx"),  // React entry
        styles: path.resolve(__dirname, "src/input.css"), // Tailwind entry
      },
      output: {
        entryFileNames: "[name].js",
        chunkFileNames: "[name].js",
        assetFileNames: "[name].[ext]"
      }
    },
  },
  server: {
    origin: "http://localhost:5173",  // for dev server
  },
});
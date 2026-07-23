# TaskForge Dashboard

A fully interactive React + Tailwind CSS implementation of the TaskForge dashboard and tasks-list designs (built from the uploaded Stitch mockups), including working light/dark mode, task CRUD, filtering, sorting, and pagination.

## Stack

- **React 18** + **React Router v6** (client-side routing between `/` and `/tasks`)
- **Vite** for dev server / build tooling
- **Tailwind CSS v3**, configured with the full "Vibrant Productivity" Material 3 color system from the design docs (light + dark, driven by CSS variables so `dark:` variants aren't needed anywhere — just toggle the `.dark` class)
- Plain JavaScript (JSX), no TypeScript — easy to convert later if you want types
- Google's **Material Symbols Outlined** icon font (loaded via `index.html`, matching the original mockups exactly)

No backend — task data lives in React state (`TaskContext`), seeded with realistic sample tasks. Swap `TaskContext.jsx` for real API calls whenever you wire up a backend.

## Getting started

```bash
npm install
npm run dev
```

Then open the printed local URL (usually `http://localhost:5173`).

```bash
npm run build     # production build -> dist/
npm run preview   # preview the production build locally
```

## Project structure

```
src/
  main.jsx                  # entry point, wraps App in providers
  App.jsx                   # layout shell + routes
  index.css                 # Tailwind directives + design-token CSS variables

  context/
    ThemeContext.jsx         # light/dark mode, persisted to localStorage
    TaskContext.jsx          # task CRUD + derived stats
    UIContext.jsx            # controls the shared create/edit modal

  data/
    seedTasks.js             # sample tasks (dates generated relative to "today")

  lib/
    taskUtils.js              # color/label/date helpers shared by every component

  components/
    Icon.jsx                  # Material Symbols wrapper
    TaskCard.jsx               # dashboard task card
    TaskTable.jsx               # sortable/paginated table (Tasks List page)
    TaskFormModal.jsx            # shared create/edit modal
    NewTaskForm.jsx               # dashboard's lightweight inline quick-add
    CompletionGauge.jsx            # animated "Finish Probability" SVG gauge
    StatsCards.jsx                  # Tasks List summary cards
    layout/
      TopNav.jsx, SideNav.jsx, MobileBottomNav.jsx

  pages/
    Dashboard.jsx
    TasksList.jsx
```

## Notable interactive behavior

- **Theme toggle** (moon/sun icon in the top bar) flips the `dark` class on `<html>` and persists the choice; an inline script in `index.html` applies the saved theme before React mounts, so there's no flash of the wrong theme.
- **Create a task** from the dashboard's inline form (title + priority + category), the "New Task" button in the sidebar/mobile FAB, or "Create New Task" on the Tasks List page — all write to the same `TaskContext`, so every view stays in sync.
- **Edit / delete / mark complete** from the task cards (dashboard) or the table row actions (Tasks List).
- **Finish Probability gauge** is computed live from your current task mix (a simple weighted heuristic in `lib/taskUtils.js` — tune `computeCompletionProbability` if you want different weighting once real data/logic is available).
- **Tasks List** supports free-text search, status/priority filters, click-to-sort columns, and pagination (6 rows/page).

## Customizing the design tokens

Every color from both DESIGN.md files (light + dark) is defined as an RGB-triplet CSS variable in `src/index.css` (`:root` for light, `.dark` for dark) and mapped in `tailwind.config.js`, so utilities like `bg-primary`, `text-on-surface-variant`, `border-outline-variant/20` all work with opacity modifiers. To adjust the palette, edit the variables in `index.css` — you won't need to touch component files.

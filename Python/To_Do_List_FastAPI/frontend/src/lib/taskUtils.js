// Central place for the small bits of "design logic" that map task data
// onto the Vibrant Productivity color tokens, so every component stays
// visually consistent without repeating conditionals everywhere.

export const PRIORITIES = ['Low', 'Medium', 'High', 'Critical']
export const CATEGORIES = ['Work', 'Personal', 'Health', 'Learning']
export const STATUSES = ['Pending', 'Due', 'Failed', 'Urgent', 'Completed']

// Chip used for a task's category on dashboard cards.
export const categoryChipStyles = {
  Work: 'bg-primary-fixed text-primary',
  Personal: 'bg-secondary-fixed text-on-secondary-fixed-variant',
  Health: 'bg-tertiary-fixed text-on-tertiary-fixed-variant',
  Learning: 'bg-tertiary-fixed-dim/40 text-on-tertiary-fixed-variant',
}

// Chip used for a task's status in the table / stat cards.
export const statusChipStyles = {
  Pending: 'bg-surface-container-high text-on-surface-variant',
  Due: 'bg-secondary-container/20 text-secondary',
  Failed: 'bg-tertiary-fixed text-on-tertiary-fixed-variant',
  Urgent: 'bg-error-container text-on-error-container',
  Completed: 'bg-surface-container-highest text-on-surface-variant line-through decoration-1',
}

// Left accent bar / border color keyed by priority.
export const priorityAccent = {
  Low: 'rgb(var(--color-outline))',
  Medium: 'rgb(var(--color-primary))',
  High: 'rgb(var(--color-secondary))',
  Critical: 'rgb(var(--color-error))',
}

export const priorityTextStyles = {
  Low: 'text-on-surface-variant font-medium',
  Medium: 'text-on-surface font-semibold',
  High: 'text-on-surface font-bold',
  Critical: 'text-error font-bold',
}

export const priorityBarClass = {
  Low: 'bg-outline',
  Medium: 'bg-primary',
  High: 'bg-secondary',
  Critical: 'bg-error',
}

/** Dashboard cards show "Urgent" for critical-priority items, otherwise the category. */
export function cardBadgeLabel(task) {
  return task.priority === 'Critical' ? 'Urgent' : task.category
}

export function cardBadgeStyle(task) {
  return task.priority === 'Critical'
    ? 'bg-error-container text-error'
    : categoryChipStyles[task.category] || categoryChipStyles.Work
}

export function formatDate(isoString) {
  if (!isoString) return '—'
  const date = new Date(isoString)
  return date.toLocaleDateString('en-US', { month: 'short', day: '2-digit', year: 'numeric' })
}

/** Friendly "time left" label for a due date, matching the dashboard mockup. */
export function dueLabel(isoString) {
  if (!isoString) return 'No due date'
  const due = new Date(isoString)
  const now = new Date()
  const msLeft = due.getTime() - now.getTime()
  const hoursLeft = msLeft / (1000 * 60 * 60)

  const sameDay = due.toDateString() === now.toDateString()
  if (sameDay) {
    if (hoursLeft <= 0) return 'Due today'
    if (hoursLeft < 6) return `${Math.max(1, Math.round(hoursLeft))}h left`
    return due.toLocaleTimeString('en-US', { hour: 'numeric', minute: '2-digit' })
  }
  if (msLeft < 0) return 'Overdue'
  const daysLeft = Math.round(hoursLeft / 24)
  return `${daysLeft}d left`
}

export function initials(name = '') {
  return name
    .split(' ')
    .map((part) => part[0])
    .filter(Boolean)
    .slice(0, 2)
    .join('')
    .toUpperCase()
}

/**
 * A lightweight "finish probability" heuristic for the dashboard gauge:
 * completed tasks count fully, in-progress/pending-review count partially,
 * overdue urgent tasks pull the score down a bit. Clamped to 5-99% so the
 * gauge always reads as encouraging-but-honest rather than 0% or 100%.
 */
export function computeCompletionProbability(tasks) {
  if (!tasks.length) return 0
  const weights = {
    Completed: 1,
    Pending: 0.75,
    Due: 0.5,
    Urgent: 0.3,
    Failed: 0.15,
  }
  const score = tasks.reduce((sum, t) => sum + (weights[t.status] ?? 0.2), 0)
  const pct = Math.round((score / tasks.length) * 100)
  return Math.min(99, Math.max(5, pct))
}

export function probabilityLabel(pct) {
  if (pct >= 80) return 'Highly Likely'
  if (pct >= 55) return 'On Track'
  if (pct >= 30) return 'Needs Focus'
  return 'At Risk'
}

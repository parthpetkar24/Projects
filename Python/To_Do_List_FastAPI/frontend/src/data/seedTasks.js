// Seed data for the demo. Dates are generated relative to "now" so the
// dashboard and task list always look current, no matter when this app
// is opened.

function daysFromNow(days, hour = 17) {
  const d = new Date()
  d.setDate(d.getDate() + days)
  d.setHours(hour, 0, 0, 0)
  return d.toISOString()
}

let seedIdCounter = 1
function nextId() {
  return `task-${seedIdCounter++}`
}

export const seedTasks = [
  {
    id: nextId(),
    title: 'Design landing page',
    description:
      'Create a vibrant, playful landing page for the new TaskForge marketing site using the latest brand guidelines.',
    category: 'Work',
    priority: 'Medium',
    status: 'In Progress',
    assignee: 'Hannah Ortiz',
    createdDate: daysFromNow(-4),
    dueDate: daysFromNow(0, 18),
  },
  {
    id: nextId(),
    title: 'Refactor auth logic',
    description:
      'Clean up the legacy JWT implementation and move to the new session-based authentication provider.',
    category: 'Work',
    priority: 'Critical',
    status: 'Urgent',
    assignee: 'Carlos Mendes',
    createdDate: daysFromNow(-2),
    dueDate: daysFromNow(0, new Date().getHours() + 2),
  },
  {
    id: nextId(),
    title: 'Afternoon walk',
    description: 'Head out for a 20-minute walk to refresh the mind and hit daily movement goals.',
    category: 'Health',
    priority: 'Low',
    status: 'Not Started',
    assignee: 'Alex Chen',
    createdDate: daysFromNow(-1),
    dueDate: daysFromNow(0, 16),
  },
  {
    id: nextId(),
    title: 'Redesign checkout flow',
    description: 'Streamline the mobile checkout experience and cut steps from 5 to 3.',
    category: 'Work',
    priority: 'High',
    status: 'In Progress',
    assignee: 'Priya Nair',
    createdDate: daysFromNow(-9),
    dueDate: daysFromNow(6),
  },
  {
    id: nextId(),
    title: 'Database migration',
    description: 'Migrate the legacy MySQL instance to the new managed Postgres cluster.',
    category: 'Work',
    priority: 'Critical',
    status: 'Urgent',
    assignee: 'Carlos Mendes',
    createdDate: daysFromNow(-7),
    dueDate: daysFromNow(2),
  },
  {
    id: nextId(),
    title: 'API documentation',
    description: 'Write endpoint reference docs for the v2 public API, including auth examples.',
    category: 'Work',
    priority: 'Medium',
    status: 'Completed',
    assignee: 'Hannah Ortiz',
    createdDate: daysFromNow(-16),
    dueDate: daysFromNow(-11),
  },
  {
    id: nextId(),
    title: 'Logo refresh concepts',
    description: 'Explore three directions for a refreshed wordmark and icon system.',
    category: 'Work',
    priority: 'Low',
    status: 'In Progress',
    assignee: 'Priya Nair',
    createdDate: daysFromNow(-5),
    dueDate: daysFromNow(15),
  },
  {
    id: nextId(),
    title: 'Read "Atomic Habits"',
    description: 'Finish the last three chapters and jot down two takeaways to try this week.',
    category: 'Personal',
    priority: 'Low',
    status: 'Pending Review',
    assignee: 'Alex Chen',
    createdDate: daysFromNow(-12),
    dueDate: daysFromNow(4),
  },
  {
    id: nextId(),
    title: 'Plan team offsite',
    description: 'Lock in a venue, catering, and a rough agenda for the Q3 offsite.',
    category: 'Work',
    priority: 'Medium',
    status: 'Not Started',
    assignee: 'Hannah Ortiz',
    createdDate: daysFromNow(-1),
    dueDate: daysFromNow(9),
  },
  {
    id: nextId(),
    title: 'Meal prep for the week',
    description: 'Prep lunches and snacks so weekday mornings stay calm.',
    category: 'Health',
    priority: 'Medium',
    status: 'Completed',
    assignee: 'Alex Chen',
    createdDate: daysFromNow(-8),
    dueDate: daysFromNow(-6),
  },
  {
    id: nextId(),
    title: 'Complete React course module',
    description: 'Finish the "Advanced Hooks" module and the accompanying exercises.',
    category: 'Learning',
    priority: 'Low',
    status: 'In Progress',
    assignee: 'Alex Chen',
    createdDate: daysFromNow(-3),
    dueDate: daysFromNow(10),
  },
  {
    id: nextId(),
    title: 'Quarterly security audit',
    description: 'Coordinate with the infra team to review access controls and rotate keys.',
    category: 'Work',
    priority: 'High',
    status: 'Pending Review',
    assignee: 'Carlos Mendes',
    createdDate: daysFromNow(-6),
    dueDate: daysFromNow(3),
  },
]

export function makeEmptyTask() {
  return {
    id: nextId(),
    title: '',
    description: '',
    category: 'Work',
    priority: 'Medium',
    status: 'Not Started',
    assignee: 'Alex Chen',
    createdDate: new Date().toISOString(),
    dueDate: daysFromNow(3),
  }
}

export function generateTaskId() {
  return nextId()
}

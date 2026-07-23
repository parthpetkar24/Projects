import { useMemo, useState } from 'react'
import Icon from '../components/Icon.jsx'
import StatsCards from '../components/StatsCards.jsx'
import TaskTable from '../components/TaskTable.jsx'
import { useTasks } from '../context/TaskContext.jsx'
import { useUI } from '../context/UIContext.jsx'
import { PRIORITIES, STATUSES } from '../lib/taskUtils.js'

const priorityRank = { Critical: 0, High: 1, Medium: 2, Low: 3 }

export default function TasksList() {
  const { tasks } = useTasks()
  const { openCreateModal } = useUI()

  const [search, setSearch] = useState('')
  const [statusFilter, setStatusFilter] = useState('All')
  const [priorityFilter, setPriorityFilter] = useState('All')
  const [sortKey, setSortKey] = useState('dueDate')
  const [sortDir, setSortDir] = useState('asc')

  function handleSort(key) {
    if (sortKey === key) {
      setSortDir((d) => (d === 'asc' ? 'desc' : 'asc'))
    } else {
      setSortKey(key)
      setSortDir('asc')
    }
  }

  const filteredSorted = useMemo(() => {
    const query = search.trim().toLowerCase()

    let result = tasks.filter((t) => {
      const matchesQuery =
        !query || t.title.toLowerCase().includes(query) || t.category.toLowerCase().includes(query)
      const matchesStatus = statusFilter === 'All' || t.status === statusFilter
      const matchesPriority = priorityFilter === 'All' || t.priority === priorityFilter
      return matchesQuery && matchesStatus && matchesPriority
    })

    const dir = sortDir === 'asc' ? 1 : -1
    result = [...result].sort((a, b) => {
      switch (sortKey) {
        case 'priority':
          return (priorityRank[a.priority] - priorityRank[b.priority]) * dir
        case 'status':
          return a.status.localeCompare(b.status) * dir
        case 'createdDate':
          return (new Date(a.createdDate) - new Date(b.createdDate)) * dir
        case 'dueDate':
        default: {
          const aTime = a.dueDate ? new Date(a.dueDate).getTime() : Infinity
          const bTime = b.dueDate ? new Date(b.dueDate).getTime() : Infinity
          return (aTime - bTime) * dir
        }
      }
    })

    return result
  }, [tasks, search, statusFilter, priorityFilter, sortKey, sortDir])

  const sprintPct = tasks.length
    ? Math.round((tasks.filter((t) => t.status === 'Completed').length / tasks.length) * 100)
    : 0

  return (
    <>
      <div className="flex flex-col md:flex-row md:items-end justify-between gap-6 mb-8">
        <div>
          <h1 className="font-display text-headline-lg-mobile sm:text-headline-lg text-primary mb-1">
            Tasks List
          </h1>
          <p className="text-on-surface-variant font-body-md max-w-md">
            Manage and monitor your throughput. Your current sprint is {sprintPct}% complete.
          </p>
        </div>
        <button
          type="button"
          onClick={openCreateModal}
          className="flex items-center gap-2 bg-secondary text-on-secondary px-6 py-3 rounded-full font-semibold shadow-lg hover:scale-[1.02] active:scale-95 transition-all"
        >
          <Icon name="add_circle" filled />
          Create New Task
        </button>
      </div>

      <StatsCards />

      <div className="flex flex-col sm:flex-row gap-3 mb-6">
        <div className="relative flex-1">
          <Icon
            name="search"
            className="absolute left-4 top-1/2 -translate-y-1/2 text-on-surface-variant"
            size="20px"
          />
          <input
            type="text"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            placeholder="Search tasks by name or category..."
            className="w-full pl-11 pr-4 py-3 bg-surface-container-lowest border border-outline-variant/40 rounded-xl focus:ring-4 focus:ring-primary/20 focus:border-primary transition-all text-body-md font-body-md text-on-surface"
          />
        </div>

        <select
          value={statusFilter}
          onChange={(e) => setStatusFilter(e.target.value)}
          className="px-4 py-3 bg-surface-container-lowest border border-outline-variant/40 rounded-xl focus:ring-4 focus:ring-primary/20 text-body-md font-body-md text-on-surface"
        >
          <option value="All">All statuses</option>
          {STATUSES.map((s) => (
            <option key={s} value={s}>
              {s}
            </option>
          ))}
        </select>

        <select
          value={priorityFilter}
          onChange={(e) => setPriorityFilter(e.target.value)}
          className="px-4 py-3 bg-surface-container-lowest border border-outline-variant/40 rounded-xl focus:ring-4 focus:ring-primary/20 text-body-md font-body-md text-on-surface"
        >
          <option value="All">All priorities</option>
          {PRIORITIES.map((p) => (
            <option key={p} value={p}>
              {p}
            </option>
          ))}
        </select>
      </div>

      <TaskTable tasks={filteredSorted} sortKey={sortKey} sortDir={sortDir} onSort={handleSort} />
    </>
  )
}

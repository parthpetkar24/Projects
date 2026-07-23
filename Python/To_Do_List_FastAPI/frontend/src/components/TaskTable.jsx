import { useEffect, useMemo, useState } from 'react'
import Icon from './Icon.jsx'
import { useUI } from '../context/UIContext.jsx'
import { useTasks } from '../context/TaskContext.jsx'
import { formatDate, priorityBarClass, priorityTextStyles, statusChipStyles } from '../lib/taskUtils.js'

const PAGE_SIZE = 6

const columns = [
  { key: 'title', label: 'Task Name', sortable: false },
  { key: 'status', label: 'Status', sortable: true },
  { key: 'priority', label: 'Priority', sortable: true },
  { key: 'createdDate', label: 'Created', sortable: true },
  { key: 'dueDate', label: 'End Date', sortable: true },
]

export default function TaskTable({ tasks, sortKey, sortDir, onSort }) {
  const { openEditModal } = useUI()
  const { deleteTask } = useTasks()
  const [page, setPage] = useState(1)

  const totalPages = Math.max(1, Math.ceil(tasks.length / PAGE_SIZE))

  useEffect(() => {
    setPage(1)
  }, [tasks.length, sortKey, sortDir])

  const paginated = useMemo(() => {
    const start = (page - 1) * PAGE_SIZE
    return tasks.slice(start, start + PAGE_SIZE)
  }, [tasks, page])

  function SortIcon({ column }) {
    if (sortKey !== column) return <Icon name="unfold_more" size="16px" className="opacity-40" />
    return <Icon name={sortDir === 'asc' ? 'arrow_upward' : 'arrow_downward'} size="16px" />
  }

  return (
    <div className="bg-surface-container-lowest rounded-2xl overflow-hidden shadow-card border border-outline-variant/20">
      <div className="overflow-x-auto">
        <table className="w-full text-left border-collapse min-w-[640px]">
          <thead>
            <tr className="bg-surface-container-low text-on-surface-variant">
              {columns.map((col) => (
                <th key={col.key} className="p-4 font-semibold text-label-sm uppercase tracking-wider">
                  {col.sortable ? (
                    <button
                      type="button"
                      onClick={() => onSort(col.key)}
                      className="flex items-center gap-1 hover:text-on-surface transition-colors"
                    >
                      {col.label}
                      <SortIcon column={col.key} />
                    </button>
                  ) : (
                    col.label
                  )}
                </th>
              ))}
              <th className="p-4 font-semibold text-label-sm uppercase tracking-wider text-right">Actions</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-outline-variant/40">
            {paginated.length === 0 && (
              <tr>
                <td colSpan={6} className="p-10 text-center text-on-surface-variant font-body-md">
                  No tasks match your filters.
                </td>
              </tr>
            )}
            {paginated.map((task) => (
              <tr key={task.id} className="hover:bg-surface-variant/30 transition-colors group">
                <td className="p-4">
                  <div className="flex items-center gap-3">
                    <div className={`w-1.5 h-10 rounded-full flex-shrink-0 ${priorityBarClass[task.priority]}`} />
                    <div className="min-w-0">
                      <div className="font-semibold text-on-surface text-body-lg truncate max-w-[220px]">
                        {task.title}
                      </div>
                      <div className="text-label-sm text-on-surface-variant">{task.category}</div>
                    </div>
                  </div>
                </td>
                <td className="p-4">
                  <span
                    className={`inline-flex items-center px-3 py-1 rounded-full text-label-sm font-semibold whitespace-nowrap ${statusChipStyles[task.status]}`}
                  >
                    {task.status}
                  </span>
                </td>
                <td className="p-4">
                  <span className={`text-body-md ${priorityTextStyles[task.priority]}`}>{task.priority}</span>
                </td>
                <td className="p-4 text-on-surface-variant whitespace-nowrap">{formatDate(task.createdDate)}</td>
                <td className="p-4 text-on-surface-variant whitespace-nowrap">{formatDate(task.dueDate)}</td>
                <td className="p-4 text-right">
                  <div className="flex items-center justify-end gap-1 opacity-0 group-hover:opacity-100 focus-within:opacity-100 transition-opacity">
                    <button
                      type="button"
                      onClick={() => openEditModal(task)}
                      className="p-2 hover:bg-primary-container hover:text-on-primary-container rounded-lg transition-colors text-on-surface-variant"
                      title="Update"
                    >
                      <Icon name="edit" size="18px" />
                    </button>
                    <button
                      type="button"
                      onClick={() => deleteTask(task.id)}
                      className="p-2 hover:bg-error-container hover:text-on-error-container rounded-lg transition-colors text-on-surface-variant"
                      title="Delete"
                    >
                      <Icon name="delete" size="18px" />
                    </button>
                  </div>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <div className="bg-surface-container-low p-4 flex flex-col sm:flex-row items-center justify-between gap-3 border-t border-outline-variant/30">
        <div className="text-body-md text-on-surface-variant">
          Showing{' '}
          <span className="font-semibold text-on-surface">
            {tasks.length === 0 ? 0 : (page - 1) * PAGE_SIZE + 1}-{Math.min(page * PAGE_SIZE, tasks.length)}
          </span>{' '}
          of <span className="font-semibold text-on-surface">{tasks.length}</span> tasks
        </div>
        <div className="flex items-center gap-2">
          <button
            type="button"
            disabled={page <= 1}
            onClick={() => setPage((p) => Math.max(1, p - 1))}
            className="p-2 bg-surface-container rounded-lg text-on-surface-variant hover:text-on-surface transition-colors border border-outline-variant/40 disabled:opacity-40 disabled:cursor-not-allowed"
            aria-label="Previous page"
          >
            <Icon name="chevron_left" size="20px" />
          </button>
          <div className="flex gap-1">
            {Array.from({ length: totalPages }, (_, i) => i + 1).map((n) => (
              <button
                key={n}
                type="button"
                onClick={() => setPage(n)}
                className={`w-8 h-8 flex items-center justify-center rounded-lg font-bold transition-colors ${
                  n === page ? 'bg-primary text-on-primary' : 'hover:bg-surface-variant text-on-surface-variant'
                }`}
              >
                {n}
              </button>
            ))}
          </div>
          <button
            type="button"
            disabled={page >= totalPages}
            onClick={() => setPage((p) => Math.min(totalPages, p + 1))}
            className="p-2 bg-surface-container rounded-lg text-on-surface-variant hover:text-on-surface transition-colors border border-outline-variant/40 disabled:opacity-40 disabled:cursor-not-allowed"
            aria-label="Next page"
          >
            <Icon name="chevron_right" size="20px" />
          </button>
        </div>
      </div>
    </div>
  )
}

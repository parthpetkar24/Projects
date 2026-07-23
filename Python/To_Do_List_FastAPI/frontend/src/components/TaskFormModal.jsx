import { useEffect, useState } from 'react'
import Icon from './Icon.jsx'
import { useUI } from '../context/UIContext.jsx'
import { useTasks } from '../context/TaskContext.jsx'
import { CATEGORIES, PRIORITIES, STATUSES } from '../lib/taskUtils.js'

const emptyForm = {
  title: '',
  description: '',
  category: 'Work',
  priority: 'Medium',
  status: 'Not Started',
  assignee: 'Alex Chen',
  dueDate: '',
}

function toDateInputValue(iso) {
  if (!iso) return ''
  return new Date(iso).toISOString().slice(0, 10)
}

export default function TaskFormModal() {
  const { modalState, closeModal } = useUI()
  const { addTask, updateTask, deleteTask } = useTasks()
  const { isOpen, mode, task } = modalState

  const [form, setForm] = useState(emptyForm)
  const [error, setError] = useState('')

  useEffect(() => {
    if (!isOpen) return
    if (mode === 'edit' && task) {
      setForm({
        title: task.title,
        description: task.description || '',
        category: task.category,
        priority: task.priority,
        status: task.status,
        assignee: task.assignee || '',
        dueDate: toDateInputValue(task.dueDate),
      })
    } else {
      setForm(emptyForm)
    }
    setError('')
  }, [isOpen, mode, task])

  useEffect(() => {
    function onKeyDown(e) {
      if (e.key === 'Escape') closeModal()
    }
    if (isOpen) document.addEventListener('keydown', onKeyDown)
    return () => document.removeEventListener('keydown', onKeyDown)
  }, [isOpen, closeModal])

  if (!isOpen) return null

  function handleChange(field, value) {
    setForm((prev) => ({ ...prev, [field]: value }))
  }

  function handleSubmit(e) {
    e.preventDefault()
    if (!form.title.trim()) {
      setError('Give the task a title before saving.')
      return
    }

    const payload = {
      ...form,
      title: form.title.trim(),
      dueDate: form.dueDate ? new Date(form.dueDate + 'T17:00:00').toISOString() : null,
    }

    if (mode === 'edit' && task) {
      updateTask(task.id, payload)
    } else {
      addTask(payload)
    }
    closeModal()
  }

  function handleDelete() {
    if (task) deleteTask(task.id)
    closeModal()
  }

  return (
    <div
      className="fixed inset-0 z-[60] flex items-end sm:items-center justify-center p-0 sm:p-4"
      role="dialog"
      aria-modal="true"
      aria-labelledby="task-modal-title"
    >
      <button
        type="button"
        aria-label="Close"
        onClick={closeModal}
        className="absolute inset-0 bg-inverse-surface/40 backdrop-blur-sm"
      />

      <form
        onSubmit={handleSubmit}
        className="relative w-full sm:max-w-lg bg-surface-container-lowest rounded-t-[32px] sm:rounded-[32px] p-6 sm:p-8 shadow-2xl animate-pop-in max-h-[90vh] overflow-y-auto"
      >
        <div className="flex items-center justify-between mb-6">
          <div className="flex items-center gap-3">
            <div className="p-3 bg-primary-fixed rounded-2xl text-primary">
              <Icon name={mode === 'edit' ? 'edit' : 'add_task'} />
            </div>
            <h3 id="task-modal-title" className="font-display text-headline-md">
              {mode === 'edit' ? 'Edit Task' : 'Create New Task'}
            </h3>
          </div>
          <button
            type="button"
            onClick={closeModal}
            aria-label="Close dialog"
            className="p-2 rounded-full text-on-surface-variant hover:bg-surface-variant/50 transition-colors"
          >
            <Icon name="close" />
          </button>
        </div>

        <div className="space-y-5">
          <div className="space-y-2">
            <label className="font-label-md text-label-md text-on-surface-variant ml-2" htmlFor="task-title">
              What needs to be done?
            </label>
            <input
              id="task-title"
              type="text"
              value={form.title}
              onChange={(e) => handleChange('title', e.target.value)}
              placeholder="e.g., Design landing page..."
              className="w-full px-6 py-4 bg-surface-container-low border-none rounded-2xl focus:ring-4 focus:ring-primary/20 focus:bg-surface-container-lowest transition-all text-body-md font-body-md text-on-surface"
              autoFocus
            />
          </div>

          <div className="space-y-2">
            <label className="font-label-md text-label-md text-on-surface-variant ml-2" htmlFor="task-desc">
              Details
            </label>
            <textarea
              id="task-desc"
              rows={3}
              value={form.description}
              onChange={(e) => handleChange('description', e.target.value)}
              placeholder="Add any useful context..."
              className="w-full px-6 py-4 bg-surface-container-low border-none rounded-2xl focus:ring-4 focus:ring-primary/20 focus:bg-surface-container-lowest transition-all text-body-md font-body-md text-on-surface resize-none"
            />
          </div>

          <div className="grid grid-cols-2 gap-4">
            <div className="space-y-2">
              <label className="font-label-md text-label-md text-on-surface-variant ml-2" htmlFor="task-priority">
                Priority
              </label>
              <select
                id="task-priority"
                value={form.priority}
                onChange={(e) => handleChange('priority', e.target.value)}
                className="w-full px-6 py-4 bg-surface-container-low border-none rounded-2xl focus:ring-4 focus:ring-primary/20 focus:bg-surface-container-lowest transition-all text-body-md font-body-md text-on-surface"
              >
                {PRIORITIES.map((p) => (
                  <option key={p} value={p}>
                    {p}
                  </option>
                ))}
              </select>
            </div>

            <div className="space-y-2">
              <label className="font-label-md text-label-md text-on-surface-variant ml-2" htmlFor="task-category">
                Category
              </label>
              <select
                id="task-category"
                value={form.category}
                onChange={(e) => handleChange('category', e.target.value)}
                className="w-full px-6 py-4 bg-surface-container-low border-none rounded-2xl focus:ring-4 focus:ring-primary/20 focus:bg-surface-container-lowest transition-all text-body-md font-body-md text-on-surface"
              >
                {CATEGORIES.map((c) => (
                  <option key={c} value={c}>
                    {c}
                  </option>
                ))}
              </select>
            </div>

            <div className="space-y-2">
              <label className="font-label-md text-label-md text-on-surface-variant ml-2" htmlFor="task-status">
                Status
              </label>
              <select
                id="task-status"
                value={form.status}
                onChange={(e) => handleChange('status', e.target.value)}
                className="w-full px-6 py-4 bg-surface-container-low border-none rounded-2xl focus:ring-4 focus:ring-primary/20 focus:bg-surface-container-lowest transition-all text-body-md font-body-md text-on-surface"
              >
                {STATUSES.map((s) => (
                  <option key={s} value={s}>
                    {s}
                  </option>
                ))}
              </select>
            </div>

            <div className="space-y-2">
              <label className="font-label-md text-label-md text-on-surface-variant ml-2" htmlFor="task-due">
                Due date
              </label>
              <input
                id="task-due"
                type="date"
                value={form.dueDate}
                onChange={(e) => handleChange('dueDate', e.target.value)}
                className="w-full px-6 py-4 bg-surface-container-low border-none rounded-2xl focus:ring-4 focus:ring-primary/20 focus:bg-surface-container-lowest transition-all text-body-md font-body-md text-on-surface"
              />
            </div>
          </div>

          <div className="space-y-2">
            <label className="font-label-md text-label-md text-on-surface-variant ml-2" htmlFor="task-assignee">
              Assignee
            </label>
            <input
              id="task-assignee"
              type="text"
              value={form.assignee}
              onChange={(e) => handleChange('assignee', e.target.value)}
              placeholder="Who's on it?"
              className="w-full px-6 py-4 bg-surface-container-low border-none rounded-2xl focus:ring-4 focus:ring-primary/20 focus:bg-surface-container-lowest transition-all text-body-md font-body-md text-on-surface"
            />
          </div>

          {error && (
            <p className="text-error text-label-md font-label-md flex items-center gap-2" role="alert">
              <Icon name="error" size="18px" />
              {error}
            </p>
          )}
        </div>

        <div className="flex items-center gap-3 mt-8">
          {mode === 'edit' && (
            <button
              type="button"
              onClick={handleDelete}
              className="p-4 rounded-2xl border-2 border-error text-error hover:bg-error-container/40 transition-all active:scale-95"
              aria-label="Delete task"
              title="Delete task"
            >
              <Icon name="delete" />
            </button>
          )}
          <button
            type="submit"
            className="flex-1 py-4 bg-primary text-on-primary rounded-2xl font-bold text-lg hover:scale-[1.01] active:scale-95 shadow-lg shadow-primary/20 transition-all"
          >
            {mode === 'edit' ? 'Save Changes' : 'Add to My List'}
          </button>
        </div>
      </form>
    </div>
  )
}

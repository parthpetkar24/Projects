import { useState } from 'react'
import Icon from './Icon.jsx'
import { useTasks } from '../context/TaskContext.jsx'
import { CATEGORIES, PRIORITIES } from '../lib/taskUtils.js'

export default function NewTaskForm() {
  const { addTask } = useTasks()
  const [title, setTitle] = useState('')
  const [priority, setPriority] = useState('Medium')
  const [category, setCategory] = useState('Work')
  const [justAdded, setJustAdded] = useState(false)

  function handleSubmit(e) {
    e.preventDefault()
    if (!title.trim()) return

    addTask({
      title: title.trim(),
      description: '',
      priority,
      category,
      status: 'Not Started',
      assignee: 'Alex Chen',
      dueDate: null,
    })

    setTitle('')
    setPriority('Medium')
    setCategory('Work')
    setJustAdded(true)
    setTimeout(() => setJustAdded(false), 1800)
  }

  return (
    <section
      id="new-task-form"
      className="col-span-12 md:col-span-7 bg-surface-container-lowest rounded-[32px] p-8 shadow-glow border border-outline-variant/10"
    >
      <div className="flex items-center gap-3 mb-6">
        <div className="p-3 bg-primary-fixed rounded-2xl text-primary">
          <Icon name="add_task" />
        </div>
        <h3 className="font-display text-headline-md">Create New Task</h3>
      </div>

      <form className="space-y-6" onSubmit={handleSubmit}>
        <div className="space-y-2">
          <label className="font-label-md text-label-md text-on-surface-variant ml-2" htmlFor="quick-title">
            What needs to be done?
          </label>
          <input
            id="quick-title"
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            placeholder="e.g., Design landing page..."
            className="w-full px-6 py-4 bg-surface-container-low border-none rounded-2xl focus:ring-4 focus:ring-primary/20 focus:bg-surface-container-lowest transition-all text-body-md font-body-md text-on-surface"
          />
        </div>

        <div className="grid grid-cols-2 gap-4">
          <div className="space-y-2">
            <label className="font-label-md text-label-md text-on-surface-variant ml-2" htmlFor="quick-priority">
              Priority
            </label>
            <select
              id="quick-priority"
              value={priority}
              onChange={(e) => setPriority(e.target.value)}
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
            <label className="font-label-md text-label-md text-on-surface-variant ml-2" htmlFor="quick-category">
              Category
            </label>
            <select
              id="quick-category"
              value={category}
              onChange={(e) => setCategory(e.target.value)}
              className="w-full px-6 py-4 bg-surface-container-low border-none rounded-2xl focus:ring-4 focus:ring-primary/20 focus:bg-surface-container-lowest transition-all text-body-md font-body-md text-on-surface"
            >
              {CATEGORIES.map((c) => (
                <option key={c} value={c}>
                  {c}
                </option>
              ))}
            </select>
          </div>
        </div>

        <button
          type="submit"
          className="w-full py-4 bg-primary text-on-primary rounded-2xl font-bold text-lg hover:scale-[1.02] active:scale-95 shadow-lg shadow-primary/20 transition-all flex items-center justify-center gap-2"
        >
          <Icon name={justAdded ? 'check_circle' : 'add'} filled={justAdded} />
          {justAdded ? 'Added to your list!' : 'Add to My List'}
        </button>
      </form>
    </section>
  )
}

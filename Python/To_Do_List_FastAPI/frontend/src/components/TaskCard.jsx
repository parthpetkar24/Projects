import Icon from './Icon.jsx'
import { useUI } from '../context/UIContext.jsx'
import { useTasks } from '../context/TaskContext.jsx'
import { cardBadgeLabel, cardBadgeStyle, dueLabel, initials, priorityAccent } from '../lib/taskUtils.js'

export default function TaskCard({ task }) {
  const { openEditModal } = useUI()
  const { deleteTask, toggleComplete } = useTasks()
  const isCompleted = task.status === 'Completed'

  return (
    <article
      className="bg-surface-container-lowest rounded-3xl p-6 shadow-card hover:shadow-xl hover:scale-[1.02] transition-all border border-outline-variant/10 task-card-accent group flex flex-col"
      style={{ '--accent-color': priorityAccent[task.priority] }}
    >
      <div className="flex justify-between items-start mb-4">
        <span className={`px-3 py-1 font-label-sm text-label-sm rounded-full ${cardBadgeStyle(task)}`}>
          {cardBadgeLabel(task)}
        </span>
        <div className="flex gap-1 opacity-0 group-hover:opacity-100 focus-within:opacity-100 transition-opacity">
          <button
            type="button"
            onClick={() => toggleComplete(task.id)}
            className="p-2 rounded-full hover:bg-surface-container text-tertiary transition-colors"
            title={isCompleted ? 'Mark as not done' : 'Mark as done'}
          >
            <Icon name={isCompleted ? 'replay' : 'check_circle'} />
          </button>
          <button
            type="button"
            onClick={() => openEditModal(task)}
            className="p-2 rounded-full hover:bg-surface-container text-primary transition-colors"
            title="Edit"
          >
            <Icon name="edit" size="18px" />
          </button>
          <button
            type="button"
            onClick={() => deleteTask(task.id)}
            className="p-2 rounded-full hover:bg-error-container text-error transition-colors"
            title="Delete"
          >
            <Icon name="delete" size="18px" />
          </button>
        </div>
      </div>

      <h4 className={`font-display text-lg mb-2 ${isCompleted ? 'line-through text-on-surface-variant' : ''}`}>
        {task.title}
      </h4>
      <p className="text-on-surface-variant text-body-md mb-6 line-clamp-2">
        {task.description || 'No additional details.'}
      </p>

      <div className="flex items-center justify-between mt-auto pt-4 border-t border-outline-variant/10">
        <div className="flex items-center gap-2 text-on-surface-variant">
          <Icon name="schedule" size="18px" />
          <span className="text-label-sm font-label-sm">{dueLabel(task.dueDate)}</span>
        </div>
        <div className="w-8 h-8 rounded-full bg-primary-fixed-dim flex items-center justify-center text-on-primary-fixed font-bold text-xs border-2 border-surface-container-lowest">
          {initials(task.assignee) || <Icon name="person" size="14px" />}
        </div>
      </div>
    </article>
  )
}

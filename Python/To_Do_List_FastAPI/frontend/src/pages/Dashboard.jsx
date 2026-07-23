import { useMemo } from 'react'
import { Link } from 'react-router-dom'
import Icon from '../components/Icon.jsx'
import NewTaskForm from '../components/NewTaskForm.jsx'
import CompletionGauge from '../components/CompletionGauge.jsx'
import TaskCard from '../components/TaskCard.jsx'
import { useTasks } from '../context/TaskContext.jsx'
import { computeCompletionProbability } from '../lib/taskUtils.js'

const priorityRank = { Critical: 0, High: 1, Medium: 2, Low: 3 }

export default function Dashboard() {
  const { tasks } = useTasks()

  const activeTasks = useMemo(
    () =>
      tasks
        .filter((t) => t.status !== 'Completed')
        .sort((a, b) => priorityRank[a.priority] - priorityRank[b.priority])
        .slice(0, 6),
    [tasks]
  )

  const percent = useMemo(() => computeCompletionProbability(tasks), [tasks])
  const tasksLeft = tasks.filter((t) => t.status !== 'Completed').length

  const firstName = 'Alex'

  return (
    <>
      <header className="mb-8">
        <h2 className="font-display text-headline-lg-mobile sm:text-headline-xl text-on-background mb-2">
          Welcome back, {firstName}! 👋
        </h2>
        <p className="font-body-lg text-body-lg text-on-surface-variant">
          You have {tasksLeft} task{tasksLeft === 1 ? '' : 's'} to crush today. Let's make it happen!
        </p>
      </header>

      <div className="grid grid-cols-12 gap-6">
        <NewTaskForm />
        <CompletionGauge percent={percent} tasksLeft={tasksLeft} />

        <section className="col-span-12 space-y-6">
          <div className="flex justify-between items-end px-2">
            <div>
              <h3 className="font-display text-headline-md text-on-background">Active Tasks</h3>
              <p className="text-on-surface-variant font-body-md">Manage and track your daily progress</p>
            </div>
            <Link
              to="/tasks"
              className="flex items-center gap-1 text-primary font-label-md text-label-md hover:underline"
            >
              View all
              <Icon name="arrow_forward" size="18px" />
            </Link>
          </div>

          {activeTasks.length === 0 ? (
            <div className="bg-surface-container-lowest rounded-3xl p-12 text-center border border-outline-variant/10">
              <Icon name="celebration" className="text-tertiary" size="40px" />
              <p className="mt-3 font-display text-headline-md">All clear!</p>
              <p className="text-on-surface-variant font-body-md">
                No active tasks right now — add one above whenever you're ready.
              </p>
            </div>
          ) : (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {activeTasks.map((task) => (
                <TaskCard key={task.id} task={task} />
              ))}
            </div>
          )}
        </section>
      </div>
    </>
  )
}

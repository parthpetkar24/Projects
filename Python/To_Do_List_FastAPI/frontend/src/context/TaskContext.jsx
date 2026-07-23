import { createContext, useContext, useMemo, useState } from 'react'
import { seedTasks, generateTaskId } from '../data/seedTasks'

const TaskContext = createContext(null)

export function TaskProvider({ children }) {
  const [tasks, setTasks] = useState(seedTasks)

  const addTask = (partialTask) => {
    const task = {
      id: generateTaskId(),
      createdDate: new Date().toISOString(),
      status: 'Not Started',
      ...partialTask,
    }
    setTasks((prev) => [task, ...prev])
    return task
  }

  const updateTask = (id, updates) => {
    setTasks((prev) => prev.map((t) => (t.id === id ? { ...t, ...updates } : t)))
  }

  const deleteTask = (id) => {
    setTasks((prev) => prev.filter((t) => t.id !== id))
  }

  const toggleComplete = (id) => {
    setTasks((prev) =>
      prev.map((t) =>
        t.id === id ? { ...t, status: t.status === 'Completed' ? 'In Progress' : 'Completed' } : t
      )
    )
  }

  const stats = useMemo(() => {
    const byStatus = (status) => tasks.filter((t) => t.status === status).length
    return {
      total: tasks.length,
      completed: byStatus('Completed'),
      inProgress: byStatus('In Progress'),
      pendingReview: byStatus('Pending Review'),
      urgent: tasks.filter((t) => t.status === 'Urgent' || t.priority === 'Critical').length,
      notStarted: byStatus('Not Started'),
    }
  }, [tasks])

  const value = { tasks, addTask, updateTask, deleteTask, toggleComplete, stats }

  return <TaskContext.Provider value={value}>{children}</TaskContext.Provider>
}

export function useTasks() {
  const ctx = useContext(TaskContext)
  if (!ctx) throw new Error('useTasks must be used within a TaskProvider')
  return ctx
}

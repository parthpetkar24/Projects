import { Routes, Route } from 'react-router-dom'
import TopNav from './components/layout/TopNav.jsx'
import SideNav from './components/layout/SideNav.jsx'
import MobileBottomNav from './components/layout/MobileBottomNav.jsx'
import TaskFormModal from './components/TaskFormModal.jsx'
import Dashboard from './pages/Dashboard.jsx'
import TasksList from './pages/TasksList.jsx'

export default function App() {
  return (
    <div className="min-h-screen bg-background text-on-background">
      <TopNav />

      <div className="flex max-w-container-max mx-auto px-4 md:px-margin-desktop py-8 gap-8 items-start">
        <SideNav />

        <main className="flex-1 min-w-0 pb-24 lg:pb-0">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/tasks" element={<TasksList />} />
            <Route path="*" element={<Dashboard />} />
          </Routes>
        </main>
      </div>

      <MobileBottomNav />
      <TaskFormModal />
    </div>
  )
}

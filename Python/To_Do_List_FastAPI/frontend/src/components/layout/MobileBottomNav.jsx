import { NavLink } from 'react-router-dom'
import Icon from '../Icon.jsx'
import { useUI } from '../../context/UIContext.jsx'

const linkClass = ({ isActive }) =>
  `flex flex-col items-center justify-center py-2 flex-1 ${
    isActive ? 'text-primary' : 'text-on-surface-variant'
  }`

export default function MobileBottomNav() {
  const { openCreateModal } = useUI()

  return (
    <nav className="fixed bottom-0 left-0 w-full flex justify-around items-center px-4 bg-surface border-t border-outline-variant/20 shadow-[0_-4px_12px_rgba(0,0,0,0.05)] backdrop-blur-lg lg:hidden z-50 py-2 pb-[calc(0.5rem+env(safe-area-inset-bottom))]">
      <NavLink to="/" end className={linkClass}>
        {({ isActive }) => (
          <>
            <Icon name="home" filled={isActive} />
            <span className="text-[10px] font-label-sm mt-1">Home</span>
          </>
        )}
      </NavLink>

      <NavLink to="/tasks" className={linkClass}>
        {({ isActive }) => (
          <>
            <Icon name="task_alt" filled={isActive} />
            <span className="text-[10px] font-label-sm mt-1">Tasks</span>
          </>
        )}
      </NavLink>

      <div className="relative -top-6 flex-1 flex justify-center">
        <button
          type="button"
          onClick={openCreateModal}
          aria-label="Create new task"
          className="bg-primary text-on-primary w-14 h-14 rounded-2xl flex items-center justify-center shadow-lg shadow-primary/40 active:scale-90 transition-transform"
        >
          <Icon name="add" size="30px" />
        </button>
      </div>

      <button type="button" className="flex flex-col items-center justify-center py-2 flex-1 text-on-surface-variant">
        <Icon name="grid_view" />
        <span className="text-[10px] font-label-sm mt-1">Projects</span>
      </button>

      <button type="button" className="flex flex-col items-center justify-center py-2 flex-1 text-on-surface-variant">
        <Icon name="bar_chart" />
        <span className="text-[10px] font-label-sm mt-1">Stats</span>
      </button>
    </nav>
  )
}

import { NavLink } from 'react-router-dom'
import Icon from '../Icon.jsx'
import { useUI } from '../../context/UIContext.jsx'

const links = [
  { to: '/', label: 'Dashboard', icon: 'dashboard', end: true },
  { to: '/tasks', label: 'Tasks', icon: 'checklist', end: false },
]

const linkClass = ({ isActive }) =>
  `rounded-xl flex items-center gap-3 px-4 py-3 transition-all font-label-md text-label-md ${
    isActive
      ? 'bg-primary-container text-on-primary-container font-bold'
      : 'text-on-surface-variant hover:bg-surface-variant/50 hover:translate-x-1'
  }`

export default function SideNav() {
  const { openCreateModal } = useUI()

  return (
    <aside className="h-[calc(100vh-104px)] w-64 sticky top-24 hidden lg:flex flex-col bg-surface-container-low border border-outline-variant/30 rounded-3xl p-unit gap-2 shadow-xl flex-shrink-0">
      <div className="flex flex-col gap-1 p-4 mb-2">
        <div className="flex items-center gap-3">
          <div className="w-12 h-12 rounded-2xl bg-primary-fixed border-2 border-primary-fixed flex items-center justify-center text-primary font-display font-bold text-lg flex-shrink-0">
            AC
          </div>
          <div>
            <p className="font-display text-headline-md font-bold text-primary leading-tight">
              Alex Chen
            </p>
            <p className="font-body-md text-label-sm text-on-surface-variant">Stay productive!</p>
          </div>
        </div>
      </div>

      <nav className="flex flex-col gap-1">
        {links.map((link) => (
          <NavLink key={link.to} to={link.to} end={link.end} className={linkClass}>
            <Icon name={link.icon} />
            <span>{link.label}</span>
          </NavLink>
        ))}
      </nav>

      <div className="mt-auto px-2 pb-2">
        <button
          type="button"
          onClick={openCreateModal}
          className="w-full py-4 bg-secondary-container text-on-secondary-container rounded-2xl font-bold flex items-center justify-center gap-2 shadow-sm hover:shadow-md hover:-translate-y-0.5 transition-all active:translate-y-0.5"
        >
          <Icon name="add" />
          New Task
        </button>
      </div>
    </aside>
  )
}

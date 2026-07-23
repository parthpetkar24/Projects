import { NavLink } from 'react-router-dom'
import Icon from '../Icon.jsx'
import { useTheme } from '../../context/ThemeContext.jsx'

const navLinkClass = ({ isActive }) =>
  `font-label-md text-label-md pb-1 border-b-2 transition-colors ${
    isActive
      ? 'text-primary border-primary font-bold'
      : 'text-on-surface-variant border-transparent hover:text-primary'
  }`

export default function TopNav() {
  const { theme, toggleTheme } = useTheme()

  return (
    <header className="w-full sticky top-0 z-40 bg-surface/80 backdrop-blur-md shadow-glow">
      <div className="max-w-container-max mx-auto flex justify-between items-center px-4 md:px-margin-desktop py-4">
        <NavLink to="/" className="flex-shrink-0">
          <h1 className="font-display text-headline-lg font-bold text-primary tracking-tight">
            TaskForge
          </h1>
        </NavLink>

        <nav className="hidden md:flex gap-12 items-center flex-grow justify-center">
          <NavLink to="/" end className={navLinkClass}>
            Dashboard
          </NavLink>
          <NavLink to="/tasks" className={navLinkClass}>
            Tasks
          </NavLink>
        </nav>

        <div className="flex items-center gap-2 md:gap-4 flex-shrink-0">
          <button
            type="button"
            aria-label="Toggle theme"
            onClick={toggleTheme}
            className="p-2 rounded-full text-on-surface-variant hover:bg-surface-variant/50 transition-colors flex items-center justify-center active:scale-90"
          >
            <Icon name={theme === 'dark' ? 'light_mode' : 'dark_mode'} />
          </button>
          <button className="hidden sm:block px-4 md:px-6 py-2 rounded-full border-2 border-primary text-primary font-bold hover:bg-primary/5 transition-all active:scale-95">
            Log In
          </button>
          <button className="px-4 md:px-6 py-2 rounded-full bg-primary text-on-primary font-bold shadow-sm hover:shadow-md hover:scale-105 transition-all active:scale-95">
            Sign Up
          </button>
        </div>
      </div>
    </header>
  )
}

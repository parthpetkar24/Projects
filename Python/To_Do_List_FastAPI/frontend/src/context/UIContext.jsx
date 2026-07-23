import { createContext, useContext, useState } from 'react'

const UIContext = createContext(null)

export function UIProvider({ children }) {
  const [modalState, setModalState] = useState({ isOpen: false, mode: 'create', task: null })

  const openCreateModal = () => setModalState({ isOpen: true, mode: 'create', task: null })
  const openEditModal = (task) => setModalState({ isOpen: true, mode: 'edit', task })
  const closeModal = () => setModalState((prev) => ({ ...prev, isOpen: false }))

  return (
    <UIContext.Provider value={{ modalState, openCreateModal, openEditModal, closeModal }}>
      {children}
    </UIContext.Provider>
  )
}

export function useUI() {
  const ctx = useContext(UIContext)
  if (!ctx) throw new Error('useUI must be used within a UIProvider')
  return ctx
}

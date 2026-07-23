import { useTasks } from '../context/TaskContext.jsx'

export default function StatsCards() {
  const { stats } = useTasks()
  const total = Math.max(stats.total, 1)

  const cards = [
    {
      label: 'In Progress',
      value: stats.inProgress,
      barClass: 'bg-primary',
      textClass: 'text-primary',
      widthPct: Math.round((stats.inProgress / total) * 100),
    },
    {
      label: 'Pending Review',
      value: stats.pendingReview,
      barClass: 'bg-tertiary',
      textClass: 'text-tertiary',
      widthPct: Math.round((stats.pendingReview / total) * 100),
    },
    {
      label: 'Urgent Blockers',
      value: stats.urgent,
      barClass: 'bg-error',
      textClass: 'text-error',
      widthPct: Math.round((stats.urgent / total) * 100),
      highlight: true,
    },
  ]

  return (
    <div className="grid grid-cols-1 sm:grid-cols-3 gap-6 mb-8">
      {cards.map((card) => (
        <div
          key={card.label}
          className={`bg-surface-container-lowest p-6 rounded-2xl shadow-card border flex flex-col gap-1 ${
            card.highlight ? 'border-error/20' : 'border-outline-variant/20'
          }`}
        >
          <span className={`text-label-sm uppercase tracking-widest font-bold ${card.textClass}`}>
            {card.label}
          </span>
          <span className="text-[40px] leading-tight font-bold font-display text-on-surface">
            {String(card.value).padStart(2, '0')}
          </span>
          <div className="w-full bg-surface-variant h-2 rounded-full mt-2 overflow-hidden">
            <div
              className={`h-full rounded-full ${card.barClass} transition-all duration-500`}
              style={{ width: `${Math.min(100, card.widthPct)}%` }}
            />
          </div>
        </div>
      ))}
    </div>
  )
}

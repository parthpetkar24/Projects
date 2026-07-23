import { useEffect, useState } from 'react'
import Icon from './Icon.jsx'
import { probabilityLabel } from '../lib/taskUtils.js'

const RADIUS = 80
const CIRCUMFERENCE = 2 * Math.PI * RADIUS

export default function CompletionGauge({ percent, tasksLeft }) {
  const [animatedPercent, setAnimatedPercent] = useState(0)

  useEffect(() => {
    const frame = requestAnimationFrame(() => setAnimatedPercent(percent))
    return () => cancelAnimationFrame(frame)
  }, [percent])

  const offset = CIRCUMFERENCE - (animatedPercent / 100) * CIRCUMFERENCE

  return (
    <section className="col-span-12 md:col-span-5 bg-primary rounded-[32px] p-8 text-on-primary relative overflow-hidden flex flex-col items-center justify-center text-center shadow-xl">
      <div className="absolute -top-12 -right-12 w-48 h-48 bg-inverse-on-surface/10 rounded-full blur-2xl" />
      <div className="absolute -bottom-8 -left-8 w-32 h-32 bg-secondary-container/20 rounded-full blur-xl" />

      <h3 className="font-display text-headline-md mb-8 z-10">Finish Probability</h3>

      <div className="relative w-48 h-48 flex items-center justify-center z-10">
        <svg className="w-full h-full -rotate-90" viewBox="0 0 192 192">
          <circle
            className="text-inverse-on-surface/20"
            cx="96"
            cy="96"
            r={RADIUS}
            fill="transparent"
            stroke="currentColor"
            strokeWidth="12"
          />
          <circle
            className="text-tertiary-fixed-dim drop-shadow-[0_0_8px_rgba(109,254,156,0.6)]"
            cx="96"
            cy="96"
            r={RADIUS}
            fill="transparent"
            stroke="currentColor"
            strokeWidth="12"
            strokeLinecap="round"
            strokeDasharray={CIRCUMFERENCE}
            strokeDashoffset={offset}
            style={{ transition: 'stroke-dashoffset 1.4s cubic-bezier(0.16, 1, 0.3, 1)' }}
          />
        </svg>
        <div className="absolute flex flex-col items-center">
          <span className="text-5xl font-bold font-display">{percent}%</span>
          <span className="text-sm font-label-md uppercase tracking-wider opacity-80">
            {probabilityLabel(percent)}
          </span>
        </div>
      </div>

      <p className="mt-8 font-body-md text-body-md z-10 leading-relaxed opacity-90">
        {tasksLeft > 0
          ? `Based on your momentum, you're on track to wrap up your ${tasksLeft} remaining task${
              tasksLeft === 1 ? '' : 's'
            } today. Keep it up!`
          : 'All caught up! Nothing left on your plate for today.'}
      </p>

      <div className="mt-6 p-4 bg-inverse-on-surface/10 rounded-2xl backdrop-blur-sm z-10 flex items-center gap-3">
        <Icon name="auto_awesome" className="text-tertiary-fixed-dim" />
        <span className="text-sm font-label-md">
          {percent >= 70 ? 'Peak performance detected' : 'Steady progress detected'}
        </span>
      </div>
    </section>
  )
}

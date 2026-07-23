export default function Icon({ name, className = '', filled = false, size }) {
  return (
    <span
      className={`material-symbols-outlined select-none ${className}`}
      style={{
        fontVariationSettings: `'FILL' ${filled ? 1 : 0}, 'wght' 400, 'GRAD' 0, 'opsz' 24`,
        ...(size ? { fontSize: size } : {}),
      }}
      aria-hidden="true"
    >
      {name}
    </span>
  )
}

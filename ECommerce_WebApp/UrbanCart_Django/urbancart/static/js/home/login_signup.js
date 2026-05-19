  /* ── State ──────────────────────────────────────────────── */
  let currentAccount = 'user';
  let currentMode    = 'login';

  const HEADINGS = {
    'user-login':   { h: 'Welcome back',      s: 'Log in to your UrbanCart account to continue shopping.' },
    'user-signup':  { h: 'Join UrbanCart',    s: 'Create your free account and start exploring.' },
    'seller-login': { h: 'Seller Hub Login',  s: 'Access your store dashboard and manage your listings.' },
    'seller-signup':{ h: 'Become a Seller',   s: 'Set up your store in minutes and reach thousands of buyers.' },
  };

  /* ── Switch account type (User ↔ Seller) ───────────────── */
  function switchAccount(type) {
    if (currentAccount === type) return;
    currentAccount = type;

    document.getElementById('tab-user').classList.toggle('active', type === 'user');
    document.getElementById('tab-user').setAttribute('aria-selected', type === 'user');
    document.getElementById('tab-seller').classList.toggle('active', type === 'seller');
    document.getElementById('tab-seller').setAttribute('aria-selected', type === 'seller');

    document.getElementById('aside-user').classList.toggle('hidden', type !== 'user');
    document.getElementById('aside-seller').classList.toggle('hidden', type === 'user');

    updateForm();
  }

  /* ── Switch login/signup mode ───────────────────────────── */
  function switchMode(mode) {
    if (currentMode === mode) return;
    currentMode = mode;

    document.getElementById('mode-login').classList.toggle('active', mode === 'login');
    document.getElementById('mode-signup').classList.toggle('active', mode === 'signup');

    updateForm();
  }

  /* ── Update visible form state & headings ────────────────── */
  function updateForm() {
    const key = currentAccount + '-' + currentMode;

    /* Hide all form states */
    document.querySelectorAll('.form-state').forEach(el => el.classList.add('hidden'));

    /* Show current */
    const target = document.getElementById('state-' + key);
    if (target) {
      target.classList.remove('hidden');
      /* Re-trigger animation */
      target.style.animation = 'none';
      target.offsetHeight;
      target.style.animation = '';
    }

    /* Update headings */
    const copy = HEADINGS[key];
    if (copy) {
      document.getElementById('form-heading').textContent    = copy.h;
      document.getElementById('form-subheading').textContent = copy.s;
    }
  }

  /* ── Password visibility toggle ─────────────────────────── */
  function togglePw(inputId, btn) {
    const input = document.getElementById(inputId);
    const icon  = btn.querySelector('.material-symbols-outlined');
    if (input.type === 'password') {
      input.type   = 'text';
      icon.textContent = 'visibility_off';
    } else {
      input.type   = 'password';
      icon.textContent = 'visibility';
    }
  }

  /* ── Fix: field-icon colour on focus ────────────────────── */
  document.querySelectorAll('.field-wrap input').forEach(input => {
    input.addEventListener('focus',  () => {
      const icon = input.previousElementSibling;
      if (icon && icon.classList.contains('field-icon')) {
        icon.style.color = 'rgb(var(--color-primary))';
      }
    });
    input.addEventListener('blur', () => {
      const icon = input.previousElementSibling;
      if (icon && icon.classList.contains('field-icon')) {
        icon.style.color = '';
      }
    });
  });
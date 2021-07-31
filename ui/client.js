function start() {
  for(i=0;i<8;i++) {
    createWorker()
  }
}

function escapeHtml(unsafe) {
    return unsafe.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/'/g, "&#039;");
}

window.logDiff = (san,out,og) => {
  var logs = document.getElementById('logs');
  var msg = document.createElement('div');
  msg.innerHTML = `
  <h1>======= CRASH========</h1><br>
  <h2>Orignal: ${escapeHtml(og)}</h2><br>
  <h2>Sanitized: ${escapeHtml(san)}</h2><br>
  <h2>Output: ${escapeHtml(out)}</h2><br>
  <h1>===============================</h1><br>
  `
  logs.appendChild(msg)
}

function createWorker() {
    var iframe = document.createElement('iframe');
    iframe.srcdoc = `
    <head>
      <title>Fuzz Worker</title>
      <script src="https://cure53.de/purify.js"></script>
      <script src='/ui/worker.js'></script>
    </head>
    <body>
    </body>
    `
    document.getElementById('frames').appendChild(iframe);
}

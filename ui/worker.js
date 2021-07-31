function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms))
}

function handleDiff(san,out,og) {
  if (san != out) {
    parent.logDiff(san,out,og)
  }
}

function genDiff(html) {
  var doll = document.createElement('div').attachShadow({mode:'open'})
  var sanI = DOMPurify.sanitize(html)
  doll.innerHTML = sanI
  handleDiff(sanI,doll.innerHTML,html)
}

async function main() {
  while (1) {
    var r = await fetch('/api/html')
    var j = await r.json()
    genDiff(j.html)
    await sleep(100)
  }
}

main()

const testFolder = './';
const fs = require('fs');
addr = 0
resFile = "0x700000_webai.bin"
try {
  fs.unlinkSync(resFile)
} catch (e) { }

res = {}
files = fs.readdirSync(testFolder)
files.forEach(file => {
  if (file == 'main.js' || file == 'go.sh') return
  var size = fs.statSync(file).size;
  binary = fs.readFileSync(file);
  fs.appendFileSync(resFile, binary, "binary")
  res[file] = [addr, size]
  addr += size
});
console.log("res=" + JSON.stringify(res))

startAddr = 0x700000
console.log("bgn address: ", "0x" + startAddr.toString(16))
console.log("end address: ", "0x" + (startAddr + addr).toString(16))

space = (13631487 - startAddr - addr)
space = parseInt(space / 1024 * 10) / 10
console.log("free space:", space + "KBytes")

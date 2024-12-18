const j = require(process.argv[2]);
let d = { 'END': -Infinity }, q = ['START'];
Object.keys(j).forEach(k => d[k] = -Infinity);
d['START'] = 0;

while (q.length) {
  let u = q.shift();
  for (let v in j[u]) {
    if (d[u] >= d[v]) {
      d[v] = d[u] + 1;
      q.push(v);
    }
  }
}
console.log(d['END'] - 1);
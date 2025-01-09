const fs = require('fs');

function parseMap(input) {
  return input.split('\n').map(row => row.split('').map(Number));
}

function dfs(map, x, y, target) {
  if (x < 0 || y < 0 || x >= map.length || y >= map[0].length || map[x][y] !== target) return 0;
  if (target === 9) return 1;
  const nextTarget = target + 1;
  map[x][y] = -1;
  let count = dfs(map, x + 1, y, nextTarget)
    + dfs(map, x - 1, y, nextTarget)
    + dfs(map, x, y + 1, nextTarget)
    + dfs(map, x, y - 1, nextTarget);
  map[x][y] = target;
  return count;
}

function sumTrailheadScores(input) {
  let map = parseMap(input);
  let score = 0;
  for (let i = 0; i < map.length; i++) {
    for (let j = 0; j < map[0].length; j++) {
      if (map[i][j] === 0) score += dfs(map, i, j, 0);
    }
  }
  return score;
}

fs.readFile('Lists/data_10.txt', 'utf8', (err, data) => {
  if (err) throw err;
  console.log(sumTrailheadScores(data.trim()));
});

const fs = require('fs');

function transformStones(initialStones, blinks) {
    let stones = [...initialStones];

    for (let blink = 0; blink < blinks; blink++) {
        let nextStones = [];

        for (let stone of stones) {
            if (stone === 0) {
                nextStones.push(1);
            } else if (stone.toString().length % 2 === 0) {
                let str = stone.toString();
                let mid = str.length / 2;
                let left = parseInt(str.slice(0, mid), 10);
                let right = parseInt(str.slice(mid), 10);
                nextStones.push(left, right);
            } else {
                nextStones.push(stone * 2024);
            }
        }

        stones = nextStones;
    }

    return stones.length;
}


fs.readFile('Lists/data_11.txt', 'utf8', (err, data) => {
    if (err) {
        console.error('Error reading the file:', err);
        return;
    }

    const initialStones = data.trim().split(/\s+/).map(Number);
    const blinks = 25;

    const result = transformStones(initialStones, blinks);
    console.log(`Number of stones after ${blinks} blinks:`, result);
});


const result = transformStones(initialStones, blinks);
console.log(`Number of stones after ${blinks} blinks:`, result);

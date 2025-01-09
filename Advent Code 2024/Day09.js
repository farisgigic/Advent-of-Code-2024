const fs = require('fs');

function parseDiskMap(diskMap) {
    const result = [];
    let fileID = 0;

    for (let i = 0; i < diskMap.length; i += 2) {
        const fileLen = parseInt(diskMap[i]);
        const freeSpace = parseInt(diskMap[i + 1]);

        for (let j = 0; j < fileLen; j++) result.push(fileID);
        for (let j = 0; j < freeSpace; j++) result.push('.');

        fileID++;
    }

    return result;
}

function compactDisk(disk) {
    const compacted = disk.filter((block) => block !== '.'); // Remove free spaces
    while (compacted.length < disk.length) compacted.push('.');
    return compacted;
}

function calculateChecksum(disk) {
    let checksum = 0;
    disk.forEach((block, position) => {
        if (block !== '.') {
            checksum += position * parseInt(block);
        }
    });
    return checksum;
}

function main() {
    const diskMap = fs.readFileSync("Lists/data9.txt", "utf-8").trim();

    let disk = parseDiskMap(diskMap);
    console.log("Initial Disk:", disk.join(''));

    disk = compactDisk(disk);
    console.log("Compacted Disk:", disk.join(''));

    const checksum = calculateChecksum(disk);
    console.log("Checksum:", checksum);
}

main();

const fs = require("fs");

const getInput = () => {
    return fs.readFileSync(__dirname + "/input.txt", "utf-8");
};

const splitLines = (input) => {
    return input.trim().split("\n");
};

const splitRound = (input) => {
    let obj = {};
    let parts = input.split(",");
    parts.forEach((element) => {
        let exploded = element.trim().split(" ");
        obj[exploded[1]] = Number(exploded[0]);
    });
    return obj;
};

const splitGames = (input) => {
    return input.split(": ")[1].split("; ").map(splitRound);
};

const checkAlwaysSmaller = (input) => {
    let maxValues = {
        red: 12,
        green: 13,
        blue: 14,
    };
    let checked = input.map((element) => {
        for (const [key, value] of Object.entries(element)) {
            if (maxValues[key] < value) return false;
        }
        return true;
    });

    return checked.reduce((a, b) => a && b, true);
};

const checkMinimumCubes = (input) => {
    let maxCubes = {
        red: 0,
        green: 0,
        blue: 0,
    };
    input.map((element) => {
        for (const [key, value] of Object.entries(element)) {
            if (maxCubes[key] < value) maxCubes[key] = value;
        }
    });

    return maxCubes.red * maxCubes.green * maxCubes.blue;
};

const firstTask = (input) => {
    return splitLines(input)
        .map(splitGames)
        .map(checkAlwaysSmaller)
        .reduce((acc, curr, index) => (curr ? acc + index + 1 : acc), 0);
};

const secondTask = (input) => {
    return splitLines(input)
        .map(splitGames)
        .map(checkMinimumCubes)
        .reduce((acc, curr) => acc + curr, 0);
};

const allFileContents = getInput();
let answer1 = firstTask(allFileContents);
let answer2 = secondTask(allFileContents);
console.log("Advent of Code 2023 Day 2");
console.log(`Result to part 1 is ${answer1}`);
console.log(`Result to part 2 is ${answer2}`);

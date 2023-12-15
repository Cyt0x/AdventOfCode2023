const fs = require("fs");

const getInput = () => {
    return fs.readFileSync(__dirname + "/input.txt", "utf-8").split("\n\n");
};

const greatestCommonDivisor = (a, b) => {
    return !b ? a : greatestCommonDivisor(b, a % b);
};

const leastCommonMultiple = (a, b) => {
    return (a * b) / greatestCommonDivisor(a, b);
};

const calculateSteps = (startLocation, endLocation) => {
    let allStartLocations = Object.keys(mapping).filter((line) =>
        line.match(new RegExp(startLocation))
    );
    let steps = Array(allStartLocations.length).fill(0);
    allStartLocations.forEach((location, index) => {
        while (!location.match(new RegExp(endLocation))) {
            let currentDirection = direction[steps[index] % direction.length];
            location = mapping[location][currentDirection];
            steps[index] += 1;
        }
    });
    return steps.reduce(leastCommonMultiple);
};

let input = getInput();
let direction = input[0];
let mapping = input[1].split("\n").reduce((acc, curr) => {
    let [key, L, R] = curr.match(/[A-Z]+/g);
    acc[key] = { L, R };
    return acc;
}, {});

let answer1 = calculateSteps("AAA", "ZZZ");
let answer2 = calculateSteps("A$", "Z$");

console.log("Advent of Code 2023 Day 7");
console.log(`Result to part 1 is ${answer1}`);
console.log(`Result to part 2 is ${answer2}`);

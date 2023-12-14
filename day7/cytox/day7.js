const fs = require("fs");

const getInput = () => {
    return fs.readFileSync(__dirname + "/input.txt", "utf-8");
};

const cardRankings = "23456789TJQKA";
const cardRankingsWithJokers = "J23456789TQKA";

const splitLines = (input) => {
    return input.trim().split("\n");
};

const parseHand = (input) => {
    let hand = input.split(" ")[0];
    let bid = Number(input.split(" ")[1]);
    return [hand, bid];
};

const sortHands = (handA, handB, jokers) => {
    let valueHandA = calculateHandRank(handA, jokers);
    let valueHandB = calculateHandRank(handB, jokers);
    if (valueHandA > valueHandB) return -1;
    if (valueHandA < valueHandB) return 1;
    return calculateTieBreaker(handA, handB, jokers);
};

const calculateHandRank = (hand, jokers) => {
    let handSet = calculateHandSets(hand, jokers);
    let sortedHand = handSet.sort((a, b) => b - a);
    let handType = sortedHand[0];

    if (handType === 5) return 7;
    if (handType === 4) return 6;
    if (handType === 3 && sortedHand[1] === 2) return 5;
    if (handType === 3) return 4;
    if (handType === 2 && sortedHand[1] === 2) return 3;
    if (handType === 2) return 2;
    return 1;
};

const calculateHandSets = (hand, jokers) => {
    let handSets = Array(cardRankings.length).fill(0);
    let rankings = jokers ? cardRankingsWithJokers : cardRankings;
    for (card of hand) {
        handSets[rankings.indexOf(card)] += 1;
    }
    if (jokers) {
        let jokersCount = (hand.match(/J/g) || []).length;
        if (jokersCount > 0 && jokersCount < 5) {
            handSets[0] = 0;
            let i = handSets.indexOf(Math.max(...handSets));
            if (i > 0) handSets[i] += jokersCount;
        }
    }
    return handSets;
};

const calculateTieBreaker = (handA, handB, jokers) => {
    let rankings = jokers ? cardRankingsWithJokers : cardRankings;
    for (let i = 0; i < handA.length; i++) {
        let cardA = rankings.indexOf(handA[i]);
        let cardB = rankings.indexOf(handB[i]);

        if (cardA > cardB) return -1;
        if (cardA < cardB) return 1;
    }
    return 0;
};

const firstTask = (input) => {
    return splitLines(input)
        .map(parseHand)
        .sort((a, b) => {
            let handA = a[0];
            let handB = b[0];
            return sortHands(handB, handA, false);
        })
        .reduce((acc, curr, index) => {
            let bid = curr[1];
            acc += bid * (index + 1);
            return acc;
        }, 0);
};

const secondTask = (input) => {
    return splitLines(input)
        .map(parseHand)
        .sort((a, b) => {
            let handA = a[0];
            let handB = b[0];
            return sortHands(handB, handA, true);
        })
        .reduce((acc, curr, index) => {
            let bid = curr[1];
            acc += bid * (index + 1);
            return acc;
        }, 0);
};

const allFileContents = getInput();
let answer1 = firstTask(allFileContents);
let answer2 = secondTask(allFileContents);

console.log("Advent of Code 2023 Day 7");
console.log(`Result to part 1 is ${answer1}`);
console.log(`Result to part 2 is ${answer2}`);

function findMaxSubstring(strings) {
    let shortestString = strings.reduce((minStr, currentStr) => currentStr.length < minStr.length ? currentStr : minStr, strings[0]);
    let shortestLength = shortestString.length;

    let indices = Array.from({ length: 2 }, () => new Array(shortestLength).fill(0));

    for (let i = 0; i < shortestLength; i++) {
        for (let j = i + 1; j <= shortestLength; j++) {
            let substring = shortestString.slice(i, j);

            if (strings.every(str => str.includes(substring))) {
                indices[0][i] = i;
                indices[1][i] = j - i;
            } else break;
        }
    }

    let lengthOfMaxSubstring = Math.max(...indices[1]);
    let index = indices[1].findIndex(len => len === lengthOfMaxSubstring);

    let result = shortestString.slice(indices[0][index], indices[0][index] + indices[1][index]);
    return result;
}

let strings = [""];
console.log(findMaxSubstring(strings));

const args = process.argv.slice(2);

if (args.length === 0)
    console.log('');
else console.log(findMaxSubstring(args));
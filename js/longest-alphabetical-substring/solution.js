function longest(str) {
    /*
    Once you've found a substring check if its length is greater than or equal to 50% of the input string's length. If it is, then no need to continue checking because that's the longest alphabetical substring to first occur.
    */

    // No need to go through entire function if single character input.
    if (str.length == 1) {
        return str;
    }

    let longestAlphaSub = str[0];
    let stagingSub = str[0];

    for (let x = 1; x < str.length + 1; x++) {
        console.log(str[x]);
        if (str[x] >= stagingSub.slice(-1)) {
            stagingSub += str[x];
        } else {
            if (stagingSub.length > longestAlphaSub.length) {
                longestAlphaSub = stagingSub;
            }

            stagingSub = str[x];
        }
    }

    return longestAlphaSub;
}

// console.log(longest('asdfaaaabbbbcttavvfffffdf'));
console.log(longest('nab'));
// console.log(longest('a'));

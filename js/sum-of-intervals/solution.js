function sumIntervals(intervals) {
  let outputArr = [];

  intervals.forEach(([a, b]) => {
    // Don't want to increment up to b. We want the different between a and b.
    for (let i = a; i < b; i++) {
      outputArr.push(i);
    }
  });

  // Only retain unique values in the array.
  outputArr = [...new Set(outputArr)];

  return outputArr.length;
}

console.log(
  sumIntervals([
    [1, 5],
    [10, 20],
    [1, 6],
    [16, 19],
    [5, 11],
  ])
);

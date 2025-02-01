let S = 990, I = 10, R = 0, beta = 0.3, gamma = 0.1, N = S + I + R, days = 100;

console.log("Day\tS\tI\tR");
for (let t = 0; t < days; t++) {
    let newInfected = (beta * S * I) / N;
    let newRecovered = gamma * I;

    S -= newInfected;
    I += newInfected - newRecovered;
    R += newRecovered;

    console.log(`${t}\t${S.toFixed(2)}\t${I.toFixed(2)}\t${R.toFixed(2)}`);
}


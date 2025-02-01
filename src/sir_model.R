SIR <- function(S, I, R, beta, gamma, days) {
  results <- data.frame(Day=0:days, S=0, I=0, R=0)
  results[1,] <- c(0, S, I, R)
  
  for (t in 1:days) {
    new_infected <- (beta * S * I) / (S + I + R)
    new_recovered <- gamma * I

    S <- S - new_infected
    I <- I + new_infected - new_recovered
    R <- R + new_recovered

    results[t+1,] <- c(t, S, I, R)
  }
  return(results)
}

data <- SIR(990, 10, 0, 0.3, 0.1, 100)
print(data)


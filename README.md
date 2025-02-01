# Infectious Disease Modeling (SIR Model)

This repository contains implementations of the Susceptible-Infected-Recovered (SIR) model, a fundamental epidemiological model used to study infectious disease spread. The model is implemented in multiple programming languages: **Python, C++, R, Java, and JavaScript (Node.js)**.

## Features
- **Multi-language support**: The same SIR model is implemented in **Python, C++, R, Java, and JavaScript**.
- **Graphical output**: The Python implementation provides a **graphical representation** of the SIR model using Matplotlib.
- **Command-line output**: The C++, R, Java, and JavaScript implementations print numerical results in a tabular format.
- **Open-source tools**: Uses only open-source programming languages and tools.

## SIR Model Overview
The **SIR Model** divides a population into three compartments:
- **S (Susceptible)**: Individuals who can be infected.
- **I (Infected)**: Individuals who have the disease and can spread it.
- **R (Recovered)**: Individuals who have recovered and are immune.

The model uses the following differential equations:

```math
\frac{dS}{dt} = -\beta \frac{S I}{N}
```
```math
\frac{dI}{dt} = \beta \frac{S I}{N} - \gamma I
```
```math
\frac{dR}{dt} = \gamma I
```

where:
- $$\beta$$ (beta) is the infection rate
- $$\gamma$$ (gamma) is the recovery rate
- N is the total population

## Set Up Your Development Environment

### 1. Install Required Software:
```
sudo apt update && sudo apt upgrade -y
sudo apt install git build-essential cmake python3 python3-pip r-base openjdk-17-jdk nodejs npm -y
```
- `git` → Version control system.
- `build-essential` → Compiler tools for C++.
- `cmake` → Build system for C++ projects.
- `python3, python3-pip` → Python programming environment.
- `r-base` → R language for statistical computing.
- `openjdk-17-jdk` → Java Development Kit.
- `nodejs, npm` → JavaScript runtime and package manager.

### 2. Clone the Repository Locally:
```
git clone https://github.com/MenakaGodakanda/infectious-disease-models.git
cd infectious-disease-models
```

## Running the SIR Model Implementations

### Python
```
python3 src/sir_model.py
```
Output: Generates a graph of S, I, and R populations over time.
![Screenshot 2025-02-02 051039](https://github.com/user-attachments/assets/5b61cd2a-edb4-42aa-a1ca-82665e0fc5ba)

Running `python3 src/sir_model.py` produces a graph like this:
- Graph (Matplotlib):
  - Blue Line → Susceptible (S)
  - Orange Line → Infected (I)
  - Green Line → Recovered (R)
- It shows how **Susceptible decreases, Infected rises and falls**, and **Recovered increases** over time.

### C++
```
g++ src/sir_model.cpp -o sir_model
./sir_model
```
Output: Prints a numerical table of S, I, and R values over 100 days.
![Screenshot 2025-02-02 051123](https://github.com/user-attachments/assets/47de1ceb-aad7-4861-b3d6-0ffe131c614e)
![Screenshot 2025-02-02 051158](https://github.com/user-attachments/assets/e6411eb9-d854-4f51-a145-21292a318a10)

- The **Susceptible (S)** population decreases.
- The **Infected (I)** population initially rises and then declines.
- The **Recovered (R)** population increases.

### R
```
Rscript src/sir_model.R
```
Output: Prints a numerical table of S, I, and R values.
![Screenshot 2025-02-02 051206](https://github.com/user-attachments/assets/88b81fc4-2dda-4727-a28d-850977a5ab5b)
![Screenshot 2025-02-02 051217](https://github.com/user-attachments/assets/a9e84ec1-311b-4d0c-8911-f2e776e2f2d5)

- Similar to C++ output but formatted as a data table.

### Java
```
javac src/SIRModel.java
java -cp src SIRModel
```
Output: Prints a numerical table of S, I, and R values.
![Screenshot 2025-02-02 051248](https://github.com/user-attachments/assets/20bf48c5-733c-4d08-ac30-e711207baae2)

![Screenshot 2025-02-02 051257](https://github.com/user-attachments/assets/0ec6e136-019b-4412-a5bf-51a99f221ef5)
- Same logic as Python & C++, but formatted for Java.

### JavaScript (Node.js)
```
node src/sir_model.js
```
Output: Prints a numerical table of S, I, and R values.
![Screenshot 2025-02-02 051332](https://github.com/user-attachments/assets/92e3402d-5235-49dc-8023-f909d7c12aaa)
![Screenshot 2025-02-02 051341](https://github.com/user-attachments/assets/8b73822e-1e6f-4540-afaa-8365ddddf35a)

- The same result, but runs on Node.js.

## Conclusion
Each language produces similar results:
- The susceptible (S) population decreases.
- The infected (I) population rises at first, then declines.
- The recovered (R) population increases.
This validates that our SIR Model is working correctly across multiple programming languages!

## Project Structure
```
infectious-disease-models/
│-- src/          # Source code (Python, C++, R, Java, JavaScript)
│   │-- sir_model.py
│   │-- sir_model.cpp
│   │-- sir_model.R
│   │-- SIRModel.java
│   │-- sir_model.js
│-- tests/        # Unit tests
│-- README.md     # Project overview
```

## License
This project is licensed under the MIT License.

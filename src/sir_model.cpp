#include <iostream>
#include <vector>

int main() {
    double beta = 0.3, gamma = 0.1;
    double S = 990, I = 10, R = 0, N = S + I + R;
    int days = 100;

    std::vector<double> S_list, I_list, R_list;
    
    for (int t = 0; t < days; ++t) {
        double new_infected = (beta * S * I) / N;
        double new_recovered = gamma * I;

        S -= new_infected;
        I += new_infected - new_recovered;
        R += new_recovered;

        S_list.push_back(S);
        I_list.push_back(I);
        R_list.push_back(R);
    }

    std::cout << "Day\tS\tI\tR\n";
    for (int i = 0; i < days; i++) {
        std::cout << i << "\t" << S_list[i] << "\t" << I_list[i] << "\t" << R_list[i] << "\n";
    }
    
    return 0;
}


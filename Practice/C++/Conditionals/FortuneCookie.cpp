#include <iostream>
#include <cstdlib>

int main() {
    // Seed
    srand(time(NULL));

    int randomNumber = std::rand();
    int finalnumber = randomNumber % 6;

    int luckyNumber1 = std::rand() % 50;
    int luckyNumber2 = std::rand() % 50;
    int luckyNumber3 = std::rand() % 50;
    int luckyNumber4 = std::rand() % 50;
    int luckyNumber5 = std::rand() % 50;
    int luckyNumber6 = std::rand() % 50;

    if (finalnumber == 1) {
        std::cout << "Don't pursue happiness - create it.";
    } else if (finalnumber == 2) {
        std::cout << "All things are difficult before they are easy.";
    } else if (finalnumber == 3) {
        std::cout << "The early bird gets the worm, but the second mouse gets the cheese.";
    } else if (finalnumber == 4) {
        std::cout << "Someone in your life needs a letter from you.";
    } else if (finalnumber == 5) {
        std::cout << "The fortune you search for is in another cookie.";
    } else {
        std::cout << "Help! I'm being held prisoner in a Chinese bakery!";
    }

    std::cout << "\nLucky number: "<< luckyNumber1 << luckyNumber2 << luckyNumber3 << luckyNumber4 << luckyNumber5 << luckyNumber6;

    return 0;
}
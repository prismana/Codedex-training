#include <iostream>

int main() {
    int age = 45;
    bool citizen = true;
    bool registered = false;

    if (age >= 18 && citizen && registered) {
        std::cout << "You can vote!";
    } else if (age < 18) {
        std::cout << "You are not old enough to vote.";
    } else if (citizen == false) {
        std::cout << "You are not eligible to vote";
    } else if (citizen == false) {
        std::cout << "You need to register first.";
    } else {
        std::cout << "You have not meet the requirements";
    }

    return 0;
}
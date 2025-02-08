#include <iostream>
#include <cstdlib>

int main(int argc, char const *argv[])
{
	srand(time(NULL));

	int num = std::rand() % 2;

	if (num > 0.5) {
		std::cout << "heads\n";
	}
	else {
		std::cout << "Talils\n"
	}
	
	return 0;
}
#include <iostream>
#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
#using namespace std;


int main()
{
	const double pi = 4 * atan(1.0);
	int x = 22;
	{
		int x = 44;
		cout << "Integer x = " << x << endl;
	}
	cout << "Integer x = " << x << endl;

	{
		int x = 66;
		cout << "Integer x = " << x << endl;
	}
	system("pause");

	return 0;

}
#include <iostream>

using namespace std;

int main()
{
	long long key;
	string plain_text = "", cipher_text = "";
	cin >> key;
	cin >> plain_text;
	
	for (int i = 0; i < plain_text.length(); i++)
	{
		cipher_text += (((plain_text[i] - 65 + key) % 26) + 65);
	}

	cout << cipher_text;

}

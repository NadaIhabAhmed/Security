#include <iostream>
#include <iomanip>    
using namespace std;
   
int main()
{
	//parsing 
	string key;
	string plain_text = "", v_cipher_text = "", T_cipher_text = "";
	int no_pad = 0;
	cin >> key;
	cin >> plain_text;
	
	//checking the lenght
	if(key.length() < plain_text.length())
	{
		int i = 0;
		no_pad = 1;
		while(key.length() < plain_text.length())
		{
			key += key[i];
			i++;
		}
	}
	
	//vigener
	for (int i = 0; i < plain_text.length(); i++)
	{
		v_cipher_text += (((plain_text[i] - 65 + key[i] - 65) % 26) + 65);
	}
	
	//VerNaM
	for(int i = 0; i < plain_text.length(); i++)
	{
		T_cipher_text += plain_text[i] ^ key[i];
	}
	
	
	// output 
	cout << "Vigenere: " << v_cipher_text <<"\n";
	cout << "Vernam: ";
	for(int i = 0; i < plain_text.length(); i++)
	{
		cout << hex << uppercase << setw(2) << setfill('0') << (int)T_cipher_text[i];
	}
	if(no_pad == 0)
	{
		cout << "\nOne-Time Pad: " << "YES";
		
	}
	else
	{
		cout << "\nOne-Time Pad: " << "NO";
		
	}
	
}

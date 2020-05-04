#include <iostream>

using namespace std;

class Solution {
public:
    int findComplement(int num) {
        
    }
};

int reverse(int num)
{
    int r, rev;
    while(num > 0)
    {
        r = num % 10;
        rev = rev * 10 + r;
        num = num / 10;
    }
    return rev;
}

int main()
{
    int  dec, rem;
    string bin;
    cin >> dec;
    while(dec > 0)
    {
        rem = dec % 2;
        dec = dec / 2;
    }
    bin = reverse(dec);

    for(int i = 0; i != '\n'; i++)
    {
        if(bin[i] == '0')
        {
            bin[i] = '1';
        }
        if(bin [i] == '1')
        {
            bin[i] == '0';
        }
    }
    
}
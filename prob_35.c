#include<stdio.h>

int IsPrime(long int number) {
    long int i;
    for (i=2; i<number; i++) {
        if (number % i == 0 && i != number) return 0;
    }
    return 1;
}

void main()
{

long int i;
long int j=0;
long int arr[1000];
long int sum = 0;

for(i=2; i < 10000; i++)
	{
		int result = IsPrime(i);
		if(result == 1)
		{
			arr[j] = i;
			j++;
		}
	}
}


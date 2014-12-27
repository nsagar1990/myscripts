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

/*for(i = 0; i <= j; i++)
{	
	sum = sum + arr[i];
	if(sum < 10000)
	{
		printf("%ld\n", sum);
	}
	else
	{
		break;
	}
	if(IsPrime(sum) == 1)
	/{
		if(sum < 1000)
		{
			printf("%d\n", sum);	
		}
	}

}*/

}


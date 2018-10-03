/*
** Author:		Brenton Moodley
** Language:	C
** Github		https://github.com/breakstate
*/

#include <stdio.h>

void	cats_bats_spiders(int i)
{
	if (!(i % 3) && !(i %5))
		printf("spiders");
	else if (!(i % 5))
		printf("bats");
	else if (!(i %3))
		printf("cats");
	printf("\n");
}

int main()
{
	for (int i = 1; i <= 100; i++)
	{
		printf("%d: ", i);
		cats_bats_spiders(i);
	}
	return (0);
}

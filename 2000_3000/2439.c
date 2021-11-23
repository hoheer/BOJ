#include <stdio.h>
int main() {
	int n;
	int k=1;
	int sum=0;
	scanf("%d",&n);

for(int i=n; i>=1; i--,k++) {
	sum=i;
	for(int i=2; i<=sum; i++) {
	printf("%c",' ');

	}
	for(int i=1;i<=k;i++) {
		printf("%c",'*');
	}
	printf("\n");
}
}

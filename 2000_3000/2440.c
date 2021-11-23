#include <stdio.h>
int main() {
	int n;
	int star=0;
	scanf("%d",&n);
for(int i=n;i>=1;i--) {
	star=i;
	for(int i=1;i<=star;i++){
		printf("%c",'*');
	}
	printf("\n");
}
}
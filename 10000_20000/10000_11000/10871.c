#include <stdio.h>


int main() {
	int n;
	int x;
	scanf("%d %d\n",&n,&x);
	int array[n];
	for(int i=0;i<n;i++) {
		scanf("%d",&array[i]);
	}
	for(int i=0;i<n;i++) {
		if (array[i]<x) printf("%d ",array[i]);
	}
}

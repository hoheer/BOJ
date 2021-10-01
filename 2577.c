#include <stdio.h>
int calcu (int number);
int main () {
	int number=0;
	int a,b,c;
	int array[3];
	int count=0;
		for (int i=0;i<3;i++) {
			scanf("%d",&array[i]);
		}
	number=array[0]*array[1]*array[2];
	count=calcu(number);
	//printf("%d",count);
		int a_array[count];
		int k=0;
		int mod=0;
			while(k<count) {
				mod=number%10;
				number=number/10;
				a_array[k]=mod;
				k++;
			}
	/*for (int i=0;i<count;i++) {
		printf("%d",a_array[i]);
	} */
	int b_array[10];
	for(int i=0;i<10;i++) {
		b_array[i]=0;
	}

	for(int i=0;i<count;i++) {
		switch (a_array[i]) {
				case 0:
				b_array[0]++;
				break;

				case 1:
				b_array[1]++;
				break;

				case 2:
				b_array[2]++;
				break;

				case 3:
				b_array[3]++;
				break;

				case 4:
				b_array[4]++;
				break;

				case 5:
				b_array[5]++;
				break;

				case 6:
				b_array[6]++;
				break;

				case 7:
				b_array[7]++;
				break;

				case 8:
				b_array[8]++;
				break;

				case 9:
				b_array[9]++;
				break;
		}
	}

	for (int i=0;i<10;i++) {
		printf("%d\n",b_array[i]);
	}




}

int calcu (int num) {
	int mod;
	int cnt=0;
		while(num>0) {
			num=num/10;
			cnt++;
		}
	return cnt;
}
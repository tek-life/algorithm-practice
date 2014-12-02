#include <stdio.h>

int array[9] = {3,1,4,8,5,6,12,32,24};

void main()
{
	int length=sizeof(array)/sizeof(array[0]);
	int min_pos,max_pos;
	int min,max;
	int base = 0;
	int scale = length;
	int i=0;
	int tmp;

	scale = length;
	for(;base<length/2; base++){
		min=array[base];
		max=array[base];
		min_pos = base;
		max_pos = base;
	 	for(i=base+1;i<(base+scale);i++){
			if(array[i]<min){
				min = array[i];
				min_pos = i;
			}
			if(array[i]>max){
				max = array[i];
				max_pos = i;
			}
		}

		tmp = array[base];
		array[base] = min;
		array[min_pos]= tmp;
		if(base == max_pos)
			max_pos = min_pos;

		tmp = array[base+scale-1];
		array[base+scale-1]=max;
		array[max_pos]=tmp;

		scale = scale-2;
	}
	for(i=0;i<length;i++)
		printf("%d ",array[i]);
	printf("\n");

}

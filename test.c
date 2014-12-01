#include <stdio.h>
int arr[10] = {1, 32, 48, 59, 23, 9, 7, 6, 0, 8};
void 
print_array(int array[], int length)
{
	int i = 0;
	for (; i < length; i++)
		printf("%d ", array[i]);
	printf("\n");
}
int 
insert_sort(int array[], int length)
{
	int temp, i, j, k;
	for (j = 1; j < length; j++) {
		temp = array[j];
		k = j;
		for (i = j - 1; i >= 0; i--) {
			if (temp < array[i]) {
				array[i + 1] = array[i];
				k = i;
			}
		}
		array[k] = temp;
		print_array(arr, 10);
	}
	return 0;
}

int 
quick_sort(int array[], int left, int right)
{
	if (left >= right)
		return 0;

	int i = right;
	int j = left;
	int temp = array[left];
	for (; i > left; i--) {
		if ((temp > array[i]) && (i > j)) {
			array[j] = array[i];
			array[i] = temp;
			j = i;
		} else if ((temp < array[i]) && (i < j)) {
			array[j] = array[i];
			array[i] = temp;
			j = i;
		}
	}
	array[j] = temp;
	quick_sort(array, left, j);
	quick_sort(array, j + 1, right);
	return 0;
}

int 
bubble_sort(int array[], int length)
{
	int temp, i, j = 0;
	for (i = 0; i < length; i++)
		for (j = i + 1; j < length; j++)
			if (array[i] > array[j]) {
				temp = array[i];
				array[i] = array[j];
				array[j] = temp;
			}
	for (i = 0; i < length; i++)
		printf("%d ", array[i]);
	return 0;
}

int insert_heap_sort(int array[], int i)
{

	int parent;
	int tmp;
	if(i==0)
		return;	
	
	parent = (i-1)/2;

	while(parent >=0){
		if(array[i]< array[parent])
		{
			tmp = array[i];
			array[i]=array[parent];
			array[parent] = tmp;		
		}
		else{
			break;
		}
		i= parent;
	        parent = (i - 1)/2;
	}

	return 0;
}
int del_heap_sort(int array[], int length)
{

	int lchild,rchild,parent,tmp,tmp_value;
	array[0] = array[length-1];
	parent = 0;
	lchild = parent*2 +1;
	rchild = parent*2 +2;
	while(lchild < length){
		if ((lchild<length) && (array[parent] >array[lchild])){
			if((rchild<length) && array[lchild] > array[rchild]){
				tmp = rchild;
			}else{
				tmp = lchild;
			}
		}else if(rchild<length && array[parent] > array[rchild])
			tmp = rchild;
		else{
			break;
		}

		tmp_value = array[parent];
		array[parent] = array[tmp];
		array[tmp] = tmp_value;
		parent = tmp;
		
		lchild = parent*2 +1;
		rchild = parent*2 +2;		
	}
	
	return 0;

}

int heap_sort(int array[], int length)
{

	int i=1;
	for(;i<length;i++)
		insert_heap_sort(array,i);
	for(i=10;i>0;i--){
		printf("%d \n",array[0]);
		del_heap_sort(array,i);
	}
	return 0;
}

int 
main()
{
	//int i;
	//scanf("%d", &i);
	//printf("%d\n", i);
	//bubble_sort(arr, 10);
	//quick_sort(arr, 0, 9);
	//insert_sort(arr, 10);
	heap_sort(arr, 10);
//	print_array(arr, 10);
	return 0;
}

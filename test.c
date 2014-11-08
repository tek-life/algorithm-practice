#include <stdio.h>
int arr[10] = {1, 3, 4, 5, 2, 9, 7, 6, 0, 8};
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

int 
main()
{
	//int i;
	//scanf("%d", &i);
	//printf("%d\n", i);
	//bubble_sort(arr, 10);
	quick_sort(arr, 0, 9);
	//insert_sort(arr, 10);
	print_array(arr, 10);
	return 0;
}

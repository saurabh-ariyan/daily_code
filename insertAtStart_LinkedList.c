#include <stdio.h>
#include <stdlib.h>

struct node {
  int data;
  struct node* next;
};

struct node* head;

//inserts the node at the begining of the node
void insert(int data_temp){
  struct node* temp = (struct node*)malloc(sizeof(struct node));
  temp->data = data_temp;
  temp->next = head;
  head = temp;
}

// prints the list up till the last node;
void print(){
  struct node* travel_pointer =head;
  printf("List is : " );
  while(travel_pointer){
    printf("%d  ", travel_pointer->data);
    travel_pointer = travel_pointer->next;
  }
  printf("\n");

}

int main(){
  head = NULL;
  int number, loop_var, data_temp;
  printf("How many number of links? \n");
  scanf("%d", &number);
  for (loop_var = 0; loop_var < number; loop_var++){
    printf("Enter the data : ");
    scanf("%d", &data_temp);
    insert(data_temp);
    print();
  }
}
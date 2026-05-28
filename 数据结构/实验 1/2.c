#define INITSIZE 100

typedef int  ElemType; 
typedef struct
{ElemType *data;
int length;
int listsize;}sqlist;

void InitList(sqlist *L)
{ElemType x;
L->data=(ElemType *)malloc(sizeof(ElemType)*INITSIZE);
L->length=0;
L->listsize=INITSIZE;
scanf("%d",&x);
while(x!=-1)
{L->data[L->length++]=x;
scanf("%d",&x);
}}

void List(sqlist *L)
{int i;
for(i=0;i<L->length;i++)
printf("%d",L->data[i]);
printf("\n");
}
void he(sqlist *A,sqlist *B,sqlist *C){
	int i,j,k;
	i=j=k=0;
	while(i<A->length&&j<B->length)
		if(A->data[i]<B->data[j]) C->data[k++]=A->data[i++];
		else C->data[k++]=B->data[j++];
	while(i<A->length) C->data[k++]=A->data[i++];
	while(j<B->length) C->data[k++]=B->data[j++];
	C->length=k;
}

main(){
	sqlist A,B,C;
	InitList(&A);InitList(&B);InitList(&C);
	List(&A);List(&B);he(&A,&B,&C);List(&C);

}

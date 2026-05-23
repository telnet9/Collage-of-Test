#define NULL 0
typedef int ElemType;
typedef struct node
{
ElemType data;
struct node *next
}slink;
slink *InitList(int n){
	slink * head,*p,*s;
	int i;
	p=head=(slink *)malloc(sizeof(slink));
	for(i=1;i<=n;i++)
	{s=(slink *)malloc(sizeof(slink));
	scanf("%d",&s->data);
	p->next=s;
	p=s;
	}
	p->next=NULL;
	return head;
}

void List(slink *head){
	slink *p;
	p=head->next;
	while(p!=NULL)
	{printf("%4d",p->data);
	p=p->next;
	}
	printf("\n");
}

int he(slink *L1,slink *L2){
	slink *head=(slink *)malloc(sizeof(slink));
	slink *p=head;
	slink *p1=L1->next;
	slink *p2=L2->next;
	while(p1!=NULL&&p2!=NULL){
		if(p1->data<=p2->data){
		p->next=p1;
		p1=p1->next;}
		else{
		p->next=p2;
		p2=p2->next;
		}
		p=p->next;

	}
if (p1 != NULL)
    p->next = p1;
else
    p->next = p2;
  	return head;
}

main(){
	slink *L1,*L2,*L3;
	L1=InitList(5);
	List(L1);
	L2=InitList(3);
	List(L2);
	L3=he(L1,L2);
	List(L3);
}

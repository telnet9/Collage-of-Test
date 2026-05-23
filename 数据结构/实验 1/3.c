#define null 0
typedef int ElemType;
typedef struct node
{ElemType data;
struct node *next;}slink;

slink *InitList(int n){
	int i;slink *p,*head,*s;
	p=head=(slink *)malloc(sizeof(slink));
	for(i=1;i<=n;i++){
		s=(slink *)malloc(sizeof(slink));
		scanf("%d",&s->data);
		p->next=s;
		p=s;
	}p->next=null;return head;
} 

void List(slink *head){
	slink *p;
	p=head->next;
	while(p!=null){
		printf("%d",p->data);
		p=p->next;
	}
	printf("\n");
}

int GetLen(slink *head){
	int n; slink *p;
	n=0;p=head->next;
	while(p!=null){n++;p=p->next;

	} return n;
}

void Insert(slink *head,int i,ElemType x){
	int j;slink *p,*s;
	if(i<1) return 0;
	p=head;j=0;
	while(p!=null&&j<i-1){
		p=p->next;j++;
	}
	if(p==null) return 0;
	s=(slink *)malloc (sizeof(slink));
	s->data=x;
	s->next=p->next;p->next=s;
	return 1;
}
void Delete(slink *head,int i,ElemType *e)
{slink *p,*q;int j;
if(i<1) return 0;p=head;j=0;
while(p->next!=null&&j<i-1){
	p=p->next;j++;
}
if(p->next==null) return 0;
q=p->next;
*e=q->data;
p->next=q->next;
free(q);return 1;
}
main(){
	int e,x;
	slink *head;
			printf("请输入链表初始长度");
		scanf("%d",&x);
				printf("请输入链表初始值");
	head=InitList(x);
		List(head);
				printf("链表长度");
	int n=GetLen(head);     
	
	printf("%d",n);
	printf("\n");
	int a,b;
		printf("请输入在链表中插入元素位数和数值");
	scanf("%d%d",&a,&b);

	Insert(head,a,b);

	List(head);
	
	Delete(head,2,&e);
	List(head);
}

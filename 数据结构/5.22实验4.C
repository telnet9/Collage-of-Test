#include<stdio.h> 
#define NULL 0
typedef char ElemType;
typedef struct node
{ElemType data;
struct node *lchild,*rchild;}BitNode;
BitNode *CreateTree(){
BitNode *T;ElemType x;
scanf("%c",&x);
if(x=='?') T=NULL;
else
{T=(BitNode*)malloc(sizeof(BitNode));
T->data=x;
T->lchild=CreateTree();
T->rchild=CreateTree();}
return T;
}

void PreOrder(BitNode *T){
    if(T)
    {printf("%c",T->data);
    PreOrder(T->lchild);
    PreOrder(T->rchild);}

}

void InOrder(BitNode *T){
    if(T)
    {
	InOrder(T->lchild);
    printf("%c",T->data);
    InOrder(T->rchild);}

}

void PostOrder(BitNode *T){
     if(T)
    {
	PostOrder(T->lchild);
    PostOrder(T->rchild);
    printf("%c",T->data);}
    

}
//背下来求深度和节点总数 !!! 
int Depth(BitNode *T){
	int h,h1,h2;
	if(T==NULL) h=0;
	else
	{h1=Depth(T->lchild);
	h2=Depth(T->rchild);
	h=(h1>h2?h1:h2)+1;} 
return h;
}

int NodeSum(BitNode *T){
 int n,n1,n2;
 if(T==NULL) n=0;
 else{
 n1=NodeSum(T->lchild);
 n2=NodeSum(T->rchild); 
n=n1+n2+1; 
}
return n; 
}

void zz(BitNode *T,int n){
	  if(T)
    {if(T->lchild==NULL&&T->rchild==NULL)
    printf("%c",T->data) ;
    else{
    	if(n>1) printf("(");
	zz(T->lchild,n+1);
    printf("%c",T->data);
    zz(T->rchild,n+1);
	if(n>1)
	printf(")");}
}
	
}
main(){
    BitNode *T;
    T=CreateTree();
    printf("中序遍历为\n");
    InOrder(T);
        printf("\n");
    printf("前序遍历为\n");
    PreOrder(T);
        printf("\n");
    printf("后序遍历为\n");
    PostOrder(T);
            printf("\n");
               printf("树的深度为%d\n",Depth(T));
            printf("\n");
              printf("节点个数为%d\n",NodeSum(T));
              
    zz(T,1);

}

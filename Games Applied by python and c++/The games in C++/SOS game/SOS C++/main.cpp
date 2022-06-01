#include <iostream>

using namespace std;
char arr [ 4 ]  [4]  ;
bool sos (int x, int y) {

for (int a=0; a<4;a++){
    for (int i=0; i<4;i++){
       cout<<arr[a] [i]<<' ' ;
    }
    cout<<endl;
}
if (arr[x][y]=='s'){
int a1 [8]= {1,1,0,-1,-1,-1,0,1};
int a2 [8]= {0,1,1,1,0,-1,-1,-1};
 for (int i=0 ; i<8 ; i++){
         if (x+a1[i]+a1[i] >= 0  && y+a2[i]+a2[i] >=0 && x+a1[i]+a1[i] <4  && y+a2[i]+a2[i]<4 ){
    if ( arr[x+a1[i]][y+a2[i]]=='o' && arr[x+(2*a1[i])][y+(2*a2[i])]=='s' ) {  return false;}
 }
 }
}
else {
int a1 [4]= {1,1,0,-1};
int a2 [4]= {0,1,1,1};
 for (int i=0 ; i<4 ; i++){
    if ( x+a1[i] >= 0  && y+a2[i]>=0 && x-a1[i]>=0 && y-a2[i] >=0 && x+a1[i] < 4  && y+a2[i]<4 && x-a1[i]<4 && y-a2[i] <4 ){
    if ( ( arr[x+a1[i]][y+a2[i]]=='s' )&& (arr[x-a1[i]][y-a2[i]]=='s') ) {  return false;}
 }
 }
}
return true ;
}
int main()
{
    string s;
    for (int a=0; a<4;a++){
    for (int i=0; i<4;i++){
       arr[a][i]='.';
    }
}
    int c=0,c1=0,c2=0;
    pair <int , int > ndx;
    while (c < 16 ) {
            while ( c < 16 ){
          c++;
        cout<<"first player to play , insert the cell coordinate  x y "<<endl;
        while (true){
        cout<<"x=";
        cin>> s[0];
        cout<<endl<<"y=";
        cin>>s[1];
        cout<<endl;
        ndx.first=((int) s[0])-49;
        ndx.second=((int)s[1])-49;
        if (   ( ndx.first>=0 ) &&( ndx.second>=0 )    && ( ndx.first < 4)  && (ndx.second < 4) &&    ( arr[ndx.first][ndx.second]== '.')      ) {
                        break;
        }
        else {
        cout<<"please enter a valid positive coordinates that fits in 4x4 grid and still empty yet"<<endl;
        }
            }
        cout<<"would you like to play 'o' or  's' , write it in lowercase " <<endl;
        while (1)
        {cin>>arr[ndx.first][ndx.second];
        if (arr[ndx.first][ndx.second]=='s' || arr[ndx.first][ndx.second]=='o'){break;}
        else  cout<<"please only enter 's' or 'o' "<<endl;
        }
        if  ( sos(ndx.first,ndx.second)  ){break;}
        else {
                c1++;

        }
            }

                while ( c < 16  ){
                   c++;
        cout<<"second player to play , insert the cell coordinate  x y "<<endl;
        while (true){
        cout<<"x=";
        cin>> s[0];
        cout<<endl<<"y=";
        cin>>s[1];
        cout<<endl;
        ndx.first=((int) s[0])-49;
        ndx.second=((int)s[1])-49;
        if (   ( ndx.first>=0 ) &&( ndx.second>=0 )    && ( ndx.first < 4)  && (ndx.second < 4) &&    ( arr[ndx.first][ndx.second]== '.')     ) {
                        break;
        }
        else {
        cout<<"please enter a valid positive coordinates that fits in 4x4 grid and still empty yet"<<endl;
        }
            }
        cout<<"would you like to play 'o' or  's' , write it in lowercase " <<endl;
        while (1)
        {
            cin>>arr[ndx.first][ndx.second];
        if (arr[ndx.first][ndx.second]=='s' || arr[ndx.first][ndx.second]=='o'){break;}
        else  cout<<"please only enter 's' or 'o' "<<endl;
        }
        if ( ( sos(ndx.first,ndx.second) ) ){break;}
        else {
                c2++;

        }
                }
}
if (c1>c2){cout<<"the first player wins "<<endl;}
else if (c1<c2){cout<<"the second player wins "<<endl;}
else {cout<<"it is a draw"<<endl;}
}

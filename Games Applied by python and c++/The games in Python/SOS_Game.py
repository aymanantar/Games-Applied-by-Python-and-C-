
arr= [ [ '.','.','.','.' ] , [ '.','.','.','.'  ]  , [ '.','.','.','.'] , ['.','.','.','.' ]] 
# checking if by this turn the player could match 'SOS'
def sos ( x,  y) :
    for  a in range (0,4) :
        for i in range (0,4) :
            print (f"{arr[a] [i]} ",end='')
        print(" \n")
    if (arr[x][y]=='s') :
        a1 = [1,1,0,-1,-1,-1,0,1]
        a2 = [0,1,1,1,0,-1,-1,-1]
        for i in range (0,8):
            if (x+2*a1[i] >= 0  and y+2*a2[i] >=0 and x+a1[i]+a1[i] <4  and y+a2[i]+a2[i]<4 ) :
                    if ( arr[x+a1[i]][y+a2[i]]=='o' and arr[x+(2*a1[i])][y+(2*a2[i])]=='s' ) :
                            return False 
    else :
        a1 = [1,1,0,-1]
        a2 = [0,1,1,1]
        for i in range (0,4):
            if ( x+a1[i] >= 0  and y+a2[i]>=0 and x-a1[i]>=0 and y-a2[i] >=0 and x+a1[i] < 4  and y+a2[i]<4 and x-a1[i]<4 and y-a2[i] <4 ):
          
                    if ( ( arr[x+a1[i]][y+a2[i]]=='s' ) and (arr[x-a1[i]][y-a2[i]]=='s') ):
                        return False
    return True ;


c=0
c1=0
c2=0
ndxfirst=0
ndxsecond=0
# Starting the game
while (c < 16 ):
    while ( c < 16 ):
        c+=1
        print("first player to play , insert the cell coordinate  x y space-separated ")
        
        while (True):
          # checking the input is an intger  
            try :
                (ndxfirst,ndxsecond)=input().split(' ')
            except :
                print ("please enter 2 digits space-separated")
                continue
    
            ndxfirst=int(ndxfirst)-1
            ndxsecond=int(ndxsecond)-1
            #checking if the chosen cell was valid 
            if (   ( ndxfirst>=0 ) and ( ndxsecond>=0 )    and ( ndxfirst < 4)  and (ndxsecond < 4) and    ( arr[ndxfirst][ndxsecond]== '.')     ) :
                break
            else :
                print("please enter a valid positive coordinates that fits in 4x4 grid and still empty yet")            

        print("would you like to play 'o' or  's' , write it in lowercase ")
        while (1):
            arr[ndxfirst][ndxsecond]=input()
            if (arr[ndxfirst][ndxsecond]=='s' or arr[ndxfirst][ndxsecond]=='o'):
                break 
            else :
                print("please only enter 's' or 'o'  ")
        if  ( sos(ndxfirst,ndxsecond)  ):
            break
                                           
        else :
                c1+=1

        
    while ( c < 16  ):
        c+=1
        print("second player to play , insert the cell coordinate  x y space-separated ")
        while (True):
            try :
                (ndxfirst,ndxsecond)=input().split(' ')
            except :
                print ("please enter 2 digits space-separated")
                continue
    
            ndxfirst=int(ndxfirst)-1
            ndxsecond=int(ndxsecond)-1
            if (   ( ndxfirst>=0 ) and ( ndxsecond>=0 )   and ( ndxfirst < 4) and (ndxsecond < 4) and   ( arr[ndxfirst][ndxsecond]== '.')     ) :
                            break;
            else :
                print("please enter a valid positive coordinates that fits in 4x4 grid and still empty yet")
        print("would you like to play 'o' or  's' , write it in lowercase ")
        while (1):
            arr[ndxfirst][ndxsecond]=input()
            if (arr[ndxfirst][ndxsecond]=='s' or arr[ndxfirst][ndxsecond]=='o'):
                break
            else  :
                print("please only enter 's' or 'o' ")

        if ( ( sos(ndxfirst,ndxsecond) ) ):
            break
        else :
            c2+=1
#showing the final result            
if (c1>c2) :
    print("the first player wins")
elif (c1<c2):
    print("the second player wins ")
else:
    print("it is a draw")

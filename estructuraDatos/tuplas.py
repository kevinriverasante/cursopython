##tuplas
# casadiego=[
#     [1,2,3,4],
#     [1,"diego",2,4]
# ]
# casadiego[1][1]="julissa"
# casadiego[1][3]="diego"
# print(casadiego)
##
casadiego=[
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5]
]
#modelo
#[
    #[0,1,1,1,1],
    #[1,0,1,1,1],
    #[1,1,0,1,1],
    #[1,1,1,0,1],
    #[1,1,1,1,0],
#]
# i0=[0,1,1,1,1]
# i1=[1,0,1,1,1]
# i2=[1,1,0,1,1]
# i3=[1,1,1,0,1]
# i3=[1,1,1,1,0]
contador=4
for i in range(0,len(casadiego)):
    for j in range(0,len(casadiego[i])):
        casadiego[i][j]=1
        casadiego[i][i]=0
        casadiego[i][contador]=0
    if contador>=0:
        contador=contador-1
    print(casadiego[i], end="\n")

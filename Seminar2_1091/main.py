from transformari_geometrice import mat3d,mattran3d

try:
    t1 = mat3d()
    print(t1)
    punct = (2,3,4)
    t_p = t1.transform(punct)
    print(t_p)
    # t1.t = ([1,2,3,3],[3,4,5,6],[2,3,9,8],[2,3,4,5])
    tran1 = mattran3d((10,20,15))
    print("Matricea de translatie:",tran1,sep="\n")
    t_punct = tran1.transform(punct)
    print(t_punct)
except Exception as ex:
    print(ex)

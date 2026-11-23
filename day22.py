'''
#Usage of variable length and keyword variable length argument

def scores(*marks,**names):
    """Scores Scenario with Variable and Keyword Variable length args"""
    print(marks)
    print(names)
    total = 0
    for mark in marks:
        if type(mark) in (int,float):
            total += mark
    print(f'Total Marks are : {total}')
    for name,value in names.items():
    #for name in names.values():
        print(f'Name : {name}')
        print(f'Value : {value}')
        
scores(25,20,15,18,16,name = "Ajay",place = "Vizag",batch = "PFS-VSP-007")

#positional arguments always follows keyword argumnts
#non default alway follows default args

'''

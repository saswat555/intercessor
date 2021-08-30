import pandas as pd 
import datetime
 
def addapple(Date,GDP):
    isThere = False                                             //A seperate function for updating the data regularly
    
    # Creating the first Dataframe using dictionary 
    df1 = pd.read_csv('apples.csv')
    
    try:
        date = datetime.datetime.strptime(Date,'%Y-%m-%d')
        date= date.strftime('%Y-%m-%d')
        gdp = int(GDP)
        print(date,gdp)
    
    
    except ValueError:
        error = "error"
        return 'erro'    
    for index, row in df1.iterrows(): 
        print(row['Date'], row['GDP']) 
        if str(row['Date']) == str(date) and str(row[GDP]) == str(gdp):
            isThere = True
    # Creating the Second Dataframe using dictionary 
    
    if isThere != True: 
        df2 = pd.DataFrame({"Date":[date], "GDP":[gdp]}) 
        dff = df1.append(df2, ignore_index = True)
        dff.to_csv('apples.csv',index = False)
        add = "added"
        return 'add'
    
    else:
        df1.to_csv('apples.csv', index = False) 
        update = "updated"
        return 'update'


def addbanana(Date,GDP):
    isThere = False
    
    # Creating the first Dataframe using dictionary 
    df1 = pd.read_csv('banana.csv')
    
    try:
        date = datetime.datetime.strptime(Date,'%Y-%m-%d')
        date= date.strftime('%Y-%m-%d')
        gdp = int(GDP)
        print(date,gdp)
    
    
    except ValueError:
        error = "error"
        return 'erro'    
    for index, row in df1.iterrows(): 
        print(row['Date'], row['GDP']) 
        if str(row['Date']) == str(date) and str(row[GDP]) == str(gdp):
            isThere = True
    # Creating the Second Dataframe using dictionary 
    
    if isThere != True: 
        df2 = pd.DataFrame({"Date":[date], "GDP":[gdp]}) 
        dff = df1.append(df2, ignore_index = True)
        dff.to_csv('banana.csv',index = False)
        add = "added"
        return 'add'
    
    else:
        df1.to_csv('banana.csv', index = False) 
        update = "updated"
        return 'update'

def addgrapes(Date,GDP):
    isThere = False
    
    # Creating the first Dataframe using dictionary 
    df1 = pd.read_csv('grapes.csv')
    
    try:
        date = datetime.datetime.strptime(Date,'%Y-%m-%d')
        date= date.strftime('%Y-%m-%d')
        gdp = int(GDP)
        print(date,gdp)
    
    
    except ValueError:
        error = "error"
        return 'erro'    
    for index, row in df1.iterrows(): 
        print(row['Date'], row['GDP']) 
        if str(row['Date']) == str(date) and str(row[GDP]) == str(gdp):
            isThere = True
    # Creating the Second Dataframe using dictionary 
    
    if isThere != True: 
        df2 = pd.DataFrame({"Date":[date], "GDP":[gdp]}) 
        dff = df1.append(df2, ignore_index = True)
        dff.to_csv('grapes.csv',index = False)
        add = "added"
        return 'add'
    
    else:
        df1.to_csv('grapes.csv', index = False) 
        update = "updated"
        return 'update'


def addmango(Date,GDP):
    isThere = False
    
    # Creating the first Dataframe using dictionary 
    df1 = pd.read_csv('mango.csv')
    
    try:
        date = datetime.datetime.strptime(Date,'%Y-%m-%d')
        date= date.strftime('%Y-%m-%d')
        gdp = int(GDP)
        print(date,gdp)
    
    
    except ValueError:
        error = "error"
        return 'erro'    
    for index, row in df1.iterrows(): 
        print(row['Date'], row['GDP']) 
        if str(row['Date']) == str(date) and str(row[GDP]) == str(gdp):
            isThere = True
    # Creating the Second Dataframe using dictionary 
    
    if isThere != True: 
        df2 = pd.DataFrame({"Date":[date], "GDP":[gdp]}) 
        dff = df1.append(df2, ignore_index = True)
        dff.to_csv('mango.csv',index = False)
        add = "added"
        return 'add'
    
    else:
        df1.to_csv('mango.csv', index = False) 
        update = "updated"
        return 'update'

def addwatermelon(Date,GDP):
    isThere = False
    
    # Creating the first Dataframe using dictionary 
    df1 = pd.read_csv('watermelon.csv')
    
    try:
        date = datetime.datetime.strptime(Date,'%Y-%m-%d')
        date= date.strftime('%Y-%m-%d')
        gdp = int(GDP)
        print(date,gdp)
    
    
    except ValueError:
        error = "error"
        return 'erro'    
    for index, row in df1.iterrows(): 
        print(row['Date'], row['GDP']) 
        if str(row['Date']) == str(date) and str(row[GDP]) == str(gdp):
            isThere = True
    # Creating the Second Dataframe using dictionary 
    
    if isThere != True: 
        df2 = pd.DataFrame({"Date":[date], "GDP":[gdp]}) 
        dff = df1.append(df2, ignore_index = True)
        dff.to_csv('watermelon.csv',index = False)
        add = "added"
        return 'add'
    
    else:
        df1.to_csv('watermelon.csv', index = False) 
        update = "updated"
        return 'update'

def addbeef(Date,GDP):
    isThere = False
    
    # Creating the first Dataframe using dictionary 
    df1 = pd.read_csv('beef.csv')
    
    try:
        date = datetime.datetime.strptime(Date,'%Y-%m-%d')
        date= date.strftime('%Y-%m-%d')
        gdp = int(GDP)
        print(date,gdp)
    
    
    except ValueError:
        error = "error"
        return 'erro'    
    for index, row in df1.iterrows(): 
        print(row['Date'], row['GDP']) 
        if str(row['Date']) == str(date) and str(row[GDP]) == str(gdp):
            isThere = True
    # Creating the Second Dataframe using dictionary 
    
    if isThere != True: 
        df2 = pd.DataFrame({"Date":[date], "GDP":[gdp]}) 
        dff = df1.append(df2, ignore_index = True)
        dff.to_csv('beef.csv',index = False)
        add = "added"
        return 'add'
    
    else:
        df1.to_csv('beef.csv', index = False) 
        update = "updated"
        return 'update'

def addchicken(Date,GDP):
    isThere = False
    
    # Creating the first Dataframe using dictionary 
    df1 = pd.read_csv('chicken.csv')
    
    try:
        date = datetime.datetime.strptime(Date,'%Y-%m-%d')
        date= date.strftime('%Y-%m-%d')
        gdp = int(GDP)
        print(date,gdp)
    
    
    except ValueError:
        error = "error"
        return 'erro'    
    for index, row in df1.iterrows(): 
        print(row['Date'], row['GDP']) 
        if str(row['Date']) == str(date) and str(row[GDP]) == str(gdp):
            isThere = True
    # Creating the Second Dataframe using dictionary 
    
    if isThere != True: 
        df2 = pd.DataFrame({"Date":[date], "GDP":[gdp]}) 
        dff = df1.append(df2, ignore_index = True)
        dff.to_csv('chicken.csv',index = False)
        add = "added"
        return 'add'
    
    else:
        df1.to_csv('chicken.csv', index = False) 
        update = "updated"
        return 'update'


def addcrabs(Date,GDP):
    isThere = False
    
    # Creating the first Dataframe using dictionary 
    df1 = pd.read_csv('crabs.csv')
    
    try:
        date = datetime.datetime.strptime(Date,'%Y-%m-%d')
        date= date.strftime('%Y-%m-%d')
        gdp = int(GDP)
        print(date,gdp)
    
    
    except ValueError:
        error = "error"
        return 'erro'    
    for index, row in df1.iterrows(): 
        print(row['Date'], row['GDP']) 
        if str(row['Date']) == str(date) and str(row[GDP]) == str(gdp):
            isThere = True
    # Creating the Second Dataframe using dictionary 
    
    if isThere != True: 
        df2 = pd.DataFrame({"Date":[date], "GDP":[gdp]}) 
        dff = df1.append(df2, ignore_index = True)
        dff.to_csv('crabs.csv',index = False)
        add = "added"
        return 'add'
    
    else:
        df1.to_csv('crabs.csv', index = False) 
        update = "updated"
        return 'update'

def addprawns(Date,GDP):
    isThere = False
    
    # Creating the first Dataframe using dictionary 
    df1 = pd.read_csv('prawns.csv')
    
    try:
        date = datetime.datetime.strptime(Date,'%Y-%m-%d')
        date= date.strftime('%Y-%m-%d')
        gdp = int(GDP)
        print(date,gdp)
    
    
    except ValueError:
        error = "error"
        return 'erro'    
    for index, row in df1.iterrows(): 
        print(row['Date'], row['GDP']) 
        if str(row['Date']) == str(date) and str(row[GDP]) == str(gdp):
            isThere = True
    # Creating the Second Dataframe using dictionary 
    
    if isThere != True: 
        df2 = pd.DataFrame({"Date":[date], "GDP":[gdp]}) 
        dff = df1.append(df2, ignore_index = True)
        dff.to_csv('prawns.csv',index = False)
        add = "added"
        return 'add'
    
    else:
        df1.to_csv('prawns.csv', index = False) 
        update = "updated"
        return 'update'

def addpork(Date,GDP):
    isThere = False
    
    # Creating the first Dataframe using dictionary 
    df1 = pd.read_csv('pork.csv')
    
    try:
        date = datetime.datetime.strptime(Date,'%Y-%m-%d')
        date= date.strftime('%Y-%m-%d')
        gdp = int(GDP)
        print(date,gdp)
    
    
    except ValueError:
        error = "error"
        return 'erro'    
    for index, row in df1.iterrows(): 
        print(row['Date'], row['GDP']) 
        if str(row['Date']) == str(date) and str(row[GDP]) == str(gdp):
            isThere = True
    # Creating the Second Dataframe using dictionary 
    
    if isThere != True: 
        df2 = pd.DataFrame({"Date":[date], "GDP":[gdp]}) 
        dff = df1.append(df2, ignore_index = True)
        dff.to_csv('pork.csv',index = False)
        add = "added"
        return 'add'
    
    else:
        df1.to_csv('pork.csv', index = False) 
        update = "updated"
        return 'update'

def addpomfret(Date,GDP):
    isThere = False
    
    # Creating the first Dataframe using dictionary 
    df1 = pd.read_csv('pomfret.csv')
    
    try:
        date = datetime.datetime.strptime(Date,'%Y-%m-%d')
        date= date.strftime('%Y-%m-%d')
        gdp = int(GDP)
        print(date,gdp)
    
    
    except ValueError:
        error = "error"
        return 'erro'    
    for index, row in df1.iterrows(): 
        print(row['Date'], row['GDP']) 
        if str(row['Date']) == str(date) and str(row[GDP]) == str(gdp):
            isThere = True
    # Creating the Second Dataframe using dictionary 
    
    if isThere != True: 
        df2 = pd.DataFrame({"Date":[date], "GDP":[gdp]}) 
        dff = df1.append(df2, ignore_index = True)
        dff.to_csv('pomfret.csv',index = False)
        add = "added"
        return 'add'
    
    else:
        df1.to_csv('pomfret.csv', index = False) 
        update = "updated"
        return 'update'




def addpork(Date,GDP):
    isThere = False
    
    # Creating the first Dataframe using dictionary 
    df1 = pd.read_csv('pork.csv')
    
    try:
        date = datetime.datetime.strptime(Date,'%Y-%m-%d')
        date= date.strftime('%Y-%m-%d')
        gdp = int(GDP)
        print(date,gdp)
    
    
    except ValueError:
        error = "error"
        return 'erro'    
    for index, row in df1.iterrows(): 
        print(row['Date'], row['GDP']) 
        if str(row['Date']) == str(date) and str(row[GDP]) == str(gdp):
            isThere = True
    # Creating the Second Dataframe using dictionary 
    
    if isThere != True: 
        df2 = pd.DataFrame({"Date":[date], "GDP":[gdp]}) 
        dff = df1.append(df2, ignore_index = True)
        dff.to_csv('pork.csv',index = False)
        add = "added"
        return 'add'
    
    else:
        df1.to_csv('pork.csv', index = False) 
        update = "updated"
        return 'update'

def addprawn(Date,GDP):
    isThere = False
    
    # Creating the first Dataframe using dictionary 
    df1 = pd.read_csv('prawns.csv')
    
    try:
        date = datetime.datetime.strptime(Date,'%Y-%m-%d')
        date= date.strftime('%Y-%m-%d')
        gdp = int(GDP)
        print(date,gdp)
    
    
    except ValueError:
        error = "error"
        return 'erro'    
    for index, row in df1.iterrows(): 
        print(row['Date'], row['GDP']) 
        if str(row['Date']) == str(date) and str(row[GDP]) == str(gdp):
            isThere = True
    # Creating the Second Dataframe using dictionary 

    if isThere != True: 
        df2 = pd.DataFrame({"Date":[date], "GDP":[gdp]}) 
        dff = df1.append(df2, ignore_index = True)
        dff.to_csv('prawns.csv',index = False)
        add = "added"
        return 'add'
    
    else:
        df1.to_csv('prawns.csv', index = False) 
        update = "updated"
        return 'update'

def addmilk(Date,GDP):
    isThere = False
    
    # Creating the first Dataframe using dictionary 
    df1 = pd.read_csv('milk.csv')
    
    try:
        date = datetime.datetime.strptime(Date,'%Y-%m-%d')
        date= date.strftime('%Y-%m-%d')
        gdp = int(GDP)
        print(date,gdp)
    
    
    except ValueError:
        error = "error"
        return 'erro'    
    for index, row in df1.iterrows(): 
        print(row['Date'], row['GDP']) 
        if str(row['Date']) == str(date) and str(row[GDP]) == str(gdp):
            isThere = True
    # Creating the Second Dataframe using dictionary 

    if isThere != True: 
        df2 = pd.DataFrame({"Date":[date], "GDP":[gdp]}) 
        dff = df1.append(df2, ignore_index = True)
        dff.to_csv('milk.csv',index = False)
        add = "added"
        return 'add'
    
    else:
        df1.to_csv('milk.csv', index = False) 
        update = "updated"
        return 'update'

def addbutter(Date,GDP):
    isThere = False
    
    # Creating the first Dataframe using dictionary 
    df1 = pd.read_csv('butter.csv')
    
    try:
        date = datetime.datetime.strptime(Date,'%Y-%m-%d')
        date= date.strftime('%Y-%m-%d')
        gdp = int(GDP)
        print(date,gdp)
    
    
    except ValueError:
        error = "error"
        return 'erro'    
    for index, row in df1.iterrows(): 
        print(row['Date'], row['GDP']) 
        if str(row['Date']) == str(date) and str(row[GDP]) == str(gdp):
            isThere = True
    # Creating the Second Dataframe using dictionary 

    if isThere != True: 
        df2 = pd.DataFrame({"Date":[date], "GDP":[gdp]}) 
        dff = df1.append(df2, ignore_index = True)
        dff.to_csv('butter.csv',index = False)
        add = "added"
        return 'add'
    
    else:
        df1.to_csv('butter.csv', index = False) 
        update = "updated"
        return 'update'

def addcheese(Date,GDP):
    isThere = False
    
    # Creating the first Dataframe using dictionary 
    df1 = pd.read_csv('cheese.csv')
    
    try:
        date = datetime.datetime.strptime(Date,'%Y-%m-%d')
        date= date.strftime('%Y-%m-%d')
        gdp = int(GDP)
        print(date,gdp)
    
    
    except ValueError:
        error = "error"
        return 'erro'    
    for index, row in df1.iterrows(): 
        print(row['Date'], row['GDP']) 
        if str(row['Date']) == str(date) and str(row[GDP]) == str(gdp):
            isThere = True
    # Creating the Second Dataframe using dictionary 

    if isThere != True: 
        df2 = pd.DataFrame({"Date":[date], "GDP":[gdp]}) 
        dff = df1.append(df2, ignore_index = True)
        dff.to_csv('cheese.csv',index = False)
        add = "added"
        return 'add'
    
    else:
        df1.to_csv('cheese.csv', index = False) 
        update = "updated"
        return 'update'

def addpaneer(Date,GDP):
    isThere = False
    
    # Creating the first Dataframe using dictionary 
    df1 = pd.read_csv('paneer.csv')
    
    try:
        date = datetime.datetime.strptime(Date,'%Y-%m-%d')
        date= date.strftime('%Y-%m-%d')
        gdp = int(GDP)
        print(date,gdp)
    
    
    except ValueError:
        error = "error"
        return 'erro'    
    for index, row in df1.iterrows(): 
        print(row['Date'], row['GDP']) 
        if str(row['Date']) == str(date) and str(row[GDP]) == str(gdp):
            isThere = True
    # Creating the Second Dataframe using dictionary 

    if isThere != True: 
        df2 = pd.DataFrame({"Date":[date], "GDP":[gdp]}) 
        dff = df1.append(df2, ignore_index = True)
        dff.to_csv('paneer.csv',index = False)
        add = "added"
        return 'add'
    
    else:
        df1.to_csv('paneer.csv', index = False) 
        update = "updated"
        return 'update'

def addcurd(Date,GDP):
    isThere = False
    
    # Creating the first Dataframe using dictionary 
    df1 = pd.read_csv('curd.csv')
    
    try:
        date = datetime.datetime.strptime(Date,'%Y-%m-%d')
        date= date.strftime('%Y-%m-%d')
        gdp = int(GDP)
        print(date,gdp)
    
    
    except ValueError:
        error = "error"
        return 'erro'    
    for index, row in df1.iterrows(): 
        print(row['Date'], row['GDP']) 
        if str(row['Date']) == str(date) and str(row[GDP]) == str(gdp):
            isThere = True
    # Creating the Second Dataframe using dictionary 

    if isThere != True: 
        df2 = pd.DataFrame({"Date":[date], "GDP":[gdp]}) 
        dff = df1.append(df2, ignore_index = True)
        dff.to_csv('curd.csv',index = False)
        add = "added"
        return 'add'
    
    else:
        df1.to_csv('curd.csv', index = False) 
        update = "updated"
        return 'update'

def addrohu(Date,GDP):
    isThere = False
    
    # Creating the first Dataframe using dictionary 
    df1 = pd.read_csv('rohu.csv')
    
    try:
        date = datetime.datetime.strptime(Date,'%Y-%m-%d')
        date= date.strftime('%Y-%m-%d')
        gdp = int(GDP)
        print(date,gdp)
    
    
    except ValueError:
        error = "error"
        return 'erro'    
    for index, row in df1.iterrows(): 
        print(row['Date'], row['GDP']) 
        if str(row['Date']) == str(date) and str(row[GDP]) == str(gdp):
            isThere = True
    # Creating the Second Dataframe using dictionary 

    if isThere != True: 
        df2 = pd.DataFrame({"Date":[date], "GDP":[gdp]}) 
        dff = df1.append(df2, ignore_index = True)
        dff.to_csv('rohu.csv',index = False)
        add = "added"
        return 'add'
    
    else:
        df1.to_csv('rohu.csv', index = False) 
        update = "updated"
        return 'update'

def addmutton(Date,GDP):
    isThere = False
    
    # Creating the first Dataframe using dictionary 
    df1 = pd.read_csv('mutton.csv')
    
    try:
        date = datetime.datetime.strptime(Date,'%Y-%m-%d')
        date= date.strftime('%Y-%m-%d')
        gdp = int(GDP)
        print(date,gdp)
    
    
    except ValueError:
        error = "error"
        return 'erro'    
    for index, row in df1.iterrows(): 
        print(row['Date'], row['GDP']) 
        if str(row['Date']) == str(date) and str(row[GDP]) == str(gdp):
            isThere = True
    # Creating the Second Dataframe using dictionary 

    if isThere != True: 
        df2 = pd.DataFrame({"Date":[date], "GDP":[gdp]}) 
        dff = df1.append(df2, ignore_index = True)
        dff.to_csv('mutton.csv',index = False)
        add = "added"
        return 'add'
    
    else:
        df1.to_csv('mutton.csv', index = False) 
        update = "updated"
        return 'update'
import operator

def is_valid_cin(cin:str):
    y = cin.isdigit()
    if len(cin) == 14 and y == True:
        Total = 0
        for i in range(0,12):
            Total += int(cin[i]) * (i+1)
            checksum = str(Total % 97)     

        if len(checksum) == 1:
            checksum = checksum.zfill(2) #getting checksum               
        if cin[-2:] == checksum and (cin[:2] == '17' or cin[:2] == '42'):
            return True
        else:
            return False
    else:
        return False   

start_inventory = {'17000372214424':'10',
'42100551007975':'10',
'17005667323396':'10',
'42100176564532':'10',
}

books = len(start_inventory)
book_cin = [p for p in list(start_inventory.keys())]
book_count = [int(p) for p in list(start_inventory.values())] #getting inputs from inventory

transaction_log = """17000372214424 INCOMING 9
17000372214424 OUTGOING 1
17000372214424 INCOMING 3
42100551007975 OUTGOING 3
42100551007975 INCOMING 1
17000372214424 OUTGOING 4
17005667323396 OUTGOING 5"""

transaction_number = len(transaction_log.split('\n'))
each_transaction = transaction_log.split('\n')
cin, transaction, count = [], [], []   

for i in range(transaction_number):
    cin.append(each_transaction[i].split(' ')[0])
    transaction.append(each_transaction[i].split(' ')[1])
    count.append(int(each_transaction[i].split(' ')[2])) #getting inputs from transaction log


def calculate_inventory(start_inventory, transaction_log): 
    for i in range(transaction_number):
        if transaction[i] == 'OUTGOING':
            count[i] = (-abs(count[i]))   

        for k in range(books):
            if book_cin[k] == cin[i]:
                book_count[k] += count[i]

    start_inventory = dict(zip(book_cin, book_count))

    for num in book_count:
        if num < 0:
            return "Negative quantity of a stock is NOT possible, Kindly check."
        else:
            return start_inventory

print(calculate_inventory(start_inventory, transaction_log))


def calculate_best_sellers(transaction_log,n):
    bs_cin, bs_count = [], []
    for i in range(transaction_number):
        if transaction[i] == 'OUTGOING' and count[i] == 0:
            bs_cin.append(cin[i])
            bs_count.append(count[i])

    result = list(zip(bs_cin, bs_count))

    best_seller = {}
    for a, b in result:
        total = best_seller.get(a, 0) + b
        best_seller[a] = total

    best_seller = dict(sorted(best_seller.items(), key=operator.itemgetter(1),reverse=True))
    desired_best_seller = list(best_seller.items())[:n]
    return desired_best_seller

# print(calculate_best_sellers(transaction_log,2))
#running the code to calculate inventory at the end of the day
# from datetime import datetime, timedelta
# from threading import Timer

# x=datetime.today()
# y = x.replace(day=x.day, hour=22, minute=0, second=0, microsecond=0) + timedelta(days=1)
# delta_t=y-x

# secs=delta_t.total_seconds()
# t = Timer(secs, calculate_inventory)
# t.start()


#another way for scheduling
# import schedule
# import time

# schedule.every(4).seconds.do(calculate_inventory)

# while True:
#     schedule.run_pending()
#     time.sleep(1) # wait one minute
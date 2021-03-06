import json

# Reading data
file = open('contacts.json')
string = ""
for i in file:
    string += i
file.close()

dataset = json.loads(string)

email_dict = dict()
phone_dict = dict()
order_dict = dict()


class User:
    def __init__(self):
        self.contacts = 0
        self.id = set()
        self.emails = set()
        self.phones = set()
        self.orders = set()

    def __str__(self):
        return '"' + '-'.join( map(str, sorted(self.id) ) ) + ', ' + str(self.contacts) + '"'


# Loop
for user in dataset:
    u = set()
    if email_dict.get(user['Email'], None):
        u.add( email_dict[ user['Email'] ] )
    if phone_dict.get(user['Phone'], None):
        u.add( phone_dict[ user['Phone'] ] )
    if order_dict.get(user['OrderId'], None):
        u.add( order_dict[ user['OrderId'] ] )

    # If no such user exists
    if len(u) == 0:
        new_user = User()
        new_user.contacts += user['Contacts']
        new_user.id.add( user["Id"] )
        if user['Email']: new_user.emails.add( user['Email'] )
        if user['Phone']: new_user.phones.add( user['Phone'] )
        if user['OrderId']: new_user.orders.add( user['OrderId'] )

        if user['Email']: email_dict[ user['Email'] ] = new_user
        if user['Phone']: phone_dict[ user['Phone'] ] = new_user
        if user['OrderId']: order_dict[ user['OrderId'] ] = new_user
    # Otherwise user existed, potentially multiple users
    else:
        new_user = User()
        new_user.contacts += user['Contacts']
        new_user.id.add(user["Id"])
        if user['Email']: new_user.emails.add(user['Email'])
        if user['Phone']: new_user.phones.add(user['Phone'])
        if user['OrderId']: new_user.orders.add(user['OrderId'])

        for existed in u:
            new_user.contacts += existed.contacts
            new_user.id = new_user.id.union( existed.id )
            new_user.emails = new_user.emails.union( existed.emails )
            new_user.phones = new_user.phones.union( existed.phones )
            new_user.orders = new_user.orders.union( existed.orders )

        for emails in new_user.emails:
            email_dict[emails] = new_user
        for phones in new_user.phones:
            phone_dict[phones] = new_user
        for orders in new_user.orders:
            order_dict[orders] = new_user


file = open('output.csv', 'w')
file.write('ticket_id,ticket_trace/contact\n')


for i in range(len(dataset) ):
    user = dataset[i]
    if user['Email']: u = email_dict[ user['Email'] ]
    elif user['Phone']: u = phone_dict[ user['Phone'] ]
    else: u = phone_dict[ user['OrderId' ] ]

    file.write( str(i) + ',' + str(u) )
    file.write('\n')



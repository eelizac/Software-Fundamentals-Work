# file that sets up the data structures  
# global variables that can be altered 

''' GUIDE TO USE -----------------------

2 lists of dictionaries: 
    - First list is to store user data - their name, emails, passwords etc. 
    - Second list is to store channel data - id, users, owners etc. 

example: to get user 3's email --> user[3].email = 

current issues/questions: 
    - I think there is a max of 3 right now so not sure how we can scale this 
    - not sure if I have included all data variables- feel free to add as you see that I have missed one


-------------------------------------'''
users = []
channels = []
owners = []
messages = []

'''
# 2 lists - one that is user
    # users = [{id, first name, last name, handle, email password}, {}, {}]

users = [
    {
        'id': auth_user_id
        'first_name': 'First', 
        'last_name': 'Last',
        'handle_str': 'firstlast'
        'email': 'first.last@unsw.edu.au',
        'password': 'asdf1212',
        'channels': [channel_id_1],
    }, 
    {
        'id': auth_user_id
        'first_name': 'Name', 
        'last_name': 'Surname',
        'handle_str': 'namesurname',
        'email': 'name.surname@unsw.edu.au',
        'password': 'dfghdfgh23465',
        'channels': [channel_id_1, channel_id_2],
    }, 

]

# channels - channel ID, who is in the channel, owner members, public or private 
# channels[{id, name, owner, public, users}, {}, {}]
channels = [
    {
        'channel_name': 'channel',
        'id': channel_id, 
        'owner_members': [],
        'is_public' : True,      # (boolean) public
        'users': [auth_user_id, auth_user_id, auth_user_id],
    }, 
    {
        'channel_name': 'channel',
        'id': channel_id,  
        'owner_members': [],
        'is_public' : False,     # (boolean) private
        'users': [auth_user_id, auth_user_id, auth_user_id],
    }, 

]

Owners - a list of auth_user_id of all the owners 
owners = [id1, id2, id3]


'messages': [
    {
        'message_id': 1,
        'u_id': 1,
        'channel_id': 0,
        'message': 'Hello world',
        'time_created': 1582426789,
    }
]

'''

from src.data import users, channels, messages
from src.error import InputError, AccessError

def channel_invite_v1(auth_user_id, channel_id, u_id):
    return {
    }

def channel_details_v1(auth_user_id, channel_id):
    return {
        'name': 'Hayden',
        'owner_members': [
            {
                'u_id': 1,
                'name_first': 'Hayden',
                'name_last': 'Jacobs',
            }
        ],
        'all_members': [
            {
                'u_id': 1,
                'name_first': 'Hayden',
                'name_last': 'Jacobs',
            }
        ],
    }

def channel_messages_v1(auth_user_id, channel_id, start):
    """
        Args:
            auth_user_id:
                The id of the user who is inviting.
            channel_id:
                The valid id of the channel.
            start:
                The start index of the messages in the channel.
        Returns:
            messages:
                A list of dictionaries of type 'message'.
            start:
                The start index of the messages in the channel.
            end:
                The end index of the messages in the channel.
        Raises:
            InputError:
                Invalid channel_id.
                
                start > total number of messages in channel.
            AccessError:
                Invalid auth_user_id.
                auth_user_id not a member of channel.
    """
    
    # list of users
    user_list = []
    for user in users:
        user_list.append(user['id'])

    # list of channels
    channels_list = []
    for chan in channels:
        channels_list.append(chan['id'])
    
    # list of channels the user belongs to
    user_channels = []
    for chan in channels:
        if auth_user_id in chan['users']:
            user_channels.append(chan['id'])

    # checking whether the channel_id exists in data.py
    if channel_id not in channels_list:
        raise InputError('Invalid channel id')

    # checking whether the auth_user_id exists in data.py
    if auth_user_id not in user_list or not isinstance(auth_user_id, int):
        raise AccessError('Invalid user')

    # checking whether user is a member of the channel
    if channel_id not in user_channels:
        raise AccessError("auth_user_id is not a member of this channel")

    # list of messages from channel with id channel_id
    channel_messages = []
    for msg in messages:
        if msg['channel_id'] == channel_id:
            channel_messages.append(msg)

    # checking whether the start index is greater than total messages
    message_total = len(channel_messages)
    if start > message_total:
        raise InputError("start is greater than the total number of messages in this channel")
    
    """
    # message with index 0 is the most recent
    # use slice() to extract the dictionaries between start and start + 50 inclusive
      from channel_messages
    # from the perspective of a user, the most recent message should be returned last
            * reverse the list ^-- ASSUMPTION
    """
    # if channel_messages is not empty
    if channel_messages:
        message_range = slice(start, start + 50)
        channel_messages.reverse()
        output = channel_messages[message_range]
    # if empty
    else:
        output = []
    
    if (start + 50) < message_total:
        end = start + 50
    else:
        end = -1

    return {
        'messages': output,
        'start': start,
        'end': end,
    }

    """
        ---THIS IS AN EXAMPLE OF A MESSAGE DICTIONARY---
        'messages': [
            {
                'message_id': 1,
                'u_id': 1,
                'message': 'Hello world',
                'time_created': 1582426789,
            }
        ],
    """


def channel_leave_v1(auth_user_id, channel_id):
    return {
    }

def channel_join_v1(auth_user_id, channel_id):
    return {
    }

def channel_addowner_v1(auth_user_id, channel_id, u_id):
    return {
    }

def channel_removeowner_v1(auth_user_id, channel_id, u_id):
    return {
    }

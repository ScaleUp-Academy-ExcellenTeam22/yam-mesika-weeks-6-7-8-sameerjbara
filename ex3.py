class PostOffice:
    """A Post Office class. Allows users to message each other.

    Parameters
    ----------
    usernames : list
        Users for which we should create PO Boxes.

    Attributes
    ----------
    message_id : int
        Incremental id of the last message sent.
    boxes : dict
        Users' inboxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def read_inbox(self, username, *N):
        """Returns the (first N/ all) unseen messages in the user inbox.

                                Parameters
                                ----------
                                username : str
                                    The wanted user name.
                                N : int/none
                                    number of messages
                                Returns
                                -------
                                list
                                    list of unseen messages in the user inbox.

                                Raises
                                ------
                                none

                                """
        messages = []
        user_box = self.boxes[username]
        number_of_messages = len(user_box) if not N else N[0]
        for index in range(0, number_of_messages):
            if user_box[index]["seen"] == "false":
                user_box[index]["seen"] = "true"
                messages.append(user_box[index])
        return messages

    def search_inbox(self, username, string):
        """Returns a list of messages that contain the given string in the user inbox.

                        Parameters
                        ----------
                        username : str
                            The wanted user name.
                        string : str
                            The string that will be searched in the user inbox.
                        Returns
                        -------
                        list
                            list of all messages that contain the string.

                        Raises
                        ------
                        none

                        """
        return [message for message in self.boxes[username] if string in message["body"]]

    def send_message(self, sender, recipient, message_body, urgent=False):
        """Send a message to a recipient.

        Parameters
        ----------
        sender : str
            The message sender's username.
        recipient : str
            The message recipient's username.
        message_body : str
            The body of the message.
        urgent : bool, optional
            The urgency of the message.
            Urgent messages appear first.

        Returns
        -------
        int
            The message ID, auto incremented number.

        Raises
        ------
        KeyError
            If the recipient does not exist.

        Examples
        --------
        After creating a PO box and sending a letter,
        the recipient should have 1 messege in the
        inbox.

        >>> po_box = PostOffice(['a', 'b'])
        >>> message_id = po_box.send_message('a', 'b', 'Hello!')
        >>> len(po_box.boxes['b'])
        1
        >>> message_id
        1
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
            'seen': "false",
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id


from enum import Enum

class OutlookFolder(Enum):
    olFilderDeletedItems = 3
    olFolderOutbox = 4
    olFolderSentMail = 5
    olFolderInbox = 6
    olFolderDrafts = 16
    olFolderJunk = 23

# An Enumerration is a way of representing built-in number which will otherwise be meaningless with a more descriptive bit of text

def get_messages(folder_name:str) -> list:

    # return a list of messages in given folder
    import win32com.cliet

    # start Outlook
    outlook = win32com.client.Dispatch("outlook.Application")

    # get at the email
    mapi = outlook.GetNamespace("MAPI") # Messaging Application Programming Interface
    # Allows you to get emails within Outlook

    # get at the inbox
    inbox = mapi.GetDefaultFolder(OutlookFolder.olFolderInbox.value)

    # get at subfolder
    subfolder = inbox.Folders.Item(folder_name)

    # get the messages in the folder
    messages = subfolder.Items

    emails =[]

    # loop over mesages, affing each to my list
    for m in messages:

        # create a tuple for this message
        this_message = (
            m.Subject,
            m.SenderEmailAddress,
            m.To,
            m.Unread,
            m.Senton.date(),
            m.body,
            m.Attachments

        )

        emails.append(this_message)

    # return accumulated list of messages
    return emails

# call function to return messages
msgs = get_messages("Junk")


# loop over these messages, saving attachmens
for msg in msgs:

    # unpack the tuple containing the information about the email
    subject, sender, to , unread, senton, body, attachments = msg

    # save the attachments
    for attachment in attachments:

        # save this attachment
        attachment.SaveAsFile("/Users/ikenna/Documents/GitHub/Python/17b - win32 and VBA/" +  attachment.FileName)

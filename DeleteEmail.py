from imapclient import IMAPClient

imapObj = IMAPClient("imap.gmail.com", ssl=True)
email = input("enter your email")
password = input("enter your password")
imapObj.login(email, password)
imapObj.select_folder("[Gmail]/Trash", readonly=False)
UIDs = imapObj.search("ALL")
imapObj.delete_messages(UIDs)
imapObj.expunge()
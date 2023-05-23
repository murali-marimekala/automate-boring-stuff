import webbrowser,sys, pyperclip

sys.argv #['mapit.py', '300', 'Wrath circle']
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])  #Combining the sysargv list into one string
else:
    address = pyperclip.paste()

#https://www.google.com/maps/place/<Address>
webbrowser.open('https://www.google.com/maps/place/' + address)



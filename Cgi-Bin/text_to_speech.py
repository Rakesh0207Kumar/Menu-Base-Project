#!/usr/bin/env python3

import cgi
import cgitb
from gtts import gTTS
import os
import sys

cgitb.enable()  # Enable debugging

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
text_input = form.getvalue('text')

if text_input:
    language = 'en'

    # Generate speech from text
    myobj = gTTS(text=text_input, lang=language, slow=False)
    audio_file = "/tmp/welcome.mp3"
    myobj.save(audio_file)

    # Return the audio file as response
    print("Content-Type: audio/mpeg")
    print(f"Content-Disposition: attachment; filename=welcome.mp3")
    print()

    with open(audio_file, "rb") as f:
        sys.stdout.buffer.write(f.read())
else:
    print("Content-Type: text/html")
    print()
    print("<html><body>No text provided</body></html>")

from graphics import GraphWin, Entry, Point, Text, Rectangle

win = GraphWin("Vigenere", 500, 300)
win.setCoords(0, 0, 10, 6)

# first line
message_entry = Entry(Point(6.5, 5), 30)
message_text = Text(Point(2, 5), 'Message to Code')

# second line
keyword_entry = Entry(Point(5, 4), 15)
keyword_text = Text(Point(2, 4), 'Enter Keyword')

# encode button
encode_button = Rectangle(Point(4, 2), Point(6, 3))
encode_text = Text(Point(5, 2.5), 'Encode')

# resulting message
resulting_message_text = Text(Point(5, 2.5), 'Resulting Message')
closing_test = Text(Point(5, 0.5), 'Click Anywhere to Close Window')
cipher_text = Text(Point(5, 2), '')

# draw everything
keyword_entry.draw(win)
keyword_text.draw(win)
message_text.draw(win)
message_entry.draw(win)
encode_text.draw(win)
encode_button.draw(win)

win.getMouse()

# get input
message_input = message_entry.getText()
keyword_input = keyword_entry.getText()

# encode the input
message = message_input.replace(' ', '').upper()
keyword = keyword_input.replace(' ', '').upper()
encrypted_message = ''
key_index = 0
for letter in message:  # loop through all the letters in the message
    key_letter = keyword[key_index]  # get a single letter from the key
    key_number = ord(key_letter) - ord('A')  # makes the key letter's numeric value from 0-25
    letter_number = ord(letter) - ord('A')  # makes the message letter's numeric value from 0-25
    new_number = (
                             letter_number + key_number) % 26  # adds the key to the letter, looping back to 0 if the sum is more than 25
    new_number = new_number + ord('A')  # converts the new number back to its unicode value between 65-90
    new_letter = chr(new_number)  # convert the unicode number back to a letter
    encrypted_message = encrypted_message + new_letter  # add the new letter to the encrypted message
    key_index = (key_index + 1) % len(keyword)  # key index needs to continuously loop from 0-lenght of key

cipher_text.setText(encrypted_message)

# hide the button
encode_text.undraw()
encode_button.undraw()

# draw the results
resulting_message_text.draw(win)
closing_test.draw(win)
cipher_text.draw(win)

# wait
win.getMouse()

win.close()

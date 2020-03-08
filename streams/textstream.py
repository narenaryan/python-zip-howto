from io import StringIO

text_stream = StringIO()
text_stream.write("I am a text buffer")

print(text_stream.getvalue()) # Prints 'I am a text buffer' to console
text_stream.close()
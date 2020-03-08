from io import StringIO

text_stream = StringIO()
text_stream.write("I am a text buffer")

print(" in python", file=text_stream) # Doesn't print to console, instead writes to stream
print(text_stream.getvalue()) # Prints 'I am a text buffer in python' to console
text_stream.close()
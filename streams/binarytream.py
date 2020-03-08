from io import BytesIO, StringIO

binary_stream =  BytesIO(b'I am a byte string \x01')

print(binary_stream.getvalue()) # Prints b'I am a byte string \x01'

try:
  text_stream = StringIO(binary_stream.getvalue())
except TypeError:
  print('Sorry, text stream cannot store bytes') # Prints 'Sorry, text stream cannot store bytes'
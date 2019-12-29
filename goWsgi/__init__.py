import sys

name = "goWsgi"
    
enc, esc = sys.getfilesystemencoding(), 'surrogateescape'

latin = 'iso-8859-1'
  
def unicode_to_wsgi(u):
  # Convert an environment variable to a WSGI "bytes-as-unicode" string
  return u.encode(enc, esc).decode(latin)

def wsgi_to_bytes(s):
  return s.encode(latin)

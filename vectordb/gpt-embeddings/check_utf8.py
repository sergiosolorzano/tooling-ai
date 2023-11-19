#!/usr/bin/env python3
import chardet

def is_utf8(text):
  """Returns True if the text is encoded in UTF-8, False otherwise."""

  detector = chardet.UniversalDetector()
  detector.feed(text)
  result = detector.result

  if result['encoding'] == 'utf-8':
    return True
  else:
    return False

def main():
  with open('myfile.txt', 'rb') as f:
    text = f.read()

  if is_utf8(text):
    print('All the text in the file is encoded in UTF-8.')
  else:
    print('Not all the text in the file is encoded in UTF-8.')

if __name__ == '__main__':
  main()

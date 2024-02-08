def decode(message_file_path):
  """
  Decodes a message from a pyramid-structured text file.

  Args:
    message_file_path: Path to the text file containing the encoded message.

  Returns:
    Decoded message as a string.
  """
  with open(message_file_path, 'r') as f:
    lines = f.readlines()

  # Build a dictionary mapping number to word
  word_map = {}
  for line in lines:
    num, word = line.strip().split()
    word_map[int(num)] = word

  # Construct the decoded message by reading words at the end of pyramid levels
  message = ""
  current_level = 1
  while True:
    for _ in range(current_level):
      if current_level not in word_map:
        return None  # Missing word in pyramid structure
      message += word_map[current_level]
    current_level += 1

  return message

# Example usage
decoded_message = decode("message.txt")  # Replace "message.txt" with your file path
print(decoded_message)

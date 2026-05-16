import uuid

def generate_file_id():
  random_id = uuid.uuid4()
  return random_id

if __name__ == "__main__":
  print(uuid.uuid4())
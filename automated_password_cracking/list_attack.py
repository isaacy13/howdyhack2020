def list_of_passwords():
  pass_list = []
  with open("pass_list.txt") as f:
    for line in f:
      password = line.rstrip("\n")
      pass_list.append(password)
  return pass_list

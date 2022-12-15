class Processor:
  def __init__(self, log_data=[]):
    self.__current_dir='/'
    self.__dir_tree={ '/' : [] }
    self.__current_command=""

    self.process_log(log_data)

  def process_log(self, log):
    for entry in log:
      if entry[0] == '$':
        self.run_command(entry)
      else:
        self.read_output(entry)

  def run_command(self, line):
    cmd = line.split(' ')[1]
    if cmd in ['cd', 'ls']:
      self.__current_command=cmd
      if cmd == 'cd':
        self.process_directory_change(' '.join(line.split(' ')[2:]))
    else:
      raise Exception('Invalid Command Given')

  def read_output(self, line):
    if self.__current_command == 'ls':
      self.process_directory_listing(line)
    else:
      raise Exception('Invalid Response to current command')

  def process_directory_listing(self, line):
    size = line.split(' ')[0]
    filename = line.split(' ')[1]
    if size == 'dir':
      if not "{}{}/".format(self.__current_dir,filename) in self.__dir_tree:
        self.__dir_tree["{}{}/".format(self.__current_dir,filename)] = []
    elif not filename in [i["name"] for i in self.__dir_tree[self.__current_dir]]:
      self.__dir_tree[self.__current_dir].append({ 'size' : int(size), 'name' : filename })

  def process_directory_change(self, new_dir):
    if new_dir == '..':
      self.__current_dir = '/'.join(self.__current_dir.split('/')[0:-2]) + '/'
    elif new_dir[0] == '/':
      self.__current_dir = new_dir
    else:
      self.__current_dir = self.__current_dir + new_dir + '/'

    if not self.__current_dir in self.__dir_tree:
      self.__dir_tree[self.__current_dir] = []
     
  def print_dir_tree(self):
    for key in sorted(self.__dir_tree):
      print(key)
      for val in self.__dir_tree[key]:
        print(" - {} {}".format(val["size"], val["name"]))

  def get_directory_sizes(self):
    ret_val={}
    dir_list = self.__dir_tree.keys()
    for key in sorted(self.__dir_tree):
      my_size=0
      subdirs = [i for i in dir_list if key in i]
      for directory in subdirs:
        for val in self.__dir_tree[directory]:
          my_size += val["size"]
      ret_val[key] = my_size
    return ret_val

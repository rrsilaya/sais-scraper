import sys, time, threading, constants

class Spinner:
  busy = False
  delay = 0.08
  label = 'Loading'

  @staticmethod
  def spinning_cursor():
    while 1: 
      for cursor in '⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏': yield cursor

  def __init__(self, delay=None):
    self.spinner_generator = self.spinning_cursor()
    if delay and float(delay): self.delay = delay

  def spinner_task(self):
    colors = constants.Colors();

    while self.busy:
      sys.stdout.write(colors.BLUE + next(self.spinner_generator) + colors.END)
      sys.stdout.write(' ' + self.label)
      sys.stdout.flush()
      time.sleep(self.delay)
      sys.stdout.write('\b' + ('\b' * (len(self.label) + 11)))
      sys.stdout.flush()

  def start(self, label):
    self.busy = True
    self.label = label
    threading.Thread(target=self.spinner_task).start()

  def stop(self):
    colors = constants.Colors();
    self.busy = False
    time.sleep(self.delay)
    sys.stdout.write(colors.GREEN + '✓ ' + colors.END + self.label + '\n')
    sys.stdout.flush()

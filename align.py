import sublime, sublime_plugin
import re

def is_function(line):
  if re.match(r"^[a-zA-Z0-9_]+\t+[*]*[a-zA-Z0-9_]+\([a-zA-Z0-9_*, ]*\)$", line):
    return 1
  return 0

def is_condition(line):
  if re.match(r"^.*(if|else if|else|while|for|do)([ ]\(.*\)){0,1}$", line):
    return 1
  return 0

def ifloor(number, floor):
  if number < floor:
    return floor
  return number

def last_char(line):
  for ch in line:
    if ch != ' ' and ch != '\t': return ch
  return ' '

def get_spaces(line):
  spaces = 0
  for ch in line:
    if ch == ' ': spaces += 1
    elif ch == '\t': spaces += 8
    else: break
  return spaces

def get_indentation(line):
  spaces = 0
  for ch in line:
    if ch == ' ' or ch == '\t': spaces += 1
    else: break
  return spaces

class EpiIndentCurrent(sublime_plugin.TextCommand):
  def run(self, edit):
    row, columns = self.view.rowcol(self.view.sel()[0].a)
    lines = (self.view.substr(self.view.line(self.view.sel()[0])), self.view.substr(self.view.line(self.view.text_point(row - 1, 0))), self.view.substr(self.view.line(self.view.text_point(row - 2, 0))))
    actual_spaces = get_indentation(lines[0])
    last_spaces = get_spaces(lines[1])
    if last_char(lines[1]) == '{':
      new_spaces = 2
    elif last_char(lines[1]) == '}':
      new_spaces = -2
    elif is_condition(lines[2]):
      new_spaces = -2
    str_spaces = "\t" * ((new_spaces + last_spaces) / 8) + " " * ((new_spaces + last_spaces) % 8)
    print "line %d : actual_spaces : %d, last_spaces : %d, new_spaces : %d" % (row + 1, actual_spaces, last_spaces, last_spaces + new_spaces)
    self.view.replace(edit, sublime.Region(self.view.text_point(row, 0), self.view.text_point(row, actual_spaces)), str_spaces)

class EpiIndentAll(sublime_plugin.TextCommand):
  def run(self, edit):
    if self.view.settings().get('sublim_tek_mode') != "true": return
    lines = self.view.substr(sublime.Region(0, self.view.size()))
    i = -1
    last_spaces = 0
    last_line = ""
    for line in lines.split("\n"):
      i += 1
      actual_spaces = 0
      new_spaces = 0
      next_line = 0
      for ch in line:
        if ch == ' ' or ch == '\t': actual_spaces += 1
        elif ch == '{':
          if not is_function(last_line):
            new_spaces += 2
          next_line += 2
          break
        elif ch == '}':
          new_spaces -= 2
          next_line -= 2
          break
        else:
          if is_condition(last_line):
            new_spaces += 2
            next_line -= 2
          break
      str_spaces = "\t" * ((new_spaces + last_spaces) / 8) + " " * ((new_spaces + last_spaces) % 8)
      if actual_spaces != len(line):
        self.view.replace(edit, sublime.Region(self.view.text_point(i, 0), self.view.text_point(i, actual_spaces)), str_spaces)
      else:
        self.view.replace(edit, sublime.Region(self.view.text_point(i, 0), self.view.text_point(i, actual_spaces)), "")
      last_spaces = ifloor(new_spaces + next_line + last_spaces, 0)
      last_line = line


class EpiNewLine(sublime_plugin.TextCommand):
  def run(self, edit):
    self.view.run_command('insert', {"characters": "\n"})
    if self.view.settings().get('sublim_tek_mode') == "true":
      self.view.run_command('epi_indent_current')

class EpiHooks(sublime_plugin.EventListener):
    def on_pre_save(self, view):
      if view.settings().get('sublim_tek_mode') == "true":
        view.run_command('epi_indent_all')
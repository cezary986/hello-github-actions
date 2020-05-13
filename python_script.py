import sys
import re

build_gradle_file = open("./build.gradle", "r")
build_gradle = build_gradle_file.read()

sys.argv[0] = build_gradle


class Version:

  def __init__(self, version_string: str):
    parts = version_string.split('.')
    
    if len(parts) > 3:
      raise Exception('Invalid version format')
    else:
      self._major = int(parts[0])
      self._minor = int(parts[1])
      self._patch = int(parts[2])

  def major(self):
    self._major += 1

  def minor(self):
    self._minor += 1

  def patch(self):
    self._patch += 1

  def __eq__(self, other):
    return (self.to_number() == other.to_number())

  def __ne__(self, other):
    return (self.to_number() != other.to_number())

  def __lt__(self, other):
    return (self.to_number() < other.to_number())

  def __le__(self, other):
    return (self.to_number() <= other.to_number())

  def __gt__(self, other):
    return (self.to_number() > other.to_number())

  def __ge__(self, other):
    return (self.to_number() >= other.to_number())

  def to_number(self):
    return (self._major * 100) + (self._minor * 10) + self._patch

  def __str__(self):
    return f'{self._major}.{self._minor}.{self._patch}'


def get_version_from_gradle(build_gradle_content):
  matches = re.search("version\s*'\S+'", build_gradle_content)
  version_line = matches.group(0)
  version_string = version_line.split("'")[1::2][0]
  return Version(version_string)


if __name__ == "__main__":
  build_gradle_file = open("./build.gradle", "r")
  my_build_gradle_content = build_gradle_file.read()
  their_build_gradle_content = sys.argv[0]
  print(their_build_gradle_content)

  my_version = get_version_from_gradle(my_build_gradle_content)
  their_version = get_version_from_gradle(their_build_gradle_content)

  if my_version <= their_version:
    raise Exception('Local version lower than their version')
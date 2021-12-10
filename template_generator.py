from glob import glob
import os
from datetime import date

folders = glob("./Day*")


def make_new():
    new_day = date.today().day

    folder_name = f"Day{new_day}"
    os.mkdir(folder_name)

    template_str = """
  with open("input.txt") as f:
    inp = f.read().split("\\n")

  def part1(inp):

  def part2(inp):

  part1(inp)
  part2(inp)
  """

    open(folder_name + "/input.txt", "w").close()
    with open(folder_name + f"/D{new_day}.py", "w") as f:
        f.write(template_str)


def cleanup():
    for i in folders:
        num = int(i.split("Day")[1])
        dest = f"D{num}.py"
        try:
            os.remove(os.path.join(i, "input.txt"))
            os.rename(os.path.join(i, dest), dest)
        except FileNotFoundError:
            pass
        os.rmdir(i)


cleanup()

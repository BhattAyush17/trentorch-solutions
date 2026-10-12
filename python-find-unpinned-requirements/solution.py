import re

_PINNED = re.compile(
    r"^[A-Za-z0-9][A-Za-z0-9._-]*(\[[^\]]*\])?\s*==\s*[^\s*,=<>!~]+$"
)


def find_unpinned(requirements: list[str]) -> list[str]:
    result = []

    for line in requirements:
        line = line.strip()

        
        if not line or line.startswith("#"):
            continue

       
        if " #" in line:
            line = line.split(" #", 1)[0].rstrip()

      
        if " --" in line:
            line = line.split(" --", 1)[0].rstrip()

        if " - -" in line:
            line =  line.split(" - -", 1)[0].rstrip()

        
        if line.endswith("\\"):
            line = line[:-1].rstrip()

        
        if ";" in line:
            line = line.split(";", 1)[0].rstrip()

       
        if not line or line.startswith("-"):
            continue

        
        if _PINNED.fullmatch(line):
            continue

        
        if " @ " in line:
            continue

        
        result.append(line)

    return result

import json


# https://github.com/Universal-Debloater-Alliance/universal-android-debloater-next-generation/tree/main/resources/assets/uad_lists.json
with open("uad_lists.json", "r") as f:
    uad = json.load(f)


with open("onphone.txt", "r") as f:
    my_package_lines = f.read().splitlines()


my_packages = [line.removeprefix("package:") for line in my_package_lines]

packages_with_description = {}
for id in my_packages:
    if id in uad:
        packages_with_description[id] = uad[id]
    else:
        packages_with_description[id] = {"description": "NA", "removal": "NA"}


print(
    """
 <table border=1>
  <tr>
    <th>id</th>
    <th>desc</th>
    <th>removal</th>
  </tr>
"""
)


def sort_pkgs(removal: str) -> int:
    removal_priority = {"Recommended": 1, "Advanced": 2, "Expert": 3, "Unsafe": 4}
    return removal_priority.get(removal, 99)


for id, infos in sorted(
    packages_with_description.items(), key=lambda x: sort_pkgs(x[1]["removal"])
):
    color = ""
    if infos["removal"] == "Unsafe":
        color = "lightsalmon"
    elif infos["removal"] == "Recommended":
        color = "lightgreen"

    print(
        f"""
  <tr bgcolor='{color}'>
    <td><a href='https://play.google.com/store/apps/details?id={id}' target='_blank'>{id}</a></td>
    <td>{infos['description']}</td>
    <td>{infos["removal"]}</td>
  </tr>
    """
    )

print("</table>")

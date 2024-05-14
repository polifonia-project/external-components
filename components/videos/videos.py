import os
import csv
from string import Template

template = """---
component-id: $id
type: $type
name: $title
description: $description
resource: $resource
pilot:
- $pilot
work-package:
- WP6
- $wp
---

# $title

$description

"""

template2 = """---
component-id: $id
type: $type
name: $title
description: $description
resource: $resource
work-package:
- WP6
- $wp
---

# $title

$description

"""

t = Template(template)
t2 = Template(template2)
file = open("videos.csv", "r")
reader = csv.reader(file, delimiter=',')
first = True
for row in reader:
    if first is True:
        first = False
        continue
    id = "video-" + row[5][32:43]
    title = row[0]
    typ = row[1] 
    pilot = row[2]
    wp = row[3]
    description = row[4]
    link = row[5]
    resource = row[5]
    if pilot != '':
        page = t.substitute(
            id=id,
            type=typ,
            description=description,
            resource=resource,
            link=link,
            wp=wp,
            title=title,
            pilot=pilot
        )
    else:
        page = t2.substitute(
            id=id,
            type=typ,
            description=description,
            resource=resource,
            link=link,
            wp=wp,
            title=title
        )
    f = open(id+".md", 'w')
    f.write(page)
    f.close()
file.close()
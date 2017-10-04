import datetime

import libcloud
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
from pprint import pprint

Engine = get_driver(Provider.ELASTICHOSTS)

driver = Engine("733b7dc7-7498-4db4-9dc4-74d3fee8abed",
                secret="6w6CDAqL6JyXFj3xNkWW2zpUjYfv9dYaLVdaaR4Y",
                secure=False)

images = driver.list_images()
sizes = driver.list_sizes()

IMAGE_ID = '38df09864d854b76b5023878ffc80161'
image = [i for i in images if i.id == IMAGE_ID][0]

pprint(images)
pprint(sizes)

node = driver.deploy_node(
    name="astricon-{}".format(datetime.datetime.now().strftime('%Y-%m-%dt%H%M%S')),
    image=image,
    size=sizes[3],
    script='deploy-script.sh',
    enable_root=True,
    vnc_password="myStr0ngr00tpa55wo7d")

print("Waiting for Node")
driver.wait_until_running([node], 10, 1000)
print("Node is now running")

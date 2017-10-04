import datetime
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
from pprint import pprint

ComputeEngine = get_driver(Provider.GCE)

driver = ComputeEngine('deployer@astricon-2017-demos.iam.gserviceaccount.com',
                       'astricon-2017-demos-e03de3565b4d.json',
                       datacenter='us-central1-a',
                       project='astricon-2017-demos')

images = driver.list_images()
sizes = driver.list_sizes()

IMAGE_ID = '8193040493265699771' # CentOS 7
image = [i for i in images if i.id == IMAGE_ID][0]

pprint(images)

# deploy_node takes the same base keyword arguments as create_node.
node = driver.deploy_node(
    "astricon-dkr-{}".format(datetime.datetime.now().strftime('%Y-%m-%dt%H%M%S')),
    sizes[0],
    image,
    'deploy-dockerized-asterisk.sh',
    ex_network='default')

print("Waiting for Node")
driver.wait_until_running([node], 10, 1000)
print("Node is now running")

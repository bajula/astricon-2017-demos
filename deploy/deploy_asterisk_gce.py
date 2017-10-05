import datetime
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
from pprint import pprint

from GCECreds import GCECreds

deployment_name = "astricon-{}"\
    .format(datetime.datetime.now().strftime('%Y-%m-%dt%H%M%S'))
print("Starting Asterisk deployment: {}".format(deployment_name))

ComputeEngine = get_driver(Provider.GCE)

driver = ComputeEngine(GCECreds.SERVICE_ACCOUNT,
                       GCECreds.KEY_FILE,
                       datacenter='us-central1-a',
                       project='astricon-2017-demos')

images = driver.list_images()
sizes = driver.list_sizes()

# pprint(images)
IMAGE_ID = '4257209330239857983' # CentOS 6
image = [i for i in images if i.id == IMAGE_ID][0]

# deploy_node takes the same base keyword arguments as create_node.
node = driver.deploy_node(
    deployment_name,
    sizes[0],
    image,
    'deploy-script.sh',
    ex_network='default')

print("Waiting for Node")
driver.wait_until_running([node], 10, 1000)
print("Node is now running")
print("")
print("Your new machine is running: {}".format(deployment_name))
print("Visit: https://console.cloud.google.com/compute/instances?project=astricon-2017-demos")
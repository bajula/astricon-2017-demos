import datetime
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
from pprint import pprint

from GCECreds import GCECreds

def gce_driver_by_region(region):
    ComputeEngine = get_driver(Provider.GCE)
    driver = ComputeEngine(GCECreds.SERVICE_ACCOUNT,
                           GCECreds.KEY_FILE,
                           datacenter=region,
                           project='astricon-2017-demos')
    return driver

def deploy_node(driver, deployment_name):
    images = driver.list_images()
    sizes = driver.list_sizes()

    # pprint(images)
    IMAGE_ID = '8193040493265699771' # CentOS 7
    image = [i for i in images if i.id == IMAGE_ID][0]

    # deploy_node takes the same base keyword arguments as create_node.
    node = driver.deploy_node(
        deployment_name,
        sizes[0],
        image,
        'deploy-dockerized-asterisk.sh',
        ex_network='default')
    return node

deployment_name = "astricon-dkr-{}".format(datetime.datetime.now().strftime('%Y-%m-%dt%H%M%S'))
print("Starting Asterisk deployment: {}".format(deployment_name))

REGIONS_TO_DEPLOY_MACHINES_AT = ['us-central1-a']

for region in REGIONS_TO_DEPLOY_MACHINES_AT:
    print("Deploying {} in region {}".format(deployment_name, region))
    driver = gce_driver_by_region('us-central1-a')
    node = deploy_node(driver, deployment_name)
    print("Waiting for Node")
    driver.wait_until_running([node], 10, 1000)
    print("Node is now running")
    print("")
    print("Your new machine is running: {}".format(deployment_name))
    print("Visit: https://console.cloud.google.com/compute/instances?project=astricon-2017-demos")
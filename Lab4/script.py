from datetime import datetime
import pycti
from stix2 import TLP_GREEN
date = datetime.today().strftime("%Y-%m-%dT%H:%M:%SZ")
api_token = 'qa78we3h-d5c8-334f-bas3-498a9479932c'
api_url = 'http://localhost:8080'
client = pycti.OpenCTIApiClient(api_url, api_token)
TLP_GREEN_CTI = client.marking_definition.read(id=TLP_GREEN["id"])
with open('hosts.txt', 'r') as f:
    domains = f.read().splitlines()
k = 1
for domain in domains:
    indicator = client.indicator.create(
    name="Malicious domain {}".format(k),
    description="MPVS hosts",
    pattern_type="stix",
    label="mpvs hosts",
    pattern="[domain-name:value = '{}']".format(domain),
    x_opencti_main_observable_type="IPv4-Addr",
    valid_from=date,
    update=True,
    score=75,
    markingDefinitions=[TLP_GREEN_CTI["id"]],
    )
    print("Created indicator with ID:", indicator["id"])
    k += 1

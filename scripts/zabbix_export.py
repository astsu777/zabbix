#=========================================================================
# Author: Gaetan (gaetan@ictpourtous.com) - Twitter: @astsu777
# Creation: Tue 02 Dec 2025 13:10:20
# Last modified: Tue 02 Dec 2025 13:10:20
# Version: 1.0
#
# Description: export Zabbix configuration to a JSON file and commits it to a Git repository
#=========================================================================

#=======================
# MODULES
#=======================

import requests
import json
import subprocess

#=======================
# VARIABLES
#=======================

API_KEY = 'ef7aefe64cc7dc080e713d9c6341280ccfb6dfcd769322be8a50891511384e01'
GIT_REPO_PATH = '/path/to/gitrepository'
ZABBIX_SERVER = 'https://zabbix.mydomain.com'

#=======================
# EXPORT
#=======================

def get_configuration(api_key):
    url = f"{ZABBIX_SERVER}/api_jsonrpc.php"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }

    # Export hosts
    payload_hosts = {
        "jsonrpc": "2.0",
        "method": "host.get",
        "params": {
            "output": "extend",
            "selectDashboards": "extend",
            "selectHostGroups": "extend",
            "selectHttpTests": "extend",
            "selectInterfaces": "extend",
            "selectMacros": "extend",
            "selectParentTemplates": "extend",
        },
        "id": "hostid"
    }
    # Accept self-signed SSL certificates
    response_hosts = requests.post(url, headers=headers, json=payload_hosts, verify=False)
    if response_hosts.status_code != 200 or 'result' not in response_hosts.json():
        print(f"Failed to get hosts: {response_hosts.content}")
        raise Exception("Failed to get hosts")

    # Export host groups
    payload_hostgroups = {
        "jsonrpc": "2.0",
        "method": "hostgroup.get",
        "params": {
            "output": "extend",
            "selectHosts": "extend"
        },
        "id": "hostgroupid"
    }
    # Accept self-signed SSL certificates
    response_hostgroups = requests.post(url, headers=headers, json=payload_hosts, verify=False)
    if response_hostgroups.status_code != 200 or 'result' not in response_hostgroups.json():
        print(f"Failed to get host groups: {response_hostgroups.content}")
        raise Exception("Failed to get host groups")

    # Export images
    payload_images = {
        "jsonrpc": "2.0",
        "method": "image.get",
        "params": {
            "output": "extend"
        },
        "id": "imageid"
    }
    # Accept self-signed SSL certificates
    response_images = requests.post(url, headers=headers, json=payload_images, verify=False)
    if response_images.status_code != 200 or 'result' not in response_images.json():
        print(f"Failed to get images: {response_images.content}")
        raise Exception("Failed to get images")

    # Export maps
    payload_maps = {
        "jsonrpc": "2.0",
        "method": "map.get",
        "params": {
            "output": "extend",
            "selectLines": "extend",
            "selectLinesselectLinks": "extend",
            "selectLinks": "extend",
            "selectSelements": "extend",
            "selectShapes": "extend",
            "selectUrls": "extend",
            "selectUserGroups": "extend",
            "selectUsers": "extend"
        },
        "id": "mapid"
    }
    # Accept self-signed SSL certificates
    response_maps = requests.post(url, headers=headers, json=payload_maps, verify=False)
    if response_maps.status_code != 200 or 'result' not in response_maps.json():
        print(f"Failed to get maps: {response_maps.content}")
        raise Exception("Failed to get maps")

    # Export mediaTypes
    payload_mediatypes = {
        "jsonrpc": "2.0",
        "method": "mediatype.get",
        "params": {
            "output": "extend",
            "selectActions": "extend",
            "selectMessageTemplates": "extend",
            "selectUsers": "extend"
        },
        "id": "mediatypeid"
    }
    # Accept self-signed SSL certificates
    response_mediatypes = requests.post(url, headers=headers, json=payload_mediatypes, verify=False)
    if response_mediatypes.status_code != 200 or 'result' not in response_mediatypes.json():
        print(f"Failed to get mediatypes: {response_mediatypes.content}")
        raise Exception("Failed to get mediatypes")

    # Export templates
    payload_templates = {
        "jsonrpc": "2.0",
        "method": "template.get",
        "params": {
            "output": "extend",
            "selectDashboards": "extend",
            "selectDiscoveryRules": "extend",
            "selectGraphs": "extend",
            "selectHosts": "extend",
            "selectHttpTests": "extend",
            "selectItems": "extend",
            # "selectMacros": "extend",
            # "selectParentTemplates": "extend",
            # "selectTags": "extend",
            # "selectTemplateGroups": "extend",
            # "selectTemplates": "extend",
            "selectTriggers": "extend",
            # "selectValueMaps": "extend"
        },
        "id": "templateid"
    }
    # Accept self-signed SSL certificates
    response_templates = requests.post(url, headers=headers, json=payload_templates, verify=False)
    if response_templates.status_code != 200 or 'result' not in response_templates.json():
        print(f"Failed to get templates: {response_templates.content}")
        raise Exception("Failed to get templates")

    # Export template groups
    payload_templategroups = {
        "jsonrpc": "2.0",
        "method": "templategroup.get",
        "params": {
            "output": "extend",
            "selectTemplates": "extend"
        },
        "id": "templategroupid"
    }
    # Accept self-signed SSL certificates
    response_templategroups = requests.post(url, headers=headers, json=payload_templategroups, verify=False)
    if response_templategroups.status_code != 200 or 'result' not in response_templategroups.json():
        print(f"Failed to get templategroups: {response_templategroups.content}")
        raise Exception("Failed to get templategroups")

    return {
        "hosts": response_hosts.json()['result'],
        "hostgroups": response_hostgroups.json()['result'],
        "images": response_images.json()['result'],
        "maps": response_maps.json()['result'],
        "mediatypes": response_mediatypes.json()['result'],
        "templates": response_templates.json()['result'],
        "templategroups": response_templategroups.json()['result'],
    }

def save_to_file(data):
    with open('zabbix_configuration.json', 'w') as f:
        json.dump(data, f, indent=4)

def git_push():
    subprocess.run(["git", "add", "zabbix_configuration.json"], cwd=GIT_REPO_PATH)
    subprocess.run(["git", "commit", "-m", "Export Zabbix configuration"], cwd=GIT_REPO_PATH)
    subprocess.run(["git", "push"], cwd=GIT_REPO_PATH)

if __name__ == "__main__":
    try:
        config = get_configuration(API_KEY)  # Pass in the API key directly
        save_to_file(config)
        git_push()
        print("Zabbix configuration exported successfully")
    except Exception as e:
        print(f"An error occurred: {e}")


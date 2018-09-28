def GenerateConfig(context):
  """Generate configuration."""
resources = []
resources.append({
    'name': 'tmpl',
    'type': 'compute.v1.instanceTemplate',
    'properties': {
        'machineType': 'zones/{{ properties["zone"] }}/machineTypes/f1-micro',
        'disks': [{
            'deviceName': 'boot',
            'type': 'PERSISTENT',
            'boot': True,
            'autoDelete': True,
            'initializeParams': {
                'sourceImage':
                    'projects/debian-cloud/global/images/family/debian-9'
            }
        }],
        'networkInterfaces': [{
            'network': 'global/networks/default'
        }]
    }
})
return {'resources': resources}

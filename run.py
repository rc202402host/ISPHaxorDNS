

import os

host_ip = os.getenv('HOST_IP')
host_password = os.getenv('HOST_PASSWORD')
host_domain = os.getenv('HOST_DOMAIN')

print("Staring iodine bot...")

# iodined -c -f 10.0.0.1 -P yourpasswordhere iodine.yourdomain.com

resp = os.system("iodined -c -f " + host_ip " -P " + host_password " " + ihost_domain )

print("Run Response: " + str(resp))

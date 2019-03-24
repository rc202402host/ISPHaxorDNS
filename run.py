

import os


print("Staring iodine bot...")

resp = os.system("iodined -c -f 10.0.0.1 -P isphaxordns isphaxordns.herokuapp.com")

print("Run Response: " + str(resp))

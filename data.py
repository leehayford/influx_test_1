from datetime import datetime

def get_utc_time( ):
    return datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

import numpy as np
def random_data( min, max ):
    num = np.random.uniform( min, max ) 
    return num


from data import get_utc_time, random_data

def rand_press( ): 
    return random_data( 12.7, 16.7 )

def rand_temp( ): 
    return random_data( 17.2, 17.5 )

def rand_flow( ): 
    return random_data( 5.6, 5.9 )

def rand_meth( ): 
    return random_data( 92.6, 92.9 )

def get_sample( event_id, user_id, device_id, time ):
    return {
        "measurement" : event_id,
        "tags": {
            "user": user_id,
            "device_id": device_id
        },
        "time": time.strftime('%Y-%m-%dT%H:%M:%SZ'),
        "fields": {
            "pressure":  rand_press( ),
            "temperature":  rand_temp( ),
            "flow":  rand_flow( ),
            "methane":  rand_meth( )
        }
    }

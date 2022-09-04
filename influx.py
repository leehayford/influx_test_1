from fastapi import APIRouter
from settings import FluxConn
from influxdb import InfluxDBClient
from data import get_utc_time, random_data
from sim import get_sample
from datetime import datetime, timedelta

flux = FluxConn( )
client = InfluxDBClient( host=flux.host, port=flux.port, username=flux.u, password=flux.pw )

router = APIRouter( )

@router.get('/influx-db-list')
async def get_flux_db_list( ):
    print( f"getting list of databases - { get_utc_time( ) }" )
    return client.get_list_database( )


@router.get('/write-to-db/{count}')
async def write_to_db( count: int ):
    client.switch_database( 'pyexample' )
    json_body = [ ]
    t = datetime.utcnow()
    for _ in range( count ):
        json_body.append( get_sample( "sample", "jeff", "DC9999", t ) )
        t = t + timedelta( seconds=1 )
    client.write_points( json_body )
    return json_body


@router.get('/read-from-db')
async def read_from_db(  ):
    client.switch_database( 'pyexample' )
    result = client.query('SELECT "pressure" FROM "pyexample"."autogen"."sample" WHERE time > now() - 4d GROUP BY "user"')
    return result.raw
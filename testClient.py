import iperf3
import os

def check_ping():
    hostname = "intel-corei7-64"
    response = os.system("ping -c 1 " + hostname)
    if response == 0:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network Error"
    if(pingstatus == 'Network Active'):
        print('Ping test on ICL completed\n')
        print('PASS')
    return pingstatus

def iperfClient():
    client = iperf3.Client()
    client.duration = 1
    client.server_hostname = '10.221.109.28'
    client.port = 5201
    result = client.run()
    print('#########################################\n')
    print('### Iperf3 client sending the data ######\n')
    print('#########################################\n')
    if(result.sent_Mbps > 17):
        print('iperf3 test completed on ICL\n')
        print('PASS')

check_ping()
iperfClient()


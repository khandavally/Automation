import iperf3

def iperfServer():
    server = iperf3.Server()
    server.bind_address = '10.221.109.28'
    server.port = '5201'
    server.verbose = False
    while True:
        print('#################################\n')
        print('##### Iperf3 Server Running #####\n')
        print('#################################\n')
        server.run()

iperfServer()


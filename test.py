import speedtest


connection = speedtest.Speedtest()
print("Getting Download")
download_speed = connection.download()
print(f"Your Download Speed : {download_speed/1024/1024}")
print(connection.get_best_server())
print(connection.get_closest_servers())
print(connection.get_servers())
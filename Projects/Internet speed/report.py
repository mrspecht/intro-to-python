# Internet speed report

from datetime import datetime
from threading import Timer
import speedtest
import os.path


def report():
    file_exists = os.path.isfile("report.txt")

    st = speedtest.Speedtest()

    download = st.download() * (10**-6)
    upload = st.upload() * (10**-6)
    dld = f"{download:.2f}"
    dld = dld.ljust(22)
    upl = f"{upload:.2f}"

    servers = []
    st.get_servers(servers)
    ping = f"{st.results.ping}"
    ping = ping.ljust(14)

    data = ping + dld + upl

    now = datetime.now()
    now = f"{now:%b %d %Y %H:%M}"
    now = now.ljust(21)

    if file_exists:
        with open("report.txt", "a") as file:
            file.write(f"\n{now} {data}")
            file.close()
    else:
        with open("report.txt", "w") as file:
            file.write("Internet connection report")
            file.write("\n\n")
            file.write(f"{'Date'.ljust(21)} {'Ping (ms)'.ljust(13)} {'Download (Mbit/s)'.ljust(21)} Upload (Mbit/s)")
            file.write(f"\n{now} {data}")
            file.close()

    Timer(40, report).start()


print("Monitoring your connection speed...")
print("Check your report file to see the results")
report()

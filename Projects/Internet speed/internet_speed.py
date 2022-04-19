# Internet speed

import speedtest

def test():
    print("Testing your Internet speed. Please wait")

    st = speedtest.Speedtest()
    st.get_best_server()

    download = round(st.download() / (10**6), 2)
    upload = round(st.upload() / (10**6), 2)

    sponsor = st.get_best_server().get('sponsor')
    city = st.get_best_server().get('name')

    print(f"\nDownload {download} Mbit/s")
    print(f"{'Upload'.ljust(8)} {upload} Mbit/s")
    print(f"\nServer hosted by {sponsor} ({city})\n")


test()

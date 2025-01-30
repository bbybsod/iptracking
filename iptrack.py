import requests
import pyfiglet

def get_ip_geolocation(ip_address):
    
    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def main():
    text = pyfiglet.figlet_format('SEAN')
    print(text)
    print('________________________________________')
    print('===========TikTok : sean myxzu==========')
    print('======Github : github.com/bbybsod=======')
    print('========================================')
    ip_address = input("Masukkan alamat IP: ")
    geolocation_data = get_ip_geolocation(ip_address)

    if geolocation_data:
        print("\nInformasi Geolokasi:")
        print(f"IP: {geolocation_data.get('ip')}")
        print(f"Kota: {geolocation_data.get('city')}")
        print(f"Wilayah: {geolocation_data.get('region')}")
        print(f"Negara: {geolocation_data.get('country')}")
        print(f"Lokasi (Lat, Lon): {geolocation_data.get('loc')}")
        print(f"Provider Internet (ISP): {geolocation_data.get('org')}")
        print(f"Kode Pos: {geolocation_data.get('postal')}")
        print(f"Zona Waktu: {geolocation_data.get('timezone')}")
    else:
        print("Gagal mendapatkan informasi geolokasi.")

if __name__ == "__main__":
    main()

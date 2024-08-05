import tkinter as tk
from tkinter import scrolledtext, filedialog
from ipaddress import ip_network, ip_address
import socket
import threading
import logging
from datetime import datetime
import os

def select_log_file():
    """Kullanıcıdan log dosyasının kaydedileceği yolu seçmesini sağlar."""
    file_path = filedialog.asksaveasfilename(
        defaultextension=".log",
        filetypes=[("Log Files", "*.log"), ("All Files", "*.*")]
    )
    return file_path

# Günlük kayıtları ayarları
log_file = select_log_file()
if not log_file:
    log_file = 'ipscanlist.log'  # Varsayılan dosya yolu

logging.basicConfig(filename=log_file, level=logging.INFO, format='%(message)s')

def scan_ip(ip, ports, retries=3):
    """Belirli bir IP adresinde verilen portları tarar ve açık olan portları döndürür."""
    open_ports = []
    port_status = {}
    
    for port in ports:
        success = False
        for attempt in range(retries):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                result = sock.connect_ex((ip, port))
                if result == 0:
                    open_ports.append(port)
                    port_status[port] = 'Açık'
                    success = True
                    break
            if not success:
                port_status[port] = 'Kapalı !'
    
    return open_ports, port_status

def scan_ip_threaded(ip, ports, retries=3):
    """IP adresini çoklu iş parçacığı ile tarar."""
    open_ports, port_status = scan_ip(ip, ports, retries)
    log_message = (
        f"İp & Port Tarama İşlemi\n"
        f"İşlem Saati: {datetime.now().strftime('%H:%M - %d.%m.%Y')}\n"
        f"Tarama Yapılan IP Adresi: {ip}\n"
        f"Tarama Yapılan Port Listesi: {ports}\n"
    )
    for port in ports:
        log_message += f"-> [{port}] => {port_status.get(port, 'Bilgi Yok')}\n"
    
    logging.info(log_message)
    return log_message

def scan_network(network, ports, retries=3):
    """Belirli bir ağ aralığındaki IP adreslerinde açık portları tarar ve raporlar."""
    open_ports = {}
    threads = []
    results = {}

    for ip in ip_network(network).hosts():
        ip_str = str(ip)
        thread = threading.Thread(target=lambda: results.update({ip_str: scan_ip_threaded(ip_str, ports, retries)}))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results

def start_scan():
    """Tarama işlemini başlatır ve sonuçları GUI'de gösterir."""
    network = network_entry.get()
    ports_input = ports_entry.get()
    ports = [int(port.strip()) for port in ports_input.split(",")]

    if scan_type.get() == "1":
        result_text.insert(tk.END, "Taramanız Yapılıyor...\n")
        root.update_idletasks()
        results = scan_network(network, ports)
    elif scan_type.get() == "2":
        ip = ip_entry.get()
        if not ip_address(ip).is_global:
            result_text.insert(tk.END, "Geçerli bir IP adresi girin.\n")
            return
        result_text.insert(tk.END, "Taramanız Yapılıyor...\n")
        root.update_idletasks()
        results = {ip: scan_ip_threaded(ip, ports)}
    else:
        result_text.insert(tk.END, "Geçersiz seçim.\n")
        return

    result_text.delete(1.0, tk.END)
    for ip, log_message in results.items():
        result_text.insert(tk.END, f"{log_message}\n")

    log_file_path = os.path.abspath(log_file)
    result_text.insert(tk.END, f"\nTarama işleminiz başarıyla yapıldı, Günlük dosyası '{log_file_path}' kaydedildi.\n")

# GUI Oluşturma
root = tk.Tk()
root.title("IP & Port Tarama Uygulaması v.1")

scan_type = tk.StringVar()
scan_type.set("1")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

tk.Label(frame, text="Tarama Türü:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
tk.Radiobutton(frame, text="Yerel Ağ", variable=scan_type, value="1").grid(row=0, column=1, padx=5, pady=5)
tk.Radiobutton(frame, text="Tekil IP", variable=scan_type, value="2").grid(row=0, column=2, padx=5, pady=5)

tk.Label(frame, text="Ağ Aralığı:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
network_entry = tk.Entry(frame, width=30)
network_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

tk.Label(frame, text="IP Adresi:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
ip_entry = tk.Entry(frame, width=30)
ip_entry.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

tk.Label(frame, text="Portlar:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
ports_entry = tk.Entry(frame, width=30)
ports_entry.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

tk.Button(frame, text="Tarama Başlat", command=start_scan).grid(row=4, column=0, columnspan=3, pady=10)

result_text = scrolledtext.ScrolledText(frame, width=50, height=15)
result_text.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()

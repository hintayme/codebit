#ENG
IP and Port Scanning Application User Guide

1. Introduction
This application allows you to scan specific ports on IP addresses and networks. After the scanning process, you can get information about open and closed ports. The application can work on local networks and single IP addresses.

2. Application Installation
Python Installation: Make sure that Python 3.x version is installed on your computer.

3. Application Usage
Starting the Application: Start your application. The GUI interface will open.

Scan Type Selection:
Local Network (Option 1): Scans the local network range. This option allows you to specify the IP range.

Single IP (Option 2): Scans ports on a single IP address.

Network Range and IP Address Entry:
Network Range: If you selected the "Local Network" option, enter the network range in CIDR format (for example, 192.168.1.0/24).
IP Address: If you selected the "Single IP" option, enter the IP address you want to scan.

Ports Entry:
Enter the port numbers you want to scan, separated by commas (for example, 80, 443, 21).

Start Scan:
Click the "Start Scan" button. The scan process will start and the results will be displayed in the GUI interface.

Display Results:
After the scan process is completed, information about open and closed ports will be displayed in the GUI interface.
The scan results will also be saved in the ipscanlist.log file.

Display Log File:
The location and content of the log file will be displayed in the GUI interface. The full path of the log file will be indicated at the bottom of the screen.

4. Troubleshooting
"Enter a valid IP address." Error:
Make sure you have entered the IP address correctly. Remember that it must be in IPv4 format.

"Invalid selection." Error:
Make sure you have selected the scan type correctly. You must select either "Local Area Network" or "Single IP".

5. Support and Contact
If you encounter any issues or need additional support, please contact me so we can continue to develop the app.


#TR
IP ve Port Tarama Uygulaması Kullanım Kılavuzu
1. Giriş
Bu uygulama, IP adreslerinde ve ağlarda belirli portları taramanıza olanak sağlar. Tarama işlemi sonrasında açık ve kapalı portlar hakkında bilgi alabilirsiniz. Uygulama, yerel ağlar ve tekil IP adresleri üzerinde çalışabilir.

2. Uygulamanın Kurulumu
Python Yüklemesi: Python 3.x sürümünün bilgisayarınıza kurulu olduğundan emin olun.

3. Uygulamanın Kullanımı
Uygulamanın Başlatılması: Uygulamanızı başlatın. GUI arayüzü açılacaktır.

Tarama Türü Seçimi:
Yerel Ağ (Seçenek 1): Yerel ağ aralığını tarar. Bu seçenek, IP aralığı belirtmenizi sağlar.
Tekil IP (Seçenek 2): Tek bir IP adresinde portları tarar.

Ağ Aralığı ve IP Adresi Girişi:
Ağ Aralığı: Eğer "Yerel Ağ" seçeneğini seçtiyseniz, ağ aralığını CIDR biçiminde girin (örneğin, 192.168.1.0/24).
IP Adresi: Eğer "Tekil IP" seçeneğini seçtiyseniz, taramak istediğiniz IP adresini girin.

Portlar Girişi:
Taramak istediğiniz port numaralarını virgülle ayrılmış şekilde girin (örneğin, 80, 443, 21).

Tarama Başlatma:
"Tarama Başlat" butonuna tıklayın. Tarama işlemi başlayacak ve sonuçlar GUI arayüzünde gösterilecektir.

Sonuçların Görüntülenmesi:
Tarama işlemi tamamlandıktan sonra, açık ve kapalı portlar hakkında bilgiler GUI arayüzünde görüntülenecektir.
Tarama sonuçları, ayrıca ipscanlist.log dosyasına kaydedilecektir.

Günlük Dosyasının Görüntülenmesi:
Günlük dosyasının kaydedildiği yer ve içeriği GUI arayüzünde gösterilecektir. Günlük dosyasının tam yolu ekranın alt kısmında belirtilecektir.

4. Hata Giderme
"Geçerli bir IP adresi girin." Hatası:
IP adresini doğru girdiğinizden emin olun. IPv4 formatında olması gerektiğini unutmayın.

"Geçersiz seçim." Hatası:
Tarama türünü doğru seçtiğinizden emin olun. "Yerel Ağ" veya "Tekil IP" seçeneklerinden birini işaretlemeniz gerekir.

5. Destek ve İletişim
Herhangi bir sorunla karşılaşırsanız veya ek destek gerekiyorsa, lütfen benimle iletişime geçin veya uygulamayı geliştirye devam edelim.

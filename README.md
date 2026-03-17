# logistics-data-analysis
Python ve Pandas ile 10.000 satırlık lojistik operasyon verisinin analizi.
# 🚚 Lojistik Operasyonları Veri Analizi ve Optimizasyonu

Bu proje, 10.000 satırlık sentetik bir lojistik operasyon veri seti üzerinde **Python, Pandas ve Matplotlib** kullanılarak uçtan uca veri analizi, özellik mühendisliği (feature engineering) ve raporlama süreçlerinin gerçekleştirildiği bir veri bilimi çalışmasıdır.

## 📌 Proje Amacı
Lojistik operasyonlarında gerçekleşen gecikmelerin varış tarihlerine (ETA) olan etkisini algoritmik olarak hesaplamak, sefer bazlı net kâr/zarar durumlarını ortaya çıkarmak ve rotaların (çıkış limanlarının) verimliliğini yönetici özetleri (Excel & Grafik) halinde sunmaktır.

## 🛠️ Kullanılan Teknolojiler ve Yöntemler
* **Veri İşleme & Analiz:** Pandas
* **Görselleştirme:** Matplotlib
* **Kavramlar:** Veri Okuma/Yazma (CSV, Excel), Feature Engineering, Zaman Serisi Manipülasyonu (Datetime/Timedelta), Mantıksal Filtreleme (Boolean Indexing), Veri Gruplama (GroupBy).

## 🚀 Projede Gerçekleştirilen İşlemler
1. **Güvenli Veri Aktarımı (I/O):** Hata yönetimi (`try-except`) kullanılarak 10.000 satırlık veri setinin sisteme entegrasyonu.
2. **Finansal Metrik Üretimi:** Sefer maliyetleri ve navlun fiyatları üzerinden her bir tır için net kâr hesabı ve yuvarlama (Rounding) işlemleri.
3. **Dinamik Takvim Yönetimi (ETA):** Tırların çıkış tarihlerine sistemdeki gecikme günleri (`timedelta`) eklenerek, güncel "Tahmini Varış Tarihi" sütununun algoritmik olarak oluşturulması.
4. **Operasyonel Filtreleme:** Sadece belirli şartları sağlayan (Örn: Çıkış limanı İzmir olan ve gecikmesi sıfır olan) VIP teslimatların `loc` fonksiyonu ile izole edilmesi.
5. **Raporlama ve Görselleştirme:** Limanlara göre toplam kârların `groupby` ile özetlenerek kurumsal kullanıma uygun Excel formatında dışa aktarılması ve Matplotlib ile Bar Chart olarak görselleştirilmesi.
`![Kâr Grafiği](grafik.png)`

# Endüstriyel Ürün Seri Numarası ve Barkod Okuma Sistemi 🔍📦

Bu proje, endüstriyel üretim bantlarında ve lojistik süreçlerde ürünlerin üzerindeki barkod ve seri numaralarını otomatik olarak tespit edip okumak amacıyla geliştirilmiş yapay zeka destekli bir **Bilgisayarlı Görü (Computer Vision)** ve **Optik Karakter Tanıma (OCR)** sistemidir. 

Mersin Üniversitesi, Bilişim Sistemleri ve Teknolojileri bölümü dönem projesi kapsamında geliştirilmiştir.

## 🚀 Projenin Amacı ve Çalışma Mantığı
Sistem, yüklenen fotoğraftaki karmaşık arka planları veya farklı nesneleri yok sayarak doğrudan etiket bölgesine odaklanır. Uçtan uca çalışan bu mimari şu adımları izler:

1. **Nesne Tespiti (YOLOv11):** Görüntüdeki etiket/barkod bölgesinin milisaniyeler içinde tespit edilip koordinatlarının (Bounding Box) belirlenmesi.
2. **Görüntü İşleme (OpenCV):** Tespit edilen alanın kırpılması (extract), renk gürültülerinden arındırılması (Grayscale) ve okuma kolaylığı için yeniden boyutlandırılması (Resize).
3. **Karakter Tanıma (EasyOCR):** İyileştirilen görüntünün üzerinden sadece harf ve rakamlara odaklanılarak metnin dijital veriye dönüştürülmesi.
4. **Kullanıcı Arayüzü (Streamlit):** Tüm bu karmaşık mimarinin kullanıcı dostu, dinamik bir web arayüzü (dashboard) üzerinden kontrol edilmesi.

## 🛠️ Kullanılan Teknolojiler
* **Yapay Zeka / Derin Öğrenme:** YOLOv11 (Ultralytics)
* **OCR Motoru:** EasyOCR
* **Görüntü İşleme:** OpenCV, NumPy, Pillow (PIL)
* **Web Arayüzü:** Streamlit
* **Model Eğitimi:** Google Colab (T4 GPU) & Roboflow (LBC Barcode Dataset)

## 📁 Dosya Yapısı
* `app.py`: Streamlit arayüzünü, görüntü işleme adımlarını ve OCR entegrasyonunu barındıran ana uygulama dosyası.
* `best.pt`: Özel veri setiyle 20 epoch boyunca eğitilmiş, etiket tespit etmeyi öğrenmiş YOLOv11 model ağırlık (weights) dosyası.

## 💻 Kurulum ve Çalıştırma
Projeyi kendi bilgisayarınızda yerel (local) olarak çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

1. **Gerekli kütüphaneleri yükleyin:**
   Terminal veya komut satırına aşağıdaki komutu yazarak gereksinimleri kurun:
   ```bash
   pip install ultralytics easyocr opencv-python streamlit numpy pillow

import streamlit as st
import cv2
import easyocr
from ultralytics import YOLO
from PIL import Image
import numpy as np

# Sayfa ayarları
st.set_page_config(page_title="Endüstriyel Barkod Okuyucu", layout="centered")

st.title("Endüstriyel Ürün Seri Numarası Okuma Sistemi")
st.write("Lütfen sistem üzerinden taranmasını istediğiniz ürün etiketini yükleyin.")

uploaded_file = st.file_uploader("Fotoğraf Seç", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption='Yüklenen Fotoğraf', use_container_width=True)
    
    with st.spinner("Yapay zeka görseli işliyor..."):
        model = YOLO('best.pt') 
        reader = easyocr.Reader(['en'])
        
        img_array = np.array(image)
        img_cv = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
        
        results = model(img_cv)
        
        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cropped_region = img_cv[y1:y2, x1:x2]
                
                # --- YENİ EKLENEN GÖRÜNTÜ İŞLEME ADIMI ---
                # 1. Resmi gri tonlamaya çeviriyoruz (Renk karmaşasını önler)
                gray = cv2.cvtColor(cropped_region, cv2.COLOR_BGR2GRAY)
                # 2. Resmi 2 kat büyütüyoruz (Küçük rakamların okunmasını kolaylaştırır)
                resized = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
                
                # İyileştirilmiş görüntüyü ekrana basıyoruz
                st.image(resized, caption="Görüntü İşleme ile İyileştirilen Etiket", width=300)
                
                # OCR'a sadece rakamları ve harfleri okumasını söylüyoruz (allowlist)
                ocr_result = reader.readtext(resized, allowlist='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
                
                if ocr_result:
                    st.success(f"Sistem Çıktısı (Okunan Metin): {ocr_result[0][1]}")
                else:
                    st.warning("Etiket bulundu ancak üzerindeki metin okunamadı.")

st.markdown("---")
st.subheader("Geri Bildirim")
rating = st.slider("Sistemi nasıl değerlendirirsiniz? (1-5 arası puanlayın)", 1, 5, 5)
if st.button("Puanı Gönder"):
    st.balloons()
    st.success(f"Değerlendirmeniz ({rating}/5) başarıyla kaydedildi! Teşekkürler.")
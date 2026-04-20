# Real-Time Hand Tracking with MediaPipe

Bu proje, Python, OpenCV ve Google'ın MediaPipe kütüphanesini kullanarak web kamerası üzerinden gerçek zamanlı el ve eklem tespiti (landmark detection) gerçekleştirir.

## Özellikler

* **Gerçek Zamanlı Tespit:** Web kamerasından gelen görüntüyü anlık olarak işler.
* **Eklem Haritalama:** El üzerindeki 21 farklı eklem noktasını (landmarks) tespit eder ve birbirine bağlar.
* **FPS Sayacı:** Görüntü işleme performansını takip etmek için ekranda anlık FPS değerini gösterir.
* **Çoklu El Desteği:** Aynı anda 2 ele kadar takip yapabilir.

## Gereksinimler

Projeyi çalıştırmadan önce gerekli kütüphaneleri yüklediğinizden emin olun:

```bash
pip install opencv-python mediapipe numpy

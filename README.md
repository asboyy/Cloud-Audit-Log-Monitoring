# Cloud Audit Log Monitoring

Cloud Audit Log Monitoring adalah sistem pemantauan berbasis desktop yang dirancang untuk melacak, mencatat, dan menganalisis jejak audit (audit trails) pada aktivitas infrastruktur cloud. Proyek ini bertujuan untuk meningkatkan visibilitas terhadap siapa, melakukan apa, dan kapan sebuah tindakan terjadi di dalam sistem, guna memperkuat postur keamanan dan kepatuhan data.

## 🛡️ Fitur Utama

- **Real-time Logging:** Mencatat setiap aktivitas pengguna dan perubahan konfigurasi sistem secara otomatis.
- **Analisis Jejak Audit:** Memungkinkan administrator untuk meninjau riwayat tindakan (Action History) untuk mendeteksi perilaku mencurigakan.
- **Sistem Notifikasi:** Memberikan peringatan dini jika ditemukan aktivitas yang tidak sah atau melanggar kebijakan keamanan.
- **Manajemen Data Log:** Penyimpanan log yang terstruktur untuk memudahkan proses audit dan investigasi forensik digital.
- **Antarmuka Pemantauan:** Dashboard visual untuk melihat statistik aktivitas secara ringkas.

## 🛠️ Teknologi yang Digunakan

- **Bahasa Pemrograman:** Visual Basic .NET (VB.NET)
- **Framework:** .NET Framework
- **Konsep Keamanan:** - **Audit Trail:** Dokumentasi kronologis dari catatan keamanan.
  - **Accountability:** Memastikan setiap tindakan dapat ditelusuri ke pengguna spesifik.
  - **Compliance:** Memenuhi standar kepatuhan regulasi TI.

## 🧠 Cara Kerja

Sistem ini beroperasi dengan memantau titik-titik akses kritis:
1. **Capture:** Menangkap event yang terjadi pada aplikasi atau simulasi layanan cloud.
2. **Normalize:** Mengubah data mentah log menjadi format yang mudah dibaca (Timestamp, UserID, Action, Status).
3. **Monitor:** Membandingkan aktivitas dengan aturan keamanan yang telah ditentukan.
4. **Alert:** Memicu sinyal peringatan jika terdeteksi anomali.

## 🚀 Cara Menjalankan

1. **Clone Repositori:**
   ```bash
   git clone [https://github.com/asboyy/Cloud-Audit-Log-Monitoring.git](https://github.com/asboyy/Cloud-Audit-Log-Monitoring.git)

from datetime import datetime

# USER & RESOURCE
users = ["admin", "fahmi", "andi"]
resources = ["data_laporan", "data_gaji", "log_server"]

# AUDIT LOG STORAGE
audit_logs = []

# ACTIVITY RISK LEVEL
risk_level = {
    "READ": "LOW",
    "UPDATE": "MEDIUM",
    "DELETE": "HIGH"
}

# SISTEM BERJALAN TERUS
print("=== CLOUD AUDIT LOG & MONITORING SYSTEM ===")

while True:
    print("\nMenu:")
    print("1. Catat aktivitas")
    print("2. Lihat audit log")
    print("3. Lihat ringkasan keamanan")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        username = input("Masukkan username: ")
        resource = input("Masukkan resource cloud: ")
        activity = input("Masukkan aktivitas (READ / UPDATE / DELETE): ").upper()

        if username not in users or resource not in resources or activity not in risk_level:
            print("Input tidak valid ❌")
            continue

        risk = risk_level[activity]

        log = {
            "user": username,
            "resource": resource,
            "activity": activity,
            "risk": risk,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        audit_logs.append(log)
        print("Aktivitas berhasil dicatat ✅")

        # ALERT AKTIVITAS BERISIKO
        if risk == "HIGH":
            print("⚠️ PERINGATAN: Aktivitas berisiko tinggi terdeteksi!")

    elif pilihan == "2":
        print("\n=== AUDIT LOG CLOUD ===")
        if not audit_logs:
            print("Belum ada aktivitas")
        for log in audit_logs:
            print(
                f"[{log['time']}] "
                f"{log['user']} -> {log['activity']} {log['resource']} "
                f"(Risk: {log['risk']})"
            )

    elif pilihan == "3":
        print("\n=== RINGKASAN KEAMANAN ===")
        summary = {"LOW": 0, "MEDIUM": 0, "HIGH": 0}
        for log in audit_logs:
            summary[log["risk"]] += 1

        print(f"Total Aktivitas : {len(audit_logs)}")
        print(f"LOW    : {summary['LOW']}")
        print(f"MEDIUM : {summary['MEDIUM']}")
        print(f"HIGH   : {summary['HIGH']}")

    elif pilihan == "4":
        print("Sistem dihentikan.")
        break

    else:
        print("Pilihan tidak valid ❌")

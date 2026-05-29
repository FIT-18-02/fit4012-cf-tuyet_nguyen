import pandas as pd

def run_mini_soc():
    # 1. Đọc dữ liệu
    df = pd.read_csv('logs.csv')
    
    print("--- BÁO CÁO MINI SOC ---")
    
    # 2. Phân tích: Đếm số lần lỗi đăng nhập (Status 401)
    failed_logins = df[df['status'] == 401]
    
    # 3. Phát hiện bất thường: IP nào lỗi quá 2 lần?
    suspicious = failed_logins['source_ip'].value_counts()
    threats = suspicious[suspicious > 2]
    
    # 4. Hiển thị Dashboard đơn giản
    print("\n[!] Cảnh báo bảo mật:")
    if not threats.empty:
        for ip, count in threats.items():
            print(f"  -> CẢNH BÁO: IP {ip} có {count} lần đăng nhập thất bại (Brute force suspect!)")
    else:
        print("  -> Trạng thái: Hệ thống bình thường.")

    print("\n--- Thống kê nhanh ---")
    print(df['status'].value_counts())

if __name__ == "__main__":
    run_mini_soc()
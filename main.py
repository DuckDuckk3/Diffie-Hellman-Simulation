import tkinter as tk
from tkinter import ttk, messagebox

def run_exchange():
    try:
        # Lấy dữ liệu đầu vào
        p = int(entry_p.get())
        g = int(entry_g.get())
        a = int(entry_a.get())
        b = int(entry_b.get())

        # Làm mới khung log
        log_text.config(state=tk.NORMAL)
        log_text.delete(1.0, tk.END)

        # Bước 1: Tính khóa công khai
        A = pow(g, a, p)
        B = pow(g, b, p)
        
        lbl_A_val.config(text=str(A))
        lbl_B_val.config(text=str(B))

        log_text.insert(tk.END, "--- 1. Public key generation ---\n")
        log_text.insert(tk.END, f"Alice calculates: A = (g^a) mod p = ({g}^{a}) mod {p} = {A}\n")
        log_text.insert(tk.END, f"Bob calculates: B = (g^b) mod p = ({g}^{b}) mod {p} = {B}\n\n")

        log_text.insert(tk.END, "--- 2. Key exchange (over public channel) ---\n")
        log_text.insert(tk.END, f"Alice sends A={A} to Bob.\n")
        log_text.insert(tk.END, f"Bob sends B={B} to Alice.\n\n")

        # Bước 2: Tính khóa phiên chung
        K_A = pow(B, a, p)
        K_B = pow(A, b, p)

        lbl_shared_A.config(text=str(K_A))
        lbl_shared_B.config(text=str(K_B))

        log_text.insert(tk.END, "--- 3. Shared secret computation ---\n")
        log_text.insert(tk.END, f"Alice computes: K = (B^a) mod p = ({B}^{a}) mod {p} = {K_A}\n")
        log_text.insert(tk.END, f"Bob computes: K = (A^b) mod p = ({A}^{b}) mod {p} = {K_B}\n\n")

        if K_A == K_B:
            log_text.insert(tk.END, f"=> Success! Both parties share the same secret key: {K_A}")
        else:
            log_text.insert(tk.END, "=> Error! Shared keys do not match.")

        log_text.config(state=tk.DISABLED)

    except ValueError:
        messagebox.showerror("Input error", "Please enter valid integers only.")

# Khởi tạo cửa sổ chính
root = tk.Tk()
root.title("Diffie-Hellman key exchange simulation")
root.geometry("750x650")

# Sử dụng theme clam cho giao diện hiện đại hơn
style = ttk.Style()
style.theme_use('clam')

# Tiêu đề
lbl_title = ttk.Label(root, text="Diffie-Hellman key exchange", font=("Arial", 16, "bold"))
lbl_title.pack(pady=15)

# Khung chính
main_frame = ttk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)

# Khung tham số công khai
frame_public = ttk.LabelFrame(main_frame, text=" Public parameters (known to everyone) ")
frame_public.pack(fill=tk.X, pady=5)

ttk.Label(frame_public, text="Prime number (p):").grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_p = ttk.Entry(frame_public, width=20)
entry_p.grid(row=0, column=1, padx=10, pady=10)

ttk.Label(frame_public, text="Generator (g):").grid(row=0, column=2, padx=10, pady=10, sticky="e")
entry_g = ttk.Entry(frame_public, width=20)
entry_g.grid(row=0, column=3, padx=10, pady=10)

# Khung người dùng 
frame_users = ttk.Frame(main_frame)
frame_users.pack(fill=tk.X, pady=10)

# Khung A
frame_alice = ttk.LabelFrame(frame_users, text=" Анастасия (sender) ")
frame_alice.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))

ttk.Label(frame_alice, text="Private key (a):").grid(row=0, column=0, sticky="w", padx=10, pady=10)
entry_a = ttk.Entry(frame_alice, width=15)
entry_a.grid(row=0, column=1, padx=10, pady=10)

ttk.Label(frame_alice, text="Generated public key (A):").grid(row=1, column=0, sticky="w", padx=10, pady=10)
lbl_A_val = ttk.Label(frame_alice, text="?", font=("Arial", 11, "bold"), foreground="blue")
lbl_A_val.grid(row=1, column=1, sticky="w", padx=10, pady=10)

ttk.Label(frame_alice, text="Computed shared secret (K):").grid(row=2, column=0, sticky="w", padx=10, pady=10)
lbl_shared_A = ttk.Label(frame_alice, text="?", font=("Arial", 11, "bold"), foreground="green")
lbl_shared_A.grid(row=2, column=1, sticky="w", padx=10, pady=10)

# Khung B
frame_bob = ttk.LabelFrame(frame_users, text=" Борис (receiver) ")
frame_bob.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))

ttk.Label(frame_bob, text="Private key (b):").grid(row=0, column=0, sticky="w", padx=10, pady=10)
entry_b = ttk.Entry(frame_bob, width=15)
entry_b.grid(row=0, column=1, padx=10, pady=10)

ttk.Label(frame_bob, text="Generated public key (B):").grid(row=1, column=0, sticky="w", padx=10, pady=10)
lbl_B_val = ttk.Label(frame_bob, text="?", font=("Arial", 11, "bold"), foreground="blue")
lbl_B_val.grid(row=1, column=1, sticky="w", padx=10, pady=10)

ttk.Label(frame_bob, text="Computed shared secret (K):").grid(row=2, column=0, sticky="w", padx=10, pady=10)
lbl_shared_B = ttk.Label(frame_bob, text="?", font=("Arial", 11, "bold"), foreground="green")
lbl_shared_B.grid(row=2, column=1, sticky="w", padx=10, pady=10)

# Nút thực thi
btn_run = ttk.Button(main_frame, text="Generate and exchange keys", command=run_exchange)
btn_run.pack(pady=15)

# Khung Log tính toán
frame_log = ttk.LabelFrame(main_frame, text=" Calculation and exchange log ")
frame_log.pack(fill=tk.BOTH, expand=True, pady=5)

log_text = tk.Text(frame_log, height=12, state=tk.DISABLED, bg="#f4f4f4", font=("Consolas", 10))
log_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

root.mainloop()

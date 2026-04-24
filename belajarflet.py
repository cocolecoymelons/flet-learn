import flet as ft
import json
import os

class Dompet(): 
    def __init__(self, username):
        self.liquid_assets = 0
        self.savings = 0
        self.username = username
        self.nama_file = f"data_dompet_{username}.json"
        self.load_data() 

    def adding(self, nominal):
        self.liquid_assets = round(self.liquid_assets + nominal, 2)
        self.save_data()
        print(f"{self.username}: Berhasil ditambahkan! Saldo mu saat ini: {self.liquid_assets} $")
        return True, f"Berhasil menambahkan saldo sebesar {nominal}!"
    def substract(self, nominal):
        if nominal < self.liquid_assets:
            self.liquid_assets = round(self.liquid_assets - nominal, 2)
            self.save_data()
            print(f"{self.username}: Berhasil withdraw! Saldo mu saat ini: {self.liquid_assets} $")
            return True, f"Berhasil melakukan withdrawal sebesar {nominal}!"
        else:
            print("Saldomu tidak cukup!")
            return False, f"Saldomu tidak mencukupi!"
    def saving(self, nominal):
        if nominal < self.liquid_assets:
            self.savings = round(self.savings + nominal, 2)
            self.liquid_assets = round(self.liquid_assets - nominal, 2)
            self.save_data()
            print(f"{self.username}: Tabungan berhasil ditambahkan!")
            return True, f"Berhasil menabung sebesar {nominal}!"
        else:
            print("Saldomu tidak cukup!")
            return False, "Saldomu tidak mencukupi!"
    def saving_wd(self, nominal):
        if nominal < self.savings:
            self.savings = round(self.savings - nominal, 2)
            self.liquid_assets = round(self.liquid_assets + nominal, 2)
            self.save_data()
            print(f"{self.username}: Tabungan berhasil di withdrawal!")
            return True, f"Berhasil melakukan withdrawal tabungan sebesar {nominal}!"
        else:
            print("Saldomu tidak cukup!")
            return False, "Saldomu tidak mencukupi!"
    def save_data(self):
        data = {
            "Liquid_assets": self.liquid_assets,
            "Savings": self.savings
        }
        with open(self.nama_file, "w") as file:
            json.dump(data, file)

    def load_data(self):
        if os.path.exists(self.nama_file):
            with open(self.nama_file, "r") as file:
                data = json.load(file)
                self.liquid_assets = data["Liquid_assets"]
                self.savings = data["Savings"]

def main(page: ft.Page):
    page.title = "User Page Login"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def login_page(e=None):
        page.controls.clear()
        page.percobaan = 0
        kotak_nama = ft.TextField(label="User")
        kotak_password = ft.TextField(
            label="Password",
            password=True,
            can_reveal_password=True
        )
        pesan = ft.Text()
        pesan_peringatan = ft.Text()

        def aksi_login(e):
            username = kotak_nama.value
            password = kotak_password.value
            database = []
            if username and password:
                if not os.path.exists("database.json"):
                    pesan.value = "Username tidak ditemukan! Silahkan Sign In."
                    pesan.color = "red"
                    page.update()
                    return
                else:
                    with open("database.json", "r") as file:
                        database = json.load(file)
                    user_ketemu = False
                    for user in database:
                        if user["user_id"] == username:
                            user_ketemu = True
                            if user["id_password"] == password:
                                main_page(username)
                                return
                            else:
                                pesan.value = "Password salah!"
                                pesan.color = "red"
                                page.percobaan += 1
                            break
                    if not user_ketemu:
                        pesan.value = "Username tidak ditemukan!"
                        pesan.color = "red"
            else:
                pesan.value = "Silahkan diisi! (Mohon tidak melakukan spam!)"
                pesan.color = "red"
                page.percobaan += 1

            if page.percobaan >= 3:
                tombol_admin.visible = True
                pesan.value = "Akses diblokir, silahkan hubungi Admin!"
                pesan.color = "red"
                kotak_nama.disabled = True
                kotak_password.disabled = True
                tombol.disabled = True
                tombol_sign_in.disabled = True
            page.update()

        def aksi_sign(e):
            username = kotak_nama.value
            password = kotak_password.value
            if not username or not password:
                pesan.value = "Username atau Password tidak boleh kosong!"
                pesan.color = "red"
                page.update()
                return
            database = []
            if os.path.exists("database.json"):
                with open("database.json", "r") as file:
                    database = json.load(file)
            for user in database:
                if user["user_id"] == username:
                    pesan.value = "Username sudah dipakai, silahkan pilih username lain."
                    pesan.color = "white"
                    page.update()
                    return
            user_baru = {"user_id": username, "id_password": password}
            database.append(user_baru)
            with open("database.json", "w") as file:
                json.dump(database, file, indent=4)
            pesan.value = "Berhasil Sign In!"
            pesan.color = "green"
            page.update()

        def aksi_admin(e):
            page.percobaan = 0
            tombol.disabled = False
            tombol_sign_in.disabled = False
            kotak_nama.disabled = False
            kotak_password.disabled = False
            tombol_admin.visible = False
            pesan_peringatan.value = ""
            pesan.value = "Admin mengembalikan akses. Silahkan dicoba kembali."
            pesan.color = "green"
            page.update()

        tombol_admin = ft.FilledButton(content=ft.Text("Admin"), visible=False, on_click=aksi_admin)
        tombol = ft.FilledButton(content=ft.Text("Masuk"), on_click=aksi_login)
        tombol_sign_in = ft.FilledButton(content=ft.Text("Sign In"), on_click=aksi_sign)

        page.add(
            ft.Column(
                [
                    ft.Row([kotak_nama, kotak_password], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([tombol, tombol_sign_in], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([tombol_admin], alignment=ft.MainAxisAlignment.CENTER),
                    pesan,
                    pesan_peringatan
                ],
                horizontal_alignment=ft.MainAxisAlignment.CENTER
            )
        )
        page.update()

    def main_page(username):
        page.controls.clear()
        dompetku = Dompet(username)
        page.title = f"Dompet: {username}"
        display_liquid = ft.Text(f"Liquid Assets: {dompetku.liquid_assets}$", size=20)
        display_savings = ft.Text(f"Savings: {dompetku.savings}$", size=20)
        input_nominal = ft.TextField(label="Nominal (dalam $)")
        def aksi_transaksi(e, tipe):
            sukses = False
            pesan = "Terjadi kesalahan"
            try:
                nominal = float(input_nominal.value)
                if tipe == "Tambah":
                    sukses, pesan = dompetku.adding(nominal)
                elif tipe == "Tarik":
                    sukses, pesan = dompetku.substract(nominal)
                elif tipe == "Tabung":
                    sukses, pesan = dompetku.saving(nominal)
                elif tipe == "WD Tabung":
                    sukses, pesan = dompetku.saving_wd(nominal)
                if sukses:
                    display_liquid.value = f"Liquid Assets: {dompetku.liquid_assets}$"
                    display_savings.value = f"Savings: {dompetku.savings}$"
                    input_nominal.value = ""
                    snack = page.snack_bar = ft.SnackBar(
                        content=ft.Text(pesan),
                        bgcolor="green",
                        duration=3000)
                    page.overlay.append(snack)
                    snack.open = True
                    tutup_dialog()
                    page.update()
                else:
                    input_nominal.error_text = pesan 
                    snack = page.snack_bar = ft.SnackBar(ft.Text(pesan), bgcolor="red")
                    page.overlay.append(snack)
                    snack.open = True
                    page.update()
            except ValueError:
                input_nominal.error_text = "Masukkan angka yang valid!"
                page.update()
        dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text(f"Transaksi"),
            content=input_nominal,
            actions=[
                ft.TextButton("Batal", on_click=lambda _: page.close(dlg)),
            ],
        )
        page.overlay.append(dlg)
        def tutup_dialog(e=None):
            dlg.open = False
            page.update()
        def buka_dialog(e, tipe):
            dlg.title.value = f"Transaksi: {tipe}"
            input_nominal.value = ""
            input_nominal.error_text = None
            dlg.actions = [
                ft.TextButton("Batal", on_click=tutup_dialog),
                ft.ElevatedButton("Proses", on_click=lambda _: aksi_transaksi(None, tipe))]
            dlg.open = True
            page.update()
        page.add(
            ft.Column(
                [
                    ft.Text(f"Selamat datang {username}!", size=25),
                    ft.Row([display_liquid, display_savings], alignment=ft.MainAxisAlignment.SPACE_AROUND),
                    ft.Divider(),
                    ft.Text("Manajemen Aset:"),
                    ft.Row([
                        ft.ElevatedButton("Tambah Saldo", icon="add", on_click=lambda e: buka_dialog(e, "Tambah")),
                        ft.ElevatedButton("Tarik Saldo", icon="remove", on_click=lambda e: buka_dialog(e, "Tarik")),
                    ]),
                    ft.Text("Manajemen Tabungan:"),
                    ft.Row([
                        ft.ElevatedButton("Pindah ke Tabungan", icon="savings", on_click=lambda e: buka_dialog(e, "Tabung")),
                        ft.ElevatedButton("Ambil dari Tabungan", icon="wallet", on_click=lambda e: buka_dialog(e, "WD Tabung")),
                    ]),
                    ft.Divider(),
                    ft.FilledButton("Log out", on_click=lambda _: login_page())
                ],
                spacing=20
            )
        )
        page.update()

    login_page()

ft.app(target=main)

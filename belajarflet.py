import flet as ft
import json
import os
def main(page: ft.Page):
    page.Title = "User Page Login"
    page.percobaan = 0
    page.percobaan_spam = 0
    page.new_user = "Baru"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    kotak_nama = ft.TextField(label="User")
    kotak_password = ft.TextField(
        label="Password",
        password=True,
        can_reveal_password=True)
    sign_in = ft.TextField(label="Sign In")
    pesan = ft.Text()
    pesan_peringatan = ft.Text()
    def aksi_password(e):
        username = kotak_nama.value
        password = kotak_password.value
        databse = []
        if username and password:
            if 
    def aksi_admin(e):
        page.percobaan = 0
        page.percobaan_spam = 0
        tombol.disabled = False
        kotak_nama.disabled = False
        tombol_admin.visible = False
        pesan_peringatan.value = ""
        pesan.value = "Admin mengembalikan akses. Silahkan dicoba kembali."
        pesan.color = "green"
        page.update()
    tombol_admin = ft.FilledButton(content=ft.Text("Admin"),visible=False,on_click=aksi_admin)
    def aksi(e):
        nama = kotak_nama.value
        if page.new_user == "Lama":
            page.percobaan_spam += 1
            if page.percobaan_spam >= 3:
                pesan.value = "Akses diblokir, silahkan hubungi admin."
                pesan.color = "red"
                tombol.disabled = True
                kotak_nama.disabled = True
                tombol_admin.visible = True
            else:
                pesan.value = "Anda sudah memberi tahu nama anda. Mohon jangan spam!"
                pesan.color = "orange"
            page.update()
            return
        else:
            if not nama:
                page.percobaan += 1
                if page.percobaan >= 3:
                    pesan.value = "Akses diblokir, silahkan hubungi admin."
                    pesan.color = "red"
                    tombol.disabled = True
                    kotak_nama.disabled = True
                    tombol_admin.visible = True
                pesan_peringatan.value = f"Silahkan diisi ya! Akses kamu akan diblokir jika peringatan mencapai 3 kali! {page.percobaan}/3"    
            else:
                pesan.value = f"Halo {nama}! Selamat datang!"
                page.update()
                page.new_user = "Lama"
    tombol = ft.ElevatedButton(content= ft.Text("Ok"), on_click=aksi)
    page.add(ft.Column(
        [
            kotak_nama,
            tombol,
            ft.Row([tombol_admin]),
            pesan,
            pesan_peringatan
            ],
            horizontal_alignment=ft.MainAxisAlignment.CENTER

    ))

ft.app(target=main)
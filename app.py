import streamlit as st
import streamlit.components.v1 as components
import base64
import mimetypes
from pathlib import Path

st.set_page_config(
    page_title="PT Nuha Berkah Abadi",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Menyembunyikan elemen bawaan Streamlit agar tampil seperti website biasa.
st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .stApp {background: #ffffff;}
        .block-container {
            max-width: 100%;
            padding: 0;
        }
        [data-testid="stAppViewContainer"],
        [data-testid="stMain"],
        .stMainBlockContainer {
            max-width: 100%;
            padding: 0;
        }
        iframe {
            display: block;
            width: 100%;
            max-width: 100%;
            border: 0;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# FOTO PRODUK
# Buat folder bernama "images" di samping file ini, lalu masukkan
# produk1.jpg sampai produk10.jpg. Nama file dapat diubah pada
# daftar_gambar yang berada di bagian bawah kode.
def baca_gambar(nama_file):
    lokasi = Path(__file__).parent / "images" / nama_file

    if not lokasi.exists():
        # Gambar cadangan agar website tetap dapat dibuka ketika foto belum ada.
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="600">
        <rect width="100%" height="100%" fill="#eefaff"/>
        <text x="50%" y="48%" text-anchor="middle" fill="#2396c4"
              font-family="Arial" font-size="34" font-weight="bold">Foto belum tersedia</text>
        <text x="50%" y="57%" text-anchor="middle" fill="#698b9b"
              font-family="Arial" font-size="22">{nama_file}</text>
        </svg>'''
        data = base64.b64encode(svg.encode("utf-8")).decode("utf-8")
        return f"data:image/svg+xml;base64,{data}"

    tipe, _ = mimetypes.guess_type(lokasi)
    tipe = tipe or "image/jpeg"

    with open(lokasi, "rb") as file:
        data = base64.b64encode(file.read()).decode("utf-8")

    return f"data:{tipe};base64,{data}"

# Seluruh tampilan website HTML ditanam langsung di dalam aplikasi Streamlit.
html_code = r'''<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>PT Nuha Berkah Abadi | Seafood & Fillet Frozen Premium</title>

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap" rel="stylesheet">

    <style>
        :root {
            --navy: #176b87;
            --dark: #125b75;
            --blue: #2396c4;
            --cyan: #54cbe8;
            --light-blue: #eefaff;
            --white: #ffffff;
            --text: #173f52;
            --muted: #698b9b;
            --border: #d9edf5;
        }

        * {
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
        }

        section[id] {
            scroll-margin-top: 76px;
        }

        body {
            margin: 0;
            font-family: "Inter", sans-serif;
            color: var(--text);
            background: #f8fdff;
            overflow-x: hidden;
        }

        h1,
        h2,
        h3,
        .brand {
            font-family: "Plus Jakarta Sans", sans-serif;
        }

        img {
            display: block;
            max-width: 100%;
        }

        button,
        input,
        select,
        textarea {
            font-family: inherit;
        }

        .container {
            width: min(1180px, calc(100% - 40px));
            margin: auto;
        }

        /* NAVBAR */
        .navbar {
            position: fixed;
            top: 0;
            right: 0;
            left: 0;
            z-index: 100;
            background: rgba(28, 112, 142, 0.92);
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(14px);
        }

        .nav-content {
            min-height: 76px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 24px;
        }

        .brand {
            display: flex;
            align-items: center;
            gap: 11px;
            color: white;
            font-weight: 800;
            text-decoration: none;
        }

        .brand-icon {
            width: 42px;
            height: 42px;
            display: grid;
            place-items: center;
            border-radius: 14px;
            background: linear-gradient(135deg, var(--cyan), var(--blue));
            font-size: 21px;
        }

        .nav-links {
            display: flex;
            align-items: center;
            gap: 27px;
        }

        .nav-links a {
            color: rgba(255, 255, 255, 0.82);
            font-size: 14px;
            font-weight: 600;
            text-decoration: none;
        }

        .nav-links a:hover {
            color: white;
        }

        .nav-button {
            padding: 11px 18px;
            color: white !important;
            background: var(--blue);
            border-radius: 999px;
        }

        .mobile-menu-toggle {
            width: 42px;
            height: 42px;
            display: none;
            align-items: center;
            justify-content: center;
            color: white;
            background: var(--blue);
            border: 0;
            border-radius: 12px;
            font-size: 23px;
            line-height: 1;
            cursor: pointer;
        }

        /* HERO */
        .hero {
            min-height: 790px;
            display: flex;
            align-items: center;
            position: relative;
            overflow: hidden;
            background:
                linear-gradient(
                    105deg,
                    rgba(18, 91, 117, 0.90) 0%,
                    rgba(30, 126, 157, 0.72) 52%,
                    rgba(65, 170, 198, 0.28) 100%
                ),
                url("https://images.unsplash.com/photo-1544943910-4c1dc44aab44?auto=format&fit=crop&w=2000&q=85")
                center/cover no-repeat;
        }

        .hero::after {
            content: "";
            position: absolute;
            right: 0;
            bottom: 0;
            left: 0;
            height: 150px;
            background: linear-gradient(transparent, rgba(18, 91, 117, 0.82));
        }

        .hero-grid {
            position: relative;
            z-index: 2;
            padding-top: 100px;
            display: grid;
            grid-template-columns: 1.15fr 0.85fr;
            align-items: center;
            gap: 70px;
        }

        .eyebrow {
            display: inline-flex;
            align-items: center;
            gap: 9px;
            padding: 8px 13px;
            color: #bff5ff;
            background: rgba(32, 188, 225, 0.12);
            border: 1px solid rgba(126, 231, 252, 0.28);
            border-radius: 999px;
            font-size: 12px;
            font-weight: 800;
            letter-spacing: 0.14em;
            text-transform: uppercase;
        }

        .eyebrow-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: #52e2ff;
        }

        .hero h1 {
            max-width: 750px;
            margin: 22px 0;
            color: white;
            font-size: clamp(42px, 5.4vw, 72px);
            line-height: 1.04;
            letter-spacing: -2.5px;
        }

        .hero h1 span {
            color: #52e2ff;
        }

        .hero-description {
            max-width: 650px;
            margin: 0 0 30px;
            color: rgba(235, 248, 253, 0.83);
            font-size: 17px;
            line-height: 1.8;
        }

        .hero-buttons {
            display: flex;
            flex-wrap: wrap;
            gap: 13px;
        }

        .button {
            min-height: 52px;
            padding: 0 21px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            border-radius: 14px;
            font-weight: 800;
            text-decoration: none;
            transition: 0.25s;
        }

        .button-primary {
            color: white;
            background: linear-gradient(135deg, var(--cyan), var(--blue));
            box-shadow: 0 15px 32px rgba(8, 127, 189, 0.3);
        }

        .button-white {
            color: var(--navy);
            background: white;
        }

        .button:hover {
            transform: translateY(-2px);
        }

        .stats {
            margin-top: 35px;
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 12px;
        }

        .stat {
            padding: 18px;
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 17px;
            background: rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(10px);
        }

        .stat strong {
            display: block;
            color: white;
            font-size: 20px;
        }

        .stat span {
            display: block;
            margin-top: 5px;
            color: rgba(232, 247, 252, 0.65);
            font-size: 11px;
        }

        .featured-card {
            overflow: hidden;
            background: white;
            border-radius: 28px;
            box-shadow: 0 35px 80px rgba(0, 0, 0, 0.3);
        }

        .featured-card img {
            width: 100%;
            height: 270px;
            object-fit: cover;
        }

        .featured-content {
            padding: 25px;
        }

        .featured-label {
            display: inline-block;
            padding: 7px 10px;
            color: var(--blue);
            background: var(--light-blue);
            border-radius: 999px;
            font-size: 10px;
            font-weight: 800;
        }

        .featured-content h3 {
            margin: 15px 0 7px;
            font-size: 25px;
        }

        .featured-description {
            margin: 0;
            color: var(--blue);
            font-size: 14px;
            line-height: 1.65;
            font-weight: 600;
        }

        /* GENERAL SECTION */
        .section {
            padding: 95px 0;
        }

        .section-header {
            margin-bottom: 42px;
            display: flex;
            align-items: end;
            justify-content: space-between;
            gap: 30px;
        }

        .section-label {
            color: var(--blue);
            font-size: 12px;
            font-weight: 800;
            letter-spacing: 0.16em;
            text-transform: uppercase;
        }

        .section-title {
            margin: 10px 0 0;
            font-size: clamp(31px, 4vw, 47px);
            line-height: 1.12;
            letter-spacing: -1.4px;
        }

        .section-description {
            max-width: 550px;
            margin: 0;
            color: var(--muted);
            font-size: 14px;
            line-height: 1.75;
        }

        /* PRODUCTS */
        .products {
            background:
                radial-gradient(circle at 15% 10%, rgba(32, 188, 225, 0.1), transparent 27%),
                #f8fdff;
        }

        .product-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 21px;
        }

        .product-card {
            overflow: hidden;
            background: white;
            border: 1px solid #e1edf4;
            border-radius: 22px;
            box-shadow: 0 12px 35px rgba(11, 75, 105, 0.07);
            transition: 0.28s;
        }

        .product-card:hover {
            transform: translateY(-7px);
            box-shadow: 0 22px 45px rgba(11, 75, 105, 0.14);
        }

        .product-image {
            position: relative;
            height: 205px;
            overflow: hidden;
        }

        .product-image img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: 0.4s;
        }

        .product-card:hover .product-image img {
            transform: scale(1.06);
        }

        .badge {
            position: absolute;
            top: 13px;
            left: 13px;
            padding: 7px 10px;
            color: #075e8e;
            background: rgba(236, 250, 255, 0.94);
            border-radius: 999px;
            font-size: 10px;
            font-weight: 800;
        }

        .product-content {
            padding: 19px;
        }

        .product-category {
            display: inline-block;
            padding: 6px 9px;
            color: var(--blue);
            background: #edf9ff;
            border-radius: 999px;
            font-size: 10px;
            font-weight: 800;
        }

        .product-content h3 {
            margin: 13px 0 7px;
            font-size: 19px;
        }

        .product-content p {
            min-height: 62px;
            margin: 0;
            color: #718396;
            font-size: 12px;
            line-height: 1.65;
        }

        .availability-note {
            margin: 28px 0 0;
            color: #8ca0af;
            font-size: 11px;
            line-height: 1.6;
            text-align: center;
        }

        /* ABOUT */
        .about {
            color: white;
            background: linear-gradient(120deg, #2c8fac, #3ba8c3 55%, #62bfd3);
        }

        .about-grid {
            display: grid;
            grid-template-columns: 1.05fr 0.95fr;
            align-items: center;
            gap: 70px;
        }

        .about .section-label {
            color: #62e3ff;
        }

        .about .section-title {
            color: white;
        }

        .about-text {
            color: rgba(232, 247, 252, 0.78);
            font-size: 15px;
            line-height: 1.8;
        }

        .about-list {
            margin-top: 25px;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 13px;
        }

        .about-item {
            display: flex;
            align-items: center;
            gap: 9px;
            font-size: 13px;
            font-weight: 600;
        }

        .check {
            width: 22px;
            height: 22px;
            display: grid;
            place-items: center;
            border-radius: 50%;
            color: #62e3ff;
            background: rgba(81, 225, 255, 0.14);
        }

        .about-image {
            width: 100%;
            height: 440px;
            object-fit: cover;
            border-radius: 28px;
            box-shadow: 0 30px 70px rgba(0, 0, 0, 0.22);
        }

        /* FEATURES */
        .features {
            background: white;
        }

        .feature-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 18px;
        }

        .feature-card {
            padding: 26px;
            border: 1px solid #e2eef5;
            border-radius: 21px;
            background: linear-gradient(180deg, white, #f7fcff);
        }

        .feature-icon {
            width: 49px;
            height: 49px;
            margin-bottom: 18px;
            display: grid;
            place-items: center;
            border-radius: 15px;
            color: var(--blue);
            background: var(--light-blue);
            font-size: 21px;
        }

        .feature-card h3 {
            margin: 0 0 8px;
            font-size: 17px;
        }

        .feature-card p {
            margin: 0;
            color: #708295;
            font-size: 12px;
            line-height: 1.7;
        }

        /* ORDER */
        .order {
            background: #f0fbff;
        }

        .order-box {
            padding: 12px;
            display: grid;
            grid-template-columns: 0.9fr 1.1fr;
            gap: 34px;
            background: white;
            border: 1px solid var(--border);
            border-radius: 28px;
            box-shadow: 0 25px 60px rgba(9, 74, 103, 0.09);
        }

        .order-info {
            padding: 35px;
            color: white;
            border-radius: 20px;
            background: linear-gradient(150deg, #2b91af, #53b9d1);
        }

        .order-info h2 {
            margin: 12px 0 15px;
            font-size: 31px;
            line-height: 1.18;
        }

        .order-info p {
            color: rgba(240, 250, 255, 0.77);
            font-size: 13px;
            line-height: 1.75;
        }

        .contact {
            margin-top: 24px;
        }

        .contact-label {
            margin-bottom: 5px;
            color: rgba(255, 255, 255, 0.56);
            font-size: 11px;
        }

        .contact a {
            color: white;
            font-size: 14px;
            font-weight: 800;
            text-decoration: none;
        }

        .order-form {
            padding: 34px 32px;
        }

        .form-title {
            margin-bottom: 23px;
            font-size: 24px;
            font-weight: 800;
        }

        .field {
            margin-bottom: 17px;
        }

        .field label {
            display: block;
            margin-bottom: 8px;
            color: #29445a;
            font-size: 12px;
            font-weight: 800;
        }

        .field input,
        .field select,
        .field textarea {
            width: 100%;
            padding: 13px 14px;
            color: #17354b;
            background: white;
            border: 1px solid #d6e5ed;
            border-radius: 13px;
            outline: none;
            font-size: 13px;
        }

        .field textarea {
            min-height: 115px;
            resize: vertical;
        }

        .field input:focus,
        .field select:focus,
        .field textarea:focus {
            border-color: var(--cyan);
            box-shadow: 0 0 0 4px rgba(32, 188, 225, 0.11);
        }

        .submit-button {
            width: 100%;
            min-height: 51px;
            color: white;
            background: linear-gradient(135deg, var(--cyan), var(--blue));
            border: none;
            border-radius: 14px;
            font-size: 14px;
            font-weight: 800;
            cursor: pointer;
            transition: 0.25s;
        }

        .submit-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 12px 25px rgba(8, 127, 189, 0.22);
        }

        .form-note {
            margin: 12px 0 0;
            color: #718798;
            font-size: 11px;
            line-height: 1.6;
            text-align: center;
        }

        /* FOOTER */
        footer {
            padding: 28px 0;
            color: #8ba6b5;
            background: var(--dark);
        }

        .footer-content {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 20px;
            font-size: 12px;
        }

        .footer-content strong {
            color: white;
        }

        /* RESPONSIVE */
        @media (max-width: 1050px) {
            .hero-grid,
            .about-grid,
            .order-box {
                grid-template-columns: 1fr;
            }

            .featured-card {
                max-width: 500px;
            }

            .product-grid,
            .feature-grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }

        @media (max-width: 760px) {
            section[id] {
                scroll-margin-top: 67px;
            }

            .container {
                width: calc(100% - 28px);
            }

            .nav-content {
                min-height: 67px;
                gap: 10px;
            }

            .nav-links {
                position: absolute;
                top: calc(100% + 8px);
                right: 0;
                left: 0;
                display: none;
                padding: 12px;
                flex-direction: column;
                align-items: stretch;
                gap: 5px;
                background: rgba(28, 112, 142, 0.98);
                border: 1px solid rgba(255, 255, 255, 0.12);
                border-radius: 16px;
                box-shadow: 0 18px 40px rgba(0, 0, 0, 0.32);
            }

            .nav-links.open {
                display: flex;
            }

            .nav-links a,
            .nav-links a:not(.nav-button) {
                display: block;
                padding: 12px 14px;
                border-radius: 10px;
                font-size: 13px;
            }

            .nav-links a:hover {
                background: rgba(255, 255, 255, 0.08);
            }

            .nav-button {
                padding: 12px 14px;
                font-size: 12px !important;
                text-align: center;
            }

            .mobile-menu-toggle {
                display: inline-flex;
            }

            .brand {
                gap: 8px;
                font-size: 14px;
            }

            .brand-icon {
                width: 36px;
                height: 36px;
                border-radius: 11px;
                font-size: 18px;
            }

            .hero {
                min-height: auto;
                padding: 90px 0 60px;
            }

            .hero-grid {
                padding-top: 15px;
                gap: 35px;
            }

            .hero h1 {
                font-size: clamp(34px, 11vw, 42px);
                line-height: 1.08;
                letter-spacing: -1.2px;
            }

            .hero-description {
                font-size: 15px;
                line-height: 1.7;
            }

            .hero-buttons {
                flex-direction: column;
            }

            .button {
                width: 100%;
            }

            .featured-card {
                width: 100%;
                border-radius: 20px;
            }

            .featured-card img {
                height: 220px;
            }

            .stats {
                grid-template-columns: 1fr;
            }

            .section {
                padding: 58px 0;
            }

            .section-header {
                display: block;
            }

            .section-description {
                margin-top: 15px;
            }

            .section-title {
                font-size: 30px;
                letter-spacing: -0.8px;
            }

            .product-grid,
            .feature-grid {
                grid-template-columns: 1fr;
            }

            .product-image {
                height: 225px;
            }

            .product-content p {
                min-height: auto;
            }

            .about-list {
                grid-template-columns: 1fr;
            }

            .about-image {
                height: 320px;
            }

            .order-info,
            .order-form {
                padding: 21px;
            }

            .order-box {
                padding: 7px;
                gap: 8px;
                border-radius: 20px;
            }

            .order-info {
                border-radius: 16px;
            }

            .order-info h2 {
                font-size: 27px;
            }

            .field input,
            .field select,
            .field textarea {
                font-size: 16px;
            }

            .footer-content {
                flex-direction: column;
                align-items: flex-start;
            }
        }

        @media (max-width: 420px) {
            .container {
                width: calc(100% - 22px);
            }

            .brand {
                font-size: 12px;
            }

            .nav-button {
                padding: 8px 10px;
                font-size: 11px !important;
            }

            .eyebrow {
                font-size: 10px;
                letter-spacing: 0.1em;
            }

            .hero h1 {
                font-size: 33px;
            }

            .section-title {
                font-size: 27px;
            }

            .about-image {
                height: 250px;
            }

            .order-info,
            .order-form {
                padding: 18px;
            }
        }
    </style>
</head>

<body>

    <!-- NAVBAR -->
    <header class="navbar">
        <div class="container nav-content">
            <a href="#beranda" class="brand">
                <span class="brand-icon">NBA</span>
                PT NUHA BERKAH ABADI
            </a>

            <button
                type="button"
                class="mobile-menu-toggle"
                aria-label="Buka menu navigasi"
                aria-expanded="false"
                aria-controls="menuNavigasi"
            >
                ☰
            </button>

            <nav class="nav-links" id="menuNavigasi">
                <a href="#beranda">Beranda</a>
                <a href="#produk">Produk</a>
                <a href="#tentang">Tentang Kami</a>
                <a href="#keunggulan">Keunggulan</a>
                <a href="#kontak" class="nav-button">Hubungi Kami</a>
            </nav>
        </div>
    </header>

    <!-- HERO -->
    <section class="hero" id="beranda">
        <div class="container hero-grid">
            <div>
                <div class="eyebrow">
                    <span class="eyebrow-dot"></span>
                    Distributor seafood & fillet frozen premium
                </div>

                <h1>
                    Penyedia Utama Seafood &
                    <span>Fillet Premium Beku (Frozen)</span>
                </h1>

                <p class="hero-description">
                    PT Nuha Berkah Abadi menyediakan berbagai pilihan seafood beku
                    dan produk fillet premium untuk hotel, restoran, katering,
                    usaha kuliner, dan rumah tangga, didukung rantai pendingin
                    yang andal.
                </p>

                <div class="hero-buttons">
                    <a href="#produk" class="button button-primary">
                        Lihat Produk
                    </a>

                    <a
                        href="https://wa.me/6282220404770?text=Halo%20PT%20Nuha%20Berkah%20Abadi,%20saya%20ingin%20menanyakan%20produk%20seafood%20dan%20fillet%20frozen."
                        target="_blank"
                        class="button button-white"
                    >
                        Tanya via WhatsApp
                    </a>
                </div>

                <div class="stats">
                    <div class="stat">
                        <strong>❄️</strong>
                        <span>Rantai Pendingin Terjaga</span>
                    </div>

                    <div class="stat">
                        <strong>✓</strong>
                        <span>Pilihan Premium Fresh Frozen</span>
                    </div>

                    <div class="stat">
                        <strong>🚚</strong>
                        <span>Pengiriman Cepat via WhatsApp</span>
                    </div>
                </div>
            </div>

            <div class="featured-card">
                <img
                    src="GAMBAR_PRODUK_1"
                    alt="Salmon Portion"
                >

                <div class="featured-content">
                    <span class="featured-label">PRODUK FAVORIT</span>
                    <h3>Salmon Portion</h3>
                    <p class="featured-description">
                        Potongan salmon premium yang presisi, higienis,
                        konsisten, dan praktis untuk sajian berkelas.
                    </p>
                </div>
            </div>
        </div>
    </section>

    <!-- PRODUCTS -->
    <section class="section products" id="produk">
        <div class="container">
            <div class="section-header">
                <div>
                    <div class="section-label">Katalog Produk</div>
                    <h2 class="section-title">Koleksi Produk Seafood & Ikan Premium Kami</h2>
                </div>

                <p class="section-description">
                    Produk frozen premium yang praktis untuk kebutuhan HORECA,
                    katering, usaha kuliner, dan rumah tangga.
                </p>
            </div>

            <div class="product-grid">

                <article class="product-card">
                    <div class="product-image">
                        <img
                            src="GAMBAR_PRODUK_1"
                            alt="Salmon Portion"
                        >
                        <span class="badge">FAVORIT</span>
                    </div>

                    <div class="product-content">
                        <span class="product-category">Salmon Premium</span>
                        <h3>Salmon Portion</h3>
                        <p>
                            <strong>Potongan Presisi untuk Sajian Berkelas.</strong><br>
                            Salmon premium yang dipotong presisi dan higienis,
                            menghasilkan porsi konsisten. Kaya Omega-3 dengan tekstur
                            juicy dan warna oranye alami yang segar.
                        </p>
                    </div>
                </article>

                <article class="product-card">
                    <div class="product-image">
                        <img
                            src="GAMBAR_PRODUK_2"
                            alt="Salmon Lempeng Slab"
                        >
                        <span class="badge">EKONOMIS</span>
                    </div>

                    <div class="product-content">
                        <span class="product-category">Salmon Premium</span>
                        <h3>Salmon Lempeng (Slab)</h3>
                        <p>
                            <strong>Fleksibilitas Tanpa Batas untuk Dapur Anda.</strong><br>
                            Pilihan ekonomis dan serbaguna dalam potongan utuh
                            memanjang, bebas dipotong menjadi dadu, irisan, atau steak.
                        </p>
                    </div>
                </article>

                <article class="product-card">
                    <div class="product-image">
                        <img
                            src="GAMBAR_PRODUK_3"
                            alt="Dori Fillet BL"
                        >
                        <span class="badge">PREMIUM</span>
                    </div>

                    <div class="product-content">
                        <span class="product-category">Fillet Ikan</span>
                        <h3>Dori Fillet BL (Blood Line)</h3>
                        <p>
                            <strong>Gurih Alami, Tekstur Lembut Sempurna.</strong><br>
                            Blood line memberi cita rasa lebih gurih dan kuat.
                            Dagingnya tebal, tidak mudah hancur, dan cocok untuk olahan berbumbu.
                        </p>
                    </div>
                </article>

                <article class="product-card">
                    <div class="product-image">
                        <img
                            src="GAMBAR_PRODUK_4"
                            alt="Dori Fillet NBL"
                        >
                        <span class="badge">SEGAR</span>
                    </div>

                    <div class="product-content">
                        <span class="product-category">Fillet Ikan</span>
                        <h3>Dori Fillet NBL (Non-Blood Line)</h3>
                        <p>
                            <strong>Kualitas Premium dengan Presentasi Putih Bersih.</strong><br>
                            Blood line dibersihkan sepenuhnya, menyisakan fillet putih
                            bersih dengan rasa lebih netral untuk hidangan elegan.
                        </p>
                    </div>
                </article>

                <article class="product-card">
                    <div class="product-image">
                        <img
                            src="GAMBAR_PRODUK_5"
                            alt="Nila Fillet"
                        >
                        <span class="badge">PREMIUM</span>
                    </div>

                    <div class="product-content">
                        <span class="product-category">Fillet Ikan</span>
                        <h3>Nila Fillet</h3>
                        <p>
                            <strong>Protein Tinggi yang Ramah di Lidah.</strong><br>
                            Daging padat, manis alami, bebas bau tanah, tinggi protein,
                            rendah lemak, dan mudah menyerap bumbu Nusantara maupun Western.
                        </p>
                    </div>
                </article>

                <article class="product-card">
                    <div class="product-image">
                        <img
                            src="GAMBAR_PRODUK_6"
                            alt="Gurami Fillet"
                        >
                        <span class="badge">PRAKTIS</span>
                    </div>

                    <div class="product-content">
                        <span class="product-category">Fillet Ikan</span>
                        <h3>Gurami Fillet</h3>
                        <p>
                            <strong>Cita Rasa Lokal dalam Format Modern.</strong><br>
                            Gurami hadir dalam bentuk fillet praktis tanpa repot
                            menyisihkan duri halus, dengan daging empuk dan gurih.
                        </p>
                    </div>
                </article>

                <article class="product-card">
                    <div class="product-image">
                        <img
                            src="GAMBAR_PRODUK_7"
                            alt="Lele Fillet"
                        >
                        <span class="badge">SEGAR</span>
                    </div>

                    <div class="product-content">
                        <span class="product-category">Fillet Ikan</span>
                        <h3>Lele Fillet</h3>
                        <p>
                            <strong>Inovasi Olahan Ikan Lele Tanpa Repot.</strong><br>
                            Daging bersih tanpa tulang dan patil, bertekstur lembut,
                            bernutrisi tinggi, praktis, dan tampil lebih bersih.
                        </p>
                    </div>
                </article>

                <article class="product-card">
                    <div class="product-image">
                        <img
                            src="GAMBAR_PRODUK_8"
                            alt="Udang Kupas"
                        >
                        <span class="badge">SIAP MASAK</span>
                    </div>

                    <div class="product-content">
                        <span class="product-category">Udang</span>
                        <h3>Udang Kupas</h3>
                        <p>
                            <strong>Segar, Kenyal, dan Siap Masak.</strong><br>
                            Udang segar berkualitas yang langsung dikupas dan dibekukan.
                            Teksturnya tetap renyah, manis, dan mempercepat proses memasak.
                        </p>
                    </div>
                </article>

                <!-- PRODUK 9: ubah nama, kategori, badge, dan keterangannya -->
                <article class="product-card">
                    <div class="product-image">
                        <img
                            src="GAMBAR_PRODUK_9"
                            alt="Cumi Ring"
                        >
                        <span class="badge">SEGAR</span>
                    </div>

                    <div class="product-content">
                        <span class="product-category">Cumi</span>
                        <h3>Cumi Ring</h3>
                        <p>
                            <strong>Potongan Calamari Sempurna Setiap Saat.</strong><br>
                            Dipotong melingkar dengan ketebalan pas, dibersihkan
                            secara saksama, dan bertekstur kenyal bila dimasak tepat.
                        </p>
                    </div>
                </article>

                <!-- PRODUK 10: ubah nama, kategori, badge, dan keterangannya -->
                <article class="product-card">
                    <div class="product-image">
                        <img
                            src="GAMBAR_PRODUK_10"
                            alt="Cumi Flower"
                        >
                        <span class="badge">PREMIUM</span>
                    </div>

                    <div class="product-content">
                        <span class="product-category">Cumi</span>
                        <h3>Cumi Flower</h3>
                        <p>
                            <strong>Cantik Mekar, Bumbu Meresap Sempurna.</strong><br>
                            Disayat silang secara profesional agar mekar saat dimasak.
                            Bentuknya cantik sekaligus membantu saus meresap maksimal.
                        </p>
                    </div>
                </article>

            </div>

            <p class="availability-note">
                *Jenis, ukuran, dan ketersediaan produk dapat berubah mengikuti
                hasil tangkapan serta kondisi stok terbaru.
            </p>
        </div>
    </section>

    <!-- ABOUT -->
    <section class="section about" id="tentang">
        <div class="container about-grid">
            <div>
                <div class="section-label">Tentang PT Nuha Berkah Abadi</div>

                <h2 class="section-title">
                    Distributor Terpercaya Seafood & Fillet Frozen Premium
                </h2>

                <p class="about-text">
                    PT Nuha Berkah Abadi adalah perusahaan distributor yang
                    berdedikasi menyediakan seafood dan ikan fillet frozen
                    berkualitas premium. Kami hadir sebagai solusi pasokan protein
                    perairan yang praktis, segar, dan berstandar tinggi untuk
                    HORECA, katering, usaha kuliner, dan dapur rumahan.
                    <br><br>
                    <strong>Komitmen pada Kualitas & Keamanan Pangan</strong><br>
                    Seluruh produk diproses, disimpan, dan didistribusikan dengan
                    sistem rantai dingin yang ketat. Suhu stabil membantu mengunci
                    nutrisi, mempertahankan tekstur, serta menjaga produk tetap
                    aman dan higienis hingga diterima pelanggan.
                </p>

                <div class="about-list">
                    <div class="about-item">
                        <span class="check">✓</span>
                        Suhu produk stabil
                    </div>

                    <div class="about-item">
                        <span class="check">✓</span>
                        Nutrisi dan tekstur terjaga
                    </div>

                    <div class="about-item">
                        <span class="check">✓</span>
                        Aman dan higienis
                    </div>

                    <div class="about-item">
                        <span class="check">✓</span>
                        Pasokan untuk bisnis & keluarga
                    </div>
                </div>
            </div>

            <img
                class="about-image"
                src="https://images.unsplash.com/photo-1535400255456-984241443b1f?auto=format&fit=crop&w=1200&q=85"
                alt="Seafood berkualitas"
            >
        </div>
    </section>

    <!-- FEATURES -->
    <section class="section features" id="keunggulan">
        <div class="container">
            <div class="section-header">
                <div>
                    <div class="section-label">Keunggulan Kami</div>
                    <h2 class="section-title">Mengapa Memilih PT Nuha Berkah Abadi?</h2>
                </div>

                <p class="section-description">
                    Kualitas, keamanan pangan, kepraktisan, dan fleksibilitas
                    pasokan menjadi dasar pelayanan kami.
                </p>
            </div>

            <div class="feature-grid">
                <div class="feature-card">
                    <div class="feature-icon">✓</div>
                    <h3>Kualitas Premium</h3>
                    <p>
                        Menyediakan pilihan seafood dan fillet ikan unggulan
                        yang diseleksi secara ketat.
                    </p>
                </div>

                <div class="feature-card">
                    <div class="feature-icon">❄️</div>
                    <h3>Sistem Rantai Dingin</h3>
                    <p>
                        Menjaga produk tetap aman, higienis, dan tidak turun mutu
                        selama penyimpanan hingga distribusi.
                    </p>
                </div>

                <div class="feature-card">
                    <div class="feature-icon">🍽️</div>
                    <h3>Praktis & Efisien</h3>
                    <p>
                        Produk siap olah yang menghemat waktu persiapan di dapur
                        komersial maupun rumah tangga.
                    </p>
                </div>

                <div class="feature-card">
                    <div class="feature-icon">📦</div>
                    <h3>Kapasitas Pasokan Fleksibel</h3>
                    <p>
                        Siap memenuhi partai besar untuk bisnis dan katering
                        maupun skala kecil untuk kebutuhan keluarga.
                    </p>
                </div>
            </div>
        </div>
    </section>

    <!-- ORDER FORM -->
    <section class="section order" id="kontak">
        <div class="container">
            <div class="order-box">
                <div class="order-info">
                    <div class="section-label" style="color:#62e3ff;">
                        Hubungi Kami
                    </div>

                    <h2>Ingin mengetahui produk yang tersedia?</h2>

                    <p>
                        Isi formulir singkat di sebelah kanan untuk menanyakan
                        informasi dan ketersediaan produk melalui WhatsApp.
                    </p>

                    <div class="contact">
                        <div class="contact-label">WhatsApp</div>
                        <a
                            href="https://wa.me/6282220404770"
                            target="_blank"
                        >
                            0822-2040-4770
                        </a>
                    </div>

                    <div class="contact">
                        <div class="contact-label">Email</div>
                        <a
                            href="mailto:nuhaberkahabadi@gmail.com"
                        >
                            nuhaberkahabadi@gmail.com
                        </a>
                    </div>
                </div>

                <div class="order-form">
                    <div class="form-title">Form Pertanyaan Produk</div>

                    <form id="orderForm" onsubmit="return false;">
                        <div class="field">
                            <label for="nama">Nama</label>
                            <input
                                type="text"
                                id="nama"
                                name="nama"
                                placeholder="Masukkan nama Anda"
                                autocomplete="name"
                            >
                        </div>

                        <div class="field">
                            <label for="produkPilihan">Produk</label>
                            <select id="produkPilihan" name="produk">
                                <option value="">Pilih produk</option>
                                <option value="Salmon Portion">Salmon Portion</option>
                                <option value="Salmon Lempeng (Slab)">Salmon Lempeng (Slab)</option>
                                <option value="Dori Fillet BL">Dori Fillet BL</option>
                                <option value="Dori Fillet NBL">Dori Fillet NBL</option>
                                <option value="Nila Fillet">Nila Fillet</option>
                                <option value="Gurami Fillet">Gurami Fillet</option>
                                <option value="Lele Fillet">Lele Fillet</option>
                                <option value="Udang Kupas">Udang Kupas</option>
                                <option value="Cumi Ring">Cumi Ring</option>
                                <option value="Cumi Flower">Cumi Flower</option>
                            </select>
                        </div>

                        <div class="field">
                            <label for="jumlah">Kebutuhan (opsional)</label>
                            <input
                                type="text"
                                id="jumlah"
                                name="jumlah"
                                placeholder="Contoh: 5 kg"
                            >
                        </div>

                        <div class="field">
                            <label for="catatan">Catatan</label>
                            <textarea
                                id="catatan"
                                name="catatan"
                                placeholder="Contoh: ingin dibersihkan atau dikirim besok pagi"
                            ></textarea>
                        </div>

                        <button
                            type="button"
                            class="submit-button"
                            onclick="kirimKeWhatsApp()"
                        >
                            Kirim ke WhatsApp
                        </button>

                        <p class="form-note">
                            WhatsApp akan terbuka dengan pesan yang sudah terisi.
                            Pelanggan tinggal menekan tombol kirim.
                        </p>
                    </form>
                </div>
            </div>
        </div>
    </section>

    <!-- FOOTER -->
    <footer>
        <div class="container footer-content">
            <div>
                © 2026 <strong>PT Nuha Berkah Abadi</strong>.
                Seafood dan fillet frozen premium.
            </div>

            <div>
                Distributor seafood & fillet frozen premium
            </div>
        </div>
    </footer>

    <script>
        /*
        =====================================================
        NAVIGASI HALAMAN DI DALAM STREAMLIT
        =====================================================

        Tautan dengan awalan # ditangani secara langsung agar
        tetap dapat berpindah bagian walaupun website berada
        di dalam iframe Streamlit.
        */
        function menujuBagian(idTujuan) {
            const bagian = document.querySelector(idTujuan);

            if (!bagian) {
                return;
            }

            bagian.scrollIntoView({
                behavior: "smooth",
                block: "start"
            });
        }

        document.addEventListener("DOMContentLoaded", function () {
            const tautanNavigasi =
                document.querySelectorAll('a[href^="#"]');

            const tombolMenu =
                document.querySelector(".mobile-menu-toggle");

            const menuNavigasi =
                document.getElementById("menuNavigasi");

            function tutupMenuMobile() {
                if (!tombolMenu || !menuNavigasi) {
                    return;
                }

                menuNavigasi.classList.remove("open");
                tombolMenu.setAttribute("aria-expanded", "false");
                tombolMenu.setAttribute("aria-label", "Buka menu navigasi");
                tombolMenu.textContent = "☰";
            }

            if (tombolMenu && menuNavigasi) {
                tombolMenu.addEventListener("click", function () {
                    const menuTerbuka =
                        menuNavigasi.classList.toggle("open");

                    tombolMenu.setAttribute(
                        "aria-expanded",
                        menuTerbuka ? "true" : "false"
                    );

                    tombolMenu.setAttribute(
                        "aria-label",
                        menuTerbuka
                            ? "Tutup menu navigasi"
                            : "Buka menu navigasi"
                    );

                    tombolMenu.textContent = menuTerbuka ? "×" : "☰";
                });
            }

            tautanNavigasi.forEach(function (tautan) {
                tautan.addEventListener("click", function (event) {
                    const idTujuan = tautan.getAttribute("href");

                    if (!idTujuan || idTujuan === "#") {
                        return;
                    }

                    event.preventDefault();
                    menujuBagian(idTujuan);
                    tutupMenuMobile();

                    if (window.history && window.history.replaceState) {
                        try {
                            window.history.replaceState(null, "", idTujuan);
                        } catch (error) {
                            /* Iframe Streamlit dapat membatasi perubahan URL. */
                        }
                    }
                });
            });

            window.addEventListener("resize", function () {
                if (window.innerWidth > 760) {
                    tutupMenuMobile();
                }
            });
        });

        /*
        =====================================================
        KONFIGURASI NOMOR WHATSAPP
        =====================================================

        Nomor 0822-2040-4770 ditulis menjadi 6282220404770.
        Jangan menggunakan tanda +, spasi, atau tanda strip.
        */
        const nomorWhatsApp = "6282220404770";

        /*
        =====================================================
        MENGIRIM FORM KE WHATSAPP
        =====================================================
        */
        function kirimKeWhatsApp() {
            const inputNama =
                document.getElementById("nama");

            const inputProduk =
                document.getElementById("produkPilihan");

            const inputJumlah =
                document.getElementById("jumlah");

            const inputCatatan =
                document.getElementById("catatan");

            const nama = inputNama.value.trim();
            const produk = inputProduk.value;
            const jumlah = inputJumlah.value.trim();
            const catatan = inputCatatan.value.trim();

            if (nama === "") {
                alert("Silakan masukkan nama Anda.");
                inputNama.focus();
                return;
            }

            if (produk === "") {
                alert("Silakan pilih produk yang ingin ditanyakan.");
                inputProduk.focus();
                return;
            }

            const isiCatatan =
                catatan === "" ? "-" : catatan;

            const isiKebutuhan =
                jumlah === "" ? "Belum ditentukan" : jumlah;

            const pesan =
`Halo, saya ${nama}.

Saya ingin mendapatkan informasi mengenai produk: ${produk}

Kebutuhan: ${isiKebutuhan}

Catatan: ${isiCatatan}`;

            const pesanTerenkripsi =
                encodeURIComponent(pesan);

            const linkWhatsApp =
                "https://wa.me/" +
                nomorWhatsApp +
                "?text=" +
                pesanTerenkripsi;

            /*
            Dibuka di tab baru. Apabila browser memblokir tab baru,
            halaman akan langsung dialihkan ke WhatsApp.
            */
            const tabWhatsApp =
                window.open(linkWhatsApp, "_blank");

            if (!tabWhatsApp) {
                window.location.href = linkWhatsApp;
            }
        }
    </script>

</body>
</html>
'''

# Hubungkan setiap penanda foto di HTML dengan file di dalam folder images.
# Jika nama foto Anda berbeda, cukup ubah bagian kanan saja.
daftar_gambar = {
    "GAMBAR_PRODUK_1": "salmon-portion.jpg",
    "GAMBAR_PRODUK_2": "salmon-lempeng.jpg",
    "GAMBAR_PRODUK_3": "dori-fillet-bl.jpg",
    "GAMBAR_PRODUK_4": "dori-fillet-nbl.jpg",
    "GAMBAR_PRODUK_5": "nila-fillet.jpg",
    "GAMBAR_PRODUK_6": "gurami-fillet.jpg",
    "GAMBAR_PRODUK_7": "lele-fillet.jpg",
    "GAMBAR_PRODUK_8": "udang-kupas.jpg",
    "GAMBAR_PRODUK_9": "cumi-ring.jpg",
    "GAMBAR_PRODUK_10": "cumi-flower.jpg",
}

for penanda in sorted(daftar_gambar, key=len, reverse=True):
    nama_file = daftar_gambar[penanda]
    html_code = html_code.replace(penanda, baca_gambar(nama_file))

components.html(
    html_code,
    height=900,
    scrolling=True,
)

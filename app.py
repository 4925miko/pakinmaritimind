import base64
import mimetypes
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="PT Nuha Berkah Abadi",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# Menyembunyikan tampilan bawaan Streamlit.
st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .stApp {background: #ffffff;}
        .block-container,
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


def normalisasi_nama(nama):
    """Abaikan perbedaan kapital, spasi, tanda hubung, dan ekstensi."""
    nama_tanpa_ekstensi = Path(nama).stem
    return "".join(
        karakter.lower()
        for karakter in nama_tanpa_ekstensi
        if karakter.isalnum()
    )


@st.cache_data(show_spinner=False)
def baca_gambar(nama_file, nama_cadangan=None):
    """Membaca gambar dari folder images dan mengubahnya menjadi data URL."""
    folder_gambar = Path(__file__).parent / "images"
    lokasi = folder_gambar / nama_file

    # Cari nama yang mirip jika nama persis tidak ditemukan.
    if not lokasi.exists() and folder_gambar.exists():
        nama_dicari = normalisasi_nama(nama_file)

        for file_gambar in folder_gambar.iterdir():
            if (
                file_gambar.is_file()
                and normalisasi_nama(file_gambar.name) == nama_dicari
            ):
                lokasi = file_gambar
                break

    # Gunakan gambar cadangan bila gambar utama belum ada.
    if not lokasi.exists() and nama_cadangan:
        lokasi_cadangan = folder_gambar / nama_cadangan

        if lokasi_cadangan.exists():
            lokasi = lokasi_cadangan

    # Placeholder apabila gambar tidak ditemukan.
    if not lokasi.exists():
        svg = f"""
        <svg xmlns="http://www.w3.org/2000/svg" width="900" height="600">
            <rect width="100%" height="100%" fill="#eefaff"/>
            <text x="50%" y="48%" text-anchor="middle"
                  fill="#2396c4" font-family="Arial"
                  font-size="34" font-weight="bold">
                Foto belum tersedia
            </text>
            <text x="50%" y="57%" text-anchor="middle"
                  fill="#698b9b" font-family="Arial" font-size="22">
                {nama_file}
            </text>
        </svg>
        """
        data = base64.b64encode(svg.encode("utf-8")).decode("utf-8")
        return f"data:image/svg+xml;base64,{data}"

    ekstensi = lokasi.suffix.lower()

    if ekstensi in (".jpg", ".jpeg"):
        tipe = "image/jpeg"
    elif ekstensi == ".png":
        tipe = "image/png"
    elif ekstensi == ".webp":
        tipe = "image/webp"
    elif ekstensi == ".gif":
        tipe = "image/gif"
    else:
        tipe = mimetypes.guess_type(lokasi)[0] or "application/octet-stream"

    data = base64.b64encode(lokasi.read_bytes()).decode("utf-8")
    return f"data:{tipe};base64,{data}"


# Seluruh tampilan website ditulis langsung di dalam app.py.
# Anda dapat mengubah teks, warna, alamat, dan bagian lain langsung di bawah ini.
html_code = r"""<!DOCTYPE html>
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
            width: 58px;
            height: 58px;
            flex-shrink: 0;
            display: block;
            object-fit: contain;
            border-radius: 50%;
            background: white;
            box-shadow: 0 8px 20px rgba(9, 74, 103, 0.2);
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

        .contact-address {
            margin: 0;
            color: white !important;
            font-size: 13px !important;
            font-weight: 600;
            line-height: 1.65 !important;
        }

        .contact-map {
            width: 100%;
            height: 180px;
            margin-top: 12px;
            display: block;
            border: 0;
            border-radius: 14px;
            background: rgba(255, 255, 255, 0.15);
        }

        .map-link {
            margin-top: 10px;
            display: inline-flex;
            align-items: center;
            gap: 7px;
            padding: 9px 13px;
            border: 1px solid rgba(255, 255, 255, 0.36);
            border-radius: 10px;
            background: rgba(255, 255, 255, 0.13);
            font-size: 12px !important;
            transition: background 0.2s ease, transform 0.2s ease;
        }

        .map-link:hover {
            background: rgba(255, 255, 255, 0.22);
            transform: translateY(-1px);
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
                width: 43px;
                height: 43px;
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
                <img
                    class="brand-icon"
                    src="data:image/webp;base64,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"
                    alt="Logo PT Nuha Berkah Abadi"
                >
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
                    src="images/salmon-portion.jpg"
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
                            src="images/salmon-portion.jpg"
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
                            src="images/salmon-lempeng.jpg"
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
                            src="images/dori-fillet-bl.jpg"
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
                            src="images/dori-fillet-nbl.jpg"
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
                            src="images/nila-fillet.jpg"
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
                            src="images/gurami-fillet.jpg"
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
                            src="images/lele-fillet.jpg"
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
                            src="images/udang-kupas.jpg"
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
                            src="images/cumi-ring.jpg"
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
                            src="images/cumi-flower.jpg"
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
                src="images/tentang-perusahaan.jpg"
                alt="Seafood dan fillet frozen PT Nuha Berkah Abadi"
                loading="lazy"
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

                    <div class="contact">
                        <div class="contact-label">Alamat</div>
                        <p class="contact-address">
                            Jl. Bantul No. KM 4, Kweni, Panggungharjo,
                            Kec. Sewon, Kota Yogyakarta, Daerah Istimewa
                            Yogyakarta 55188
                        </p>

                        <iframe
                            class="contact-map"
                            src="https://www.google.com/maps?q=-7.8332465,110.3532744&amp;z=17&amp;output=embed"
                            title="Lokasi PT Nuha Berkah Abadi"
                            loading="lazy"
                            allowfullscreen
                            referrerpolicy="no-referrer-when-downgrade"
                        ></iframe>

                        <a
                            class="map-link"
                            href="https://www.google.com/maps/search/?api=1&amp;query=-7.8332465,110.3532744"
                            target="_blank"
                            rel="noopener noreferrer"
                        >
                            📍 Buka di Google Maps
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
"""


# Hubungkan gambar dalam HTML dengan file produk di folder images.
daftar_gambar = {
    "images/salmon-portion.jpg": ("salmon-portion.jpg", None),
    "images/salmon-lempeng.jpg": ("salmon-lempeng.jpg", None),
    "images/dori-fillet-bl.jpg": ("dori-fillet-bl.jpg", None),
    "images/dori-fillet-nbl.jpg": ("dori-fillet-nbl.jpg", None),
    "images/nila-fillet.jpg": ("nila-fillet.jpg", None),
    "images/gurami-fillet.jpg": ("gurami-fillet.jpg", None),
    "images/lele-fillet.jpg": ("lele-fillet.jpg", None),
    "images/udang-kupas.jpg": ("udang-kupas.jpg", None),
    "images/cumi-ring.jpg": ("cumi-ring.jpg", None),
    "images/cumi-flower.jpg": ("cumi-flower.jpg", None),

    # Jika foto khusus Tentang Kami belum ada, gunakan Cumi Flower.
    "images/tentang-perusahaan.jpg": (
        "tentang-perusahaan.jpg",
        "cumi-flower.jpg",
    ),
}


for alamat_html in sorted(daftar_gambar, key=len, reverse=True):
    nama_file, nama_cadangan = daftar_gambar[alamat_html]

    html_code = html_code.replace(
        alamat_html,
        baca_gambar(nama_file, nama_cadangan),
    )


components.html(
    html_code,
    height=900,
    scrolling=True,
)

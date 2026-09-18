import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="PakinMaritimInd",
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

# Seluruh tampilan website HTML ditanam langsung di dalam aplikasi Streamlit.
html_code = r'''<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>PakinMaritimInd | Seafood Berkualitas</title>

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap" rel="stylesheet">

    <style>
        :root {
            --navy: #062436;
            --dark: #031923;
            --blue: #087fbd;
            --cyan: #20bce1;
            --light-blue: #eaf8ff;
            --white: #ffffff;
            --text: #102a43;
            --muted: #667f91;
            --border: #dcecf5;
        }

        * {
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            margin: 0;
            font-family: "Inter", sans-serif;
            color: var(--text);
            background: #f6fbff;
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
            background: rgba(3, 25, 35, 0.88);
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
                    rgba(2, 20, 31, 0.96) 0%,
                    rgba(4, 43, 61, 0.82) 52%,
                    rgba(4, 43, 61, 0.35) 100%
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
            background: linear-gradient(transparent, var(--dark));
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
                #f6fbff;
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
            background: linear-gradient(120deg, #05283a, #073a50 55%, #075d7e);
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
            background: #eef9ff;
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
            background: linear-gradient(150deg, #06344b, #087cac);
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
            .container {
                width: calc(100% - 28px);
            }

            .nav-content {
                min-height: 67px;
                gap: 10px;
            }

            .nav-links {
                display: flex;
                gap: 0;
            }

            .nav-links a:not(.nav-button) {
                display: none;
            }

            .nav-button {
                padding: 9px 13px;
                font-size: 12px !important;
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
                <span class="brand-icon">🌊</span>
                PAKINMARITIMIND
            </a>

            <nav class="nav-links">
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
                    Seafood pilihan berkualitas
                </div>

                <h1>
                    Seafood segar untuk
                    <span>setiap kebutuhan.</span>
                </h1>

                <p class="hero-description">
                    PakinMaritimInd menyediakan pilihan seafood untuk kebutuhan
                    rumah tangga, restoran, katering, dan usaha kuliner. Informasi
                    produk disajikan dengan jelas, sedangkan ketersediaannya
                    menyesuaikan hasil tangkapan yang diperoleh.
                </p>

                <div class="hero-buttons">
                    <a href="#produk" class="button button-primary">
                        Lihat Produk
                    </a>

                    <a
                        href="https://wa.me/6285872869460?text=Halo%20PakinMaritimInd,%20saya%20ingin%20menanyakan%20produk%20seafood."
                        target="_blank"
                        class="button button-white"
                    >
                        Tanya via WhatsApp
                    </a>
                </div>

                <div class="stats">
                    <div class="stat">
                        <strong>8+</strong>
                        <span>Pilihan produk seafood</span>
                    </div>

                    <div class="stat">
                        <strong>Segar</strong>
                        <span>Fokus pada kualitas produk</span>
                    </div>

                    <div class="stat">
                        <strong>Cepat</strong>
                        <span>Informasi melalui WhatsApp</span>
                    </div>
                </div>
            </div>

            <div class="featured-card">
                <img
                    src="https://images.unsplash.com/photo-1565680018093-ebb6a9e8c6e0?auto=format&fit=crop&w=1000&q=85"
                    alt="Udang Vaname"
                >

                <div class="featured-content">
                    <span class="featured-label">PRODUK FAVORIT</span>
                    <h3>Udang Vaname</h3>
                    <p class="featured-description">
                        Udang pilihan dengan tekstur padat dan rasa gurih,
                        cocok untuk beragam hidangan seafood.
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
                    <h2 class="section-title">Pilihan seafood untuk pelanggan.</h2>
                </div>

                <p class="section-description">
                    Setiap produk ditampilkan melalui foto, nama, dan deskripsi
                    singkat agar pengunjung mudah mengenal produk kami.
                </p>
            </div>

            <div class="product-grid">

                <article class="product-card">
                    <div class="product-image">
                        <img
                            src="https://images.unsplash.com/photo-1565680018093-ebb6a9e8c6e0?auto=format&fit=crop&w=900&q=85"
                            alt="Udang Vaname"
                        >
                        <span class="badge">FAVORIT</span>
                    </div>

                    <div class="product-content">
                        <span class="product-category">Udang</span>
                        <h3>Udang Vaname</h3>
                        <p>
                            Tekstur padat dan rasa gurih. Cocok untuk grill,
                            tumis, tempura, dan saus seafood.
                        </p>
                    </div>
                </article>

                <article class="product-card">
                    <div class="product-image">
                        <img
                            src="https://images.unsplash.com/photo-1544551763-46a013bb70d5?auto=format&fit=crop&w=900&q=85"
                            alt="Cumi Segar"
                        >
                        <span class="badge">FRESH</span>
                    </div>

                    <div class="product-content">
                        <span class="product-category">Cumi</span>
                        <h3>Cumi Segar</h3>
                        <p>
                            Daging kenyal dengan rasa gurih. Cocok untuk calamari,
                            bakar, tumis, dan saus tiram.
                        </p>
                    </div>
                </article>

                <article class="product-card">
                    <div class="product-image">
                        <img
                            src="https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?auto=format&fit=crop&w=900&q=85"
                            alt="Fillet Salmon"
                        >
                        <span class="badge">PREMIUM</span>
                    </div>

                    <div class="product-content">
                        <span class="product-category">Ikan</span>
                        <h3>Fillet Salmon</h3>
                        <p>
                            Tekstur lembut dan cita rasa khas. Cocok untuk grill,
                            steak, sushi, dan menu sehat.
                        </p>
                    </div>
                </article>

                <article class="product-card">
                    <div class="product-image">
                        <img
                            src="https://images.unsplash.com/photo-1534482421-64566f976cfa?auto=format&fit=crop&w=900&q=85"
                            alt="Kerang Hijau"
                        >
                        <span class="badge">SEGAR</span>
                    </div>

                    <div class="product-content">
                        <span class="product-category">Kerang</span>
                        <h3>Kerang Hijau</h3>
                        <p>
                            Rasa gurih dan tekstur lembut. Cocok untuk saus padang,
                            saus tiram, rebus, dan bakar.
                        </p>
                    </div>
                </article>

                <article class="product-card">
                    <div class="product-image">
                        <img
                            src="https://images.unsplash.com/photo-1559339352-11d035aa65de?auto=format&fit=crop&w=900&q=85"
                            alt="Kepiting Bakau"
                        >
                        <span class="badge">PREMIUM</span>
                    </div>

                    <div class="product-content">
                        <span class="product-category">Kepiting</span>
                        <h3>Kepiting Bakau</h3>
                        <p>
                            Daging lezat dengan cita rasa kuat. Cocok untuk menu
                            restoran dan olahan saus seafood.
                        </p>
                    </div>
                </article>

                <article class="product-card">
                    <div class="product-image">
                        <img
                            src="https://images.unsplash.com/photo-1559737558-2f5a35f4523b?auto=format&fit=crop&w=900&q=85"
                            alt="Fillet Dori"
                        >
                        <span class="badge">PRAKTIS</span>
                    </div>

                    <div class="product-content">
                        <span class="product-category">Fillet Ikan</span>
                        <h3>Fillet Dori</h3>
                        <p>
                            Fillet siap olah untuk fish and chips, goreng tepung,
                            steak ikan, dan menu keluarga.
                        </p>
                    </div>
                </article>

                <article class="product-card">
                    <div class="product-image">
                        <img
                            src="https://images.unsplash.com/photo-1588168333986-5078d3ae3976?auto=format&fit=crop&w=900&q=85"
                            alt="Tiram Segar"
                        >
                        <span class="badge">SEGAR</span>
                    </div>

                    <div class="product-content">
                        <span class="product-category">Tiram</span>
                        <h3>Tiram Segar</h3>
                        <p>
                            Pilihan untuk panggang, butter sauce, dan berbagai
                            sajian seafood premium.
                        </p>
                    </div>
                </article>

                <article class="product-card">
                    <div class="product-image">
                        <img
                            src="https://images.unsplash.com/photo-1566847438217-76e82d383f84?auto=format&fit=crop&w=900&q=85"
                            alt="Seafood Mix"
                        >
                        <span class="badge">PAKET</span>
                    </div>

                    <div class="product-content">
                        <span class="product-category">Mix Seafood</span>
                        <h3>Seafood Mix</h3>
                        <p>
                            Kombinasi seafood pilihan untuk steamboat, hotpot,
                            grill, dan menu keluarga.
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
                <div class="section-label">Tentang PakinMaritimInd</div>

                <h2 class="section-title">
                    Lebih mudah memilih seafood sesuai kebutuhan.
                </h2>

                <p class="about-text">
                    PakinMaritimInd menghadirkan bahan makanan laut dengan
                    informasi produk yang jelas agar pelanggan dapat memilih
                    dengan cepat dan nyaman. Produk cocok untuk kebutuhan
                    rumah tangga maupun pelanggan usaha kuliner.
                </p>

                <div class="about-list">
                    <div class="about-item">
                        <span class="check">✓</span>
                        Informasi produk jelas
                    </div>

                    <div class="about-item">
                        <span class="check">✓</span>
                        Deskripsi produk mudah dipahami
                    </div>

                    <div class="about-item">
                        <span class="check">✓</span>
                        Informasi mudah ditanyakan
                    </div>

                    <div class="about-item">
                        <span class="check">✓</span>
                        Cocok untuk usaha kuliner
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
                    <div class="section-label">Kenapa Memilih Kami</div>
                    <h2 class="section-title">Pelayanan mudah dan terpercaya.</h2>
                </div>

                <p class="section-description">
                    Kami memberikan informasi produk dan jalur komunikasi
                    yang mudah untuk membantu kebutuhan pelanggan.
                </p>
            </div>

            <div class="feature-grid">
                <div class="feature-card">
                    <div class="feature-icon">🐟</div>
                    <h3>Pilihan Produk</h3>
                    <p>
                        Beragam kategori seafood untuk menyesuaikan kebutuhan
                        rumah tangga dan usaha.
                    </p>
                </div>

                <div class="feature-card">
                    <div class="feature-icon">🌊</div>
                    <h3>Hasil Tangkapan</h3>
                    <p>
                        Ketersediaan produk diinformasikan sesuai hasil tangkapan
                        dan kondisi stok terbaru.
                    </p>
                </div>

                <div class="feature-card">
                    <div class="feature-icon">✓</div>
                    <h3>Fokus Kualitas</h3>
                    <p>
                        Kualitas dan penanganan produk menjadi bagian penting
                        dalam pelayanan.
                    </p>
                </div>

                <div class="feature-card">
                    <div class="feature-icon">💬</div>
                    <h3>Mudah Dihubungi</h3>
                    <p>
                        Pelanggan dapat menanyakan jenis, ukuran, ketersediaan,
                        dan informasi produk melalui WhatsApp.
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
                            href="https://wa.me/6285872869460"
                            target="_blank"
                        >
                            +62 858-7286-9460
                        </a>
                    </div>

                    <div class="contact">
                        <div class="contact-label">Instagram</div>
                        <a
                            href="https://instagram.com/pakinmaritimind"
                            target="_blank"
                        >
                            @pakinmaritimind
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
                                <option value="Udang Vaname">Udang Vaname</option>
                                <option value="Cumi Segar">Cumi Segar</option>
                                <option value="Fillet Salmon">Fillet Salmon</option>
                                <option value="Kerang Hijau">Kerang Hijau</option>
                                <option value="Kepiting Bakau">Kepiting Bakau</option>
                                <option value="Fillet Dori">Fillet Dori</option>
                                <option value="Tiram Segar">Tiram Segar</option>
                                <option value="Seafood Mix">Seafood Mix</option>
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
                © 2026 <strong>PakinMaritimInd</strong>.
                Seafood dan bahan makanan laut.
            </div>

            <div>
                            Website promosi dan informasi produk
            </div>
        </div>
    </footer>

    <script>
        /*
        =====================================================
        KONFIGURASI NOMOR WHATSAPP
        =====================================================

        Nomor 0858-7286-9460 ditulis menjadi 6285872869460.
        Jangan menggunakan tanda +, spasi, atau tanda strip.
        */
        const nomorWhatsApp = "6285872869460";

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

components.html(
    html_code,
    height=900,
    scrolling=True,
)


import json
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer


HTML = r"""<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>EUCLID LAB | Motion Geometry Studio</title>

<style>
:root {
    --bg: #090a0f;
    --panel: #12141c;
    --panel2: #191d28;
    --border: rgba(255,255,255,.09);
    --coral: #ff7a59;
    --orange: #ff9f43;
    --cyan: #00e5ff;
    --gold: #ffd166;
    --purple: #b388ff;
    --green: #38d996;
    --text: #f8fafc;
    --muted: #94a3b8;
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    min-height: 100vh;
    color: var(--text);
    background:
        radial-gradient(circle at 15% 10%, #27202a 0, transparent 35%),
        radial-gradient(circle at 90% 70%, #10242b 0, transparent 35%),
        var(--bg);
    font-family: "Segoe UI", Arial, sans-serif;
}

button, input {
    font: inherit;
}

button {
    cursor: pointer;
}

header {
    position: sticky;
    top: 0;
    z-index: 20;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    padding: 17px 5%;
    border-bottom: 1px solid var(--border);
    background: rgba(9,10,15,.92);
    backdrop-filter: blur(14px);
}

.brand {
    display: flex;
    align-items: center;
    gap: 12px;
}

.logo {
    width: 43px;
    height: 43px;
    display: grid;
    place-items: center;
    border-radius: 14px;
    background: linear-gradient(135deg, var(--coral), var(--orange));
    color: #111;
    font-weight: 1000;
    font-size: 21px;
}

.brand-name {
    font-size: 18px;
    font-weight: 900;
    letter-spacing: 2px;
}

.brand-sub {
    margin-top: 3px;
    color: var(--muted);
    font-size: 10px;
    letter-spacing: 2px;
}

.status {
    display: flex;
    align-items: center;
    gap: 8px;
    color: var(--muted);
    font-size: 12px;
}

.status-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: var(--green);
    box-shadow: 0 0 12px var(--green);
}

.container {
    width: min(1320px, 92%);
    margin: 0 auto;
    padding: 30px 0 50px;
}

.hero {
    display: flex;
    align-items: end;
    justify-content: space-between;
    gap: 20px;
    flex-wrap: wrap;
    margin-bottom: 24px;
}

.eyebrow {
    color: var(--coral);
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 2.5px;
    margin-bottom: 12px;
}

h1 {
    font-size: clamp(28px, 4vw, 44px);
    line-height: 1.12;
    letter-spacing: -1px;
}

h1 span {
    color: var(--coral);
}

.hero p {
    color: var(--muted);
    margin-top: 12px;
    line-height: 1.7;
    max-width: 650px;
}

.tag {
    border: 1px solid var(--border);
    background: var(--panel);
    padding: 10px 15px;
    border-radius: 30px;
    color: var(--muted);
    font-size: 12px;
}

.layout {
    display: grid;
    grid-template-columns: minmax(0, 1.35fr) minmax(310px, .8fr);
    gap: 20px;
}

.panel {
    border: 1px solid var(--border);
    border-radius: 22px;
    background: rgba(18,20,28,.92);
    overflow: hidden;
    box-shadow: 0 20px 70px rgba(0,0,0,.15);
}

.panel-head {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    padding: 18px 20px;
    border-bottom: 1px solid var(--border);
}

.panel-title {
    font-size: 13px;
    font-weight: 800;
    letter-spacing: 1px;
}

.panel-kicker {
    color: var(--muted);
    font-size: 11px;
}

.visual-stage {
    min-height: 370px;
    position: relative;
    display: grid;
    place-items: center;
    padding: 18px;
    background-image: radial-gradient(#343947 1px, transparent 1px);
    background-size: 22px 22px;
}

#geometry {
    width: 100%;
    max-width: 620px;
    height: auto;
    overflow: visible;
}

.shape {
    stroke: var(--coral);
    stroke-width: 4;
    stroke-linejoin: round;
    fill: rgba(255,122,89,.12);
    stroke-dasharray: 1200;
    stroke-dashoffset: 1200;
}

.shape.draw {
    animation: drawShape 1.2s ease forwards;
}

.shape.fill {
    animation: fillShape .8s ease forwards;
}

@keyframes drawShape {
    to { stroke-dashoffset: 0; }
}

@keyframes fillShape {
    from { fill: rgba(255,122,89,0); }
    to { fill: rgba(255,122,89,.2); }
}

.measure {
    stroke: var(--cyan);
    stroke-width: 2;
    stroke-dasharray: 6 5;
    opacity: 0;
}

.measure.show {
    animation: appear .45s ease forwards;
}

.label {
    fill: var(--cyan);
    font-size: 16px;
    font-weight: 800;
    opacity: 0;
}

.label.show {
    animation: appear .45s ease forwards;
}

@keyframes appear {
    to { opacity: 1; }
}

.area-highlight {
    fill: rgba(255,209,102,.3);
    opacity: 0;
}

.area-highlight.show {
    animation: appear .8s ease forwards;
}

.stage-caption {
    position: absolute;
    bottom: 15px;
    left: 18px;
    color: var(--muted);
    font-size: 11px;
    letter-spacing: 1px;
}

.step-row {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    gap: 8px;
    padding: 16px 18px 18px;
    border-top: 1px solid var(--border);
}

.step {
    text-align: center;
    padding: 11px 4px;
    border-radius: 11px;
    border: 1px solid var(--border);
    color: var(--muted);
    font-size: 10px;
    font-weight: 800;
    background: #0d0f15;
    transition: .25s;
}

.step.active {
    color: #fff;
    border-color: var(--coral);
    background: rgba(255,122,89,.13);
    box-shadow: 0 0 18px rgba(255,122,89,.1);
}

.step.done {
    color: var(--green);
    border-color: rgba(56,217,150,.35);
}

.lesson-body {
    padding: 22px;
}

.lesson-count {
    color: var(--coral);
    font-size: 11px;
    font-weight: 900;
    letter-spacing: 2px;
}

.lesson-title {
    margin-top: 9px;
    font-size: 25px;
    font-weight: 900;
}

.lesson-description {
    margin-top: 12px;
    min-height: 94px;
    color: #cbd5e1;
    font-size: 14px;
    line-height: 1.9;
}

.speech-line {
    padding: 14px;
    margin-top: 15px;
    border-radius: 13px;
    border: 1px solid rgba(0,229,255,.18);
    background: rgba(0,229,255,.045);
    min-height: 100px;
    line-height: 1.9;
    color: #b6c5d5;
    font-size: 14px;
}

.speech-line .word {
    display: inline;
    padding: 2px 1px;
    border-radius: 4px;
    transition: background .1s, color .1s;
}

.speech-line .word.active {
    background: var(--gold);
    color: #111827;
    box-shadow: 0 0 12px rgba(255,209,102,.2);
}

.speech-label {
    margin-top: 14px;
    color: var(--cyan);
    font-size: 10px;
    font-weight: 900;
    letter-spacing: 1.8px;
}

.controls {
    padding: 18px 22px 22px;
    border-top: 1px solid var(--border);
}

.control-buttons {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 8px;
}

.btn {
    border: 1px solid var(--border);
    background: var(--panel2);
    color: var(--text);
    padding: 12px 8px;
    border-radius: 11px;
    font-size: 12px;
    font-weight: 800;
    transition: .2s;
}

.btn:hover {
    border-color: var(--coral);
    transform: translateY(-1px);
}

.btn.primary {
    background: var(--coral);
    color: #111;
    border-color: var(--coral);
}

.btn:disabled {
    opacity: .4;
    cursor: not-allowed;
    transform: none;
}

.speed-row {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-top: 17px;
    color: var(--muted);
    font-size: 12px;
}

.speed-row input {
    flex: 1;
    accent-color: var(--coral);
}

.speed-value {
    color: var(--coral);
    font-weight: 900;
    min-width: 42px;
    text-align: right;
}

.formula-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
    margin-top: 20px;
}

.formula-card {
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 15px;
    background: #0d0f15;
}

.formula-label {
    color: var(--muted);
    font-size: 10px;
    font-weight: 900;
    letter-spacing: 1.5px;
}

.formula-value {
    color: var(--gold);
    font-size: 19px;
    font-weight: 900;
    margin-top: 9px;
    overflow-wrap: anywhere;
}

.formula-note {
    color: var(--muted);
    font-size: 11px;
    line-height: 1.6;
    margin-top: 6px;
}

.result-panel {
    padding: 18px 20px;
    margin-top: 16px;
    border: 1px solid rgba(56,217,150,.2);
    border-radius: 14px;
    background: rgba(56,217,150,.045);
}

.result-panel h3 {
    color: var(--green);
    font-size: 11px;
    letter-spacing: 1.7px;
}

.result-value {
    margin-top: 9px;
    font-size: 14px;
    line-height: 1.9;
    color: #dce7f1;
    overflow-wrap: anywhere;
}

.footer {
    text-align: center;
    padding: 28px 10px 0;
    color: #64748b;
    font-size: 11px;
    letter-spacing: 1px;
}

.toast {
    position: fixed;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%) translateY(30px);
    background: #202632;
    border: 1px solid var(--border);
    color: var(--text);
    padding: 12px 18px;
    border-radius: 12px;
    font-size: 12px;
    opacity: 0;
    pointer-events: none;
    transition: .25s;
    z-index: 100;
}

.toast.show {
    opacity: 1;
    transform: translateX(-50%) translateY(0);
}

@media (max-width: 900px) {
    .layout {
        grid-template-columns: 1fr;
    }
    .visual-stage {
        min-height: 300px;
    }
}

@media (max-width: 520px) {
    header {
        padding: 13px 4%;
    }
    .brand-sub {
        letter-spacing: 1px;
    }
    .container {
        width: 94%;
        padding-top: 22px;
    }
    .step-row {
        grid-template-columns: repeat(3, 1fr);
    }
    .control-buttons {
        grid-template-columns: repeat(2, 1fr);
    }
    .visual-stage {
        min-height: 260px;
    }
    .formula-grid {
        grid-template-columns: 1fr;
    }
}
</style>
</head>

<body>
<header>
    <div class="brand">
        <div class="logo">E</div>
        <div>
            <div class="brand-name">EUCLID LAB</div>
            <div class="brand-sub">INTERACTIVE GEOMETRY LEARNING</div>
        </div>
    </div>
    <div class="status">
        <span class="status-dot"></span>
        <span id="statusText">STUDIO SIAP</span>
    </div>
</header>

<main class="container">
    <section class="hero">
        <div>
            <div class="eyebrow">MOTION GEOMETRY STUDIO / 01</div>
            <h1>Belajar geometri dengan<br><span>melihat dan mendengar.</span></h1>
            <p>
                Ikuti bentuk, rumus, dan penjelasan secara bertahap.
                Narator akan membacakan materi sementara kata-kata
                yang diucapkan disorot pada layar.
            </p>
        </div>
        <div class="tag">● VISUAL LEARNING MODE</div>
    </section>

    <section class="layout">
        <div class="panel">
            <div class="panel-head">
                <div class="panel-title">VISUALISASI BANGUN</div>
                <div class="panel-kicker" id="shapeBadge">GEOMETRY / 2D</div>
            </div>

            <div class="visual-stage">
                <svg id="geometry" viewBox="0 0 600 390"
                     role="img" aria-label="Animasi bangun geometri">
                    <defs>
                        <linearGradient id="shapeGradient"
                                        x1="0" y1="0" x2="1" y2="1">
                            <stop offset="0%" stop-color="#ff7a59"
                                  stop-opacity=".35"/>
                            <stop offset="100%" stop-color="#ff9f43"
                                  stop-opacity=".04"/>
                        </linearGradient>
                        <filter id="glow">
                            <feGaussianBlur stdDeviation="5"
                                            result="blur"/>
                            <feMerge>
                                <feMergeNode in="blur"/>
                                <feMergeNode in="SourceGraphic"/>
                            </feMerge>
                        </filter>
                    </defs>
                    <g id="shapeGroup"></g>
                </svg>
                <div class="stage-caption" id="visualCaption">
                    MENUNGGU PEMBELAJARAN
                </div>
            </div>

            <div class="step-row" id="stepRow">
                <div class="step active">01<br>Kenali</div>
                <div class="step">02<br>Bentuk</div>
                <div class="step">03<br>Ukuran</div>
                <div class="step">04<br>Rumus</div>
                <div class="step">05<br>Hitung</div>
                <div class="step">06<br>Kesimpulan</div>
            </div>
        </div>

        <div class="panel">
            <div class="panel-head">
                <div class="panel-title">PANDUAN PEMBELAJARAN</div>
                <div class="panel-kicker" id="stepCounter">01 / 06</div>
            </div>

            <div class="lesson-body">
                <div class="lesson-count" id="lessonCount">TAHAP 01</div>
                <div class="lesson-title" id="lessonTitle">Mengenal bangun</div>
                <div class="lesson-description" id="lessonDescription">
                    Pembelajaran akan dimulai setelah tombol putar ditekan.
                </div>

                <div class="speech-label">NARASI LANGSUNG</div>
                <div class="speech-line" id="speechLine">
                    Teks narator akan muncul di sini.
                </div>

                <div class="formula-grid">
                    <div class="formula-card">
                        <div class="formula-label">RUMUS LUAS</div>
                        <div class="formula-value" id="areaFormula">—</div>
                        <div class="formula-note" id="areaNote">
                            Rumus luas bangun.
                        </div>
                    </div>
                    <div class="formula-card">
                        <div class="formula-label">RUMUS KELILING</div>
                        <div class="formula-value" id="perimeterFormula">—</div>
                        <div class="formula-note" id="perimeterNote">
                            Rumus keliling bangun.
                        </div>
                    </div>
                </div>

                <div class="result-panel">
                    <h3>HASIL PERHITUNGAN</h3>
                    <div class="result-value" id="resultValue">
                        Hasil akan ditampilkan di sini.
                    </div>
                </div>
            </div>

            <div class="controls">
                <div class="control-buttons">
                    <button class="btn primary" id="playBtn">▶ Putar</button>
                    <button class="btn" id="pauseBtn">Ⅱ Jeda</button>
                    <button class="btn" id="restartBtn">↻ Ulangi</button>
                    <button class="btn" id="stopBtn">■ Berhenti</button>
                </div>
                <div class="speed-row">
                    <label for="speed">Kecepatan suara</label>
                    <input id="speed" type="range"
                           min="0.65" max="1.25" step="0.05" value="0.9">
                    <span class="speed-value" id="speedValue">0.90×</span>
                </div>
            </div>
        </div>
    </section>

    <div class="footer">
        EUCLID LAB · INTERACTIVE MATHEMATICS · LEARN BY VISUALIZING
    </div>
</main>

<div class="toast" id="toast"></div>

<script>
"use strict";

const DATA = __DATA__;

const $ = id => document.getElementById(id);

const state = {
    stage: 0,
    running: false,
    paused: false,
    stopped: false,
    utterance: null,
    words: [],
    activeWord: -1,
    stageToken: 0,
    voices: [],
    speechSupported: "speechSynthesis" in window &&
                     "SpeechSynthesisUtterance" in window
};

const stageNames = [
    "Mengenal bangun",
    "Mengamati bentuk",
    "Mengenal ukuran",
    "Memahami rumus",
    "Menghitung hasil",
    "Kesimpulan"
];

const stageDescriptions = [
    "Kenali nama bangun dan perhatikan karakteristik dasarnya.",
    "Amati garis dan sisi yang membentuk bangun geometri.",
    "Perhatikan ukuran yang digunakan dalam perhitungan.",
    "Pahami hubungan antara ukuran dan rumus matematika.",
    "Masukkan nilai ukuran ke dalam rumus dan amati hasilnya.",
    "Simpulkan cara menghitung luas dan keliling bangun."
];

const shape = normalizeShape(DATA);
const measures = normalizeMeasures(DATA.ukuran || {});
const results = normalizeResults(DATA.hasil || {});

function normalizeText(value) {
    if (value === null || value === undefined) return "";
    if (typeof value === "number") {
        return Number.isInteger(value)
            ? String(value)
            : String(Number(value.toFixed(4)));
    }
    if (typeof value === "string") return value;
    return "";
}

function firstValue(obj, keys, fallback = null) {
    for (const key of keys) {
        if (obj && obj[key] !== undefined && obj[key] !== null) {
            return obj[key];
        }
    }
    return fallback;
}

function normalizeShape(data) {
    const raw = JSON.stringify(data).toLowerCase();

    if (raw.includes("jari_jari") ||
        raw.includes("jari-jari") ||
        raw.includes("lingkaran") ||
        raw.includes("radius")) {
        return "lingkaran";
    }

    if (raw.includes("panjang") || raw.includes("lebar")) {
        return "persegi_panjang";
    }

    if (raw.includes("alas") || raw.includes("tinggi") ||
        raw.includes("segitiga")) {
        return "segitiga";
    }

    if (raw.includes("sisi") || raw.includes("persegi")) {
        return "persegi";
    }

    return "persegi";
}

function normalizeMeasures(input) {
    const obj = input || {};

    return {
        sisi: Number(firstValue(obj, ["sisi", "s"], 0)) || 0,
        panjang: Number(firstValue(obj, ["panjang", "p"], 0)) || 0,
        lebar: Number(firstValue(obj, ["lebar", "l"], 0)) || 0,
        alas: Number(firstValue(obj, ["alas", "a"], 0)) || 0,
        tinggi: Number(firstValue(obj, ["tinggi", "t"], 0)) || 0,
        sisi1: Number(firstValue(obj, ["sisi1"], 0)) || 0,
        sisi2: Number(firstValue(obj, ["sisi2"], 0)) || 0,
        sisi3: Number(firstValue(obj, ["sisi3"], 0)) || 0,
        jari_jari: Number(
            firstValue(obj, ["jari_jari", "jari-jari", "radius", "r"], 0)
        ) || 0
    };
}

function normalizeResults(input) {
    const obj = input || {};

    if (typeof obj === "number" || typeof obj === "string") {
        return { raw: normalizeText(obj), luas: null, keliling: null };
    }

    return {
        raw: "",
        luas: firstValue(obj, ["luas", "area"], null),
        keliling: firstValue(obj, ["keliling", "perimeter"], null)
    };
}

function fmt(value) {
    if (value === null || value === undefined || value === "") return "—";
    const n = Number(value);
    if (!Number.isFinite(n)) return normalizeText(value);
    return n.toLocaleString("id-ID", {
        maximumFractionDigits: 4
    });
}

function getShapeTitle() {
    const names = {
        persegi: "Persegi",
        persegi_panjang: "Persegi Panjang",
        segitiga: "Segitiga",
        lingkaran: "Lingkaran"
    };
    return names[shape] || "Bangun Geometri";
}

function getFormulas() {
    if (shape === "persegi") {
        return {
            area: "L = s × s",
            perimeter: "K = 4 × s",
            areaNote: "Sisi dikalikan dengan sisi.",
            perimeterNote: "Empat sisi sama panjang."
        };
    }

    if (shape === "persegi_panjang") {
        return {
            area: "L = p × l",
            perimeter: "K = 2(p + l)",
            areaNote: "Panjang dikalikan lebar.",
            perimeterNote: "Dua kali jumlah panjang dan lebar."
        };
    }

    if (shape === "segitiga") {
        return {
            area: "L = ½ × a × t",
            perimeter: "K = a + b + c",
            areaNote: "Setengah alas dikalikan tinggi.",
            perimeterNote: "Jumlah ketiga sisi segitiga."
        };
    }

    return {
        area: "L = π × r²",
        perimeter: "K = 2 × π × r",
        areaNote: "Pi dikalikan kuadrat jari-jari.",
        perimeterNote: "Dua kali pi kali jari-jari."
    };
}

function calculateFallback() {
    if (shape === "persegi") {
        return {
            luas: measures.sisi ** 2,
            keliling: measures.sisi * 4
        };
    }

    if (shape === "persegi_panjang") {
        return {
            luas: measures.panjang * measures.lebar,
            keliling: 2 * (measures.panjang + measures.lebar)
        };
    }

    if (shape === "segitiga") {
        return {
            luas: 0.5 * measures.alas * measures.tinggi,
            keliling: measures.sisi1 + measures.sisi2 + measures.sisi3
        };
    }

    return {
        luas: Math.PI * measures.jari_jari ** 2,
        keliling: 2 * Math.PI * measures.jari_jari
    };
}

function getResults() {
    const fallback = calculateFallback();

    return {
        luas: results.luas !== null ? results.luas : fallback.luas,
        keliling: results.keliling !== null
            ? results.keliling
            : fallback.keliling
    };
}

function getMeasureSummary() {
    if (shape === "persegi") {
        return `panjang sisi ${fmt(measures.sisi)} satuan`;
    }

    if (shape === "persegi_panjang") {
        return `panjang ${fmt(measures.panjang)} satuan dan lebar ${fmt(measures.lebar)} satuan`;
    }

    if (shape === "segitiga") {
        return `alas ${fmt(measures.alas)} satuan dan tinggi ${fmt(measures.tinggi)} satuan, dengan sisi ${fmt(measures.sisi1)}, ${fmt(measures.sisi2)}, dan ${fmt(measures.sisi3)} satuan`;
    }

    return `jari-jari ${fmt(measures.jari_jari)} satuan`;
}

function getCalculationNarration() {
    const r = getResults();

    if (shape === "persegi") {
        return `Luas sama dengan sisi dikali sisi. Kita masukkan nilai ${fmt(measures.sisi)} dikali ${fmt(measures.sisi)}, sehingga luasnya ${fmt(r.luas)} satuan persegi. Keliling sama dengan empat dikali sisi, yaitu empat dikali ${fmt(measures.sisi)}, hasilnya ${fmt(r.keliling)} satuan.`;
    }

    if (shape === "persegi_panjang") {
        return `Luas sama dengan panjang dikali lebar. Kita hitung ${fmt(measures.panjang)} dikali ${fmt(measures.lebar)}, sehingga luasnya ${fmt(r.luas)} satuan persegi. Keliling sama dengan dua dikali panjang ditambah lebar. Hasil kelilingnya ${fmt(r.keliling)} satuan.`;
    }

    if (shape === "segitiga") {
        return `Luas segitiga sama dengan setengah dikali alas dikali tinggi. Kita hitung setengah dikali ${fmt(measures.alas)} dikali ${fmt(measures.tinggi)}, sehingga luasnya ${fmt(r.luas)} satuan persegi. Keliling diperoleh dengan menjumlahkan ketiga sisi, yaitu ${fmt(measures.sisi1)}, ${fmt(measures.sisi2)}, dan ${fmt(measures.sisi3)}. Hasilnya ${fmt(r.keliling)} satuan.`;
    }

    return `Luas lingkaran sama dengan pi dikali jari-jari kuadrat. Jari-jari kita adalah ${fmt(measures.jari_jari)}. Hasil luasnya ${fmt(r.luas)} satuan persegi. Keliling sama dengan dua dikali pi dikali jari-jari. Hasil kelilingnya ${fmt(r.keliling)} satuan.`;
}

function getStageNarration(index) {
    const name = getShapeTitle();
    const measure = getMeasureSummary();
    const formulas = getFormulas();
    const r = getResults();

    const narrations = [
        `Halo, selamat datang di Euclid Lab. Pada pembelajaran ini kita akan mengenal bangun ${name}. Perhatikan gambar yang tampil di layar. Kita akan mempelajari bentuk, ukuran, rumus luas, dan rumus kelilingnya.`,
        `Sekarang, amati bentuk ${name}. Setiap bangun memiliki ciri yang berbeda. Perhatikan garis, sisi, atau lengkungan pada gambar. Bentuk ini membantu kita memahami bagaimana bangun geometri tersusun.`,
        `Berikutnya, kita mengenal ukuran bangun. Ukuran yang digunakan adalah ${measure}. Perhatikan penanda ukuran berwarna biru pada gambar. Ukuran ini akan kita gunakan untuk menghitung luas dan keliling.`,
        `Sekarang kita masuk ke rumus. Rumus luas ${name} adalah ${formulas.area}. Rumus kelilingnya adalah ${formulas.perimeter}. Luas menunjukkan besar daerah di dalam bangun, sedangkan keliling adalah panjang seluruh batas bangun.`,
        getCalculationNarration(),
        `Sebagai kesimpulan, kita telah mempelajari bangun ${name}, mengenali ukurannya, dan menggunakan rumus luas serta keliling. Luas bangun ini adalah ${fmt(r.luas)} satuan persegi dan kelilingnya ${fmt(r.keliling)} satuan. Terus berlatih agar semakin memahami geometri. Terima kasih sudah belajar bersama Euclid Lab.`
    ];

    return narrations[index] || narrations[0];
}

function setStatus(text) {
    $("statusText").textContent = text;
}

function toast(message) {
    const el = $("toast");
    el.textContent = message;
    el.classList.add("show");
    clearTimeout(toast.timer);
    toast.timer = setTimeout(() => el.classList.remove("show"), 2400);
}

function setFormulaCards() {
    const f = getFormulas();
    const r = getResults();

    $("areaFormula").textContent = f.area;
    $("perimeterFormula").textContent = f.perimeter;
    $("areaNote").textContent = f.areaNote;
    $("perimeterNote").textContent = f.perimeterNote;

    $("resultValue").textContent =
        `Luas = ${fmt(r.luas)} satuan persegi · Keliling = ${fmt(r.keliling)} satuan`;

    $("shapeBadge").textContent = getShapeTitle().toUpperCase();
}

function updateStepUI(index) {
    state.stage = index;

    $("lessonCount").textContent =
        `TAHAP ${String(index + 1).padStart(2, "0")}`;

    $("stepCounter").textContent =
        `${String(index + 1).padStart(2, "0")} / 06`;

    $("lessonTitle").textContent = stageNames[index];
    $("lessonDescription").textContent = stageDescriptions[index];

    document.querySelectorAll(".step").forEach((el, i) => {
        el.classList.toggle("active", i === index);
        el.classList.toggle("done", i < index);
    });

    $("visualCaption").textContent =
        `${getShapeTitle().toUpperCase()} · ${stageNames[index].toUpperCase()}`;

    drawGeometry(index);
}

function svgElement(tag, attrs = {}) {
    const node = document.createElementNS(
        "http://www.w3.org/2000/svg", tag
    );

    for (const [key, value] of Object.entries(attrs)) {
        node.setAttribute(key, String(value));
    }

    return node;
}

function addText(group, x, y, text, color = "#00e5ff", size = 16) {
    const node = svgElement("text", {
        x, y,
        fill: color,
        "font-size": size,
        "font-weight": "800",
        "text-anchor": "middle",
        opacity: 0
    });
    node.textContent = text;
    node.classList.add("label");

    if (state.stage >= 2) {
        node.classList.add("show");
    }

    group.appendChild(node);
    return node;
}

function addLine(group, x1, y1, x2, y2) {
    const line = svgElement("line", {
        x1, y1, x2, y2,
        class: "measure"
    });

    if (state.stage >= 2) {
        line.classList.add("show");
    }

    group.appendChild(line);
    return line;
}

function addShape(group, tag, attrs) {
    const node = svgElement(tag, attrs);
    node.classList.add("shape");
    group.appendChild(node);

    requestAnimationFrame(() => {
        node.classList.add("draw");
        if (state.stage >= 3) node.classList.add("fill");
    });

    return node;
}

function drawGeometry(index) {
    const group = $("shapeGroup");
    group.replaceChildren();

    const centerX = 300;
    const centerY = 185;

    if (shape === "persegi") {
        const side = 170;
        const x = centerX - side / 2;
        const y = centerY - side / 2;

        addShape(group, "rect", {
            x, y, width: side, height: side,
            rx: 3,
            fill: "url(#shapeGradient)",
            filter: index >= 1 ? "url(#glow)" : ""
        });

        if (index >= 2) {
            addLine(group, x, y + side + 28, x + side, y + side + 28);
            addText(group, centerX, y + side + 53, `s = ${fmt(measures.sisi)}`);
            addText(group, x - 15, centerY, fmt(measures.sisi));
        }

        if (index >= 3) {
            addText(group, centerX, centerY + 7, "L = s × s", "#ffd166", 21);
        }
    } else if (shape === "persegi_panjang") {
        const w = 260;
        const h = 145;
        const x = centerX - w / 2;
        const y = centerY - h / 2;

        addShape(group, "rect", {
            x, y, width: w, height: h,
            rx: 3,
            fill: "url(#shapeGradient)",
            filter: index >= 1 ? "url(#glow)" : ""
        });

        if (index >= 2) {
            addLine(group, x, y + h + 28, x + w, y + h + 28);
            addText(group, centerX, y + h + 53, `p = ${fmt(measures.panjang)}`);
            addLine(group, x - 30, y, x - 30, y + h);
            addText(group, x - 52, centerY, `l = ${fmt(measures.lebar)}`);
        }

        if (index >= 3) {
            addText(group, centerX, centerY + 7, "L = p × l", "#ffd166", 21);
        }
    } else if (shape === "segitiga") {
        const points = "300,70 440,300 160,300";

        addShape(group, "polygon", {
            points,
            fill: "url(#shapeGradient)",
            filter: index >= 1 ? "url(#glow)" : ""
        });

        if (index >= 2) {
            addLine(group, 300, 70, 300, 300);
            addText(group, 320, 190, `t = ${fmt(measures.tinggi)}`);
            addText(group, 300, 330, `a = ${fmt(measures.alas)}`);
            addText(group, 220, 185, fmt(measures.sisi1));
            addText(group, 380, 185, fmt(measures.sisi2));
        }

        if (index >= 3) {
            addText(group, centerX, centerY + 10, "L = ½ × a × t",
                    "#ffd166", 19);
        }
    } else {
        const radius = 115;

        addShape(group, "circle", {
            cx: centerX, cy: centerY, r: radius,
            fill: "url(#shapeGradient)",
            filter: index >= 1 ? "url(#glow)" : ""
        });

        if (index >= 2) {
            addLine(group, centerX, centerY, centerX + radius, centerY);
            addText(group, centerX + radius / 2, centerY - 13,
                    `r = ${fmt(measures.jari_jari)}`);
        }

        if (index >= 3) {
            addText(group, centerX, centerY + 7, "L = π × r²",
                    "#ffd166", 21);
        }
    }

    if (index >= 4) {
        addText(group, 300, 365,
            `Luas ${fmt(getResults().luas)} · Keliling ${fmt(getResults().keliling)}`,
            "#38d996", 16);
    }

    if (index >= 5) {
        addText(group, 300, 35, "PEMBELAJARAN SELESAI", "#38d996", 15);
    }
}

function renderWords(text) {
    const container = $("speechLine");
    container.replaceChildren();

    state.words = [];

    const parts = text.match(/\S+\s*/g) || [text];

    parts.forEach((part, index) => {
        const span = document.createElement("span");
        span.className = "word";
        span.textContent = part;
        span.dataset.wordIndex = String(index);
        container.appendChild(span);
        state.words.push(span);
    });

    state.activeWord = -1;
}

function highlightWord(index) {
    if (!state.words.length) return;

    const safeIndex = Math.max(0, Math.min(index, state.words.length - 1));

    state.words.forEach((word, i) => {
        word.classList.toggle("active", i === safeIndex);
    });

    state.activeWord = safeIndex;

    const active = state.words[safeIndex];
    if (active) {
        active.scrollIntoView({
            block: "nearest",
            inline: "nearest",
            behavior: "smooth"
        });
    }
}

function findWordIndex(charIndex) {
    const line = $("speechLine");
    const textBefore = state.words
        .map((word, index) => ({
            index,
            length: word.textContent.length
        }));

    let count = 0;

    for (const word of textBefore) {
        if (charIndex < count + word.length) return word.index;
        count += word.length;
    }

    return Math.max(0, state.words.length - 1);
}

function chooseIndonesianVoice() {
    const voices = window.speechSynthesis.getVoices() || [];
    state.voices = voices;

    const exact = voices.find(v =>
        v.lang && v.lang.toLowerCase() === "id-id"
    );

    if (exact) return exact;

    const indonesian = voices.find(v =>
        v.lang && v.lang.toLowerCase().startsWith("id")
    );

    if (indonesian) return indonesian;

    const googleIndonesian = voices.find(v =>
        /indonesia|indonesian/i.test(v.name)
    );

    return googleIndonesian || null;
}

function speakText(text, token, onEnd) {
    if (!state.speechSupported) {
        toast("Browser ini belum mendukung narator suara.");
        onEnd();
        return;
    }

    window.speechSynthesis.cancel();

    const utterance = new SpeechSynthesisUtterance(text);
    state.utterance = utterance;

    utterance.lang = "id-ID";
    utterance.rate = Number($("speed").value);
    utterance.pitch = 1;
    utterance.volume = 1;

    const voice = chooseIndonesianVoice();
    if (voice) {
        utterance.voice = voice;
        utterance.lang = voice.lang || "id-ID";
    }

    utterance.onstart = () => {
        if (token !== state.stageToken) return;
        state.running = true;
        state.paused = false;
        setStatus("NARATOR BERBICARA");
    };

    utterance.onboundary = event => {
        if (token !== state.stageToken) return;

        if (typeof event.charIndex === "number") {
            highlightWord(findWordIndex(event.charIndex));
        }
    };

    utterance.onend = () => {
        if (token !== state.stageToken) return;

        if (state.words.length) {
            highlightWord(state.words.length - 1);
        }

        state.utterance = null;
        onEnd();
    };

    utterance.onerror = event => {
        if (token !== state.stageToken) return;

        if (event.error === "canceled" || event.error === "interrupted") {
            return;
        }

        console.warn("Kesalahan speech synthesis:", event.error);
        state.utterance = null;
        onEnd();
    };

    window.speechSynthesis.speak(utterance);
}

function playStage(index) {
    if (index >= 6) {
        finishLesson();
        return;
    }

    state.stageToken += 1;
    const token = state.stageToken;

    state.stage = index;
    state.running = true;
    state.paused = false;
    state.stopped = false;

    updateStepUI(index);

    const narration = getStageNarration(index);
    renderWords(narration);

    $("playBtn").textContent = "▶ Putar";
    $("pauseBtn").textContent = "Ⅱ Jeda";
    setStatus("MENYIAPKAN NARASI");

    speakText(narration, token, () => {
        if (token !== state.stageToken || state.stopped) return;

        if (index < 5) {
            playStage(index + 1);
        } else {
            finishLesson();
        }
    });
}

function startLesson() {
    if (!state.speechSupported) {
        toast("Gunakan Microsoft Edge atau Google Chrome terbaru.");
        return;
    }

    if (state.paused) {
        window.speechSynthesis.resume();
        state.paused = false;
        state.running = true;
        setStatus("NARATOR BERBICARA");
        $("pauseBtn").textContent = "Ⅱ Jeda";
        return;
    }

    if (state.running && !state.stopped) {
        toast("Pembelajaran sedang berjalan.");
        return;
    }

    state.stage = 0;
    state.stopped = false;
    playStage(0);
}

function pauseLesson() {
    if (!state.speechSupported) return;

    if (window.speechSynthesis.speaking &&
        !window.speechSynthesis.paused) {
        window.speechSynthesis.pause();
        state.paused = true;
        state.running = false;
        setStatus("NARATOR DIJEDA");
        $("pauseBtn").textContent = "▶ Lanjut";
        return;
    }

    if (window.speechSynthesis.paused) {
        window.speechSynthesis.resume();
        state.paused = false;
        state.running = true;
        setStatus("NARATOR BERBICARA");
        $("pauseBtn").textContent = "Ⅱ Jeda";
    }
}

function restartLesson() {
    window.speechSynthesis.cancel();

    state.stageToken += 1;
    state.running = false;
    state.paused = false;
    state.stopped = false;
    state.utterance = null;

    setTimeout(() => playStage(0), 120);
}

function stopLesson() {
    state.stageToken += 1;
    state.stopped = true;
    state.running = false;
    state.paused = false;
    state.utterance = null;

    if (state.speechSupported) {
        window.speechSynthesis.cancel();
    }

    setStatus("PEMBELAJARAN DIHENTIKAN");
    $("lessonDescription").textContent =
        "Pembelajaran dihentikan. Tekan Putar untuk memulai kembali.";
    $("speechLine").textContent =
        "Narasi berhenti. Tekan Putar untuk mengulang pembelajaran.";

    toast("Narator dan animasi dihentikan.");
}

function finishLesson() {
    state.running = false;
    state.paused = false;
    state.stopped = false;
    state.utterance = null;

    setStatus("PEMBELAJARAN SELESAI");
    $("lessonCount").textContent = "SELESAI";
    $("stepCounter").textContent = "06 / 06";
    $("lessonTitle").textContent = "Hebat! Materi selesai.";
    $("lessonDescription").textContent =
        "Kamu telah menyelesaikan seluruh tahapan pembelajaran geometri. " +
        "Tekan Ulangi untuk mempelajari kembali materi dari awal.";

    document.querySelectorAll(".step").forEach(el => {
        el.classList.remove("active");
        el.classList.add("done");
    });

    $("visualCaption").textContent =
        "EUCLID LAB · PEMBELAJARAN SELESAI";

    toast("Materi selesai. Terima kasih sudah belajar!");
}

$("playBtn").addEventListener("click", startLesson);
$("pauseBtn").addEventListener("click", pauseLesson);
$("restartBtn").addEventListener("click", restartLesson);
$("stopBtn").addEventListener("click", stopLesson);

$("speed").addEventListener("input", () => {
    const speed = Number($("speed").value);
    $("speedValue").textContent = `${speed.toFixed(2)}×`;

    if (window.speechSynthesis.speaking) {
        toast("Kecepatan baru digunakan pada tahap berikutnya.");
    }
});

if (state.speechSupported) {
    window.speechSynthesis.onvoiceschanged = () => {
        chooseIndonesianVoice();
    };
}

setFormulaCards();
updateStepUI(0);
renderWords("Tekan tombol Putar untuk mendengarkan penjelasan.");
setStatus(state.speechSupported ? "STUDIO SIAP" : "SUARA TIDAK DIDUKUNG");

if (!state.speechSupported) {
    $("lessonDescription").textContent =
        "Browser ini tidak mendukung narator otomatis. " +
        "Silakan buka proyek menggunakan Microsoft Edge atau Google Chrome.";
}
</script>
</body>
</html>
"""


def _buat_halaman(hasil, ukuran):
    data = {
        "hasil": hasil if isinstance(hasil, (dict, list, str, int, float)) else str(hasil),
        "ukuran": ukuran if isinstance(ukuran, dict) else {},
    }

    data_json = json.dumps(data, ensure_ascii=False, default=str)
    return HTML.replace("__DATA__", data_json)


class _Handler(BaseHTTPRequestHandler):
    halaman = ""

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            isi = self.halaman.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(isi)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(isi)
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Halaman tidak ditemukan.")

    def log_message(self, format_string, *args):
        # Menonaktifkan log setiap permintaan browser agar terminal rapi.
        return


def tampilkan_animasi(hasil, ukuran):
    """
    Menampilkan EUCLID LAB di browser.

    Parameter:
        hasil: hasil perhitungan dari src.proses
        ukuran: dictionary ukuran bangun yang dimasukkan pengguna
    """
    halaman = _buat_halaman(hasil, ukuran)

    class Handler(_Handler):
        pass

    Handler.halaman = halaman

    server = HTTPServer(("127.0.0.1", 0), Handler)
    port = server.server_address[1]
    url = f"http://127.0.0.1:{port}/"

    thread = threading.Thread(
        target=server.serve_forever,
        daemon=True
    )
    thread.start()

    print("\nEUCLID LAB berhasil dijalankan.")
    print(f"Alamat visualisasi: {url}")
    print("Tutup tab browser untuk mengakhiri sesi visualisasi.")

    try:
        webbrowser.open(url)
    except Exception as error:
        print(f"Browser tidak dapat dibuka otomatis: {error}")
        print(f"Silakan buka alamat berikut secara manual: {url}")

    # Server tetap hidup selama program utama berjalan.
    # Thread bersifat daemon agar tidak menghambat penutupan program.
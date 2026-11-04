"""Plan 3: Kashmir in winter by train (Delhi → Jammu → Vande Bharat → Srinagar), 6 people, Airbnb/houseboats."""
from common import PlanDoc, totals, k
import sections as X

BUDGET = [
    ("Train Hyderabad → Delhi (12723)", 800, 2100, "SL vs 3A"),
    ("Delhi day (metro, cloak room, entries)", 400, 500, ""),
    ("Delhi → Jammu overnight", 450, 450, "14033 Jammu Mail SL (3A ≈ ₹1,250)"),
    ("Vande Bharat Jammu → Srinagar", 1000, 1000, "Chair car; fare reports vary ₹700–1,600"),
    ("Vande Bharat Srinagar → Jammu", 1000, 1000, ""),
    ("Jammu → Delhi overnight", 450, 450, "SL (3A ≈ ₹1,250)"),
    ("Delhi half-day on 2 Jan", 300, 400, ""),
    ("Train Delhi → Hyderabad (12724)", 800, 2100, "SL vs 3A"),
    ("Innova day trips: Gulmarg, Doodhpathri, Sonamarg", 1950, 1950, "≈ ₹11.6k ÷ 6"),
    ("Pahalgam 2-day Innova + union taxi (Betaab, Aru)", 1900, 1900, "≈ ₹11.5k ÷ 6"),
    ("Shikara, autos", 400, 400, ""),
    ("Gulmarg Gondola", 810, 1820, "Phase 1 only vs both phases"),
    ("Airbnb houseboat/villa 5N Srinagar + 1N Pahalgam", 5400, 8000, "3 rooms / entire home ÷ 6"),
    ("Food (beyond houseboat breakfast/dinner)", 5000, 5500, ""),
    ("Gear rentals (Tangmarg)", 800, 1000, ""),
    ("Buffer", 800, 1000, ""),
]


def build(path):
    lo, hi = totals(BUDGET)
    d = PlanDoc(path,
                "Plan 3 · Kashmir in Winter (by train)",
                "Delhi day → Jammu → Vande Bharat over the Chenab bridge → Srinagar houseboat, Gulmarg Gondola, Drung frozen waterfall, Doodhpathri, "
                "Sonamarg, Pahalgam–Aru, Martand. 6 people · Airbnb/houseboats · 24 Dec 2026 – 3 Jan 2027",
                "#7c3aed", "PLAN 3 · KASHMIR WINTER")

    d.h1("At a glance")
    d.table([
        ["Route", "Hyderabad → Delhi day → overnight train → Jammu → <b>Vande Bharat</b> → Srinagar 5N (+ day trips) · Pahalgam 1N → Vande Bharat → "
                  "Jammu → overnight → Delhi → Hyderabad"],
        ["Why Kashmir", "Most reliable snow in North India for these dates (Chillai Kalan starts 21 Dec). Train all the way since the Jammu–Srinagar "
                        "Vande Bharat (May 2026). Sonamarg open in winter since the Z-Morh tunnel (Jan 2025). Winter is off-season for houseboats."],
        ["Snow chances", "Very high: Gulmarg, Apharwat, Sonamarg, Aru, Doodhpathri. Medium–high: Srinagar city"],
        ["Crowd level", "Medium at Gulmarg (high 30 Dec–1 Jan). Low at Doodhpathri, Drung, Aru, Martand, old Srinagar"],
        ["Budget per person (6 people)", f"<b>≈ {k(lo)} shoestring</b> · <b>≈ {k(hi)} recommended</b> · flying Srinagar → Hyderabad instead of the 2 "
                                         "return trains adds ≈ ₹7–8.5k"],
        ["Temperatures", "Srinagar −6 to 6 °C · Gulmarg/Pahalgam −12 to 0 °C"],
    ], [0.22, 0.78], header=False, bold_first_col=True)
    d.callout("Status check (latest reports found)",
              ["Gulmarg, Sonamarg and Pahalgam reopened June 2025; <b>Doodhpathri and Yusmarg reopened 16 Feb 2026</b>. "
               "<b>Baisaran</b> reopening is unconfirmed. <b>Chandanwari</b> was listed closed till 31 Dec 2026. Gurez, Bangus and Sinthan Top are snow-bound.",
               "Prepaid SIMs from outside J&amp;K <b>do not work</b>. Make sure at least 2 of the 6 have postpaid connections."], "warn")

    d.h1("Getting there and back")
    X.onward(d, (1, 2, 3, 4))
    X.delhi_day(d)
    d.h2("Delhi ↔ Jammu ↔ Srinagar (cheapest that still connects)")
    d.table([
        ["Leg", "Option", "Timing", "Fare / person", "Buffer logic"],
        ["Delhi → Jammu (25 Dec night)", "<b>14033 Jammu Mail</b> from Old Delhi (cheapest, daily)", "Old Delhi 20:05–20:10 → Jammu early morning "
         "(continues to Katra ~09:15–11:15)", "SL ≈ ₹450 · 3A ≈ ₹1,250", "Arrives after the 06:20 Vande Bharat, so take the <b>13:20</b> one"],
        ["Faster alternative", "12425 Jammu Rajdhani from New Delhi (late evening)", "Jammu ~05:00", "3A ≈ ₹1,900–2,100",
         "Catches the <b>06:20</b> Vande Bharat (~1 h buffer)"],
        ["<b>Jammu → Srinagar</b>", "<b>26401 Vande Bharat</b> 06:20 → 11:10 · <b>26403</b> 13:20 → 18:00", "~4 h 50 m", "CC ≈ ₹700–1,600 (check IRCTC)",
         "Book as soon as the Delhi–Jammu PNR confirms"],
        ["<b>Srinagar → Jammu</b> (1 Jan)", "<b>26402 Vande Bharat</b> 14:00 → 18:50", "~4 h 50 m", "Same", "Pick a Jammu→Delhi train leaving after ~20:30"],
        ["Jammu → Delhi (1 Jan night)", "Overnight trains (Jammu Mail / Uttar Sampark Kranti / Rajdhani)", "Reach Delhi ~05:00–08:00 on 2 Jan",
         "SL ≈ ₹450 · 3A ≈ ₹1,250", "Then 12724 at 16:00 = 8–11 h Delhi buffer"],
    ], [0.15, 0.25, 0.22, 0.16, 0.22])
    d.small("Vande Bharat timings from the May 2026 launch reports. Jammu Mail times from ConfirmTkt/indiantrain/RailMitra (sources differ by a few minutes).")
    X.returns(d, (1, 2, 4))
    X.flights(d, (1, 3), "Comfort option: fly back from Srinagar")
    X.vehicles(d)

    d.h1("Day-by-day itinerary")
    d.day("Day 1 · Thu 24 Dec", "Hyderabad → Delhi", ["<b>06:00 12723 Telangana Express</b> (or 12:50 12285 Duronto, Thu)."], stay="Train", cost="₹300 food")
    d.day("Day 2 · Fri 25 Dec", "Delhi day → Jammu Mail", [
        "Old Delhi circuit (box above), Christmas at Sacred Heart. Board <b>14033 Jammu Mail</b> at Old Delhi ~20:05–20:10 (it's the same station "
        "as your cloak room, so no cross-city transfer).",
    ], stay="Train (SL)", cost="₹700 Delhi + ₹450 train")
    d.day("Day 3 · Sat 26 Dec", "Jammu → Vande Bharat over the Chenab → Srinagar", [
        "Morning in Jammu: Raghunath temple, Bahu fort/Bagh-e-Bahu (or stay on the Jammu Mail to Katra and board the Vande Bharat there).",
        "<b>13:20 Vande Bharat 26403</b> → Srinagar 18:00. Left side for the Chenab bridge (world's highest rail arch) and the Anji Khad bridge.",
        "Houseboat check-in on <b>Nigeen / Dal</b>. Ask for the bukhari or heaters and electric blankets.",
    ], stay="Houseboat (Airbnb)", cost="₹1,000 VB + ₹600 food")
    d.day("Day 4 · Sun 27 Dec", "Gulmarg + Drung frozen waterfall", [
        "Pre-book the <b>Gulmarg Gondola</b> on the official J&amp;K Cable Car portal: Phase 1 ≈ ₹810, Phase 2 to Apharwat (3,980 m) ≈ ₹1,010.",
        "Innova Srinagar ⇄ Gulmarg ≈ ₹3,500–4,000. At <b>Tangmarg</b> rent coats + boots (₹300–500). <b>Drung waterfall</b> (5 km detour) freezes in Chillai Kalan.",
        "Gulmarg: Apharwat snowfields, St Mary's Church, Maharani temple, sledges (agree the rate first), beginner ski lesson.",
    ], stay="Houseboat", cost="₹650 cab share + ₹810–1,820 gondola + ₹400 rent + ₹600 food")
    d.day("Day 5 · Mon 28 Dec", "Doodhpathri · sunset shikara", [
        "<b>Doodhpathri</b> (42 km): snow meadows and the Shaliganga stream, almost no tourists. Via <b>Charar-e-Sharif</b>. Backup: Yusmarg.",
        "Back by 16:00 for the <b>sunset shikara</b> (≈ ₹800–900/hour per boat; one boat takes 4–6). Dinner at Khayyam Chowk.",
    ], stay="Houseboat", cost="₹600 cab share + ₹150 shikara + ₹700 food")
    d.day("Day 6 · Tue 29 Dec", "Sonamarg + Kheer Bhawani", [
        "<b>Sonamarg</b> (80 km) snowfields and Thajiwas glacier walk/sledge (union rate boards; bargain). Return via <b>Kheer Bhawani</b> temple. "
        "Optional <b>Naranag</b> 8th-century temples near Kangan if the side road is clear.",
    ], stay="Houseboat", cost="₹720 cab share + ₹500 activities + ₹600 food")
    d.day("Day 7 · Wed 30 Dec", "Pampore · Awantipora · Martand → Pahalgam", [
        "Saffron and kahwa at <b>Pampore</b>, <b>Awantipora</b> ruins, <b>Martand Sun Temple</b> (offbeat), bat workshops at Sangam.",
        "Afternoon <b>Betaab valley</b> by union taxi. Lidder river walk.",
    ], stay="Pahalgam (Airbnb cottage)", cost="₹1,900 two-day cab + union share + ₹600 food")
    d.day("Day 8 · Thu 31 Dec", "Aru valley snow → Srinagar for NYE", [
        "<b>Aru valley</b> (12 km): the quietest snow of the trip. Baisaran/Chandanwari only if officially reopened.",
        "Back to Srinagar. NYE on the houseboat: kangri, kahwa, a wazwan dinner (pre-order ₹600–1,200 pp).",
    ], stay="Houseboat", cost="₹1,000 food/NYE")
    d.day("Day 9 · Fri 1 Jan", "Old Srinagar → Vande Bharat → Jammu → night train", [
        "Dawn floating vegetable market (shikara, 05:30–07:00). <b>Khanqah-e-Moula</b>, <b>Jamia Masjid</b>, <b>Pari Mahal</b>, Hazratbal; dry fruits at Lal Chowk.",
        "<b>14:00 Vande Bharat 26402</b> → Jammu 18:50 → overnight train to Delhi (leaving after ~20:30).",
    ], stay="Train", cost="₹1,000 VB + ₹450–1,300 train + ₹600 food")
    d.day("Day 10 · Sat 2 Jan", "Delhi → Hyderabad", ["Humayun's Tomb / Lodhi Garden → <b>16:00 12724</b> (or 22692 Rajdhani)."], stay="Train",
          cost="₹400 + ₹600 food")
    d.day("Day 11 · Sun 3 Jan", "Home", ["Hyderabad ~17:10."])

    X.airbnb(d, [
        ["5 (26–29, 31 Dec)", "Srinagar (Nigeen / Dal)", "<b>Heide houseboat</b>: 3 bedrooms + dining and sitting rooms, 4.65★ (177). "
         "Or <b>Luxe Houseboat in Dal Lake by IRI Homes</b>",
         "<b>Houseboat Royal Lodge</b> (rooms were ~₹650/night in Aug 2025; book 3) · <b>New Kolohai Houseboats</b> · land option: "
         "<b>Bhaag E Nishat</b> 3BR villa, Rajbagh, 5.0★ (12), up to 8 guests", (5000, 9000)],
        ["1 (30 Dec)", "Pahalgam", "<b>Trout Water Lodge</b> 5.0★ (8) · <b>Pahalgam Mir River Lodge</b> 5-BR cottage 4.42★ (31; listed price is per room)",
         "<b>Cottage in the woods</b> 3BR cabin (5.0★, 1 review) · Lidder-side guesthouses at winter rates", (4500, 8000)],
    ])

    d.h1("Offbeat vs main places")
    d.table([
        ["Place", "Type", "Winter access"],
        ["Dal / Nigeen, houseboats, old Srinagar", "Main", "Open"],
        ["Gulmarg + Gondola", "Main", "Open (Phase 2 shuts in high wind)"],
        ["Drung frozen waterfall", "Offbeat", "Usually open from Tangmarg"],
        ["Doodhpathri (Yusmarg backup)", "Offbeat", "Reopened Feb 2026; snow can block"],
        ["Sonamarg, Thajiwas", "Main", "Year-round since the Z-Morh tunnel"],
        ["Kheer Bhawani, Naranag", "Offbeat", "Kheer Bhawani open; Naranag weather-dependent"],
        ["Pampore, Awantipora, Martand", "Offbeat", "Open"],
        ["Pahalgam, Betaab, Aru", "Main + offbeat", "Open; Chandanwari closed till 31 Dec; Baisaran unconfirmed"],
    ], [0.4, 0.2, 0.4])
    d.p("<b>Bike rentals:</b> Srinagar RE rentals exist (≈ ₹1,200–2,000/day), but black ice in Chillai Kalan makes them a bad idea. "
        "For 6, an Innova costs about the same as 3 bikes plus fuel.")

    X.gear(d, [
        ["Point", "What you can rent", "Rate"],
        ["Tangmarg (Gulmarg road)", "Long coat, snow boots, gloves", "₹300–500 per set"],
        ["Gulmarg ski shops", "Skis/boots/poles, jacket, trousers, goggles", "≈ ₹700 + ₹300 + ₹200 + ₹100 per day"],
        ["Sonamarg / Pahalgam stalls", "Gumboots, coats, sledges", "₹200–400"],
        ["Srinagar markets (buy)", "Pheran ₹800–1,500, woollen socks, kangri", "Buy"],
    ])

    d.h1("Budget per person (6 people sharing)")
    d.budget(BUDGET, "Fits ₹25–30k on the shoestring line. Six people cut cabs and houseboats to ~⅔ of the 4-person cost.")

    d.h1("Bookings to do now")
    d.bullets([
        "Return chain first: VB Srinagar→Jammu (1 Jan) + Jammu→Delhi overnight (1 Jan) + 12724 (2 Jan).",
        "Onward: 12723 (24 Dec) + 14033 Jammu Mail (25 Dec) + VB 26403 Jammu→Srinagar (26 Dec).",
        "Houseboat 26–29 + 31 Dec; Pahalgam 30 Dec. Gondola online ~1 week before, only on the official portal.",
    ])
    X.packing_and_safety(d, ["Carry ID at all times; frequent security checks. Houseboats with generators and bukharis are worth ₹300–500 more."])
    d.sources([
        "Vande Bharat Jammu–Srinagar (26401/26402/26403): Kashmir Life, NewsX, Inshorts, newkerala (Apr–May 2026)",
        "14033 Jammu Mail: ConfirmTkt, indiantrain, RailMitra, travelkhana (Old Delhi 20:05–20:10, daily)",
        "Z-Morh tunnel / Sonamarg: Daily Excelsior, The Tribune, Kashmir Life; reopened sites Feb 2026: ETV Bharat, ThePrint, Business Today",
        "Pahalgam union rates & closures: zoutons 2026, vargiskhan.com; Gondola fares: zoutons, travelcoffee, kashmirtourbazaar",
        "Airbnb listings: airbnb.com/.co.in Dal Lake houseboats, Nigeen Lake, Pahalgam, Gulmarg pages via search (Nov 2026)",
        "HYD–SXR fares: Skyscanner, MakeMyTrip, HappyFares, Air India Express (Nov 2026)",
    ])
    d.build()
    return lo, hi

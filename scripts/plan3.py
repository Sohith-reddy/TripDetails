"""Plan 3 (my pick for 'North'): Kashmir in winter, by the new Jammu–Srinagar Vande Bharat."""
from common import PlanDoc
import sections as X


def build(path):
    d = PlanDoc(path,
                "Plan 3 · Kashmir in Winter (my pick)",
                "Snow you can count on in late December: Srinagar houseboat, Gulmarg Gondola, Drung frozen waterfall, Doodhpathri, "
                "Sonamarg, Pahalgam–Aru, Martand, plus the new train over the Chenab bridge. 24 Dec 2026 – 3 Jan 2027",
                "#7c3aed", "PLAN 3 · KASHMIR WINTER")

    d.h1("Why Kashmir is my choice for Plan 3")
    d.bullets([
        "<b>Most reliable snow in North India for these dates.</b> 21 Dec starts <i>Chillai Kalan</i>, the 40 coldest days. Gulmarg/Apharwat "
        "almost always has snow by late December. Himachal and Uttarakhand snow at 2,000–2,700 m is hit-or-miss in some years.",
        "<b>The train now goes all the way.</b> Vande Bharat Jammu Tawi ↔ Srinagar (direct since 2 May 2026) crosses the Chenab bridge "
        "(world's highest railway arch bridge) and the Anji Khad cable-stayed bridge. You avoid the 8–10 h winter road via Banihal.",
        "<b>Sonamarg is now open in winter.</b> The Z-Morh tunnel (opened 13 Jan 2025) keeps it accessible year-round.",
        "<b>Winter is off-season.</b> Houseboats and hotels are cheaper than summer, except Gulmarg on NYE.",
    ])
    d.table([
        ["Route", "Hyderabad → Delhi → (overnight) Jammu → Vande Bharat → Srinagar 4N (+day trips) → Pahalgam 1N → Srinagar 1N → "
                  "Vande Bharat → Jammu → Delhi → Hyderabad"],
        ["Snow chances", "Very high: Gulmarg, Apharwat, Sonamarg, Aru, Doodhpathri. Medium–high: Srinagar city (a few snowfalls a winter; Dal edges freeze)"],
        ["Crowd level", "Medium at Gulmarg (high on 30 Dec–1 Jan). Low at Doodhpathri, Drung, Aru, Martand, old Srinagar"],
        ["Difficulty", "Easy. Cold is the challenge: −5 to −12 °C at night in Gulmarg/Pahalgam, −2 to −6 °C in Srinagar"],
        ["Budget (per person, 4 people)", "≈ ₹22.7k shoestring (SL, Phase-1 gondola) · ≈ ₹30.4k recommended (3A, both gondola phases) · "
                                          "≈ ₹38k if you fly Srinagar → Hyderabad back"],
    ], [0.22, 0.78], header=False, bold_first_col=True)

    d.callout("Status check (as of the latest reports found)",
              ["J&amp;K reopened Gulmarg, Sonamarg and Pahalgam in June 2025, and Yusmarg and <b>Doodhpathri</b> on 16 Feb 2026 (42 sites open by then).",
               "<b>Baisaran</b> (Pahalgam) reopening could not be confirmed. <b>Chandanwari</b> was listed closed by District Anantnag till 31 Dec 2026. "
               "<b>Gurez, Bangus, Sinthan Top</b> are snow-bound in winter, so they're left out.",
               "Prepaid SIMs from outside J&amp;K <b>do not work</b> there. Make sure at least 2 people in the group have postpaid connections."], "warn")

    d.h1("Getting there and back")
    X.delhi_trains(d, onward_idx=(4, 1, 2, 3), return_idx=(1, 2, 3, 6))
    d.h2("Delhi ↔ Jammu ↔ Srinagar")
    d.table([
        ["Leg", "Option", "Timing", "Approx fare"],
        ["Delhi → Jammu Tawi (25 Dec night)", "Several overnight trains from New Delhi / Old Delhi (e.g. 12425 Jammu Rajdhani, "
         "12445 Uttar Sampark Kranti, 14033 Jammu Mail)", "Leave ~19:30–22:00, reach ~05:00–07:30", "SL ≈ ₹450–550 · 3A ≈ ₹1,200–1,400 (Rajdhani ≈ ₹1,800–2,100)"],
        ["Alt: Delhi → Katra", "22439 Vande Bharat, New Delhi 06:00 → Katra 14:00 (not Tue)", "8 h", "CC ≈ ₹1,550–1,650"],
        ["<b>Jammu → Srinagar</b>", "<b>26401 Vande Bharat</b> Jammu 06:20 → Srinagar 11:10 · <b>26403</b> Jammu 13:20 → Srinagar 18:00",
         "~4 h 50 m", "CC ≈ ₹700–1,600 (fares vary between reports; check IRCTC)"],
        ["<b>Srinagar → Jammu</b>", "<b>26402 Vande Bharat</b> Srinagar 14:00 → Jammu 18:50", "~4 h 50 m", "Same"],
        ["Jammu → Delhi (1 Jan night)", "Overnight trains leave Jammu ~19:30–22:00", "Reach Delhi ~05:00–08:00", "SL ≈ ₹500 · 3A ≈ ₹1,300"],
        ["Direct Jammu → Secunderabad", "22706 Humsafar, Jammu 05:45 (weekly; one source says Fri)", "~36 h", "3A ≈ ₹3,300–3,900"],
    ], [0.2, 0.4, 0.2, 0.2])
    d.small("Vande Bharat timings are from the May 2026 launch reports (Kashmir Life, NewsX, Inshorts). Book the Jammu–Srinagar leg the moment "
            "your Delhi–Jammu ticket is confirmed: the chair car fills fast in holiday weeks. Keep 2–3 h between connections because "
            "winter fog delays Delhi trains.")
    X.flights(d, (1, 3))
    d.callout("Comfort option",
              "Fly back Srinagar → Hyderabad (IndiGo direct, ~₹9,600–11,100; NYE week can reach ₹15k) on 2 Jan. You get the whole of 1 Jan in "
              "Srinagar and skip ~40 h of trains, for about ₹7–8.5k extra per person. Or fly both ways (≈ ₹20–24k for flights alone, "
              "which goes over budget).")

    d.h1("Day-by-day itinerary")
    d.day("Day 1 · Thu 24 Dec", "Hyderabad → Delhi", [
        "<b>12:50 12285 Duronto</b> (Secunderabad, Thu) → Nizamuddin 10:40 on 25 Dec. Or 06:00 12723 Telangana Express → New Delhi 07:40.",
    ], stay="Train", cost="₹300 food (Duronto includes meals)")
    d.day("Day 2 · Fri 25 Dec", "Christmas in Delhi → night train to Jammu", [
        "Leave bags at the station cloak room. Humayun's Tomb (near Nizamuddin), Sacred Heart Cathedral (Christmas), Connaught Place, India Gate.",
        "Night train to Jammu Tawi. Buy snacks; carry water.",
    ], stay="Train", cost="₹700 food + ₹200 local")
    d.day("Day 3 · Sat 26 Dec", "Jammu → Srinagar on the Vande Bharat · Dal Lake", [
        "<b>06:20 Vande Bharat 26401</b> (or 13:20 26403). Sit on the left side for the Chenab bridge views. Tunnels include the 12.7 km T-50.",
        "Check in to a <b>houseboat on Nigeen / Dal</b> (quieter than Boulevard-facing boats). Ask for a bukhari/heater and electric blankets.",
        "Sunset <b>shikara ride</b> (1–2 h, ₹600–900 per boat per hour, fixed boards at ghats). Evening walk on the Boulevard / Polo View market.",
    ], stay="Houseboat (₹2,000–3,500 per room with breakfast & dinner in winter)", cost="₹1,000 train + ₹200 shikara share + ₹500 food")
    d.day("Day 4 · Sun 27 Dec", "Gulmarg + Drung frozen waterfall", [
        "Pre-book the <b>Gulmarg Gondola</b> on the official J&amp;K Cable Car Corporation portal a few days ahead (fake sites exist): "
        "Phase 1 Gulmarg→Kongdoori ≈ ₹810, Phase 2 Kongdoori→Apharwat (3,980 m) ≈ ₹1,010. The Kongdoori–Mary's Shoulder chairlift is a separate ≈ ₹300 ticket.",
        "Cab Srinagar ⇄ Gulmarg ≈ ₹2,600–3,000 for the day. Leave 07:30. At <b>Tangmarg</b>, rent a long coat + snow boots (₹300–500). "
        "Tourist vehicles may have to switch to local taxis/chains after heavy snow.",
        "<b>Drung waterfall</b> (offbeat, ~5 km detour from Tangmarg) usually freezes solid in Chillai Kalan.",
        "In Gulmarg: Apharwat snowfields, St Mary's Church, Maharani temple, sledge rides (negotiate the rate first), beginner ski lesson "
        "(gear ≈ ₹700/day + instructor).",
    ], stay="Srinagar houseboat (or a night in Tangmarg if you want sunrise)", cost="₹700 cab share + ₹1,820 gondola + ₹400 rent + ₹600 food")
    d.day("Day 5 · Mon 28 Dec", "Doodhpathri, the quiet snow meadow", [
        "<b>Doodhpathri</b> (42 km, Budgam): open snow meadows, the Shaliganga stream, pine forests, very few tourists. Reopened Feb 2026.",
        "En route: <b>Charar-e-Sharif</b> shrine. If Doodhpathri is snow-bound, swap to <b>Yusmarg</b> (also reopened; road can close for "
        "days after snow, so ask in the morning).",
        "Evening: old-city food at Khayyam Chowk (kebabs, harissa in winter mornings, nadru monje).",
    ], stay="Srinagar", cost="₹700 cab share + ₹700 food")
    d.day("Day 6 · Tue 29 Dec", "Sonamarg + Kheer Bhawani", [
        "<b>Sonamarg</b> (80 km): winter snowfields; Thajiwas glacier walk or sledge (pony/sledge unions have rate boards, so bargain). "
        "Year-round access thanks to the Z-Morh tunnel.",
        "Return via <b>Kheer Bhawani</b> temple (Tulmulla) and the Sindh river villages. Optional: <b>Naranag</b> 8th-century temples near "
        "Kangan, if the side road is clear.",
    ], stay="Srinagar", cost="₹800 cab share + ₹500 activities + ₹600 food")
    d.day("Day 7 · Wed 30 Dec", "Srinagar → Pahalgam via saffron & ruins", [
        "<b>Pampore</b> (saffron town, kahwa tasting), <b>Awantipora</b> 9th-century temple ruins, <b>Martand Sun Temple</b> (offbeat, "
        "Mattan, Anantnag), cricket-bat workshops at Sangam/Bijbehara.",
        "Afternoon: <b>Betaab valley</b> by Pahalgam union taxi (union rates ≈ ₹2,000–3,000 for the circuit). Lidder river walk.",
    ], stay="Pahalgam riverside hotel (₹1,500–2,500 per room in winter)", cost="₹1,625 two-day cab share + ₹600 food")
    d.day("Day 8 · Thu 31 Dec", "Aru valley snow → back to Srinagar for NYE", [
        "<b>Aru valley</b> (12 km): snowbound meadow village. The quietest snow you'll get on this trip.",
        "Baisaran / Chandanwari only if officially reopened by then (ask the union stand).",
        "Back to Srinagar (~2.5 h). NYE on the houseboat: kangri, kahwa, wazwan dinner (pre-order ₹600–1,200 pp).",
    ], stay="Srinagar houseboat / hotel", cost="₹625 union taxi share + ₹1,000 food/NYE")
    d.day("Day 9 · Fri 1 Jan", "Old Srinagar → Vande Bharat to Jammu → night train", [
        "Dawn <b>floating vegetable market</b> on Dal (05:30–07:00, by shikara).",
        "<b>Shah-e-Hamdan (Khanqah-e-Moula)</b> papier-mâché interiors, <b>Jamia Masjid</b>, <b>Pari Mahal</b> (city view), Hazratbal; "
        "Shankaracharya hill if time allows. Buy dry fruits and kahwa near Lal Chowk.",
        "<b>14:00 Vande Bharat 26402</b> → Jammu 18:50 → overnight train to Delhi (~20:00–22:00 dep).",
    ], stay="Train", cost="₹1,000 VB + ₹600 food")
    d.day("Day 10 · Sat 2 Jan", "Delhi → Hyderabad", [
        "Arrive Delhi early morning. <b>16:00 12724 Telangana Express</b> (or 22692 Rajdhani from Nizamuddin late evening).",
    ], stay="Train", cost="₹600 food")
    d.day("Day 11 · Sun 3 Jan", "Home", ["Hyderabad ~17:10."])

    d.h1("Offbeat vs main places in this plan")
    d.table([
        ["Place", "Type", "Why", "Winter access"],
        ["Dal / Nigeen lake, Boulevard", "Main", "Houseboats, shikara, floating market", "Open"],
        ["Gulmarg + Gondola to Apharwat", "Main", "Highest gondola in Asia; assured snow", "Open (Phase 2 shuts in high wind)"],
        ["Drung frozen waterfall", "Offbeat", "Ice formations in Chillai Kalan", "Usually open from Tangmarg"],
        ["Doodhpathri", "Offbeat", "Quiet snow meadows, no crowd", "Reopened Feb 2026; snow can block"],
        ["Yusmarg (backup)", "Offbeat", "Pine meadows", "Reopened; road may shut for weeks after snow"],
        ["Sonamarg, Thajiwas", "Main", "Snowfields and glacier", "Year-round since Z-Morh tunnel (Jan 2025)"],
        ["Kheer Bhawani, Naranag", "Offbeat", "Spring temple; 8th-c. temple ruins", "Kheer Bhawani open; Naranag road weather-dependent"],
        ["Pampore, Awantipora, Martand", "Offbeat", "Saffron, 9th-c. ruins, Sun temple", "Open"],
        ["Pahalgam, Betaab, Aru", "Main + offbeat", "Lidder valley in snow", "Open; Chandanwari closed till 31 Dec; Baisaran unconfirmed"],
        ["Old Srinagar (Khanqah, Jamia, Pari Mahal)", "Main", "Heritage + food", "Open"],
    ], [0.27, 0.13, 0.3, 0.3])

    d.h1("Bike rentals")
    d.p("Srinagar has a few RE rental shops (≈ ₹1,200–2,000/day) but riding in Chillai Kalan means black ice on the Gulmarg, Sonamarg and "
        "Pahalgam roads and −5 °C wind. <b>Not recommended this season.</b> Shared cabs at ₹2,600–3,500 per day split 4 ways cost about "
        "the same as 2 bikes plus fuel.")

    X.gear(d, [
        ["Point", "What you can rent", "Rate"],
        ["Tangmarg (on the Gulmarg road)", "Long coat, gumboots/snow boots, gloves", "₹300–500 per set"],
        ["Gulmarg ski shops (incl. govt shop)", "Skis/boots/poles, ski jacket, trousers, goggles", "≈ ₹700 + ₹300 + ₹200 + ₹100 per day"],
        ["Sonamarg / Pahalgam stalls", "Gumboots, coats, sledges", "₹200–400"],
        ["Srinagar markets (buy)", "Pheran (₹800–1,500, warm souvenir), woollen socks, kangri", "Buy"],
    ])

    d.h1("Budget (per person, 4 people)")
    d.budget([
        ("Train Hyderabad → Delhi", 800, 2100, "SL vs 3A Telangana (Duronto 3A ≈ ₹3,300)"),
        ("Train Delhi → Jammu (overnight)", 500, 1300, "SL vs 3A"),
        ("Vande Bharat Jammu → Srinagar", 1000, 1000, "CC; fare estimates vary"),
        ("Vande Bharat Srinagar → Jammu", 1000, 1000, ""),
        ("Train Jammu → Delhi (overnight)", 500, 1300, ""),
        ("Train Delhi → Hyderabad", 800, 2100, ""),
        ("Cabs: Gulmarg, Doodhpathri, Sonamarg (shared)", 2200, 2200, "≈ ₹8.8k ÷ 4"),
        ("Cab Srinagar ⇄ Pahalgam 2 days + union taxi", 2250, 2250, "≈ ₹9k ÷ 4"),
        ("Shikara, autos, metro", 600, 600, ""),
        ("Gulmarg Gondola", 810, 1820, "Phase 1 only vs both phases"),
        ("Stays: 5N Srinagar (houseboat/hotel) + 1N Pahalgam", 5400, 7200, "2 per room; houseboats incl. breakfast + dinner"),
        ("Food (beyond houseboat meals) incl. train food", 5000, 5500, ""),
        ("Gear rentals (Tangmarg etc.)", 800, 1000, ""),
        ("Buffer", 1000, 1000, ""),
    ], "Fits ₹25–30k on trains. Flying back from Srinagar instead of the 2 return trains adds ≈ ₹7–8.5k.")

    d.h1("Bookings to do now")
    d.bullets([
        "Return chain first: Vande Bharat Srinagar→Jammu (1 Jan) + Jammu→Delhi overnight (1 Jan) + Delhi→Hyderabad (2 Jan). "
        "Or the Srinagar→Hyderabad flight for 2 Jan if you choose comfort.",
        "Onward: Duronto 12285 / Telangana 12723 (24 Dec) + Delhi→Jammu overnight (25 Dec) + Vande Bharat Jammu→Srinagar (26 Dec).",
        "Houseboat for 26–29 Dec and 31 Dec (book via JKTDC-registered owners, with reviews). Pahalgam hotel 30 Dec.",
        "Gondola tickets: book online ~1 week before (only on the official portal).",
    ])
    X.packing_and_safety(d, [
        "Carry ID at all times; there are frequent security checks. Follow local advisories and keep the J&amp;K Tourism / police helplines handy.",
        "Power cuts are common in winter. Houseboats with generators and bukhari heaters are worth the extra ₹300–500.",
    ])
    d.sources([
        "Vande Bharat Jammu–Srinagar launch, timings 26401/26402/26403: Kashmir Life, NewsX, Inshorts, newkerala (Apr–May 2026)",
        "Delhi–Katra Vande Bharat 22439: The Quint, Business Today, EaseMyTrip, FabHotels",
        "Z-Morh tunnel / Sonamarg winter access: Herald Goa, Daily Excelsior, The Tribune, Kashmir Life (Jan 2025)",
        "Reopening of 14 sites incl. Doodhpathri & Yusmarg (16–17 Feb 2026): ETV Bharat, Kashmir Reader, ThePrint, Business Today, India TV",
        "Chandanwari/Aru/Betaab status & Pahalgam union rates: zoutons Pahalgam guide 2026, vargiskhan.com rate lists, charzanholidays",
        "Gulmarg Gondola fares: zoutons Gulmarg guide 2026, travelcoffee.in, kashmirtourbazaar; ski rental rates: cliffhangersindia, theunstumbled, aajtak",
        "Kashmir winter access (Yusmarg/Gurez/Doodhpathri): vargiskhan.com winter guide, travelcoffee.in, charzanholidays",
        "HYD–SXR fares: Skyscanner, MakeMyTrip, HappyFares, Air India Express, Goibibo (Nov 2026)",
    ])
    d.build()

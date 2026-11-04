"""Plan 2: Offbeat Shimla (by toy train) + Manali side: Mashobra, Shali Tibba, Narkanda, Thanedar, Jibhi, Shoja, Tirthan, Naggar, Sethan."""
from common import PlanDoc, totals, k
import sections as X

BUDGET = [
    ("Train Hyderabad → Delhi (12723)", 800, 2100, "SL vs 3A"),
    ("Delhi day (metro, cloak room, entries)", 400, 500, ""),
    ("12311 Kalka Mail, Old Delhi → Kalka", 200, 200, "SL (short overnight run; 3A ≈ +₹400)"),
    ("Toy train Kalka → Shimla", 65, 65, "52453 2S (Shivalik Deluxe CC ≈ ₹510 if you prefer)"),
    ("Shimla → Mashobra taxi + Naldehra", 250, 250, "₹1,500 ÷ 6"),
    ("One Innova, 27 Dec – 1 Jan (6 days + driver nights + tolls)", 5600, 6000, "≈ ₹33.5–36k ÷ 6 (more if Jalori is shut)"),
    ("Manali → Delhi bus", 1000, 1800, "HRTC ordinary vs Volvo"),
    ("Delhi half-day on 2 Jan", 300, 400, ""),
    ("Train Delhi → Hyderabad (12724)", 800, 2100, "SL vs 3A"),
    ("Airbnb/homestays: Mashobra 1N, Narkanda 2N, Jibhi 2N, Sethan 1N (NYE)", 5600, 8000, "Entire homes / 3 rooms ÷ 6"),
    ("Food (homestay dinners ₹300–400)", 5500, 6000, ""),
    ("Serolsar guide, GHNP entry, misc entries", 400, 500, ""),
    ("Winter gear rentals", 800, 1000, ""),
    ("Buffer", 800, 1000, ""),
]


def build(path):
    lo, hi = totals(BUDGET)
    d = PlanDoc(path,
                "Plan 2 · Offbeat Shimla + Manali (toy train)",
                "Toy train to Shimla, then quiet valleys only: Mashobra, Shali Tibba, Narkanda–Hatu, Thanedar–Kotgarh, Jibhi, Chehni Kothi, Shoja, "
                "Jalori/Serolsar, Tirthan, Naggar, Jana, Sethan (NYE). 6 people · one Innova · Airbnb/homestays",
                "#0f766e", "PLAN 2 · OFFBEAT SHIMLA–MANALI")

    d.h1("At a glance")
    d.table([
        ["Route", "Hyderabad → Delhi day → Kalka Mail → <b>toy train</b> → Shimla (lunch) → Mashobra 1N → Narkanda 2N → Jibhi 2N → Tirthan (day) → "
                  "Naggar → Sethan 1N (NYE) → Manali → bus → Delhi → Hyderabad"],
        ["Why offbeat", "You sleep in villages, not Mall Road hotels, and NYE is in a snow village instead of jammed Old Manali. Shimla's Ridge, "
                        "Hadimba and Vashisht are still covered."],
        ["Snow chances", "High: Hatu, Jalori/Serolsar, Sethan, Shali Tibba top. Medium: Narkanda, Shoja. Low–medium: Jibhi, Tirthan"],
        ["Crowd level", "Low almost everywhere"],
        ["Difficulty", "Easy–moderate. Optional snow hikes: Shali Tibba (3 km up), Hatu (if the road is shut), Serolsar (5 km each way)"],
        ["Budget per person (6 people)", f"<b>≈ {k(lo)} shoestring</b> · <b>≈ {k(hi)} recommended</b>"],
        ["Temperatures", "Narkanda −6 to 6 °C · Jibhi −2 to 10 °C · Sethan −10 to 2 °C"],
    ], [0.22, 0.78], header=False, bold_first_col=True)
    d.callout("The one road to watch: Jalori Pass (3,120 m)",
              ["Jalori (Narkanda → Luhri → Ani → Jalori → Shoja → Jibhi, ~110 km, 5 h) usually closes after heavy snow from <b>mid to late December</b> "
               "and reopens in March–April.",
               "<b>Decide on 28 Dec evening</b> (ask your Narkanda host / Ani police). Open → via Jalori. Closed → Narkanda → Shimla bypass → Sundernagar → "
               "Mandi → Aut → Banjar → Jibhi (~260 km, 8–9 h; ≈ ₹2,000 extra on the Innova). Jibhi itself is open year-round via Aut; you can still hike "
               "to Jalori / Serolsar from Shoja."], "warn")

    d.h1("Getting there and back")
    X.onward(d, (1, 2, 3, 4))
    X.kalka_toy_train(d)
    X.returns(d, (1, 2, 4))
    X.vehicles(d)
    d.small("Book <b>one Innova Crysta with the same driver from 27 Dec to 1 Jan</b> (pickup Mashobra, drop Manali). A fixed per-day rate "
            "(≈ ₹4,500–5,500 + ₹400 driver night + tolls/parking) is cheaper than separate point-to-point taxis and keeps the luggage in one place.")

    d.h1("Day-by-day itinerary")
    d.day("Day 1 · Thu 24 Dec", "Hyderabad → on the train", ["<b>06:00 12723 Telangana Express</b> (Secunderabad 06:25, Kazipet 08:05)."],
          stay="Train", cost="₹300 food")
    d.day("Day 2 · Fri 25 Dec", "Delhi sightseeing day → 21:10 Kalka Mail", [
        "Bags at the Old Delhi cloak room → Red Fort → Jama Masjid → Chandni Chowk → India Gate → Agrasen ki Baoli → CP → Sacred Heart (Christmas).",
        "Board <b>12311 Kalka Mail ~21:10</b> from Old Delhi (SL).",
    ], stay="Train", cost="₹700 Delhi + ₹200 train")
    d.day("Day 3 · Sat 26 Dec", "Toy train to Shimla → Mashobra", [
        "Kalka ~03:00–04:40 → <b>52451 Shivalik Deluxe</b> (05:20–05:45) or <b>52453 Express</b> (06:00–06:20, 2S ≈ ₹65) → Shimla ~10:30–11:50.",
        "Quick Ridge + Christ Church + lunch on Mall Road → taxi to <b>Mashobra</b> (12 km) → sunset at <b>Naldehra</b> deodar meadow.",
    ], stay="Airbnb Mashobra", cost="₹65–510 toy train + ₹250 taxi + ₹700 food")
    d.day("Day 4 · Sun 27 Dec", "Shali Tibba trek → Narkanda", [
        "Innova starts. Drive to Khatnol, then <b>Shali Tibba (2,872 m)</b>: 3 km up to the Bhima Kali summit temple, the best panorama near Shimla. "
        "3–4 h return; spikes help in snow.",
        "Drive to <b>Narkanda</b> via Fagu–Theog (~2 h).",
    ], stay="Airbnb Narkanda", cost="₹930 Innova share + ₹700 food")
    d.day("Day 5 · Mon 28 Dec", "Hatu Peak · Tani Jubbar · Thanedar–Kotgarh", [
        "Sunrise at <b>Hatu Peak (3,400 m)</b>: Hatu Mata temple (7 km snow walk if the road is shut). <b>Tani Jubbar lake</b>.",
        "<b>Thanedar &amp; Kotgarh</b>: Stokes' apple orchards, 1843 St Mary's Church, Sutlej views. Evening: decide the Jalori route.",
    ], stay="Airbnb Narkanda", cost="₹930 Innova share + ₹700 food")
    d.day("Day 6 · Tue 29 Dec", "Narkanda → Jibhi", [
        "Route A (Jalori open): Luhri → Ani → <b>Jalori Pass</b> dhabas in snow → Shoja → Jibhi. Route B (closed): via Mandi–Aut, leave by 07:00.",
        "Evening: Jibhi village walk, riverside café.",
    ], stay="Airbnb Jibhi", cost="₹930–1,250 Innova share + ₹700 food")
    d.day("Day 7 · Wed 30 Dec", "Chehni Kothi · Jibhi waterfall · Shoja · Serolsar", [
        "<b>Chehni Kothi</b> tower temple (2 km walk up). <b>Jibhi waterfall</b> and the 'Mini Thailand' pool.",
        "<b>Shoja</b> (2,700 m) → if Jalori is open, hike 5 km to <b>Serolsar lake</b> with a local guide (₹1,500–2,000 per group); if closed, hike "
        "from Shoja as far as it's safe. Cafés close by ~21:00.",
    ], stay="Airbnb Jibhi", cost="₹930 Innova share + ₹300 guide share + ₹700 food")
    d.day("Day 8 · Thu 31 Dec", "Tirthan morning → Naggar → Jana → Sethan (NYE in snow)", [
        "Early to <b>Gushaini (Tirthan)</b>: river walk towards Bandal, trout farms at Nagini, GHNP (UNESCO) gate.",
        "Aut tunnel → Kullu → <b>Naggar Castle</b> + <b>Roerich gallery</b> → lunch at <b>Jana waterfall</b> → up to <b>Sethan (2,700 m)</b>.",
        "NYE bonfire away from the Manali crowd. Upgrade option: one igloo night (₹4,500–7,500 pp with meals).",
    ], stay="Sethan / Prini homestay or chalet", cost="₹930 Innova share + ₹900 food/NYE")
    d.day("Day 9 · Fri 1 Jan", "Sethan snow → Vashisht → Old Manali → bus to Delhi", [
        "Morning snow walk on the Hampta trail head. Down to Manali: <b>Hadimba temple</b>, <b>Vashisht hot springs</b>, Old Manali lunch. Innova drop.",
        "Evening bus to Delhi (16:00–18:00).",
    ], stay="Overnight bus", cost="₹930 Innova share + ₹1,000–1,800 bus + ₹600 food")
    d.day("Day 10 · Sat 2 Jan", "Delhi → train home", ["Humayun's Tomb / Lodhi Garden → <b>16:00 12724 Telangana Express</b>."],
          stay="Train", cost="₹400 Delhi + ₹600 food")
    d.day("Day 11 · Sun 3 Jan", "Home", ["Hyderabad ~17:10."])

    X.airbnb(d, [
        ["1 (26 Dec)", "Mashobra", "<b>Private Sunset Lawn 3BHK family cottage</b>: 4.94★ (17)",
         "<b>Shimla View Homestay, Mashobra</b> (rooms)", (5000, 8000)],
        ["2 (27–28 Dec)", "Narkanda", "<b>Hatu Peak View 3BR Villa | Homeyhuts</b>: 4.8★ (10). Splurge: Villa Vistas (5.0★, 6 reviews)",
         "<b>Wild Orchard Pure Veg Homestay</b> or <b>Pahadi House</b> B&amp;B (3 rooms)", (5000, 8000)],
        ["2 (29–30 Dec)", "Jibhi", "<b>Jalori View Log House, Jibhi</b>: 4.97★ (74); or a Jibhi treehouse at 4.91★ (209) split across 2 units",
         "Two-cottage riverside place in Tirthan (6 guests) · <b>Bini cottage</b> (2 cottages, 6) · <b>Hikers wooden cottage</b>", (5000, 8000)],
        ["1 (31 Dec)", "Sethan / Prini",
         "<b>Woodland Chalet, Sethan</b> (5.0★, new, 3 reviews), or an igloo night", "<b>Private rooms in Hamta village, Prini</b>: 4.85★ (133); book 3 rooms",
         (6000, 9000)],
    ])

    d.h1("Offbeat places in this plan")
    d.table([
        ["Place", "Altitude", "What's special", "Snow late Dec", "Crowd"],
        ["Kalka–Shimla toy train", "656 → 2,076 m", "UNESCO hill railway", "—", "Medium"],
        ["Mashobra / Naldehra", "2,150 m", "Orchard ridge, deodar meadow", "Low–medium", "Low"],
        ["Shali Tibba", "2,872 m", "Summit temple trek", "Medium–high", "Very low"],
        ["Narkanda + Hatu, Tani Jubbar", "2,708 / 3,400 m", "Snow slopes, wooden temple, lake", "High", "Low"],
        ["Thanedar–Kotgarh", "~2,000 m", "Where Himachal's apples began; 1843 church", "Low", "Very low"],
        ["Jalori + Serolsar lake", "3,120 m", "Snow pass, sacred forest lake", "Very high (road may shut)", "Very low"],
        ["Jibhi, Chehni Kothi, Shoja", "1,900–2,700 m", "Wooden villages, tower temple", "Medium", "Low"],
        ["Tirthan / Gushaini", "1,600 m", "Trout river, GHNP edge", "Low–medium", "Very low"],
        ["Naggar, Jana, Sethan", "1,800–2,700 m", "Old capital, village food, igloo village", "Sethan high", "Low"],
    ], [0.24, 0.14, 0.32, 0.16, 0.14])

    d.h1("Bike / scooty rentals")
    d.table([
        ["Where", "Rates", "Notes"],
        ["Jibhi / Banjar", "Scooty ₹700–1,000 (few shops; ask your host)", "Fine for Jibhi–Chehni–Shoja on dry roads. Not on Jalori in snow"],
        ["Manali", "Scooty ₹500–800 · RE ₹1,200–2,500", "Day 9 only if time allows. Sethan road is steep and icy, so use the Innova"],
    ], [0.15, 0.4, 0.45])

    X.gear(d, [
        ["Point", "What you can rent", "Rate"],
        ["Narkanda ski shops / HPTDC", "Ski kit, gumboots, snow suits (when slopes are open)", "₹300–500 suit; ski kit ₹700–1,000"],
        ["Shoja / Jibhi homestays", "Gumboots, sometimes microspikes and poles", "₹100–250"],
        ["Sethan igloo operators", "Snow suits, boots, skis / snowboards", "₹300–600"],
        ["Indiahikes rentals (online)", "Padded jacket, trek shoes, microspikes", "₹55–150/day"],
    ])

    d.h1("Budget per person (6 people sharing)")
    d.budget(BUDGET, "Fits ₹25–30k on SL. One shared Innova is the single biggest saving versus 4 people (≈ ₹2,000 pp less).")

    d.h1("Bookings to do now")
    d.bullets([
        "Return 12724 (2 Jan) → 12723 (24 Dec) → <b>12311 Kalka Mail (25 Dec)</b> → <b>toy train (26 Dec)</b>, 6 on one PNR each.",
        "Sethan for 31 Dec first (fills fastest), then Jibhi, Narkanda, Mashobra.",
        "Fix the Innova (27 Dec–1 Jan) in writing: per-day rate, driver nights, tolls/parking, extra km if you take the Mandi route.",
        "Manali → Delhi bus for 1 Jan.",
    ])
    d.h1("Plan B")
    d.bullets([
        "Jalori shut and you don't want the 8–9 h detour: reverse the loop (Delhi → overnight bus to Aut → Jibhi/Tirthan → Manali/Sethan → Kullu → "
        "Shimla–Narkanda → toy train down to Kalka → Kalka Mail to Delhi).",
        "Heavy snow at Narkanda: sleep in Thanedar (lower) and do Hatu on foot only in clear weather.",
        "Sethan road shut: sleep in Prini/Hamta village and walk up once it's cleared.",
    ])
    X.packing_and_safety(d)
    d.sources([
        "Toy train & Kalka Mail: travelcoffee.in, Shimla Tourism, exploreindia, totaltraininfo, Cleartrip, RailMitra",
        "Jalori seasonal closure & Jibhi access: vargiskhan.com, travelcoffee.in, The Tribune (NH-305), Team-BHP 'Quiet flows Tirthan'",
        "Jibhi/Shoja/Tirthan winter: tourmyholiday 2025, travelcoffee 'Jibhi in December', Asianet Newsable",
        "Airbnb listings (ratings/reviews): airbnb.co.in Mashobra/Narkanda/Jibhi/Tirthan/Sethan/Prini pages via search (Nov 2026)",
        "Innova/Tempo rates: Rajputana Cabs, Triveni Cabs; HRTC Manali–Delhi fares: mytnstc table, EaseMyTrip",
    ])
    d.build()
    return lo, hi

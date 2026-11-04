"""Plan 2: Offbeat Shimla + Manali: Mashobra, Shali Tibba, Narkanda, Thanedar, Jibhi, Shoja, Tirthan, Naggar, Sethan."""
from common import PlanDoc
import sections as X


def build(path):
    d = PlanDoc(path,
                "Plan 2 · Offbeat Shimla + Manali",
                "Same two hubs, but you stay in the quiet valleys: Mashobra, Shali Tibba, Narkanda–Hatu, Thanedar–Kotgarh, "
                "Jibhi, Shoja, Jalori/Serolsar, Tirthan, Naggar, Sethan. 24 Dec 2026 – 3 Jan 2027",
                "#0f766e", "PLAN 2 · OFFBEAT SHIMLA–MANALI")

    d.h1("At a glance")
    d.table([
        ["Route", "Hyderabad → Delhi → Shimla (evening walk) → Mashobra 1N → Narkanda 2N → Jibhi 2N → Tirthan 1N → Sethan 1N (NYE) → "
                  "Manali → Delhi → Hyderabad"],
        ["Why offbeat", "You sleep in villages, not Mall Road hotels. NYE is spent in Sethan (snow village) instead of jammed Old Manali. "
                        "You still see Shimla's Ridge, and Manali's Hadimba/Vashisht on the last day."],
        ["Snow chances", "High: Hatu, Jalori/Serolsar, Sethan. Medium: Narkanda, Shoja. Low–medium: Jibhi, Tirthan (snow in some years after mid-Dec)"],
        ["Crowd level", "Low almost everywhere; medium only at Shimla Mall on 25 Dec and Manali on 1 Jan"],
        ["Difficulty", "Easy–moderate. Optional snow hikes: Shali Tibba (3 km), Hatu (if road closed), Serolsar (5 km each way)"],
        ["Budget (per person)", "≈ ₹25.4k shoestring · ≈ ₹31.2k recommended (group of 4). ≈ ₹29k with 6 people sharing a Tempo Traveller"],
        ["Temperatures", "Narkanda −6 to 6 °C · Jibhi −2 to 10 °C · Sethan −10 to 2 °C"],
    ], [0.22, 0.78], header=False, bold_first_col=True)

    d.callout("The one road to watch: Jalori Pass (3,120 m)",
              ["Jalori is the short link from Narkanda to Jibhi (via Luhri–Ani–Jalori–Shoja, ~110 km, 5 h). It usually closes to vehicles after "
               "heavy snow from <b>mid to late December</b> and reopens in March–April. Travel blogs say the Jalori route is not reliable in December.",
               "<b>Decision on 27 Dec evening</b> (ask your Narkanda host / Ani police): open → go via Jalori (best views). Closed → go "
               "Narkanda → Shimla → Sundernagar → Mandi → Aut → Banjar → Jibhi (~260 km, 8–9 h). Jibhi itself is reachable year-round via Aut; "
               "only the section above Shoja shuts. You can still hike to Jalori / Serolsar from Shoja in snow."], "warn")

    d.h1("Getting there and back")
    X.delhi_trains(d, onward_idx=(2, 1, 4, 7))
    d.h2("Hill transfers")
    d.table([
        ["Leg", "How", "Time", "Approx cost"],
        ["Delhi → Shimla", "HRTC Volvo, ISBT Kashmere Gate (06:45 / 08:00 if on Rajdhani; 09:25 / 11:55 if on Telangana)", "8–9.5 h", "₹980–1,100 pp"],
        ["Shimla → Mashobra", "Local taxi (12 km)", "40 min", "₹600–800 per car"],
        ["Mashobra → Shali Tibba (Khatnol) → Narkanda", "Day taxi", "4–5 h with trek", "₹3,500–4,000 per car"],
        ["Narkanda → Jibhi", "Taxi via Jalori (if open) or via Mandi–Aut", "5 h / 8–9 h", "₹6,000–7,000 / ₹8,000–9,500 per car"],
        ["Jibhi ↔ Shoja ↔ Jalori, Jibhi → Gushaini", "Local taxi / HRTC Banjar–Shoja bus (₹30–60)", "30–60 min", "₹1,500–2,500 per car per day"],
        ["Gushaini → Aut → Naggar → Sethan", "Taxi via Aut tunnel and Kullu", "4.5–5 h", "₹5,000–5,500 per car"],
        ["Manali → Delhi", "HRTC / private Volvo (16:00–18:00 dep)", "12–14 h", "₹1,600–2,000 pp"],
    ], [0.27, 0.43, 0.12, 0.18])
    d.small("Public-transport option for Jibhi: overnight Volvo Delhi → Aut (from ~₹660, last bus ~23:35), then a local bus to Banjar (~₹40) and Jibhi "
            "(~₹20). Useful if you do Jibhi before Narkanda (reverse loop).")
    X.flights(d, (1, 2))

    d.h1("Day-by-day itinerary")
    d.day("Day 1 · Thu 24 Dec", "Hyderabad → on the train", [
        "<b>Best: 07:10 22691 Rajdhani</b> from Secunderabad → Nizamuddin 05:30 (25 Dec). Gets you on the early Shimla Volvo.",
        "Else <b>06:00 12723 Telangana Express</b> (Hyderabad Deccan) → New Delhi ~07:40.",
    ], stay="Train", cost="₹300 food (Rajdhani includes meals)")
    d.day("Day 2 · Fri 25 Dec", "Delhi → Shimla → Mashobra", [
        "Volvo to Shimla. If you arrive by 15:00–16:00, walk the Ridge and Christ Church for Christmas, then taxi to <b>Mashobra</b> (12 km, 2,150 m).",
        "If you arrive late, sleep in Shimla and move to Mashobra in the morning.",
    ], stay="Mashobra homestay / cottage (₹1,800–3,000 per room)", cost="₹1,000 bus + ₹200 taxi share + ₹600 food")
    d.day("Day 3 · Sat 26 Dec", "Shali Tibba trek → Narkanda", [
        "<b>Shali Tibba (2,872 m)</b>, offbeat: drive to Khatnol village, 3 km uphill trail to the Bhima Kali temple on the summit. "
        "360° view of Shimla hills and the Pir Panjal. 3–4 h return. Snow likely on top late Dec, so spikes help.",
        "Optional quick stop: <b>Naldehra</b> deodar meadow (golf course) near Mashobra.",
        "Drive on to <b>Narkanda</b> via Kufri–Fagu–Theog (~2 h).",
    ], stay="Narkanda homestay / HPTDC Hatu (₹1,800–2,800 per room)", cost="₹900 taxi share + ₹700 food")
    d.day("Day 4 · Sun 27 Dec", "Hatu Peak · Tani Jubbar · Thanedar–Kotgarh", [
        "Sunrise drive/hike to <b>Hatu Peak (3,400 m)</b>: Hatu Mata temple and Bhim's chulha rocks. If snow blocks the road, it's a 7 km snow walk up.",
        "<b>Tani Jubbar lake</b>: quiet forest lake.",
        "Afternoon: <b>Thanedar &amp; Kotgarh</b> (offbeat apple country, 17 km): Samuel Stokes' orchards, the 1843 St Mary's Church at Kotgarh, "
        "Sutlej valley views.",
        "Evening: confirm the Jalori status (box above) and fix tomorrow's taxi.",
    ], stay="Narkanda", cost="₹750 taxi share + ₹700 food")
    d.day("Day 5 · Mon 28 Dec", "Narkanda → Jibhi", [
        "Route A (Jalori open): Narkanda → Luhri (Sutlej) → Ani → <b>Jalori Pass</b> (stop at the dhabas, snow) → Shoja → Jibhi.",
        "Route B (Jalori closed): via Shimla bypass → Sundernagar → Mandi → Aut tunnel → Banjar → Jibhi. Leave by 07:00.",
        "Evening: Jibhi village walk and riverside café.",
    ], stay="Jibhi treehouse / riverside homestay (₹1,500–2,500 per room, meals ₹300–400)", cost="₹1,750–2,375 taxi share + ₹700 food")
    d.day("Day 6 · Tue 29 Dec", "Jibhi · Chehni Kothi · Shoja · Serolsar", [
        "<b>Chehni Kothi</b>: centuries-old ~15-storey stone-and-wood tower temple. 2 km walk up from Bahu/Chehni village.",
        "<b>Jibhi waterfall</b> and the 'Mini Thailand' rock pool on the Pushpabhadra river.",
        "<b>Shoja</b> (2,700 m): viewpoint and waterfall. If Jalori is open, drive up and hike 5 km to <b>Serolsar lake</b> (Budhi Nagin temple) "
        "through oak forest, with a local guide (₹1,500–2,000 per group). If it's closed, hike from Shoja towards Jalori as far as is safe.",
        "Cafés in Shoja/Jibhi close early (by ~21:00) in winter.",
    ], stay="Jibhi", cost="₹600 taxi share + ₹400 guide share + ₹700 food")
    d.day("Day 7 · Wed 30 Dec", "Tirthan valley (Great Himalayan National Park)", [
        "Short move to <b>Gushaini</b> (Tirthan valley, ~35 km).",
        "Walk the river trail to <b>Bandal</b> village, see the trout farms at Nagini, and visit the GHNP (UNESCO site) entry/interpretation area. "
        "Winter treks inside the park need a permit and guide, so keep it to day walks.",
        "Evening by the Tirthan river (trout dinner if you eat fish).",
    ], stay="Tirthan riverside homestay (₹1,500–2,500 per room)", cost="₹375 taxi share + ₹800 food")
    d.day("Day 8 · Thu 31 Dec", "Tirthan → Naggar → Jana → Sethan (quiet NYE in snow)", [
        "Drive via Aut tunnel → Kullu → left bank road to <b>Naggar Castle</b> + <b>Roerich Art Gallery</b>.",
        "Lunch at <b>Jana waterfall</b> village dhabas.",
        "Up to <b>Sethan (2,700 m)</b> above Prini: snow village with igloo cafés, bonfire NYE away from the Manali crowd.",
        "Upgrade option: a night in an igloo stay (₹4,500–7,500 pp with meals). Otherwise a homestay, and visit the igloos in the day.",
    ], stay="Sethan homestay (₹2,000–3,000 per room incl. dinner)", cost="₹1,375 taxi share + ₹800 food")
    d.day("Day 9 · Fri 1 Jan", "Sethan snow morning → Vashisht → Old Manali → Volvo to Delhi", [
        "Morning snow walk on the Hampta trail head (no crowd, great light).",
        "Down to Manali: <b>Hadimba temple</b>, <b>Vashisht hot springs</b>, Old Manali lunch.",
        "Evening HRTC/private Volvo to Delhi (book ahead; 16:00–18:00 departure).",
    ], stay="Overnight Volvo", cost="₹300 taxi share + ₹1,800 Volvo + ₹600 food")
    d.day("Day 10 · Sat 2 Jan", "Delhi → train home", [
        "Arrive Delhi 06:00–08:00. Day room in Paharganj (shared) or the station waiting lounge.",
        "<b>16:00 12724 Telangana Express</b> (or 22692 Rajdhani from Nizamuddin in the late evening).",
    ], stay="Train", cost="₹300 room share + ₹600 food")
    d.day("Day 11 · Sun 3 Jan", "Home", ["Hyderabad ~17:10."])

    d.h1("Offbeat places in this plan")
    d.table([
        ["Place", "Altitude", "What's special", "Snow chance late Dec", "Crowd"],
        ["Mashobra / Naldehra", "2,150 m", "Apple-orchard ridge and deodar meadows next to Shimla", "Low–medium", "Low"],
        ["Shali Tibba", "2,872 m", "Summit temple trek, best panorama near Shimla", "Medium–high", "Very low"],
        ["Narkanda + Hatu Peak", "2,708 / 3,400 m", "Snow slopes, Hatu Mata temple", "High", "Low"],
        ["Thanedar–Kotgarh", "~2,000 m", "Where Himachal's apples began; 1843 church", "Low", "Very low"],
        ["Jalori Pass + Serolsar lake", "3,120 m", "Snow pass and sacred forest lake", "Very high (road may close)", "Very low"],
        ["Jibhi, Chehni Kothi, Shoja", "1,900–2,700 m", "Wooden villages, tower temple, treehouses", "Medium (Shoja higher)", "Low"],
        ["Tirthan / Gushaini / Bandal", "1,600 m", "Trout river, GHNP edge", "Low–medium", "Very low"],
        ["Naggar, Jana waterfall", "1,800–2,300 m", "Old Kullu capital, village food", "Low–medium", "Low"],
        ["Sethan", "2,700 m", "Igloo village, Hampta trail head", "High", "Low"],
    ], [0.24, 0.12, 0.34, 0.16, 0.14])
    d.small("Main sights still covered: Shimla Ridge/Christ Church/Mall (Day 2), Kufri (passing through), Hadimba, Vashisht, Old Manali (Day 9).")

    d.h1("Bike / scooty rentals")
    d.table([
        ["Where", "Rates", "Notes"],
        ["Shimla", "Scooty ₹500–800 · 150–200 cc ₹900–1,500", "Good for Mashobra–Naldehra on a dry day; not for Narkanda in snow"],
        ["Jibhi / Banjar", "Scooty ₹700–1,000 (few shops; ask your homestay)", "Useful for Jibhi–Chehni–Shoja on dry roads. Jalori road in snow: no"],
        ["Manali", "Scooty ₹500–800 · RE ₹1,200–2,500", "Day 9 only; Sethan road is steep and icy, so take a taxi"],
    ], [0.15, 0.4, 0.45])

    X.gear(d, [
        ["Point", "What you can rent", "Rate"],
        ["Narkanda (ski shops / HPTDC)", "Ski kit, gumboots, snow suits (when slopes are open)", "₹300–500 suit; ski kit ₹700–1,000"],
        ["Shoja / Jibhi homestays", "Gumboots, sometimes microspikes and poles for the Serolsar hike", "₹100–250"],
        ["Sethan (igloo operators)", "Snow suits, boots, skis/snowboards", "₹300–600"],
        ["Indiahikes rentals (online)", "Padded jacket, trek shoes, microspikes", "₹55–150/day"],
    ])

    d.h1("Budget (per person, 4 people)")
    d.budget([
        ("Train Hyderabad → Delhi", 800, 2100, "SL vs 3A Telangana (Rajdhani 3A adds ≈ ₹1,200)"),
        ("Train Delhi → Hyderabad", 800, 2100, "SL vs 3A Telangana"),
        ("Delhi → Shimla HRTC Volvo", 1000, 1000, ""),
        ("Manali → Delhi Volvo", 1600, 1800, ""),
        ("Taxis: Shimla–Mashobra–Shali Tibba–Narkanda, Hatu/Thanedar day", 1850, 1850, "≈ ₹7.4k ÷ 4"),
        ("Taxi Narkanda → Jibhi", 1750, 2375, "Via Jalori vs via Mandi"),
        ("Taxis Jibhi/Shoja day, Jibhi → Tirthan", 975, 975, ""),
        ("Taxi Tirthan → Naggar → Jana → Sethan, Sethan → Manali", 1675, 1675, ""),
        ("Metro, local buses", 400, 400, ""),
        ("Stays: Mashobra, Narkanda ×2, Jibhi ×2, Tirthan, Sethan (NYE)", 6200, 7700, "Homestays, 2 per room"),
        ("Food, 10 days", 6000, 6500, "Homestay meals ₹300–400"),
        ("Guide for Serolsar / entries", 500, 700, ""),
        ("Winter gear rentals", 800, 1000, ""),
        ("Buffer", 1000, 1000, ""),
    ], "Slightly above ₹30k in 3A because of the private taxis. With 6 people in one Tempo Traveller the taxi share falls by about a third (≈ ₹29k).")

    d.h1("Bookings to do now")
    d.bullets([
        "Return train for 2 Jan (opened 3 Nov), then the onward train for 24 Dec (22691 Rajdhani first, then 12723).",
        "HRTC Volvo Delhi → Shimla (25 Dec) and Manali → Delhi (1 Jan).",
        "Homestays: Sethan for NYE (fills first), Jibhi (treehouses fill by mid-Dec), Narkanda. Most homestays take UPI advances and are flexible on dates.",
        "Save the Narkanda/Jibhi taxi number. One driver for Days 3–5 often gives a better package (~₹3,500–4,000 per day + ₹300 night halt).",
    ])
    d.h1("Plan B")
    d.bullets([
        "Jalori closed and you don't want the 8–9 h detour: do the loop in reverse. Delhi → overnight Volvo to Aut → Jibhi/Tirthan first → "
        "Manali/Sethan → Kullu → Shimla–Narkanda at the end → Delhi.",
        "Heavy snow at Narkanda/Hatu: stay in Thanedar (lower) and do Hatu on foot only in clear weather.",
        "Sethan road closed by fresh snow: stay in Prini/Hampta village or Old Manali and walk up when it's cleared.",
    ])
    X.packing_and_safety(d)
    d.sources([
        "Jalori Pass seasonal closure and Jibhi access: vargiskhan.com Jalori guide, travelcoffee.in, The Tribune (NH-305 snow closures), Team-BHP 'Quiet flows Tirthan' travelogue",
        "Jibhi/Shoja/Tirthan winter conditions: tourmyholiday 2025 winter guide, travelcoffee.in 'Jibhi in December', Asianet Newsable winter guide",
        "Narkanda as a quiet snow alternative: indianholiday.com December guide, viacation.com",
        "Delhi–Aut bus and local Jibhi links: trekgo 'Jibhi by public bus', ixigo/abhibus Delhi–Aut listings",
        "Jibhi homestay rate ranges: Booking.com/Hotels.com Jibhi listings (Nov 2026 snapshots)",
        "Trains, HRTC and flights: same sources as the Overview PDF",
    ])
    d.build()

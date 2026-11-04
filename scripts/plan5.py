"""Plan 5: Uttarakhand: Rishikesh, Devprayag, Sari–Deoria Tal, Chopta–Tungnath–Chandrashila, Joshimath–Auli, Haridwar."""
from common import PlanDoc
import sections as X


def build(path):
    d = PlanDoc(path,
                "Plan 5 · Uttarakhand: Rishikesh to Chandrashila &amp; Auli",
                "Ganga aarti and cafés in Rishikesh, Devprayag confluence, Deoria Tal, a snow trek to Tungnath &amp; Chandrashila (4,000 m), "
                "Auli's slopes and Gorson Bugyal, Haridwar. 24 Dec 2026 – 3 Jan 2027",
                "#be123c", "PLAN 5 · UTTARAKHAND")

    d.h1("At a glance")
    d.table([
        ["Route", "Hyderabad → Delhi → Rishikesh 2N → Devprayag → Sari 1N → Chopta/Duggalbitta 2N → Joshimath 2N (Auli) → Haridwar → "
                  "Delhi → Hyderabad"],
        ["Snow chances", "High: Tungnath–Chandrashila, Auli, Gorson. Medium: Deoria Tal, Chopta. None: Rishikesh, Haridwar"],
        ["Crowd level", "Medium in Rishikesh. Low–medium at Chopta (weekend trekkers). Low at Auli (ropeway shut) and Deoria Tal"],
        ["Difficulty", "Moderate. Chandrashila in snow is a 6–8 h day (about 10 km round trip from Chopta) and needs microspikes and a guide"],
        ["Temperatures", "Rishikesh 7–20 °C · Sari 0–12 °C · Chopta −8 to 3 °C · Auli/Joshimath −6 to 8 °C"],
        ["Budget (per person, 4 people)", "≈ ₹20.1k shoestring (buses + shared jeeps) · ≈ ₹30.3k recommended (one cab for 6 days)"],
    ], [0.22, 0.78], header=False, bold_first_col=True)
    d.callout("Things that changed recently",
              ["<b>Joshimath–Auli ropeway is shut</b> (since Jan 2023 land subsidence). A new line is only at project-report stage. Auli is reached by "
               "road (16 km from Joshimath; local jeeps run). Don't pay any 'ropeway ticket' website.",
               "<b>Tungnath temple doors are closed in winter</b> (the deity moves to Makkumath). The trek is open and snow-covered. In winter, stays "
               "beyond Duggalbitta are closed and there is no electricity at the higher points.",
               "Rishikesh's old <b>Laxman Jhula</b> bridge has been closed for safety since 2022; use Ram Jhula / Janki Setu."], "warn")

    d.h1("Getting there and back")
    X.delhi_trains(d)
    d.h2("Delhi ↔ Rishikesh / Haridwar and the hill loop")
    d.table([
        ["Leg", "Option", "Time", "Approx cost"],
        ["Delhi → Rishikesh (25 Dec)", "UTC / private Volvo from ISBT Kashmere Gate (frequent through the day)", "6–7 h", "₹500–900 pp"],
        ["Alt: Delhi → Dehradun / Haridwar by train", "Delhi–Dehradun Vande Bharat / Shatabdi / Jan Shatabdi (VB CC ≈ ₹1,065 at launch; the morning Shatabdi leaves too early "
         "for a 07:40 arrival). Check IRCTC for 25 Dec afternoon chair cars", "4.5–5 h", "₹600–1,100"],
        ["Rishikesh → Ukhimath (budget)", "GMOU / Uttarakhand Roadways bus from Rishikesh bus stand ~05:00–07:00, then shared jeep to Sari", "8–9 h", "≈ ₹400–500"],
        ["Hill loop by cab (recommended)", "Dzire/Ertiga/Bolero with driver 27 Dec – 1 Jan: Rishikesh → Sari → Chopta → Joshimath/Auli → Haridwar", "6 days",
         "≈ ₹3,500–4,000/day + ₹300 driver night + tolls ≈ ₹24–25k per car"],
        ["Haridwar → Delhi (1 Jan night)", "Overnight train (e.g. Mussoorie Exp-type departures ~22:00–23:30; verify) or UTC Volvo", "6–7 h", "₹450–800"],
    ], [0.22, 0.46, 0.12, 0.2])
    X.flights(d, (1, 5))
    d.callout("Faster by air",
              "Fly Hyderabad → Dehradun (IndiGo direct, about 10 flights a week; ₹5–9k) on 24 Dec and taxi to Rishikesh (~1 h). You gain a full day: "
              "add Kunjapuri sunrise + Neer Garh falls, or a night in Khirsu/Lansdowne (offbeat) on the way back.")

    d.h1("Day-by-day itinerary")
    d.day("Day 1 · Thu 24 Dec", "Hyderabad → on the train", [
        "<b>06:00 12723 Telangana Express</b> (or 07:10 22691 Rajdhani from Secunderabad).",
    ], stay="Train", cost="₹300 food")
    d.day("Day 2 · Fri 25 Dec", "Delhi → Rishikesh · Ganga aarti", [
        "Metro to Kashmere Gate → Volvo to Rishikesh (~09:00 → ~16:00).",
        "Evening <b>Triveni Ghat</b> or <b>Parmarth Niketan</b> Ganga aarti (around sunset, ~17:30 in winter).",
    ], stay="Tapovan / Laxman Jhula-side hostel (dorm ₹400–800) or guesthouse (₹1,200–2,000 per room)", cost="₹700 bus + ₹600 food")
    d.day("Day 3 · Sat 26 Dec", "Rishikesh by scooty", [
        "Rent a scooty (₹500–700 + ₹1,500 deposit). <b>Beatles Ashram (Chaurasi Kutia)</b>, Ram Jhula, Janki Setu, Parmarth & Swarg Ashram ghats.",
        "<b>Neer Garh waterfall</b> (short trek, offbeat-ish). Optional river rafting from Shivpuri (16 km, ₹600–1,000). The water is cold but rafts do run.",
        "Cafés on the Tapovan side, sunset at Beatles Ashram.",
    ], stay="Rishikesh", cost="₹350 scooty share + ₹200 fuel + ₹700 rafting (optional) + ₹600 food")
    d.day("Day 4 · Sun 27 Dec", "Rishikesh → Devprayag → Rudraprayag → Sari", [
        "Leave 06:30. <b>Devprayag</b>: Alaknanda meets Bhagirathi and the Ganga begins. Short walk down to the sangam.",
        "Optional quick stops: Dhari Devi temple (Srinagar Garhwal), Rudraprayag confluence. Then Ukhimath → <b>Sari village</b> (~2,000 m), 7–8 h total.",
    ], stay="Sari homestay (₹1,000–1,800 per room, meals ₹250–350)", cost="₹1,035 cab share + ₹600 food")
    d.day("Day 5 · Mon 28 Dec", "Deoria Tal → Chopta / Duggalbitta", [
        "Early trek to <b>Deoria Tal</b> (2.5–3 km, 1.5 h up): mirror view of Chaukhamba. Ice on the edges in late Dec. Small entry/eco fee.",
        "Descend, drive to <b>Duggalbitta / Chopta</b> (25 km). Rent microspikes + gaiters for tomorrow (₹150–250/day).",
        "Book your Tungnath guide tonight (₹1,500–2,000 per group).",
    ], stay="Duggalbitta camp / lodge with meals (₹1,000–1,500 pp)", cost="₹1,035 cab share + ₹250 rentals")
    d.day("Day 6 · Tue 29 Dec", "Tungnath (3,680 m) + Chandrashila summit (4,000 m) in snow", [
        "Start 06:30 from Chopta. 3.5 km to <b>Tungnath</b> (world's highest Shiva temple; doors shut in winter) + 1.5 km steep to <b>Chandrashila</b>: "
        "360° view of Nanda Devi, Trishul, Chaukhamba, Kedar peaks.",
        "Turn-around time 12:30 whatever happens. Back by 15:00–16:00. Hot Maggi + chai at Chopta.",
    ], stay="Duggalbitta (or drop to Ukhimath)", cost="₹450 guide share + ₹1,200 camp + ₹300 food")
    d.day("Day 7 · Wed 30 Dec", "Ukhimath → the five prayags → Joshimath", [
        "<b>Omkareshwar temple, Ukhimath</b>, the winter seat of Kedarnath (puja happens here in winter).",
        "Drive via Rudraprayag → Karnaprayag → Nandprayag → Chamoli → <b>Joshimath</b> (6–7 h). If the Chopta–Mandal–Gopeshwar road is open, it's shorter.",
        "Evening: Narsingh temple (winter seat of Badrinath).",
    ], stay="Joshimath budget hotel (₹1,500–2,500 per room)", cost="₹1,035 cab share + ₹700 food")
    d.day("Day 8 · Thu 31 Dec", "Auli snow day + Gorson Bugyal · quiet NYE", [
        "Drive up to <b>Auli</b> (16 km). Snow slopes, the GMVN ski area (beginner lessons + gear ≈ ₹1,500–2,500/day in season), Auli artificial lake.",
        "<b>Gorson Bugyal</b> (offbeat): 3 km snow walk through oak and rhododendron to a meadow facing Nanda Devi.",
        "NYE in Joshimath/Auli is low-key: bonfire and dinner at the hotel.",
    ], stay="Joshimath (or Auli GMVN/resorts, ₹3,000+ per room)", cost="₹1,035 cab share + ₹300–800 snow activities + ₹800 food")
    d.day("Day 9 · Fri 1 Jan", "Joshimath → Haridwar (Har Ki Pauri) → night to Delhi", [
        "Leave by 07:00 (~255 km, 8–9 h). If you reach by 17:30, catch the <b>Har Ki Pauri</b> evening aarti in Haridwar.",
        "Overnight train / Volvo Haridwar → Delhi.",
    ], stay="Train / bus", cost="₹1,035 cab share + ₹700 train/bus + ₹600 food")
    d.day("Day 10 · Sat 2 Jan", "Delhi → Hyderabad", ["<b>16:00 12724 Telangana Express</b> (or 22692 Rajdhani late evening)."], stay="Train", cost="₹300 room share + ₹600 food")
    d.day("Day 11 · Sun 3 Jan", "Home", ["Hyderabad ~17:10."])

    d.h1("Places: main vs offbeat")
    d.table([
        ["Place", "Type", "Why"],
        ["Rishikesh (ghats, aarti, Beatles Ashram)", "Main", "Yoga capital, Ganga, cafés"],
        ["Neer Garh falls, Kunjapuri (sunrise)", "Offbeat", "Short hikes near Rishikesh"],
        ["Devprayag sangam", "Semi-offbeat", "Where the Ganga officially begins"],
        ["Sari village + Deoria Tal", "Offbeat", "Village homestay, mirror lake"],
        ["Chopta, Tungnath, Chandrashila", "Main (trekkers)", "Snow trek to 4,000 m with a giant Himalayan panorama"],
        ["Omkareshwar (Ukhimath), Narsingh (Joshimath)", "Offbeat", "Winter seats of Kedarnath and Badrinath"],
        ["Auli slopes", "Main", "India's best-known ski slopes"],
        ["Gorson Bugyal", "Offbeat", "Snow meadow above Auli, few people"],
        ["Haridwar Har Ki Pauri", "Main", "Evening aarti"],
    ], [0.42, 0.18, 0.4])

    d.h1("Variants if you prefer")
    d.table([
        ["Variant", "What changes", "Cost impact"],
        ["<b>Kedarkantha winter trek</b> (classic Dec snow trek, summit ~3,800 m)", "Fly HYD → Dehradun 24 Dec; operator pickup Dehradun 25/26 Dec → "
         "Sankri → 6D/5N trek → Dehradun 31 Dec/1 Jan; train/flight back", "Trek ₹6,000–11,000 (Sankri–Sankri to Dehradun–Dehradun; "
         "+5% GST; forest fee ₹150–300). Total ≈ ₹28–34k with one flight"],
        ["<b>Kumaon</b>: Nainital (main) + Mukteshwar + Binsar / Munsiyari (offbeat)", "Delhi → Kathgodam train; Munsiyari is 10–11 h further "
         "and gets snow from late Dec", "Similar to this plan; more driving"],
        ["<b>Easy hills</b>: Mussoorie–Landour–Dhanaulti–Kanatal", "Base in Mussoorie/Landour, day trips; no trekking", "≈ ₹24–28k"],
    ], [0.3, 0.42, 0.28])

    d.h1("Bike / scooty rentals")
    d.table([
        ["Where", "Rates", "Notes"],
        ["Rishikesh (Tapovan, Laxman Jhula road)", "Scooty ₹500–700 · RE ₹1,750–1,900", "Deposit ≈ ₹1,500. Many shops restrict use to Rishikesh limits"],
        ["Dehradun (app rentals)", "RE / bikes ₹1,200–2,000", "Outstation allowed by some, but snow and ice above 2,500 m (Chopta, Auli) make it unsafe in late Dec"],
        ["Joshimath", "Few shops; ₹800–1,500", "Use local jeeps for Auli after snowfall"],
    ], [0.27, 0.28, 0.45])

    X.gear(d, [
        ["Point", "What you can rent", "Rate"],
        ["Sari / Chopta / Duggalbitta shops", "Microspikes, gaiters, trekking poles, gumboots, jackets", "₹100–250 per item/day"],
        ["Auli (GMVN & private ski shops)", "Skis, boots, poles, suits; lessons", "₹1,500–2,500 per day with instruction"],
        ["Decathlon Dehradun (buy)", "Thermals, fleeces, trek shoes, spikes", "Cheaper than buying in the hills"],
        ["Trek operators (Indiahikes, Trek The Himalayas rentals)", "Padded jacket, shoes", "₹55–150/day"],
    ])

    d.h1("Budget (per person, 4 people)")
    d.budget([
        ("Train Hyderabad → Delhi", 800, 2100, "SL vs 3A"),
        ("Train Delhi → Hyderabad", 800, 2100, ""),
        ("Delhi → Rishikesh bus", 500, 800, "Ordinary vs Volvo"),
        ("Haridwar → Delhi overnight", 450, 700, ""),
        ("Hill loop transport 27 Dec – 1 Jan", 3500, 6200, "Buses + shared jeeps vs one cab ≈ ₹24.8k ÷ 4"),
        ("Rishikesh scooty + fuel", 300, 350, ""),
        ("Rafting (optional)", 0, 700, ""),
        ("Guide for Tungnath–Chandrashila", 450, 450, "≈ ₹1,800 ÷ 4"),
        ("Microspikes, gaiters", 300, 300, ""),
        ("Auli snow activities", 300, 800, ""),
        ("Stays: 2N Rishikesh, 1N Sari, 2N Duggalbitta, 2N Joshimath", 5600, 7700, "Dorms/camps vs rooms (camps include meals)"),
        ("Food", 5000, 5500, ""),
        ("Metro, autos, misc", 400, 500, ""),
        ("Delhi day room (2 Jan)", 300, 300, ""),
        ("Gear rentals (jackets etc.)", 600, 800, ""),
        ("Buffer", 800, 1000, ""),
    ], "Fits the ₹25–30k range comfortably. The cheapest of the five if you use buses.")

    d.h1("Bookings to do now")
    d.bullets([
        "Return train 2 Jan + Haridwar→Delhi on 1 Jan night, then the onward train for 24 Dec.",
        "Cab for 27 Dec – 1 Jan from a Rishikesh agency (fix the per-day rate, night halts, and who pays tolls/parking in writing).",
        "Duggalbitta camp (2 nights) and Joshimath hotel (30–31 Dec). Rishikesh hostels can be booked a week before.",
    ])
    d.h1("Plan B")
    d.bullets([
        "Heavy snow closes Chopta road: stay at Ukhimath/Sari and do Deoria Tal + Kartik Swami (offbeat summit temple, 3 km trek) instead.",
        "Joshimath–Auli road blocked: Gorson/Auli on foot only if police allow; else go to Khirsu or Lansdowne on the way back.",
        "Fog delays the train into Delhi on 25 Dec: take a later Volvo, or the overnight Volvo and sleep on the bus.",
    ])
    X.packing_and_safety(d, [
        "Chandrashila: don't go without a guide after fresh snow (hidden trail edges). Start early, turn back by 12:30, carry a head-torch.",
    ])
    d.sources([
        "Auli ropeway closure since 2023 and DPR status: happyfares Auli guide (Oct 2026), discoverwithdheeraj, Pioneer Edge, The Week",
        "Chopta–Tungnath–Chandrashila winter conditions & package costs: Indiahikes Chopta guide, Trek The Himalayas, himalayashelter, trekupindia, tourmyholiday",
        "Kedarkantha 2026 prices: Adventure Club Pune, Trek The Himalayas, Trek Hievers, Himalayan Hikers, TrekGo cost guide (Aug 2026), discoverwithdheeraj",
        "Uttarakhand offbeat winter (Munsiyari, Chakrata, Khirsu, Harsil, Kanatal): explurger, Outlook Traveller, StayVista, India TV (Dec 2025)",
        "Delhi–Dehradun Vande Bharat fares/timings: WION, Zee News, NativePlanet (launch 2023; verify current)",
        "Rishikesh rentals: Thrillophilia, Onn Bikes tariff; Dehradun/hill rentals: bikewalebhaiya",
        "HYD–DED flights: flightconnections, Skyscanner, HappyFares, tourmyindia (IndiGo direct)",
    ])
    d.build()

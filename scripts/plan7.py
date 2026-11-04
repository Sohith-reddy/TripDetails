"""Plan 7 (new): Kinnaur winter by toy train: Shimla, Narkanda, Sarahan, Sangla, Kalpa, Nako, 6 people."""
from common import PlanDoc, totals, k
import sections as X

BUDGET = [
    ("Train Hyderabad → Delhi (12723)", 800, 2100, "SL vs 3A"),
    ("Delhi day (25 Dec)", 400, 500, ""),
    ("12311 Kalka Mail, Old Delhi → Kalka", 200, 200, "SL (short overnight run; 3A ≈ +₹400)"),
    ("Toy train Kalka → Shimla", 65, 65, "52453 2S"),
    ("Innova 26–31 Dec (6 days, Kinnaur winter rates, driver nights, tolls)", 6000, 6300, "≈ ₹36–38k ÷ 6"),
    ("Shimla local on 1 Jan + toy train Shimla → Kalka", 300, 400, "52454 2S (52452 Shivalik Deluxe CC ≈ ₹510)"),
    ("Kalka → Delhi overnight (12312 Kalka Mail)", 200, 200, "SL (short overnight run; 3A ≈ +₹400)"),
    ("Delhi day (2 Jan)", 300, 400, ""),
    ("Train Delhi → Hyderabad (12724)", 800, 2100, "SL vs 3A"),
    ("Stays: Narkanda, Sarahan, Sangla, Kalpa ×2, Shimla (NYE)", 5400, 7800, "Homestays / HPTDC / Airbnb ÷ 6"),
    ("Food", 5000, 5500, ""),
    ("Entries, misc", 300, 500, ""),
    ("Winter gear rentals", 800, 1000, ""),
    ("Buffer", 800, 1000, ""),
]


def build(path):
    lo, hi = totals(BUDGET)
    d = PlanDoc(path,
                "Plan 7 · Kinnaur in Winter (by toy train)",
                "Toy train up to Shimla, then the Sutlej road into Kinnaur: Narkanda–Hatu, Sarahan's Bhimakali temple, Sangla and Kamru fort, "
                "Kalpa facing Kinnaur Kailash, Nako's frozen lake, then NYE back on Shimla's Ridge and the toy train down. 6 people",
                "#0369a1", "PLAN 7 · KINNAUR WINTER")

    d.h1("At a glance")
    d.table([
        ["Route", "Hyderabad → Delhi day → Kalka Mail → <b>toy train</b> → Shimla → Narkanda 1N → Sarahan 1N → Sangla 1N → Kalpa 2N (Nako day) → "
                  "Shimla 1N (NYE) → <b>toy train</b> down → Kalka Mail → Delhi → Hyderabad"],
        ["Why Kinnaur", "The most dramatic snow scenery you can reach by road in late December without a flight. The Shimla–Reckong Peo road (NH-5) "
                        "is kept open in winter. Very few tourists. It's the lower half of the Spiti winter road, which itself doesn't fit 10 days."],
        ["Snow chances", "Very high: Kalpa, Nako, Sangla. High: Hatu, Sarahan. Chitkul is usually cut off after mid-December"],
        ["Crowd level", "Very low (except Shimla Ridge on NYE)"],
        ["Difficulty", "Easy walking, but long mountain drives (5–8 h/day), black ice and −10 to −15 °C nights. Needs an experienced Kinnaur driver with chains"],
        ["Budget per person (6 people)", f"<b>≈ {k(lo)} shoestring</b> · <b>≈ {k(hi)} recommended</b>"],
    ], [0.22, 0.78], header=False, bold_first_col=True)
    d.callout("Road reality in late December",
              ["Kalpa and Reckong Peo are reliable because BRO/PWD clear them. <b>Sangla can close after heavy snow; Chitkul usually stays closed after "
               "mid-December</b> until March. Black ice on the Sarahan, Sangla, Kalpa and Nako roads.",
               "Keep 31 Dec flexible: if snow blocks the way down, stay in Narkanda/Rampur and come to Shimla on 1 Jan morning (the toy train down is at 17:40)."], "warn")

    d.h1("Getting there and back")
    X.onward(d, (1, 2, 3, 4))
    X.kalka_toy_train(d, show_return=True)
    d.h2("Coming down on 1 Jan")
    d.table([
        ["Step", "Train", "Time", "Buffer"],
        ["Shimla → Kalka", "<b>52452 Shivalik Deluxe</b> (or 52454 Express, 2S ≈ ₹65)", "~17:40 → ~22:25–22:45 (52454: ~18:30 → ~23:30)", "—"],
        ["Kalka → Delhi", "<b>12312 Netaji (Kalka Mail)</b>, SL", "Kalka around midnight (verify) → Old Delhi ~06:00 on 2 Jan", "~1–1.5 h at Kalka"],
        ["Delhi → Hyderabad", "<b>12724 Telangana Exp</b> from New Delhi", "16:00 → ~17:10 on 3 Jan", "~10 h Delhi day"],
    ], [0.17, 0.33, 0.33, 0.17])
    d.small("If the Kalka Mail timing doesn't line up, take the 10:40 Himalayan Queen down (Kalka 16:10) and an evening train or bus from Kalka/"
            "Chandigarh to Delhi.")
    X.vehicles(d)

    d.h1("Day-by-day itinerary")
    d.day("Day 1 · Thu 24 Dec", "Hyderabad → Delhi", ["<b>06:00 12723 Telangana Express</b>."], stay="Train", cost="₹300 food")
    d.day("Day 2 · Fri 25 Dec", "Delhi day → 21:10 Kalka Mail", ["Old Delhi circuit, India Gate, Sacred Heart. Kalka Mail from Old Delhi (SL)."],
          stay="Train", cost="₹700 + ₹200 train")
    d.day("Day 3 · Sat 26 Dec", "Toy train → Shimla → Narkanda", [
        "Kalka toy train (05:20–06:20) → Shimla ~10:30–11:50 → Innova picks you up at Shimla station → lunch on the Ridge → <b>Narkanda</b> (2 h).",
    ], stay="Airbnb Narkanda", cost="₹65–510 toy train + ₹1,000 Innova share + ₹700 food")
    d.day("Day 4 · Sun 27 Dec", "Hatu Peak → Rampur → Sarahan", [
        "Sunrise at <b>Hatu Peak</b> → down to the Sutlej at <b>Rampur</b> (Padam Palace) → <b>Sarahan</b> (2,165 m): <b>Bhimakali temple</b> (Indo-Tibetan wooden "
        "architecture), Shrikhand Mahadev views.",
    ], stay="Sarahan (HPTDC Shrikhand / homestay)", cost="₹1,000 Innova share + ₹700 food")
    d.day("Day 5 · Mon 28 Dec", "Sarahan → Karcham → Sangla (Chitkul if open)", [
        "Karcham dam → Baspa valley → <b>Sangla</b>: <b>Kamru fort</b> village, Bering Nag temple, apple orchards in snow.",
        "<b>Chitkul</b> (last village before Tibet) only if the road is open; otherwise <b>Rakchham</b>.",
    ], stay="Sangla homestay", cost="₹1,000 Innova share + ₹700 food")
    d.day("Day 6 · Tue 29 Dec", "Sangla → Kalpa", [
        "<b>Kalpa</b> (2,960 m): Kinnaur Kailash at sunrise and sunset, <b>Chini village</b> and Narayan-Nagini temple, <b>Roghi village</b> and the "
        "Suicide Point cliff road. Reckong Peo market for supplies.",
    ], stay="Kalpa homestay", cost="₹1,000 Innova share + ₹700 food")
    d.day("Day 7 · Wed 30 Dec", "Khab confluence · Nako frozen lake (day trip)", [
        "Leave 07:00: Spillow → <b>Khab</b> (Sutlej–Spiti confluence) → <b>Nako</b> (3,660 m): village and the lake, usually frozen in winter. "
        "Back to Kalpa by dark (~8–9 h round trip). Skip it if there's fresh snow.",
    ], stay="Kalpa homestay", cost="₹1,000 Innova share + ₹700 food")
    d.day("Day 8 · Thu 31 Dec", "Kalpa → Shimla · NYE on the Ridge", [
        "Long drive down (~220 km, 8–9 h, leave 07:00). Evening: Shimla Winter Carnival on the Ridge, Mall Road for New Year's Eve.",
    ], stay="Airbnb Shimla", cost="₹1,000 Innova share + ₹1,000 NYE food")
    d.day("Day 9 · Fri 1 Jan", "Shimla day → toy train down → Kalka Mail", [
        "Jakhoo ropeway, Christ Church, Viceregal Lodge, Lakkar Bazaar, ice-skating rink if open. <b>17:40 Shivalik Deluxe</b> (or 18:30 Express) down to Kalka.",
        "Kalka Mail overnight to Old Delhi.",
    ], stay="Train", cost="₹300–700 + ₹200–600 train + ₹600 food")
    d.day("Day 10 · Sat 2 Jan", "Delhi → Hyderabad", ["Old Delhi ~06:00 → Humayun's Tomb / Lodhi Garden → <b>16:00 12724</b>."], stay="Train",
          cost="₹400 + ₹600 food")
    d.day("Day 11 · Sun 3 Jan", "Home", ["Hyderabad ~17:10."])

    X.airbnb(d, [
        ["1 (26 Dec)", "Narkanda", "<b>Hatu Peak View 3BR Villa | Homeyhuts</b>: 4.8★ (10)", "<b>Pahadi House</b> / <b>Wild Orchard</b> homestay rooms", (5000, 8000)],
        ["1 (27 Dec)", "Sarahan", "Not on Airbnb: <b>HPTDC Hotel Shrikhand</b> or temple-side homestays", "Homestay rooms ₹1,000–1,500", (3500, 6000)],
        ["1 (28 Dec)", "Sangla", "Not on Airbnb: Baspa-side homestays (Booking.com / phone)", "Homestay rooms ₹1,000–1,500", (3500, 6000)],
        ["2 (29–30 Dec)", "Kalpa", "Few Airbnbs: Kinnaur Kailash-view homestays · <b>HPTDC Kinner Kailash</b>", "Homestays ₹1,000–1,800 per room", (4000, 7000)],
        ["1 (31 Dec)", "Shimla", "<b>VICTORIAN VILLAS 3BHK</b> (4.51★, 106, 6 guests)", "<b>Jasm Homes 3BHK</b>", (7000, 10000)],
    ])

    d.h1("Bike rentals")
    d.p("<b>Not in winter Kinnaur.</b> Black ice, −10 °C wind and 200 km days. The Innova with a local driver and snow chains is the safe (and, for 6, "
        "cheaper) option.")
    X.gear(d, [
        ["Point", "What you can rent", "Rate"],
        ["Narkanda / Hatu stalls", "Snow suits, gumboots", "₹300–500"],
        ["Kalpa / Reckong Peo market (buy)", "Woollen socks, caps, Kinnauri shawls/caps", "Buy"],
        ["Indiahikes rentals (online)", "Down jacket (−10 °C), shoes", "₹55–150/day"],
    ])
    d.h1("Budget per person (6 people sharing)")
    d.budget(BUDGET, "Fits ₹25–30k on SL. The Innova is the main cost; winter Kinnaur drivers charge a little more.")
    d.h1("Bookings to do now")
    d.bullets([
        "12724 (2 Jan) → 12723 (24 Dec) → 12311 Kalka Mail (25 Dec) → toy train up (26 Dec) → toy train down + 12312 (1 Jan).",
        "An Innova from a Shimla/Rampur operator who does winter Kinnaur (ask about chains and 4x4 backup).",
        "Shimla NYE Airbnb (31 Dec) first; Kinnaur homestays by phone a week ahead.",
    ])
    X.packing_and_safety(d, ["Altitude: Nako is 3,660 m, so walk slowly and stay hydrated. Carry dry fruits and a thermos in the car."])
    d.sources([
        "Kinnaur winter roads (Kalpa open; Sangla may close; Chitkul shut after mid-Dec): vargiskhan Kinnaur winter guides, discoverwithdheeraj, raachotrekkers, travelcoffee",
        "Toy train both directions: travelcoffee, Shimla Tourism, exploreindia, sunrisevilla timetable, totaltraininfo; Kalka Mail: Cleartrip, RailMitra, indiantrain",
        "Spiti winter (why not a full plan): discoverwithdheeraj, treksandtrails, Spiti Holiday Adventure, travelshoebum",
        "Innova rates: Rajputana Cabs, Triveni Cabs; Airbnb Narkanda/Shimla listings via search (Nov 2026)",
    ])
    d.build()
    return lo, hi
